import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // You may have an existing index.css file, keep it
import './styles.css'; // Add this line to import styles.css
import App from './App';
import reportWebVitals from './reportWebVitals';

reportWebVitals();

const rootElement = document.getElementById('root');
ReactDOM.createRoot(rootElement).render(<App />);