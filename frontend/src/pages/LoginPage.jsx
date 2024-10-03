import React, { useEffect } from 'react';
import Cookies from 'js-cookie';

const LoginPage = () => {
  // Function to handle login button click
  const googleLogin = () => {
    // const oidcLoginUrl = import.meta.env.VITE_BACKEND_URL || 'http://backend';
    window.location.href = '/api/oidc/authenticate/';
    // Redirect to Django OIDC login page and return to /orders after successful login
  };

  // Check for sessionId in cookies when the component mounts
  useEffect(() => {
    const sessionId = Cookies.get('sessionid');
    console.log('username:', Cookies.get('username'));
    if (sessionId) {
      // Redirect to /orders if sessionId exists
      window.location.href = '/orders';
    }
  }, []);

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <h2 className="text-center mb-4">Login</h2>
          <div className="text-center">
            <button className="btn btn-primary" onClick={googleLogin}>Login with OIDC</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
