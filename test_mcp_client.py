import pytest
from unittest.mock import Mock, patch
import httpx
from src.client.mcp_client import MCPClient

class TestMCPClient:
    """Testes para o cliente MCP."""
    
    @pytest.fixture
    def client(self):
        """Fixture para criar um cliente MCP."""
        return MCPClient("http://test-server:8000")
    
    @patch('httpx.Client')
    def test_search_automobiles_success(self, mock_httpx_client, client):
        """Testa busca de automóveis com sucesso."""
        # Configurar mock
        mock_response = Mock()
        mock_response.json.return_value = [
            {"brand": "Toyota", "model": "Corolla", "year": 2020},
            {"brand": "Honda", "model": "Civic", "year": 2019}
        ]
        mock_response.raise_for_status.return_value = None
        
        mock_client_instance = Mock()
        mock_client_instance.post.return_value = mock_response
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        filters = {"brand": "Toyota"}
        results = client.search_automobiles(filters)
        
        # Verificar resultados
        assert len(results) == 2
        assert results[0]["brand"] == "Toyota"
        mock_client_instance.post.assert_called_once_with(
            "http://test-server:8000/search",
            json=filters,
            headers={"Content-Type": "application/json"}
        )
    
    @patch('httpx.Client')
    def test_search_automobiles_http_error(self, mock_httpx_client, client):
        """Testa busca de automóveis com erro HTTP."""
        # Configurar mock para erro
        mock_client_instance = Mock()
        mock_client_instance.post.side_effect = httpx.HTTPError("Connection error")
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        filters = {"brand": "Toyota"}
        results = client.search_automobiles(filters)
        
        # Verificar que retorna lista vazia em caso de erro
        assert results == []
    
    @patch('httpx.Client')
    def test_get_all_automobiles_success(self, mock_httpx_client, client):
        """Testa obtenção de todos os automóveis com sucesso."""
        # Configurar mock
        mock_response = Mock()
        mock_response.json.return_value = [
            {"id": 1, "brand": "Toyota", "model": "Corolla"},
            {"id": 2, "brand": "Honda", "model": "Civic"}
        ]
        mock_response.raise_for_status.return_value = None
        
        mock_client_instance = Mock()
        mock_client_instance.get.return_value = mock_response
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        results = client.get_all_automobiles(skip=0, limit=10)
        
        # Verificar resultados
        assert len(results) == 2
        assert results[0]["id"] == 1
        mock_client_instance.get.assert_called_once_with(
            "http://test-server:8000/automobiles",
            params={"skip": 0, "limit": 10}
        )
    
    @patch('httpx.Client')
    def test_get_all_automobiles_http_error(self, mock_httpx_client, client):
        """Testa obtenção de todos os automóveis com erro HTTP."""
        # Configurar mock para erro
        mock_client_instance = Mock()
        mock_client_instance.get.side_effect = httpx.HTTPError("Connection error")
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        results = client.get_all_automobiles()
        
        # Verificar que retorna lista vazia em caso de erro
        assert results == []
    
    @patch('httpx.Client')
    def test_get_automobile_by_id_success(self, mock_httpx_client, client):
        """Testa obtenção de automóvel por ID com sucesso."""
        # Configurar mock
        mock_response = Mock()
        mock_response.json.return_value = {"id": 1, "brand": "Toyota", "model": "Corolla"}
        mock_response.raise_for_status.return_value = None
        
        mock_client_instance = Mock()
        mock_client_instance.get.return_value = mock_response
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        result = client.get_automobile_by_id(1)
        
        # Verificar resultado
        assert result["id"] == 1
        assert result["brand"] == "Toyota"
        mock_client_instance.get.assert_called_once_with(
            "http://test-server:8000/automobiles/1"
        )
    
    @patch('httpx.Client')
    def test_get_automobile_by_id_not_found(self, mock_httpx_client, client):
        """Testa obtenção de automóvel por ID não encontrado."""
        # Configurar mock para 404
        mock_response = Mock()
        mock_response.status_code = 404
        
        mock_error = httpx.HTTPError("Not found")
        mock_error.response = mock_response
        
        mock_client_instance = Mock()
        mock_client_instance.get.side_effect = mock_error
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        result = client.get_automobile_by_id(999)
        
        # Verificar que retorna None para 404
        assert result is None
    
    @patch('httpx.Client')
    def test_get_automobile_by_id_other_error(self, mock_httpx_client, client):
        """Testa obtenção de automóvel por ID com outro erro HTTP."""
        # Configurar mock para erro diferente de 404
        mock_response = Mock()
        mock_response.status_code = 500
        
        mock_error = httpx.HTTPError("Server error")
        mock_error.response = mock_response
        
        mock_client_instance = Mock()
        mock_client_instance.get.side_effect = mock_error
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        result = client.get_automobile_by_id(1)
        
        # Verificar que retorna None para outros erros
        assert result is None
    
    @patch('httpx.Client')
    def test_close_client(self, mock_httpx_client, client):
        """Testa o fechamento do cliente."""
        mock_client_instance = Mock()
        mock_httpx_client.return_value = mock_client_instance
        
        # Executar teste
        client.close()
        
        # Verificar que close foi chamado
        mock_client_instance.close.assert_called_once()
    
    def test_client_initialization(self):
        """Testa a inicialização do cliente."""
        client = MCPClient("http://custom-server:9000")
        assert client.base_url == "http://custom-server:9000"
        
        # Teste com URL padrão
        default_client = MCPClient()
        assert default_client.base_url == "http://localhost:8000"

