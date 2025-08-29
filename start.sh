#!/bin/bash
set -e

echo "�� Iniciando PNTP Fullstack..."

# Verificar arquivos
if [ ! -f "backend/app/main.py" ]; then
    echo "❌ backend/app/main.py não encontrado!"
    exit 1
fi

# Instalar dependências do backend se necessário
if [ -f "backend/requirements.txt" ]; then
    echo "�� Instalando dependências do backend..."
    pip install -r backend/requirements.txt
elif [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências da raiz..."
    pip install -r requirements.txt
fi

# Configurar porta
export PORT=${PORT:-8000}

echo "🌐 Servidor iniciando na porta $PORT"
echo "📡 API disponível em: /api/*"
echo "🎨 React App disponível em: /"

# Adicionar backend ao PYTHONPATH e iniciar servidor
export PYTHONPATH="${PYTHONPATH}:$(pwd)/backend"
exec uvicorn backend.app.main:app \
    --host 0.0.0.0 \
    --port $PORT \
    --workers 1 \
    --log-level info