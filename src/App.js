import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './App.css';

function App() {
  const [data, setData] = useState([]);

  const handleWriteData = () => {
    fetch('http://127.0.0.1:5000/api/insert_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        value: Math.random(),
      })
    })
    .then(response => response.json())
    .then(data =>
      setData(data)
    )
    .catch(error => console.log(error));
  }

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/query_data')
    .then(res => res.json())
    .then(data => {
      setData(data);
    })
    .catch(e=>console.error(e))
  }, []);

  return (
    <div className="App">
      <header className="App-header">
          <button className="btn" onClick={handleWriteData}>
            Write Event
          </button>
  
          <Plot
            data={[
              {
                x: data.map(e=>e.time),
                y: data.map(e=>e.value),
                type: 'scatter',
                mode: 'lines+markers',
                marker: {color: 'red'},
              }
            ]}
            layout={ {width: 500, height: 240, title: 'Events'} }
          />


      </header>
    </div>
  );
}

export default App;
