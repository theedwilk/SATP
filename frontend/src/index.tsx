// Conteúdo do arquivo: src/index.tsx (ou main.tsx)

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Seus estilos globais, incluindo TailwindCSS
import App from './App'; // Importa o novo componente App

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
