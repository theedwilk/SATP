// Conteúdo do arquivo: src/hooks/useOrgaos.ts

import { useState, useEffect, useCallback } from 'react';
import { OrgaoMap, EstatisticasMapa, FiltrosOrgaos, ResultadoBusca } from '../types/orgaos'; // Importações corrigidas
import { OrgaosApiService } from '../services/orgaosApi';

interface UseOrgaosReturn {
  orgaos: OrgaoMap[];
  estatisticas: EstatisticasMapa | null;
  filters: FiltrosOrgaos;
  setFilters: (newFilters: FiltrosOrgaos) => void;
  isLoading: boolean;
  error: string | null;
  refreshOrgaos: () => void;
}

export const useOrgaos = (): UseOrgaosReturn => {
  const [orgaos, setOrgaos] = useState<OrgaoMap[]>([]);
  const [estatisticas, setEstatisticas] = useState<EstatisticasMapa | null>(null);
  const [filters, setFilters] = useState<FiltrosOrgaos>({});
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchOrgaos = useCallback(async () => {
    setIsLoading(true);
    setError(null);
    try {
      // Assumindo que OrgaosApiService.buscarOrgaosMapa agora retorna ResultadoBusca
      const data: ResultadoBusca = await OrgaosApiService.buscarOrgaosMapa(filters);
      setOrgaos(data.orgaos);
      setEstatisticas(data.estatisticas);
    } catch (err: any) {
      setError(err.message || 'Erro ao carregar órgãos.');
      console.error('Erro ao buscar órgãos:', err);
    } finally {
      setIsLoading(false);
    }
  }, [filters]); // Refetch quando os filtros mudam

  useEffect(() => {
    fetchOrgaos();
  }, [fetchOrgaos]);

  const refreshOrgaos = useCallback(() => {
    fetchOrgaos();
  }, [fetchOrgaos]);

  return {
    orgaos,
    estatisticas,
    filters,
    setFilters,
    isLoading,
    error,
    refreshOrgaos,
  };
};
