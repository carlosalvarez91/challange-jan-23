import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './App.css';

function App() {
  const [data, setData] = useState([]);
  const [selectedTime, setSelectedTime] = useState('minute')

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
    .then(data =>{
      handleQueryData(selectedTime)
    })
    .catch(error => console.log(error));
  }

  const handleQueryData = (value) => {
    fetch(`http://127.0.0.1:5000/api/query_data/${value}`)
    .then(res => res.json())
    .then(d => {
      console.log(d)
      setData(d)
    })
    .catch(e=>console.error(e))
  }

  useEffect(() => {
    // on init query avg per minute
    handleQueryData('minute')
  }, []);

  return (
    <div className="App">
      <header className="App-header">
          <button className="btn" onClick={handleWriteData}>
            Write Event
          </button>
          <select className='select' onChange={(e)=>{
            setSelectedTime(e.target.value)
            handleQueryData(e.target.value)
          }} value={selectedTime}>
            <option value="minute">AVG / Minute</option>
            <option value="hour">AVG / Hour</option>
            <option value="day">AVG / Day</option>
            <option value="all">All Events</option>
          </select>
  
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
