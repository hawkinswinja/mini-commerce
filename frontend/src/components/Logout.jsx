import React from 'react';
import axios from 'axios';
import { getCookie } from '../utils';
import Cookies from 'js-cookie';

export const logout = async (navigate) => {
  try {
    // Make POST request to logout endpoint
    const response = await axios.post('/api/auth/logout/', {}, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
      },
      withCredentials: true, // Send sessionid with the request
    });

    if (response.status === 200) {
      // Clear CSRF and session cookies
      Cookies.remove('csrftoken');
      Cookies.remove('sessionid');

      // Redirect to login page
      navigate('/');
    }
  } catch (error) {
    alert('Logout failed', error);
    // console.error('Logout failed:', error);
  }
};
//     }
