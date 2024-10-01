import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
    const googleLoginUrl = `${import.meta.env.VITE_BACKEND_URL}/oidc/authenticate/`;
    const navigate = useNavigate();

    // Redirect to home if user is already authenticated
    useEffect(() => {
        // Replace this with your actual authentication check logic
        const isAuthenticated = document.cookie.includes('sessionid'); // Example: check for a session cookie

        if (isAuthenticated) {
            navigate('/'); // Redirect to home if authenticated
        }
    }, [navigate]);

    return (
        <div className="d-flex flex-column align-items-center justify-content-center vh-100 bg-light">
            <div className="text-center">
                <h1 className="mb-4">m-Commerce</h1>
                <button 
                    className="btn btn-primary btn-lg"
                    onClick={() => window.location.href = googleLoginUrl}
                >
                    Continue with Google
                </button>
            </div>
        </div>
    );
};

export default LoginPage;

