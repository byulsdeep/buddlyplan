import axios from 'axios';

// Create an Axios instance with a predefined base URL.
// This means you don't have to type 'http://localhost:8000/api/v1' for every call.
const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

// We will add an interceptor here later to automatically attach the JWT token.
// apiClient.interceptors.request.use(config => { ... });

export default apiClient;