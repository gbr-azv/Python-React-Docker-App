import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';

import Home from './pages/Home';
import Logon from './pages/Logon';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route exact path='/' Component={Home} />
        <Route path='/logon' Component={Logon} />
      </Routes>
    </Router>
  );
}

export default App;
