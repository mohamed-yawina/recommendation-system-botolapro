import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { authService } from '../services/api';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await authService.login(email, password);
      navigate('/');
    } catch (err) {
      setError('Identifiants invalides');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-botola-green to-gray-900 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-display font-bold text-botola-green mb-2">Scouting Assistant</h1>
          <p className="text-gray-500">Connectez-vous à votre espace Club</p>
        </div>

        {error && (
          <div className="bg-red-50 text-red-600 p-3 rounded-lg mb-4 text-sm text-center">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-botola-green focus:border-transparent outline-none transition-all"
              placeholder="club@botola.ma"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Mot de passe</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-botola-green focus:border-transparent outline-none transition-all"
              placeholder="••••••••"
              required
            />
          </div>

          <button
            type="submit"
            className="w-full bg-botola-green text-white font-bold py-3 rounded-lg hover:bg-green-800 transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
          >
            Se connecter
          </button>
        </form>

        <div className="mt-6 text-center text-sm text-gray-500">
          <p>Compte de démo: admin@botola.com / admin</p>
        </div>
      </div>
    </div>
  );
};

export default Login;
