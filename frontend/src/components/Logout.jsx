import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';

export const logout = async (navigate) => {
  try {
    // Make POST request to logout endpoint
    const response = await axios.post('/api/api-auth/logout/', {}, {
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken'), // Include CSRF token
      },
      withCredentials: true, // Send sessionid with the request
    });

    if (response.status === 200) {
      // Clear CSRF and session cookies
      Cookies.remove('csrftoken');
      Cookies.remove('sessionid');

      // Redirect to login page
      navigate('/login');
    }
  } catch (error) {
    console.error('Logout failed:', error);
  }
};
