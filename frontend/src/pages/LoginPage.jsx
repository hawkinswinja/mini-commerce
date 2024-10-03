// import React, { useEffect } from 'react';
// import Cookies from 'js-cookie';

// const LoginPage = () => {
//   // Function to handle login button click
//   const googleLogin = () => {
//     // const oidcLoginUrl = import.meta.env.VITE_BACKEND_URL || 'http://backend';
//     window.location.href = '/api/oidc/authenticate/';
//     // Redirect to Django OIDC login page and return to /orders after successful login
//   };

//   // Check for sessionId in cookies when the component mounts
//   useEffect(() => {
//     const sessionId = Cookies.get('sessionid');
//     console.log('username:', Cookies.get('username'));
//     if (sessionId) {
//       // Redirect to /orders if sessionId exists
//       window.location.href = '/orders';
//     }
//   }, []);

//   return (
//     <div className="container mt-5">
//       <div className="row justify-content-center">
//         <div className="col-md-6">
//           <h2 className="text-center mb-4">Login</h2>
//           <div className="text-center">
//             <button className="btn btn-primary" onClick={googleLogin}>Login with OIDC</button>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default LoginPage;


import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { getCookie } from '../utils';
axios.defaults.withCredentials = true;

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Function to handle OIDC login button click
  const googleLogin = () => {
    window.location.href = '/api/oidc/authenticate/';
  };

  // Handle form submission for username/password login
  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMessage(''); // Clear any previous errors

    try {
      const response = await axios.post(
        '/api/api-auth/login/',
        { username, password },
        {
          headers: {
            'X-CSRFToken': getCookie('csrftoken'), // CSRF token from cookies
          },
          withCredentials: true, 
        }
      );

      if (response.status === 200) {
        // If login is successful, redirect to orders page
        window.location.href = '/products';
      } else {
        // Handle login failure (e.g., invalid credentials)
        setErrorMessage('Invalid username or password');
      }
    } catch (error) {
      console.error('Login failed', error);
      setErrorMessage('Something went wrong. Please try again later.');
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h2 className="text-center mb-4">Login</h2>

          {/* Username/Password Login Form */}
          <form onSubmit={handleLogin}>
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                type="text"
                id="username"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {errorMessage && (
              <div className="alert alert-danger mt-3">
                {errorMessage}
              </div>
            )}

            <div className="text-center mt-4">
              <button type="submit" className="btn btn-success">
                Login with Username and Password
              </button>
            </div>
          </form>
          <h2 className="text-center mb-4"></h2>
          {/* OIDC Login Button */}
          <div className="text-center mb-4">
            <button className="btn btn-primary" onClick={googleLogin}>
              Continue with Google
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
