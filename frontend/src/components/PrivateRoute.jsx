import { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie';

const useAuth = () => { 
    const [isAuth, setIsAuth] = useState(null);
    const session = Cookies.get('sessionid');
    console.log('session id: ', session);
  
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
                console.log('auth', auth);
                setIsAuth(auth);
                // console.log(auth);
            } catch (error) {
                setIsAuth(false);
            }
        };

        checkAuth();
    }, []);
    return isAuth;
}


const PrivateRoute = ({ element: Element }) => {
    const isAuth = useAuth();
    // console.log('isAuth', isAuth);
    if (isAuth === null)
        return null;
    return isAuth ? Element : <Navigate to="/login" />;
};

export default PrivateRoute;