#!/bin/bash
set -e
echo "🚀 Iniciando PNTP Fullstack..."

# Verificar arquivos no local correto (estrutura atual)
if [ ! -f "backend/app/main.py" ]; then
    echo "❌ backend/app/main.py não encontrado!"
    exit 1
fi

# Verificar se arquivos estáticos do React existem
if [ ! -f "backend/app/static/index.html" ]; then
    echo "⚠️ Arquivos estáticos do React não encontrados em backend/app/static/"
    echo "Certifique-se que o build foi executado corretamente"
fi

# Instalar dependências
if [ -f "backend/requirements.txt" ]; then
    echo "📦 Instalando dependências do backend..."
    pip install -r backend/requirements.txt
elif [ -f "requirements.txt" ]; then
    echo "📦 Instalando dependências da raiz..."
    pip install -r requirements.txt
else
    echo "❌ requirements.txt não encontrado!"
    exit 1
fi

# Configurar porta
export PORT=${PORT:-8000}
echo "🌐 Servidor iniciando na porta $PORT"
echo "📡 API disponível em: /api/*"
echo "🎨 React App disponível em: /"

# Ajustar PYTHONPATH para incluir o diretório backend
export PYTHONPATH="${PYTHONPATH}:$(pwd):$(pwd)/backend"

# Executar servidor
exec uvicorn backend.app.main:app \
    --host 0.0.0.0 \
    --port $PORT \
    --workers 1 \
    --log-level info
