import React, { useState, useEffect } from 'react';

const DigitalTimer = ({ initialTimeMs, onTimerComplete, timerRunning, isReset, setIsReset}) => {
  // State to store the time in milliseconds, and timer running status
  const [timeLeft, setTimeLeft] = useState(initialTimeMs); // in milliseconds
  const [isRunning, setIsRunning] = useState(false);

  useEffect(()=>{
    setTimeLeft(initialTimeMs)
  }, [initialTimeMs])

  useEffect(()=>{
    setIsRunning(timerRunning)
  }, [timerRunning])

  useEffect(()=>{
    if(isReset){
        handleReset()
        setIsReset(false)
    }
  }, [isReset])

  // useEffect hook to handle the countdown every second (1000ms)
  useEffect(() => {
    let interval;
    if (isRunning && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((prevTime) => prevTime - 1000); // Decrease by 1000ms (1 second)
      }, 1000);
    } else if (timeLeft === 0) {
      setIsRunning(false); // Stop the timer when it reaches 0
      if (onTimerComplete) {
        onTimerComplete(); // Call the callback when the timer reaches 0
      }
    }

    return () => clearInterval(interval); // Clean up the interval when the component unmounts or when the timer is paused
  }, [isRunning, timeLeft, onTimerComplete]);

  const handleStartStop = () => {
    if (timeLeft > 0) {
      setIsRunning(!isRunning); // Toggle between start and stop
    }
  };

  const handleReset = () => {
    setTimeLeft(initialTimeMs);
    setIsRunning(true) // Reset to the initial time provided as prop
  };

  const formatTime = (timeInMs) => {
    const seconds = Math.floor(timeInMs / 1000);
    return seconds > 0 ? seconds : 0; // Display seconds, not fractions of a second
  };

  return (
      <div className="text-center">
        <p className="text-4xl font-bold text-white">
          {formatTime(timeLeft)}s
        </p>
      </div>
  );
};

export default DigitalTimer;
