#!/bin/bash
set -e

echo "🚀 Iniciando PNTP Fullstack..."

# Verificar arquivos
if [ ! -f "app/main.py" ]; then
    echo "❌ app/main.py não encontrado!"
    exit 1
fi

# Configurar porta
export PORT=${PORT:-8000}

echo "🌐 Servidor iniciando na porta $PORT"
echo "📡 API disponível em: /api/*"
echo "🎨 React App disponível em: /"

# Iniciar servidor
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port $PORT \
    --workers 1 \
    --log-level info