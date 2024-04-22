import React from 'react';
import ReactDOM from 'react-dom';
import {App} from './assets/App.jsx';
import './assets/index.css'
const root = document.getElementById('root');

//react está renderizando los elementos que le estamos retornando con los componentes que hemos hecho
ReactDOM.createRoot(root).render(
    <App />
);
