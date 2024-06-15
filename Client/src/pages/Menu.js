import '../styles/Menu.css';

import { useEffect, useState } from 'react'; 

import Product from '../components/Product';
import Footer from '../components/Footer';

function Menu() {

    const [products, setProducts] = useState([]);

    useEffect(() => {

        const fetchProducts = async () => {
            const response =  await fetch('http://localhost:8000/menu');
            const result = await response.json();

            setProducts(result);
        }

        fetchProducts();
    }, []);

    return (
        <div className="menu-products-container">
            <div className='menu-container'>
                {products.length > 0 ? (
                    products.map((product, index) => (
                    <Product
                        key={index}
                        name={product.name} 
                        description={product.description} 
                        price={product.price} 
                    />
                    ))
                ) : (
                    <div>Loading...</div>
                )}
            </div>
            <div className='menu-footer-container'>
                <Footer
                    backFooter="logon-footer"
                    where="logon"
                />
            </div>
        </div>
    );
}

export default Menu;
