import pytest
from unittest.mock import Mock, MagicMock
from src.agent.virtual_agent import VirtualAgent

class TestVirtualAgent:
    """Testes para o agente virtual."""
    
    @pytest.fixture
    def mock_mcp_client(self):
        """Fixture para criar um cliente MCP mock."""
        return Mock()
    
    @pytest.fixture
    def agent(self, mock_mcp_client):
        """Fixture para criar um agente virtual."""
        return VirtualAgent(mock_mcp_client)
    
    def test_parse_brand_query(self, agent):
        """Testa a extração de marca da consulta."""
        filters = agent.parse_user_query("Quero um Toyota Corolla")
        assert filters["brand"] == "Toyota"
        
        filters = agent.parse_user_query("Procuro um Honda")
        assert filters["brand"] == "Honda"
        
        filters = agent.parse_user_query("BMW série 3")
        assert filters["brand"] == "BMW"
    
    def test_parse_fuel_type_query(self, agent):
        """Testa a extração de tipo de combustível."""
        filters = agent.parse_user_query("Carro flex")
        assert filters["fuel_type"] == "Flex"
        
        filters = agent.parse_user_query("Quero um elétrico")
        assert filters["fuel_type"] == "Elétrico"
        
        filters = agent.parse_user_query("Diesel econômico")
        assert filters["fuel_type"] == "Diesel"
    
    def test_parse_transmission_query(self, agent):
        """Testa a extração de transmissão."""
        filters = agent.parse_user_query("Carro automático")
        assert filters["transmission"] == "Automática"
        
        filters = agent.parse_user_query("Prefiro manual")
        assert filters["transmission"] == "Manual"
    
    def test_parse_color_query(self, agent):
        """Testa a extração de cor."""
        filters = agent.parse_user_query("Carro branco")
        assert filters["color"] == "Branco"
        
        filters = agent.parse_user_query("Azul metálico")
        assert filters["color"] == "Azul"
        
        filters = agent.parse_user_query("Vermelho esportivo")
        assert filters["color"] == "Vermelho"
    
    def test_parse_year_query(self, agent):
        """Testa a extração de ano."""
        filters = agent.parse_user_query("Carro de 2020")
        assert filters["year_min"] == 2020
        assert filters["year_max"] == 2020
        
        filters = agent.parse_user_query("Entre 2018 e 2022")
        assert filters["year_min"] == 2018
        assert filters["year_max"] == 2022
        
        filters = agent.parse_user_query("De 2015 a 2020")
        assert filters["year_min"] == 2015
        assert filters["year_max"] == 2020
    
    def test_parse_price_query(self, agent):
        """Testa a extração de preço."""
        filters = agent.parse_user_query("Até R$ 50.000")
        assert filters["price_max"] == 50000.0
        
        filters = agent.parse_user_query("Entre R$ 30.000 e R$ 80.000")
        assert filters["price_min"] == 30000.0
        assert filters["price_max"] == 80000.0
        
        filters = agent.parse_user_query("Máximo 100000")
        assert filters["price_max"] == 100000.0
    
    def test_parse_mileage_query(self, agent):
        """Testa a extração de quilometragem."""
        filters = agent.parse_user_query("Até 50.000 km")
        assert filters["mileage_max"] == 50000
        
        filters = agent.parse_user_query("Máximo 80000 km")
        assert filters["mileage_max"] == 80000
        
        filters = agent.parse_user_query("Quilometragem até 100.000")
        assert filters["mileage_max"] == 100000
    
    def test_complex_query(self, agent):
        """Testa uma consulta complexa com múltiplos filtros."""
        query = "Toyota Corolla 2020 branco automático flex até R$ 90.000"
        filters = agent.parse_user_query(query)
        
        assert filters["brand"] == "Toyota"
        assert filters["year_min"] == 2020
        assert filters["year_max"] == 2020
        assert filters["color"] == "Branco"
        assert filters["transmission"] == "Automática"
        assert filters["fuel_type"] == "Flex"
        assert filters["price_max"] == 90000.0
    
    def test_search_automobiles(self, agent, mock_mcp_client):
        """Testa a busca de automóveis."""
        # Configurar mock
        mock_results = [
            {"brand": "Toyota", "model": "Corolla", "year": 2020},
            {"brand": "Toyota", "model": "Camry", "year": 2021}
        ]
        mock_mcp_client.search_automobiles.return_value = mock_results
        
        # Executar busca
        results = agent.search_automobiles("Toyota")
        
        # Verificar resultados
        assert len(results) == 2
        assert results[0]["brand"] == "Toyota"
        mock_mcp_client.search_automobiles.assert_called_once()
    
    def test_format_automobile_info(self, agent):
        """Testa a formatação das informações do automóvel."""
        automobile = {
            "brand": "Honda",
            "model": "Civic",
            "year": 2019,
            "price": 75000.50,
            "color": "Prata",
            "fuel_type": "Gasolina",
            "transmission": "Manual",
            "engine_size": 1.8,
            "num_doors": 4,
            "mileage": 25000,
            "plate": "HND-2019"
        }
        
        formatted = agent.format_automobile_info(automobile)
        
        assert "Honda Civic (2019)" in formatted
        assert "R$ 75,000.50" in formatted
        assert "Prata" in formatted
        assert "Gasolina" in formatted
        assert "Manual" in formatted
        assert "1.8L" in formatted
        assert "4" in formatted
        assert "25,000 km" in formatted
        assert "HND-2019" in formatted
    
    def test_generate_response_no_results(self, agent):
        """Testa a geração de resposta quando não há resultados."""
        response = agent.generate_response("Toyota", [])
        assert "Não encontrei nenhum carro" in response
        assert "😔" in response
    
    def test_generate_response_with_results(self, agent):
        """Testa a geração de resposta com resultados."""
        results = [
            {
                "brand": "Toyota", "model": "Corolla", "year": 2020,
                "price": 85000.0, "color": "Branco", "fuel_type": "Flex",
                "transmission": "Automática", "engine_size": 1.8,
                "num_doors": 4, "mileage": 15000, "plate": "TOY-2020"
            }
        ]
        
        response = agent.generate_response("Toyota", results)
        
        assert "Encontrei 1 carro(s)" in response
        assert "Toyota Corolla (2020)" in response
        assert "🎉" in response
    
    def test_generate_response_many_results(self, agent):
        """Testa a geração de resposta com muitos resultados."""
        results = []
        for i in range(10):
            results.append({
                "brand": "Toyota", "model": f"Model{i}", "year": 2020,
                "price": 50000.0, "color": "Branco", "fuel_type": "Flex",
                "transmission": "Manual", "engine_size": 1.0,
                "num_doors": 4, "mileage": 10000, "plate": f"TOY-{i:04d}"
            })
        
        response = agent.generate_response("Toyota", results)
        
        assert "Encontrei 10 carro(s)" in response
        assert "mais 5 carros" in response  # Mostra apenas 5, menciona os outros

