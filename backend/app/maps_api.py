# app/maps_api.py
from fastapi import APIRouter, HTTPException
from typing import Dict, List, Optional
from pydantic import BaseModel
import json
from geopy.distance import geodesic

# Importar seus dados existentes - CORRIGIDO para usar import relativo
from .services.orgaos_data import ORGAOS_DATA

router = APIRouter()

# Coordenadas de Manaus como referência
COORDENADAS_MANAUS = {
    'latitude': -3.1190,
    'longitude': -60.0217
}

class OrgaoMap(BaseModel):
    id: str
    nome: str
    endereco: str
    latitude: float
    longitude: float
    site: str
    transparencia: str
    tipo: str
    esfera: str
    poder: str
    distancia_manaus: Optional[float] = None

@router.get("/api/orgaos-mapa", response_model=List[OrgaoMap])
async def get_orgaos_para_mapa(
    esfera: Optional[str] = None,
    poder: Optional[str] = None,
    raio_km: Optional[float] = None
):
    """
    Retorna todos os órgãos formatados para exibição no mapa
    """
    orgaos_mapa = []
    
    for esfera_nome, esferas in ORGAOS_DATA.items():
        # Filtrar por esfera se especificado
        if esfera and esfera_nome.lower() != esfera.lower():
            continue
            
        for poder_nome, poderes in esferas.items():
            # Filtrar por poder se especificado
            if poder and poder_nome.lower() != poder.lower():
                continue
                
            for orgao_nome, dados in poderes.items():
                # Verificar se tem coordenadas
                if dados.get('coordenadas'):
                    coords = dados['coordenadas']
                    
                    # Calcular distância de Manaus
                    distancia = geodesic(
                        (COORDENADAS_MANAUS['latitude'], COORDENADAS_MANAUS['longitude']),
                        (coords['latitude'], coords['longitude'])
                    ).kilometers
                    
                    # Filtrar por raio se especificado
                    if raio_km and distancia > raio_km:
                        continue
                    
                    orgao_map = OrgaoMap(
                        id=f"{esfera_nome}_{poder_nome}_{orgao_nome}".replace(" ", "_").replace("-", "_"),
                        nome=orgao_nome,
                        endereco=dados.get('endereco', ''),
                        latitude=coords['latitude'],
                        longitude=coords['longitude'],
                        site=dados.get('site', ''),
                        transparencia=dados.get('transparencia', ''),
                        tipo=f"{esfera_nome} - {poder_nome}",
                        esfera=esfera_nome,
                        poder=poder_nome,
                        distancia_manaus=round(distancia, 1)
                    )
                    
                    orgaos_mapa.append(orgao_map)
    
    return orgaos_mapa

@router.get("/api/estatisticas-mapa")
async def get_estatisticas_mapa():
    """
    Retorna estatísticas para o dashboard do mapa
    """
    orgaos = await get_orgaos_para_mapa()
    
    # Contar por esfera
    por_esfera = {}
    for orgao in orgaos:
        esfera = orgao.esfera
        por_esfera[esfera] = por_esfera.get(esfera, 0) + 1
    
    # Contar por poder
    por_poder = {}
    for orgao in orgaos:
        poder = orgao.poder
        por_poder[poder] = por_poder.get(poder, 0) + 1
    
    # Calcular distância média de Manaus
    distancias = [o.distancia_manaus for o in orgaos if o.distancia_manaus]
    distancia_media = round(sum(distancias) / len(distancias), 1) if distancias else 0
    
    return {
        "total_orgaos": len(orgaos),
        "por_esfera": por_esfera,
        "por_poder": por_poder,
        "distancia_media_manaus": distancia_media,
        "orgao_mais_distante": max(distancias) if distancias else 0,
        "orgao_mais_proximo": min(distancias) if distancias else 0
    }

@router.get("/api/orgao/{orgao_id}")
async def get_orgao_detalhes(orgao_id: str):
    """
    Retorna detalhes específicos de um órgão
    """
    orgaos = await get_orgaos_para_mapa()
    orgao = next((o for o in orgaos if o.id == orgao_id), None)
    
    if not orgao:
        raise HTTPException(status_code=404, detail="Órgão não encontrado")
    
    return orgao

@router.get("/api/buscar-orgaos")
async def buscar_orgaos(
    termo: str,
    esfera: Optional[str] = None,
    poder: Optional[str] = None
):
    """
    Busca órgãos por termo de pesquisa
    """
    orgaos = await get_orgaos_para_mapa(esfera=esfera, poder=poder)
    
    termo_lower = termo.lower()
    resultados = [
        orgao for orgao in orgaos
        if termo_lower in orgao.nome.lower() or 
           termo_lower in orgao.endereco.lower() or
           termo_lower in orgao.tipo.lower()
    ]
    
    return {
        "termo_pesquisado": termo,
        "total_encontrados": len(resultados),
        "resultados": resultados
    }
