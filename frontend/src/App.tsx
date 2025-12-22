import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import PlayerList from './pages/PlayerList';
import Layout from './layout/Layout';
import { authService } from './services/api';

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const token = authService.getCurrentUser();
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  return <>{children}</>;
};

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        
        <Route path="/" element={
          <ProtectedRoute>
            <Layout />
          </ProtectedRoute>
        }>
          <Route index element={<Dashboard />} />
          <Route path="players" element={<PlayerList />} />
          <Route path="recommendations/:id" element={<div className="text-center p-10">Recommandations (À venir)</div>} />
          <Route path="visualization" element={<div className="text-center p-10">Visualisation Graph (À venir)</div>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
