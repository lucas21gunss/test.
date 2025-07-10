# 🎬 Instruções para Vídeo de Demonstração

## Roteiro Detalhado (5 minutos)

### 1. Introdução (30 segundos)
**O que mostrar:**
- Tela inicial com estrutura do projeto
- Explicar brevemente o desafio técnico

**Script sugerido:**
> "Olá! Este é o Assistente Virtual de Busca de Carros, desenvolvido para o desafio técnico da C2S. O projeto implementa uma aplicação de terminal com agente virtual que utiliza processamento de linguagem natural para buscar carros em um banco de dados."

**Comandos:**
```bash
ls -la
tree src/ -I "__pycache__"
```

### 2. Arquitetura e Componentes (1 minuto)
**O que mostrar:**
- Estrutura de diretórios
- Principais arquivos de código
- Banco de dados populado

**Script sugerido:**
> "A solução está organizada em 4 componentes principais: modelagem de dados com SQLAlchemy, comunicação cliente-servidor usando protocolo MCP, agente virtual com processamento de linguagem natural, e interface CLI rica. Vamos ver o banco de dados já populado com mais de 100 carros fictícios."

**Comandos:**
```bash
cat src/models/automobile.py | head -20
sqlite3 automobiles.db "SELECT COUNT(*) FROM automobiles;"
sqlite3 automobiles.db "SELECT brand, model, year, price FROM automobiles LIMIT 5;"
```

### 3. Inicialização do Sistema (1 minuto)
**O que mostrar:**
- Instalação de dependências
- Inicialização do servidor
- Documentação automática da API

**Script sugerido:**
> "Primeiro, vamos instalar as dependências e iniciar o servidor FastAPI. O servidor implementa o protocolo MCP com endpoints REST para busca de automóveis."

**Comandos:**
```bash
pip install -r requirements.txt
python3 -m src.server.main &
curl http://localhost:8000/
```

**Abrir no navegador:**
- http://localhost:8000/docs (documentação Swagger)

### 4. Demonstração da Aplicação (2 minutos)
**O que mostrar:**
- Interface de boas-vindas
- Diferentes tipos de consultas
- Respostas formatadas do agente

**Script sugerido:**
> "Agora vamos usar a aplicação. O agente virtual entende consultas em português e converte automaticamente em filtros de busca. Vou demonstrar diferentes tipos de consultas."

**Consultas para demonstrar:**
1. `Toyota` - Busca simples por marca
2. `Honda até R$ 70.000` - Filtro por marca e preço
3. `Carros de 2020 a 2023` - Filtro por faixa de anos
4. `Flex automático azul` - Múltiplos filtros
5. `BMW elétrico` - Consulta sem resultados

**Comando:**
```bash
python3 -m src.cli_app
```

### 5. Testes e Qualidade (1 minuto)
**O que mostrar:**
- Execução da suíte de testes
- Cobertura de código
- Estrutura de testes

**Script sugerido:**
> "A solução inclui testes automatizados abrangentes para garantir a qualidade e testabilidade do código, conforme solicitado no desafio."

**Comandos:**
```bash
python3 -m pytest tests/ -v
ls tests/
cat tests/test_virtual_agent.py | head -20
```

### 6. Conclusão (30 segundos)
**O que mostrar:**
- README.md com documentação completa
- Estrutura final do projeto

**Script sugerido:**
> "O projeto está completamente documentado, com instruções de instalação, uso e extensão. Implementa todos os requisitos do desafio com diferenciais técnicos como arquitetura limpa, experiência de usuário rica e robustez. Obrigado pela oportunidade!"

**Comandos:**
```bash
cat README.md | head -30
```

## 🎯 Pontos Importantes a Destacar

### Requisitos Técnicos Atendidos
- ✅ Modelagem de dados com 12+ atributos
- ✅ População com 100+ registros fictícios
- ✅ Protocolo de comunicação cliente-servidor (MCP)
- ✅ Agente virtual com processamento de linguagem natural
- ✅ Aplicação de terminal interativa
- ✅ Testabilidade com testes automatizados

### Diferenciais Técnicos
- **Arquitetura limpa** com separação de responsabilidades
- **Interface rica** com Rich e Typer
- **Processamento de linguagem natural** em português
- **Tratamento robusto de erros**
- **Documentação completa**
- **Testes abrangentes**

### Tecnologias Utilizadas
- Python 3.11, FastAPI, SQLAlchemy, SQLite
- HTTPX, Typer, Rich, Faker, Pytest

## 📋 Checklist de Gravação

### Antes de Gravar
- [ ] Verificar que o servidor não está rodando
- [ ] Limpar terminal (clear)
- [ ] Verificar resolução da tela
- [ ] Testar áudio e vídeo
- [ ] Preparar ambiente limpo

### Durante a Gravação
- [ ] Falar claramente e em ritmo adequado
- [ ] Aguardar comandos carregarem completamente
- [ ] Destacar pontos importantes
- [ ] Mostrar resultados na tela
- [ ] Manter foco nos requisitos do desafio

### Após a Gravação
- [ ] Revisar o vídeo
- [ ] Verificar qualidade de áudio/vídeo
- [ ] Confirmar que todos os pontos foram cobertos
- [ ] Exportar em formato adequado (MP4, 1080p)

## 🛠️ Comandos de Preparação

### Resetar Ambiente (se necessário)
```bash
# Parar servidor se estiver rodando
pkill -f "src.server.main"

# Limpar cache Python
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete

# Verificar banco de dados
sqlite3 automobiles.db "SELECT COUNT(*) FROM automobiles;"
```

### Script de Demonstração Automática
```bash
# Usar o script preparado
./run_demo.sh
```

## 📝 Notas Adicionais

- **Duração ideal**: 4-5 minutos
- **Formato**: MP4, 1080p, 30fps
- **Áudio**: Claro e sem ruídos
- **Foco**: Demonstrar competência técnica e atenção aos requisitos
- **Tom**: Profissional mas acessível

---

*Boa sorte com a gravação! 🎬*

