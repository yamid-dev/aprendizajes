import React, { useState, useEffect } from 'react';

export function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds(seconds => seconds + 1);
    }, 1000);

    return () => clearInterval(intervalId); 
  }, []);
  return (
    <div>
      <p className="p-timer">Tiempo transcurrido: {seconds} segundos</p>
    </div>
  );
}