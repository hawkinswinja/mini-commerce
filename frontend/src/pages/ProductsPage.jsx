import React from 'react';
import { useState } from 'react';
import axios from 'axios';
import { getCookie, setCookie, products } from '../utils';

const ProductPage = () => {
// Fetch cart items from cookies
  const getCartItemsFromCookies = () => {
    const cartCookie = getCookie('cart');
    return cartCookie ? JSON.parse(cartCookie) : [];
  };

  const [showCart, setShowCart] = useState(false);
  const [cart, setCart] = useState(getCartItemsFromCookies());


  // Handle Add to Cart functionality
  const handleAddToCart = (product) => {
    const cart = getCartItemsFromCookies();
    const existingProduct = cart.find((item) => item.id === product.id);
    if (existingProduct) {
      existingProduct.quantity += 1;
    } else {
      cart.push({ id: product.id, name: product.name, quantity: 1, price: product.price });
    }
    setCookie('cart', JSON.stringify(cart));
    setCart(cart);
    alert(`${product.name} added to cart!`);
  };

  // Calculate total price of the cart
  const calculateTotalPrice = () => {
    return cart.reduce((total, item) => total + item.quantity * item.price, 0);
  };

  // Handle Checkout (POST request to /api/orders)
  const handleCheckout = async () => {
    try {
      // Convert product names array into a single comma-separated string
      const productNames = cart.map((item) => item.name).join(', ');
      const total = calculateTotalPrice();
  
      // Create the body for the POST request
      const orderData = {
        product: productNames, // Comma-separated string of product names
        total: total // Total price
      };
  
      const response = await axios.post(
        '/api/orders/',
        orderData,
        {
          headers: {
            'X-CSRFToken': getCookie('csrftoken'), // CSRF token from cookies
          },
          withCredentials: true, 
        }
      );

      if (response.status === 201) {
        setShowCart(false); // Close the cart modal
        alert('Order placed successfully!');
        setCookie('cart', JSON.stringify([])); // Clear cart after successful order
        setCart([]); // Clear cart in state
        window.location.href = '/orders'; // Redirect to orders page
      } else {
        const errorData = await response.json();
        alert(`Error placing order: ${errorData.detail}`);
      }
    } catch (error) {
      alert('An error occurred during checkout.', error);
    }
  };
  
  

  // Render Cart items in the modal
  const renderCartItems = () => {
    if (cart.length === 0) {
      return <p>Your cart is empty.</p>;
    }

    return (
      <div>
        <ul className="list-group mb-3">
          {cart.map((item) => (
            <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
              <span>{item.name} (x{item.quantity})</span>
              <span>${item.price * item.quantity}</span>
            </li>
          ))}
        </ul>
        <h5 className="text-right">Total: ${calculateTotalPrice()}</h5>
      </div>
    );
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Product Page</h2>
      <div className="row">
        {products.map((product) => (
          <div key={product.id} className="col-md-4 mb-4">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">{product.name}</h5>
                <h6 className="card-subtitle mb-2 text-muted">Stock: {product.stock}</h6>
                <p className="card-text">Price: ${product.price}</p>
                <button
                  className="btn btn-primary"
                  onClick={() => handleAddToCart(product)}
                  disabled={product.stock === 0}
                >
                  {product.stock > 0 ? 'Add to Cart' : 'Out of Stock'}
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Checkout Button */}
      <div className="text-center mt-5">
        <button className="btn btn-success" onClick={() => setShowCart(true)}>
          Checkout
        </button>
      </div>

      {/* Modal for Cart */}
      {showCart && (
        <div className="modal show d-block" tabIndex="-1">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Your Cart</h5>
                <button type="button" className="close" onClick={() => setShowCart(false)}>
                  <span>&times;</span>
                </button>
              </div>
              <div className="modal-body">
                {renderCartItems()}
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={() => setShowCart(false)}>
                  Close
                </button>
                <button type="button" className="btn btn-primary" onClick={handleCheckout}>
                  Place Order
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProductPage;
