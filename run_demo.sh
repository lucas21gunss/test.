#!/bin/bash

echo "🚗 Demonstração do Assistente Virtual de Busca de Carros"
echo "======================================================="
echo ""

echo "1. Verificando se o servidor está rodando..."
if ! curl -s http://localhost:8000/ > /dev/null; then
    echo "   Iniciando servidor FastAPI..."
    python3 -m src.server.main &
    SERVER_PID=$!
    sleep 3
    echo "   ✅ Servidor iniciado (PID: $SERVER_PID)"
else
    echo "   ✅ Servidor já está rodando"
fi

echo ""
echo "2. Executando consultas de demonstração..."
echo "   Consultas que serão executadas:"
echo "   - Toyota"
echo "   - Honda até 70000"
echo "   - Carros de 2020 a 2023"
echo "   - Flex automático"
echo ""

# Executar a aplicação com as consultas de demonstração
cat demo_queries.txt | python3 -m src.cli_app

echo ""
echo "3. Demonstração concluída!"

# Parar o servidor se foi iniciado por este script
if [ ! -z "$SERVER_PID" ]; then
    echo "   Parando servidor..."
    kill $SERVER_PID 2>/dev/null
    echo "   ✅ Servidor parado"
fi

echo ""
echo "Para usar interativamente:"
echo "1. python3 -m src.server.main &"
echo "2. python3 -m src.cli_app"

