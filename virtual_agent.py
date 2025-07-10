import re
from typing import Dict, Any, List
from src.client.mcp_client import MCPClient

class VirtualAgent:
    """
    Agente virtual para interpretar consultas de usuário e converter em filtros de busca.
    """
    
    def __init__(self, mcp_client: MCPClient):
        self.mcp_client = mcp_client
        self.brands = [
            "Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "BMW", "Mercedes", 
            "Audi", "Nissan", "Hyundai", "Kia", "Mazda", "Subaru", "Volvo", "Peugeot",
            "Renault", "Fiat", "Jeep", "Land Rover", "Porsche", "Ferrari", "Lamborghini"
        ]
        self.fuel_types = ["Gasolina", "Etanol", "Diesel", "Flex", "Elétrico"]
        self.transmissions = ["Automática", "Manual"]
        self.colors = [
            "Branco", "Preto", "Prata", "Cinza", "Azul", "Vermelho", "Verde", 
            "Amarelo", "Marrom", "Bege", "Rosa", "Roxo", "Laranja"
        ]
    
    def parse_user_query(self, query: str) -> Dict[str, Any]:
        """
        Analisa a consulta do usuário e extrai filtros de busca.
        
        Args:
            query: Consulta em linguagem natural do usuário
            
        Returns:
            Dicionário com filtros de busca
        """
        filters = {}
        query_lower = query.lower()
        
        # Extrair marca
        for brand in self.brands:
            if brand.lower() in query_lower:
                filters["brand"] = brand
                break
        
        # Extrair tipo de combustível
        for fuel in self.fuel_types:
            if fuel.lower() in query_lower:
                filters["fuel_type"] = fuel
                break
        
        # Extrair transmissão
        for transmission in self.transmissions:
            if transmission.lower() in query_lower:
                filters["transmission"] = transmission
                break
        
        # Extrair cor
        for color in self.colors:
            if color.lower() in query_lower:
                filters["color"] = color
                break
        
        # Extrair ano
        year_patterns = [
            r"ano (\d{4})",
            r"de (\d{4})",
            r"(\d{4})",
            r"entre (\d{4}) e (\d{4})",
            r"de (\d{4}) a (\d{4})"
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, query_lower)
            if match:
                if len(match.groups()) == 1:
                    year = int(match.group(1))
                    if 1900 <= year <= 2024:
                        filters["year_min"] = year
                        filters["year_max"] = year
                elif len(match.groups()) == 2:
                    year_min = int(match.group(1))
                    year_max = int(match.group(2))
                    if 1900 <= year_min <= 2024 and 1900 <= year_max <= 2024:
                        filters["year_min"] = year_min
                        filters["year_max"] = year_max
                break
        
        # Extrair preço
        price_patterns = [
            r"até r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?)",
            r"máximo r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?)",
            r"preço até r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?)",
            r"entre r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?) e r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?)",
            r"de r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?) a r?\$?\s?(\d+(?:\.\d{3})*(?:,\d{2})?)"
        ]
        
        for pattern in price_patterns:
            match = re.search(pattern, query_lower)
            if match:
                if len(match.groups()) == 1:
                    price_str = match.group(1).replace(".", "").replace(",", ".")
                    price = float(price_str)
                    filters["price_max"] = price
                elif len(match.groups()) == 2:
                    price_min_str = match.group(1).replace(".", "").replace(",", ".")
                    price_max_str = match.group(2).replace(".", "").replace(",", ".")
                    filters["price_min"] = float(price_min_str)
                    filters["price_max"] = float(price_max_str)
                break
        
        # Extrair quilometragem
        mileage_patterns = [
            r"até (\d+(?:\.\d{3})*) km",
            r"máximo (\d+(?:\.\d{3})*) km",
            r"quilometragem até (\d+(?:\.\d{3})*)"
        ]
        
        for pattern in mileage_patterns:
            match = re.search(pattern, query_lower)
            if match:
                mileage_str = match.group(1).replace(".", "")
                filters["mileage_max"] = int(mileage_str)
                break
        
        return filters
    
    def search_automobiles(self, query: str) -> List[Dict[str, Any]]:
        """
        Busca automóveis com base na consulta do usuário.
        
        Args:
            query: Consulta em linguagem natural
            
        Returns:
            Lista de automóveis encontrados
        """
        filters = self.parse_user_query(query)
        return self.mcp_client.search_automobiles(filters)
    
    def format_automobile_info(self, automobile: Dict[str, Any]) -> str:
        """
        Formata as informações de um automóvel para exibição.
        
        Args:
            automobile: Dados do automóvel
            
        Returns:
            String formatada com as informações
        """
        return f"""
🚗 {automobile['brand']} {automobile['model']} ({automobile['year']})
   💰 Preço: R$ {automobile['price']:,.2f}
   🎨 Cor: {automobile['color']}
   ⛽ Combustível: {automobile['fuel_type']}
   🔧 Transmissão: {automobile['transmission']}
   📏 Motor: {automobile['engine_size']}L
   🚪 Portas: {automobile['num_doors']}
   📊 Quilometragem: {automobile['mileage']:,} km
   🏷️  Placa: {automobile['plate']}
        """.strip()
    
    def generate_response(self, query: str, results: List[Dict[str, Any]]) -> str:
        """
        Gera uma resposta amigável para o usuário.
        
        Args:
            query: Consulta original do usuário
            results: Resultados da busca
            
        Returns:
            Resposta formatada
        """
        if not results:
            return "😔 Não encontrei nenhum carro que atenda aos seus critérios. Que tal tentar uma busca diferente?"
        
        response = f"🎉 Encontrei {len(results)} carro(s) para você!\n\n"
        
        for i, automobile in enumerate(results[:5], 1):  # Limitar a 5 resultados
            response += f"{i}. {self.format_automobile_info(automobile)}\n\n"
        
        if len(results) > 5:
            response += f"... e mais {len(results) - 5} carros. Digite 'mais' para ver todos os resultados."
        
        return response

