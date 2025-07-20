import { useState } from 'react';
import type { FormEvent } from 'react';
import { useNavigate } from 'react-router-dom';
import apiClient from '../api'; // Our configured Axios client
import { useAuthStore } from '../store/authStore';

const LoginPage = () => {
  const [email, setEmail] = useState(''); // We use email as the username
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { setTokens, setUser } = useAuthStore();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setError('');

    try {
      // Create the form data object for OAuth2
      const formData = new URLSearchParams();
      formData.append('username', email); // The backend expects 'username' field
      formData.append('password', password);

      // Call the /token endpoint
      const response = await apiClient.post('/auth/token', formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      
      const { access_token, refresh_token } = response.data;
      
      // Save tokens to our Zustand store
      setTokens({ accessToken: access_token, refreshToken: refresh_token });

      // Fetch the user's profile with the new token
      const userResponse = await apiClient.get('/users/me', {
          headers: { Authorization: `Bearer ${access_token}` }
      });
      
      // Save user to our Zustand store
      setUser(userResponse.data);

      // Redirect to the homepage on successful login
      navigate('/');

    } catch (err: any) {
      console.error(err);
      setError('Failed to log in. Please check your credentials.');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;