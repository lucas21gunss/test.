🚗 Assistente Virtual de Busca de Carros

Descrição

Este projeto implementa uma aplicação de terminal com agente virtual para buscar carros em um banco de dados, desenvolvido como resposta ao desafio técnico da C2S. A solução utiliza um protocolo de comunicação cliente-servidor (MCP) e oferece uma interface conversacional intuitiva para os usuários.

🏗️ Arquitetura

O projeto está estruturado em quatro componentes principais:

1. Modelagem de Dados

•
Modelo Automobile: Representa um automóvel com 12 atributos (marca, modelo, ano, cor, quilometragem, preço, combustível, transmissão, motor, portas, placa)

•
ORM SQLAlchemy: Gerenciamento do banco de dados SQLite

•
Validação: Restrições de integridade e índices para performance

2. Banco de Dados

•
100+ registros fictícios: Gerados automaticamente usando Faker

•
Dados realistas: Marcas, modelos e especificações verossímeis

•
Diversidade: Ampla variedade de características para testes abrangentes

3. Comunicação Cliente-Servidor (MCP)

•
Servidor FastAPI: API REST com endpoints para busca e consulta

•
Cliente HTTP: Comunicação via HTTPX com tratamento de erros

•
Protocolo MCP: Estrutura padronizada para filtros e respostas

•
CORS habilitado: Suporte para requisições cross-origin

4. Agente Virtual

•
Processamento de linguagem natural: Interpreta consultas em português

•
Interface CLI rica: Terminal interativo com Rich e Typer

•
Respostas contextuais: Formatação amigável dos resultados

•
Tratamento de erros: Feedback claro para o usuário

🚀 Instalação e Execução

Pré-requisitos

•
Python 3.11+

•
pip (gerenciador de pacotes Python)

1. Clonar o repositório

Bash


git clone <url-do-repositorio>
cd assistente-carros


2. Instalar dependências

Bash


pip install -r requirements.txt


3. Inicializar o banco de dados

Bash


python3 -m src.populate_db


4. Iniciar o servidor

Bash


python3 -m src.server.main


5. Executar a aplicação (em outro terminal)

Bash


python3 -m src.cli_app


💬 Como Usar

Exemplos de Consultas

A aplicação aceita consultas em linguagem natural em português:

•
Por marca: "Quero um Toyota"

•
Por modelo: "Honda Civic"

•
Por preço: "Carros até R$ 50.000"

•
Por ano: "Carros de 2020 a 2023"

•
Por combustível: "Carros flex"

•
Por transmissão: "Automático"

•
Por cor: "Carro branco"

•
Por quilometragem: "Até 80.000 km"

•
Consulta complexa: "Toyota Corolla 2020 branco automático flex até R$ 90.000"

Interface

Plain Text


🚗 Bem-vindo ao Assistente de Busca de Carros!

Eu sou seu agente virtual e posso te ajudar a encontrar o carro perfeito!

💬 Como posso te ajudar?: Toyota até 60000
🤔 Analisando sua consulta...

🎉 Encontrei 3 carro(s) para você!

1. 🚗 Toyota Corolla (2019)
   💰 Preço: R$ 55,000.00
   🎨 Cor: Branco
   ⛽ Combustível: Flex
   🔧 Transmissão: Automática
   📏 Motor: 1.8L
   🚪 Portas: 4
   📊 Quilometragem: 45,000 km
   🏷️ Placa: ABC-1234


🧪 Testes

Executar todos os testes

Bash


python3 -m pytest tests/ -v


Cobertura de testes

Bash


python3 -m pytest tests/ --cov=src --cov-report=html


Tipos de testes implementados

•
Testes unitários: Modelos, agente virtual, cliente MCP

•
Testes de integração: Comunicação cliente-servidor

•
Testes de regressão: Validação de funcionalidades críticas

📁 Estrutura do Projeto

Plain Text


assistente-carros/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── automobile.py          # Modelo de dados
│   ├── server/
│   │   ├── __init__.py
│   │   └── main.py               # Servidor FastAPI
│   ├── client/
│   │   ├── __init__.py
│   │   └── mcp_client.py         # Cliente MCP
│   ├── agent/
│   │   ├── __init__.py
│   │   └── virtual_agent.py      # Agente virtual
│   ├── __init__.py
│   ├── database.py               # Configuração do banco
│   ├── populate_db.py            # Script para popular DB
│   └── cli_app.py               # Aplicação CLI principal
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_mcp_client.py
│   └── test_virtual_agent.py
├── automobiles.db               # Banco de dados SQLite
├── requirements.txt             # Dependências
├── README.md                   # Esta documentação
└── todo.md                     # Lista de tarefas


🔧 Tecnologias Utilizadas

•
Python 3.11: Linguagem principal

•
FastAPI: Framework web para API REST

•
SQLAlchemy: ORM para banco de dados

•
SQLite: Banco de dados relacional

•
HTTPX: Cliente HTTP assíncrono

•
Typer: Framework para CLI

•
Rich: Interface rica para terminal

•
Faker: Geração de dados fictícios

•
Pytest: Framework de testes

📊 Funcionalidades Implementadas

✅ Requisitos Atendidos

1.
Modelagem de Dados




Estrutura com 12+ atributos




Relacionamentos e índices




Validações de integridade



2.
População do Banco




100+ registros fictícios




Dados realistas e diversificados




Script automatizado



3.
Comunicação MCP




Protocolo cliente-servidor




API REST com FastAPI




Cliente HTTP robusto




Tratamento de erros



4.
Agente Virtual




Processamento de linguagem natural




Interface CLI interativa




Respostas contextuais




Múltiplos tipos de filtros



5.
Testabilidade




Testes unitários




Testes de integração




Cobertura de código




Mocks e fixtures



🎯 Diferenciais Técnicos

Arquitetura Limpa

•
Separação clara de responsabilidades

•
Baixo acoplamento entre componentes

•
Facilidade de manutenção e extensão

Experiência do Usuário

•
Interface conversacional intuitiva

•
Feedback visual rico com emojis e cores

•
Tratamento gracioso de erros

•
Suporte a consultas complexas

Robustez

•
Validação de entrada em múltiplas camadas

•
Tratamento abrangente de exceções

•
Logs estruturados para debugging

•
Testes automatizados extensivos

Performance

•
Índices otimizados no banco de dados

•
Conexões HTTP reutilizáveis

•
Paginação para grandes resultados

•
Cache de consultas frequentes

🚀 Demonstração em Vídeo

Para gravar o vídeo de demonstração, siga este roteiro:

1. Introdução (30s)

•
Apresentar o projeto e seus objetivos

•
Mostrar a estrutura de arquivos

•
Explicar a arquitetura em alto nível

2. Inicialização (1min)

•
Demonstrar a instalação das dependências

•
Executar o script de população do banco

•
Iniciar o servidor FastAPI

•
Mostrar a documentação automática da API

3. Uso da Aplicação (2min)

•
Executar a aplicação CLI

•
Demonstrar diferentes tipos de consultas:

•
Busca simples por marca

•
Filtro por preço

•
Consulta complexa com múltiplos filtros

•
Tratamento de consulta sem resultados



4. Testes (1min)

•
Executar a suíte de testes

•
Mostrar relatório de cobertura

•
Destacar a qualidade do código

5. Conclusão (30s)

•
Resumir os diferenciais técnicos

•
Mencionar possíveis extensões futuras

•
Agradecer pela oportunidade

🔮 Próximos Passos

Melhorias Futuras

•
IA Avançada: Integração com LLMs para compreensão mais sofisticada

•
Interface Web: Dashboard React para visualização de dados

•
API GraphQL: Consultas mais flexíveis e eficientes

•
Cache Redis: Performance para alta concorrência

•
Containerização: Deploy com Docker e Kubernetes

•
Monitoramento: Métricas e alertas com Prometheus/Grafana

Extensões Possíveis

•
Recomendações: Sistema de sugestões baseado em preferências

•
Comparação: Ferramenta para comparar múltiplos veículos

•
Histórico: Tracking de preços e tendências de mercado

•
Integração: APIs de concessionárias e classificados

•


👨‍💻 Autor

Desenvolvido por: [Lucas Nascimento]


GitHub: [github.com/lucas21gunss]

📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.





Desenvolvido com ❤️ para o desafio técnico da C2S

