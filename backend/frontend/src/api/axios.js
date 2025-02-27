import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000',  // or your backend URL
});

// Add an interceptor to include the token in all requests
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('access_token');  // or however you store your token
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api; 