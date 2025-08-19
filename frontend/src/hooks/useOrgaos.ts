import { useState, useEffect, useCallback } from 'react';
import { OrgaoMap, EstatisticasMapa, FiltrosOrgaos } from '../types/orgaos';
import { OrgaosApiService } from '../services/orgaosApi';

interface UseOrgaosReturn {
  orgaos: OrgaoMap[];
  estatisticas: EstatisticasMapa | null;
  loading: boolean;
  error: string | null;
  buscarOrgaos: (termo: string, filtros?: FiltrosOrgaos) => Promise<void>;
  recarregarOrgaos: () => Promise<void>;
}

export const useOrgaos = (filters: FiltrosOrgaos = {}): UseOrgaosReturn => {
  const [orgaos, setOrgaos] = useState<OrgaoMap[]>([]);
  const [estatisticas, setEstatisticas] = useState<EstatisticasMapa | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadOrgaos = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      
      const [orgaosData, statsData] = await Promise.all([
        OrgaosApiService.fetchOrgaos(filters),
        OrgaosApiService.fetchEstatisticas()
      ]);
      
      setOrgaos(orgaosData);
      setEstatisticas(statsData);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro desconhecido';
      setError(errorMessage);
      console.error('Erro ao carregar órgãos:', err);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    loadOrgaos();
  }, [loadOrgaos]);

  const buscarOrgaos = async (termo: string, filtros: FiltrosOrgaos = {}) => {
    try {
      setLoading(true);
      setError(null);
      const resultados = await OrgaosApiService.buscarOrgaos(termo, filtros);
      setOrgaos(resultados.resultados);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro na busca';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    orgaos,
    estatisticas,
    loading,
    error,
    buscarOrgaos,
    recarregarOrgaos: loadOrgaos
  };
};
