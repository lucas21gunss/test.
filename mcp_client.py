import httpx
from typing import List, Optional, Dict, Any
import json

class MCPClient:
    """
    Cliente para comunicação com o servidor usando o protocolo MCP.
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.client = httpx.Client()
    
    def search_automobiles(self, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Buscar automóveis com base nos filtros fornecidos.
        
        Args:
            filters: Dicionário com os filtros de busca
            
        Returns:
            Lista de automóveis encontrados
        """
        try:
            response = self.client.post(
                f"{self.base_url}/search",
                json=filters,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"Erro na comunicação com o servidor: {e}")
            return []
    
    def get_all_automobiles(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Obter todos os automóveis com paginação.
        
        Args:
            skip: Número de registros para pular
            limit: Número máximo de registros para retornar
            
        Returns:
            Lista de automóveis
        """
        try:
            response = self.client.get(
                f"{self.base_url}/automobiles",
                params={"skip": skip, "limit": limit}
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            print(f"Erro na comunicação com o servidor: {e}")
            return []
    
    def get_automobile_by_id(self, automobile_id: int) -> Optional[Dict[str, Any]]:
        """
        Obter um automóvel específico por ID.
        
        Args:
            automobile_id: ID do automóvel
            
        Returns:
            Dados do automóvel ou None se não encontrado
        """
        try:
            response = self.client.get(f"{self.base_url}/automobiles/{automobile_id}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            if e.response.status_code == 404:
                return None
            print(f"Erro na comunicação com o servidor: {e}")
            return None
    
    def close(self):
        """
        Fechar a conexão do cliente.
        """
        self.client.close()

# Exemplo de uso
if __name__ == "__main__":
    client = MCPClient()
    
    # Buscar carros Toyota
    filters = {"brand": "Toyota"}
    results = client.search_automobiles(filters)
    print(f"Encontrados {len(results)} carros Toyota")
    
    # Buscar carros com preço entre 20000 e 50000
    filters = {"price_min": 20000, "price_max": 50000}
    results = client.search_automobiles(filters)
    print(f"Encontrados {len(results)} carros na faixa de preço")
    
    client.close()

