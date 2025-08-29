#!/bin/bash
set -e

echo "🚀 PNTP - Iniciando build fullstack..."

# Verificar arquivos essenciais
if [ ! -f "package.json" ]; then
    echo "❌ Erro: package.json não encontrado!"
    exit 1
fi

if [ ! -f "app/main.py" ]; then
    echo "❌ Erro: app/main.py não encontrado!"
    exit 1
fi

# Mostrar versões
echo "📋 Versões instaladas:"
echo "   Python: $(python --version)"
echo "   Node: $(node --version)"  
echo "   NPM: $(npm --version)"

# Instalar dependências do frontend
echo "📦 Instalando dependências do React..."
npm ci

# Build do frontend
echo "🔨 Buildando React..."
npm run build

# Verificar se build foi criado
if [ ! -d "build" ]; then
    echo "❌ Build do React falhou!"
    exit 1
fi

# Instalar dependências Python
echo "🐍 Instalando dependências Python..."
pip install -r requirements.txt

# Preparar diretório estático
echo "📁 Configurando arquivos estáticos..."
mkdir -p app/static
cp -r build/* app/static/

# Verificações finais
if [ ! -f "app/static/index.html" ]; then
    echo "❌ Erro: index.html não foi copiado!"
    exit 1
fi

echo "✅ Build concluído com sucesso!"