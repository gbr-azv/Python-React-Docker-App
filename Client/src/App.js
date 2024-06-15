import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';

import Home from './pages/Home';
import Logon from './pages/Logon';
import Menu from './pages/Menu';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route exact path='/' Component={Home} />
        <Route path='/logon' Component={Logon} />
        <Route path='/cardapio' Component={Menu} />
      </Routes>
    </Router>
  );
}

export default App;
