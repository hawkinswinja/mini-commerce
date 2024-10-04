import { useState, useEffect } from 'react';
import axios from 'axios';
axios.defaults.withCredentials = true;


const products = [
    { id: 1, name: 'Product 1', stock: 10, price: 20 },
    { id: 2, name: 'Product 2', stock: 5, price: 35 },
    { id: 3, name: 'Product 3', stock: 15, price: 15 },
];

// Function to get a cookie by name
const getCookie = (name) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
};

  // Function to set a cookie
const setCookie = (name, value, days = 7) => {
  let expires = '';
  if (days) {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    expires = `; expires=${date.toUTCString()}`;
  }
  document.cookie = `${name}=${value || ''}${expires}; path=/`;
};

const useAuth = () => { 
  const [isAuth, setIsAuth] = useState(null);  
  useEffect(() => {
      const checkAuth = async () => {
          try {
              const response = await axios.get(
                  '/api/user/isauthenticated/', 
                  {
                      withCredentials: true,
                  }
              );
              const auth = response.data.authenticated;
              // console.log('auth', auth);
              setIsAuth(auth);
              // console.log(auth);
          } catch (error) {
              setIsAuth(false);
              console.error('Error checking authentication', error);
          }
      };

      checkAuth();
  }, []);
  return isAuth;
}

const setCSRF = async () => {
  const response = await axios.get('/api/user/csrf/');
  setCookie('csrftoken', response.data.csrftoken);
};

export { getCookie, setCookie, products, setCSRF, useAuth};