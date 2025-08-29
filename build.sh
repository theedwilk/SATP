#!/bin/bash
set -e

echo "🚀 PNTP - Iniciando build fullstack..."

# Mover para a pasta do frontend e verificar o package.json lá
cd frontend
if [ ! -f "package.json" ]; then
    echo "❌ Erro: package.json não encontrado na pasta 'frontend'!"
    exit 1
fi
echo "✅ package.json encontrado!"

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

# Voltar para a pasta raiz do projeto
cd ..

# Instalar dependências Python
echo "🐍 Instalando dependências Python..."
pip install -r requirements.txt

# Preparar diretório estático
echo "📁 Configurando arquivos estáticos..."
mkdir -p app/static

# Copiar os arquivos do frontend build para o diretório do backend
# O caminho agora é 'frontend/build'
cp -r frontend/build/* app/static/

# Verificações finais
if [ ! -f "app/static/index.html" ]; then
    echo "❌ Erro: index.html não foi copiado!"
    exit 1
fi

echo "✅ Build concluído com sucesso!"