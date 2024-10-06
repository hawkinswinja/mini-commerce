import React from 'react';
import { useEffect, useState } from 'react';
import axios from 'axios';
axios.defaults.withCredentials = true;

const OrdersPage = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch orders from the backend
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    const response = await axios.get('/api/orders/',
      { withCredentials: true }
    );
    
    if (response.status === 200) {
      // console.log(response.data); # update to response.data.results when using pagination
      setOrders(response.data);
      // console.log('Orders:', orders)
    } else {
      alert('Failed to fetch orders');
      console.error('Failed to fetch orders', response);
    }
    setLoading(false);
  };

  return (
    <div className="container mt-5">
      <h2>Your Orders</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="table table-bordered">
          <thead>
            <tr>
              <th>Item</th>
              <th>Amount</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {orders.map(order => (
              <tr key={order.order_id}>
                <td>{order.product}</td>
                <td>{order.total}</td>
                <td>{new Date(order.created_at).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default OrdersPage;
