import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const authService = {
  login: async (email, password) => {
    const response = await api.post('/auth/login', { email, password });
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
      localStorage.setItem('club_id', response.data.club_id);
    }
    return response.data;
  },
  logout: () => {
    localStorage.removeItem('token');
    localStorage.removeItem('club_id');
  },
  getCurrentUser: () => {
    return localStorage.getItem('token');
  }
};

export const playerService = {
  getAll: async () => {
    const response = await api.get('/players');
    return response.data;
  },
  getRecommendations: async (playerId) => {
    const response = await api.get(`/recommendations/${playerId}`);
    return response.data;
  },
  create: async (data) => {
    const response = await api.post('/players', data);
    return response.data;
  },
  delete: async (id) => {
    await api.delete(`/players/${id}`);
  }
};

export default api;
