# 🔍 Sistema de Avaliação de Portais de Transparência

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Beta](https://img.shields.io/badge/Version-Beta-orange.svg)](https://github.com/seu-usuario/sistema-transparencia)

> Sistema automatizado para auditoria e avaliação de portais de transparência de órgãos públicos do Amazonas, baseado na Lei de Acesso à Informação (LAI) e legislação específica.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Critérios de Avaliação](#critérios-de-avaliação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Roadmap](#roadmap)
- [Licença](#licença)

## 🎯 Sobre o Projeto

O **Sistema de Avaliação de Portais de Transparência** é uma ferramenta desenvolvida para automatizar a auditoria de transparência de órgãos públicos, verificando a conformidade com a Lei de Acesso à Informação (LAI) e outras normativas específicas.

### 🏛️ Órgãos Suportados

**Estaduais:**
- Poder Executivo
- Poder Legislativo  
- Poder Judiciário
- Tribunal de Contas
- Ministério Público
- Defensoria Pública
- Consórcios Públicos
- Estatais (Dependentes e Independentes)

**Municipais:**
- Poder Executivo (62 prefeituras)
- Poder Legislativo (62 câmaras municipais)

## ✨ Funcionalidades

### 🔍 Auditoria Automatizada
- ✅ Verificação automática de **132+ critérios legais**
- ✅ Análise de **~200 órgãos** do Amazonas
- ✅ **Filtros inteligentes** por tipo de poder
- ✅ **Web scraping** automatizado
- ✅ **Scoring** de relevância das evidências

### 📊 Relatórios Detalhados
- ✅ **Métricas de conformidade** em tempo real
- ✅ **Exportação para Excel** (múltiplas abas)
- ✅ **Links de evidência** para cada critério
- ✅ **Fundamentação legal** completa
- ✅ **Observações detalhadas** sobre cada verificação

### 🎨 Interface Intuitiva
- ✅ **Interface web responsiva** com Streamlit
- ✅ **Navegação simplificada** por filtros
- ✅ **Status em tempo real** dos sites
- ✅ **Visualização organizada** por dimensões
- ✅ **Botão flutuante** para navegação

## 🛠️ Tecnologias

- **Frontend:** Streamlit
- **Backend:** Python 3.8+
- **Web Scraping:** BeautifulSoup4, Requests
- **Data Processing:** Pandas, NumPy
- **Export:** OpenPyXL, XlsxWriter
- **Arquitetura:** Modular com critérios separados

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/sistema-transparencia.git
cd sistema-transparencia