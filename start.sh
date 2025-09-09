#!/bin/bash
set -e
echo "🚀 Iniciando PNTP Fullstack..."

# CORRIGIR: Verificar arquivos no local correto
if [ ! -f "app/main.py" ]; then
    echo "❌ app/main.py não encontrado!"
    exit 1
fi

# Instalar dependências (mantenha como está)
if [ -f "backend/requirements.txt" ]; then
    echo "📦 Instalando dependências do backend..."
    pip install -r backend/requirements.txt
elif [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências da raiz..."
    pip install -r requirements.txt
fi

# Configurar porta (mantenha como está)
export PORT=${PORT:-8000}
echo "🌐 Servidor iniciando na porta $PORT"
echo "📡 API disponível em: /api/*"
echo "🎨 React App disponível em: /"

# CORRIGIR: PYTHONPATH e comando uvicorn
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
exec uvicorn app.main:app \
    --host 0.0.0.0 \
    --port $PORT \
    --workers 1 \
    --log-level info
