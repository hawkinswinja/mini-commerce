import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        axios.get('/api/current_user/')
            .then(response => {
                setUser(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the user!', error);
            });
    }, []);

    return (
        <div>
            <h1>Welcome to M-Commerce</h1>
            <p>Your one-stop shop for all your needs.</p>
            {user && (
                <div>
                    <h2>Welcome back, {user.username}!</h2>
                </div>
            )}
        </div>
    );
};

export default Home;