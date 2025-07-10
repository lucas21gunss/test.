import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from typing import Optional
import sys
import os

# Adicionar o diretório raiz ao path para importações
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.client.mcp_client import MCPClient
from src.agent.virtual_agent import VirtualAgent

app = typer.Typer()
console = Console()

def display_welcome():
    """Exibe a mensagem de boas-vindas."""
    welcome_text = Text()
    welcome_text.append("🚗 ", style="bold blue")
    welcome_text.append("Bem-vindo ao Assistente de Busca de Carros!", style="bold green")
    welcome_text.append("\n\nEu sou seu agente virtual e posso te ajudar a encontrar o carro perfeito!")
    welcome_text.append("\n\nExemplos de consultas:")
    welcome_text.append("\n• 'Quero um Toyota Corolla'")
    welcome_text.append("\n• 'Carros até R$ 50.000'")
    welcome_text.append("\n• 'Honda automático azul'")
    welcome_text.append("\n• 'Carros de 2020 a 2023'")
    welcome_text.append("\n• 'Flex até 80.000 km'")
    welcome_text.append("\n\nDigite 'sair' para encerrar.")
    
    panel = Panel(welcome_text, title="🤖 Agente Virtual de Carros", border_style="blue")
    console.print(panel)

def display_thinking():
    """Exibe animação de pensamento."""
    console.print("🤔 Analisando sua consulta...", style="yellow")

def display_error(message: str):
    """Exibe mensagem de erro."""
    error_panel = Panel(f"❌ {message}", title="Erro", border_style="red")
    console.print(error_panel)

@app.command()
def main(
    server_url: Optional[str] = typer.Option(
        "http://localhost:8000", 
        "--server", 
        "-s", 
        help="URL do servidor MCP"
    )
):
    """
    Aplicação de terminal com agente virtual para buscar carros.
    """
    
    # Inicializar cliente e agente
    try:
        mcp_client = MCPClient(server_url)
        agent = VirtualAgent(mcp_client)
    except Exception as e:
        display_error(f"Erro ao conectar com o servidor: {e}")
        raise typer.Exit(1)
    
    # Exibir boas-vindas
    display_welcome()
    
    # Loop principal da aplicação
    try:
        while True:
            console.print()
            query = Prompt.ask("💬 [bold cyan]Como posso te ajudar?[/bold cyan]")
            
            # Verificar se o usuário quer sair
            if query.lower() in ['sair', 'exit', 'quit', 'bye']:
                console.print("👋 Obrigado por usar o assistente! Até logo!", style="green")
                break
            
            # Verificar se a consulta não está vazia
            if not query.strip():
                console.print("🤷 Por favor, digite sua consulta.", style="yellow")
                continue
            
            # Processar consulta
            display_thinking()
            
            try:
                # Buscar carros
                results = agent.search_automobiles(query)
                
                # Gerar e exibir resposta
                response = agent.generate_response(query, results)
                
                response_panel = Panel(
                    response, 
                    title="🤖 Resposta do Agente", 
                    border_style="green"
                )
                console.print(response_panel)
                
            except Exception as e:
                display_error(f"Erro ao processar consulta: {e}")
                console.print("💡 Tente reformular sua pergunta.", style="yellow")
    
    except KeyboardInterrupt:
        console.print("\n👋 Encerrando aplicação. Até logo!", style="green")
    
    finally:
        # Fechar conexão
        try:
            mcp_client.close()
        except:
            pass

if __name__ == "__main__":
    app()

