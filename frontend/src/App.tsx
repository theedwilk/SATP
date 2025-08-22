// Conteúdo do arquivo: src/App.tsx

import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import HomePage from './components/HomePage';
import AuditoriaPage from './components/AuditoriaPage';
import RankingPage from './components/RankingPage';

// Define os tipos de visualização que o App pode ter
type CurrentView = 'mapa' | 'ranking' | 'auditoria';

const App: React.FC = () => {
  const [currentView, setCurrentView] = useState<CurrentView>('mapa'); // Inicia na página do mapa

  // Renderiza o conteúdo da página com base na visualização atual
  const renderContent = () => {
    switch (currentView) {
      case 'mapa':
        return <HomePage />;
      case 'ranking':
        return <RankingPage />;
      case 'auditoria':
        return <AuditoriaPage />;
      default:
        return <HomePage />; // Fallback
    }
  };

  return (
    <div className="flex min-h-screen">
      {/* O menu lateral */}
      <Sidebar setCurrentView={setCurrentView} currentView={currentView} />
      {/* A área principal de conteúdo */}
      <main className="flex-1 overflow-auto"> {/* Adicionado overflow-auto para permitir rolagem no conteúdo principal */}
        {renderContent()}
      </main>
    </div>
  );
};

export default App;
