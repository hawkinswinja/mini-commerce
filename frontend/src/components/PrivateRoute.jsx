import { Navigate } from 'react-router-dom';
import { useAuth } from '../utils';

const PrivateRoute = ({ element: Element }) => {
    const isAuth = useAuth();
    if (isAuth === null)
        return null;
    return isAuth ? Element : <Navigate to="/login" />;
};

export default PrivateRoute;