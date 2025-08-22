import React from 'react';

// 1. Definir uma interface para o tipo de dado de cada item do ranking
interface RankingDataItem {
  entidade: string;
  municipio: string;
  uf: string;
  indice_final: number;
  nivel_final: string;
}

// Dados extraídos e filtrados para a UF 'AM' do seu arquivo CSV.
// Importante: Não há registros para 'AM' no arquivo que você forneceu,
// portanto, esta array estará vazia.
// Agora, 'filteredDataAM' é explicitamente tipado como um array de 'RankingDataItem'.
const filteredDataAM: RankingDataItem[] = [];

const RankingPage: React.FC = () => {
  return (
    <div className="flex-1 bg-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-extrabold text-blue-900 mb-6 text-center">
          🏆 Ranking de Conformidade (UF: AM)
        </h1>
        <div className="card text-center text-gray-700 p-6 bg-white rounded-lg shadow-md">
          {filteredDataAM.length === 0 ? (
            <p className="text-lg mb-4">
              Não foram encontrados dados para a UF 'AM' no arquivo fornecido.
              Por favor, verifique o arquivo ou tente outro filtro.
            </p>
          ) : (
            <>
              <p className="text-lg mb-4">
                Esta é a lista de órgãos e municípios da UF 'AM' com base nos resultados das auditorias:
              </p>
              <div className="overflow-x-auto">
                <table className="min-w-full bg-white border border-gray-300">
                  <thead>
                    <tr>
                      <th className="py-2 px-4 border-b text-left">Entidade</th>
                      <th className="py-2 px-4 border-b text-left">Município</th>
                      <th className="py-2 px-4 border-b text-left">UF</th>
                      <th className="py-2 px-4 border-b text-left">Índice Final</th>
                      <th className="py-2 px-4 border-b text-left">Nível Final</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredDataAM.map((item, index) => (
                      <tr key={index} className="hover:bg-gray-50">
                        <td className="py-2 px-4 border-b">{item.entidade}</td>
                        <td className="py-2 px-4 border-b">{item.municipio}</td>
                        <td className="py-2 px-4 border-b">{item.uf}</td>
                        <td className="py-2 px-4 border-b">{item.indice_final}</td>
                        <td className="py-2 px-4 border-b">{item.nivel_final}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default RankingPage;
