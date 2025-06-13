# scraper.py - Versão melhorada
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import os
import re
from datetime import datetime

class TransparenciaScraperTurbinado:
    def __init__(self, headless=True):
        self.setup_driver(headless)
        self.screenshots_dir = 'screenshots'
        self.create_screenshots_dir()
        
    def setup_driver(self, headless):
        """Configura o driver do Selenium"""
        options = webdriver.ChromeOptions()
        
        if headless:
            options.add_argument('--headless')
        
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_page_load_timeout(30)
            print("✅ WebDriver configurado")
        except Exception as e:
            print(f"❌ Erro no WebDriver: {e}")
            raise
            
    def create_screenshots_dir(self):
        """Cria diretório para screenshots"""
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
            
    def take_screenshot(self, name, url):
        """Tira screenshot da página"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(self.screenshots_dir, filename)
            
            self.driver.save_screenshot(filepath)
            return {
                'filename': filename,
                'path': filepath,
                'url': url,
                'timestamp': timestamp
            }
        except Exception as e:
            print(f"Erro no screenshot: {e}")
            return None
            
    def search_and_interact(self, search_terms, criterion_name):
        """Busca por termos específicos na página"""
        result = {
            'encontrado': False,
            'screenshots': [],
            'observacoes': [],
            'links_relacionados': []
        }
        
        try:
            # Busca por links
            for term in search_terms:
                links = self.driver.find_elements(By.PARTIAL_LINK_TEXT, term)
                for link in links:
                    try:
                        href = link.get_attribute('href')
                        if href and href not in result['links_relacionados']:
                            result['links_relacionados'].append(href)
                            result['encontrado'] = True
                            result['observacoes'].append(f"Link encontrado: '{term}'")
                    except:
                        continue
                
                # Busca no texto da página
                try:
                    page_text = self.driver.find_element(By.TAG_NAME, 'body').text.lower()
                    if term.lower() in page_text:
                        result['encontrado'] = True
                        result['observacoes'].append(f"Termo '{term}' encontrado na página")
                except:
                    continue
                    
        except Exception as e:
            result['observacoes'].append(f"Erro na busca: {str(e)}")
            
        return result
    
    def check_data_freshness(self):
        """Verifica se os dados estão atualizados"""
        observations = []
        try:
            date_patterns = [
                r'\d{1,2}/\d{1,2}/\d{4}',
                r'\d{4}-\d{1,2}-\d{1,2}',
                r'(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+\d{4}'
            ]
            
            page_text = self.driver.find_element(By.TAG_NAME, 'body').text
            current_year = datetime.now().year
            
            for pattern in date_patterns:
                dates = re.findall(pattern, page_text, re.IGNORECASE)
                for date in dates:
                    if str(current_year) in str(date):
                        observations.append(f"Dados atualizados (data: {date})")
                        return observations
                        
            observations.append("Atualidade não verificada")
            
        except Exception as e:
            observations.append(f"Erro na verificação: {str(e)}")
            
        return observations
    
    def check_download_options(self):
        """Verifica opções de download"""
        download_info = {
            'tem_download': False,
            'formatos': [],
            'observacoes': []
        }
        
        try:
            download_indicators = ['download', 'baixar', 'exportar', 'csv', 'xlsx', 'pdf']
            
            for indicator in download_indicators:
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, indicator)
                if elements:
                    download_info['tem_download'] = True
                    download_info['observacoes'].append(f"Download disponível: {indicator}")
                    
                    if 'csv' in indicator.lower():
                        download_info['formatos'].append('CSV')
                    elif 'xlsx' in indicator.lower():
                        download_info['formatos'].append('XLSX')
                    elif 'pdf' in indicator.lower():
                        download_info['formatos'].append('PDF')
                            
        except Exception as e:
            download_info['observacoes'].append(f"Erro: {str(e)}")
            
        return download_info
    
    def avaliar_criterio(self, url, criterio):
        """Avalia um critério específico"""
        resultado = {
            'nome': criterio['nome'],
            'pergunta': criterio['pergunta'],
            'atende': False,
            'disponibilidade': False,
            'atualidade': False,
            'download_disponivel': False,
            'screenshots': [],
            'observacoes': []
        }
        
        try:
            # Navega para a URL
            self.driver.get(url)
            time.sleep(random.uniform(2, 4))
            
            # Screenshot inicial
            screenshot = self.take_screenshot(f"{criterio['nome']}_inicial", url)
            if screenshot:
                resultado['screenshots'].append(screenshot)
            
            # Busca pelos termos
            busca_resultado = self.search_and_interact(criterio['termos_busca'], criterio['nome'])
            
            if busca_resultado['encontrado']:
                resultado['atende'] = True
                resultado['disponibilidade'] = True
                resultado['observacoes'].extend(busca_resultado['observacoes'])
                
                # Se encontrou links, visita o primeiro
                if busca_resultado['links_relacionados']:
                    link = busca_resultado['links_relacionados'][0]
                    
                    try:
                        self.driver.get(link)
                        time.sleep(2)
                        
                        # Verifica atualidade
                        freshness_obs = self.check_data_freshness()
                        resultado['observacoes'].extend(freshness_obs)
                        if 'atualizados' in str(freshness_obs):
                            resultado['atualidade'] = True
                            
                        # Verifica downloads
                        download_info = self.check_download_options()
                        if download_info['tem_download']:
                            resultado['download_disponivel'] = True
                            resultado['observacoes'].extend(download_info['observacoes'])
                            
                        # Screenshot da página específica
                        screenshot_detalhe = self.take_screenshot(f"{criterio['nome']}_detalhe", link)
                        if screenshot_detalhe:
                            resultado['screenshots'].append(screenshot_detalhe)
                        
                    except Exception as e:
                        resultado['observacoes'].append(f"Erro ao acessar link: {str(e)}")
                        
            else:
                resultado['observacoes'].append("Informação não encontrada")
                
        except Exception as e:
            resultado['observacoes'].append(f"Erro na avaliação: {str(e)}")
            
        return resultado

# Dicionário com URLs conhecidas dos órgãos do Amazonas
URLS_CONHECIDAS = {
    'Tribunal de Contas do Estado do Amazonas': 'https://www2.tce.am.gov.br',
    'Governo do Estado do Amazonas': 'https://www.amazonas.am.gov.br',
    'Assembleia Legislativa do Amazonas': 'https://www.ale.am.gov.br',
    'Ministério Público do Amazonas': 'https://www.mpam.mp.br',
    'Defensoria Pública do Amazonas': 'https://www.defensoria.am.def.br',
    'Prefeitura de Manaus': 'https://www.manaus.am.gov.br',
    'Câmara Municipal de Manaus': 'https://www.cmm.am.gov.br',
    'Prefeitura de Parintins': 'https://www.parintins.am.gov.br',
    'Prefeitura de Itacoatiara': 'https://www.itacoatiara.am.gov.br',
    'Prefeitura de Maués': 'https://www.maues.am.gov.br',
    'Prefeitura de Tefé': 'https://www.tefe.am.gov.br',
    'Prefeitura de Coari': 'https://www.coari.am.gov.br'
}

def encontrar_site_oficial(esfera, matriz, orgao):
    """Encontra o site oficial - primeiro tenta URLs conhecidas, depois busca"""
    
    print(f"🔍 Buscando site para: {orgao}")
    
    # Primeiro, verifica se temos a URL conhecida
    if orgao in URLS_CONHECIDAS:
        url = URLS_CONHECIDAS[orgao]
        print(f"✅ URL conhecida encontrada: {url}")
        
        # Testa se a URL está acessível
        if testar_url_acessivel(url):
            return url
        else:
            print(f"❌ URL conhecida não está acessível: {url}")
    
    # Se não tiver ou não estiver acessível, faz busca
    print("🔍 Fazendo busca no Google...")
    return buscar_site_google(esfera, matriz, orgao)

def testar_url_acessivel(url):
    """Testa se uma URL está acessível"""
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(10)
        
        driver.get(url)
        time.sleep(2)
        
        # Verifica se carregou uma página válida
        title = driver.title
        if title and len(title.strip()) > 0:
            return True
        
    except Exception as e:
        print(f"Erro ao testar URL {url}: {e}")
        return False
    finally:
        if driver:
            driver.quit()
    
    return False

def buscar_site_google(esfera, matriz, orgao):
    """Busca o site oficial através do Google"""
    
    # Monta query de busca melhorada
    queries = []
    
    if esfera == 'Municipal':
        if 'Prefeitura' in orgao:
            municipio = orgao.replace('Prefeitura de ', '')
            queries = [
                f'site:gov.br prefeitura {municipio} amazonas',
                f'prefeitura {municipio} amazonas site oficial',
                f'{municipio}.am.gov.br'
            ]
        elif 'Câmara' in orgao:
            municipio = orgao.replace('Câmara Municipal de ', '')
            queries = [
                f'site:gov.br câmara municipal {municipio} amazonas',
                f'câmara municipal {municipio} amazonas site oficial'
            ]
    elif esfera == 'Estadual':
        if 'Tribunal de Contas' in orgao:
            queries = [
                'site:tce.am.gov.br',
                'tribunal contas estado amazonas site oficial',
                'TCE amazonas'
            ]
        elif matriz == 'Poder Executivo':
            queries = [
                'site:amazonas.am.gov.br',
                'governo estado amazonas site oficial'
            ]
        elif matriz == 'Poder Legislativo':
            queries = [
                'site:ale.am.gov.br',
                'assembleia legislativa amazonas site oficial'
            ]
        elif matriz == 'Ministério Público':
            queries = [
                'site:mpam.mp.br',
                'ministério público amazonas site oficial'
            ]
        elif matriz == 'Defensoria':
            queries = [
                'site:defensoria.am.def.br',
                'defensoria pública amazonas site oficial'
            ]
    
    # Tenta cada query
    for query in queries:
        print(f"🔍 Tentando busca: {query}")
        resultado = executar_busca_google(query)
        if resultado:
            print(f"✅ Site encontrado: {resultado}")
            return resultado
    
    print("❌ Nenhum site oficial encontrado")
    return None

def executar_busca_google(query):
    """Executa uma busca específica no Google"""
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(15)
        
        # Busca no Google
        driver.get('https://www.google.com')
        time.sleep(2)
        
        # Aceita cookies se aparecer
        try:
            accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Aceitar') or contains(text(), 'Accept')]")
            accept_button.click()
            time.sleep(1)
        except:
            pass
        
        # Faz a busca
        search_box = driver.find_element(By.NAME, 'q')
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
        
        time.sleep(3)
        
        # Pega os resultados
        results = driver.find_elements(By.CSS_SELECTOR, 'h3')
        
        for result in results[:5]:  # Verifica os 5 primeiros
            try:
                parent = result.find_element(By.XPATH, '..')
                href = parent.get_attribute('href')
                
                if href and is_official_domain(href):
                    # Testa se a URL funciona
                    if testar_url_acessivel(href):
                        return href
                        
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Erro na busca Google: {e}")
        return None
    finally:
        if driver:
            driver.quit()
    
    return None

def is_official_domain(url):
    """Verifica se é um domínio oficial"""
    if not url:
        return False
        
    official_indicators = [
        '.gov.br', '.am.gov.br', '.leg.br', '.mp.br', '.def.br',
        'prefeitura', 'camara', 'governo', 'assembleia', 
        'tribunal', 'defensoria', 'tce.am', 'ale.am', 'mpam'
    ]
    
    url_lower = url.lower()
    
    # Verifica se contém indicadores oficiais
    has_official = any(indicator in url_lower for indicator in official_indicators)
    
    # Exclui alguns domínios não-oficiais comuns
    excluded = ['facebook.com', 'youtube.com', 'instagram.com', 'twitter.com', 'linkedin.com']
    has_excluded = any(excluded_site in url_lower for excluded_site in excluded)
    
    return has_official and not has_excluded
