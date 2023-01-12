import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Routes, Route } from 'react-router-dom';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/time')
    .then(res => res.json())
    .then(data => {
      setCurrentTime(data.time);
    })
    .catch(e=>console.error(e))
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <BrowserRouter>
          <div>
            <Link className="App-link" to="/">Home</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/page2">Page2</Link>
          </div>
          <Routes>
            <Route exact path="/" element={<React.Fragment><p>The current time is {currentTime}.</p></React.Fragment>}/>
            <Route exact path="/page2" element={<React.Fragment><p>The current time is {currentTime}.</p></React.Fragment>}/>
          </Routes>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
