import React, { useState, useEffect, useRef } from 'react';
import cardsData from './data/cards.json'; // Import the JSON file directly
import './game.css'; // Importing custom styles for the game
import DigitalTimer from './digital-timer';
import { useNavigate } from 'react-router-dom';

const FlipCardGame = () => {
    const gridContainer = useRef(null); // React ref for the grid container
    const [cards, setCards] = useState([]);
    const [firstCard, setFirstCard] = useState(null);
    const [secondCard, setSecondCard] = useState(null);
    const [lockBoard, setLockBoard] = useState(false);
    const [score, setScore] = useState(0);
    const [difficulty, setDifficulty] = useState('medium');
    const [timer, setTimer] = useState(60000)
    const [timerRunning, setTimerRunning]=useState(false)
    const [resetTimer, setResetTimer]=useState(false)
    const navigate = useNavigate()

    useEffect(()=>{
        if(difficulty==="easy"){
            setTimer(90000)
        }else if(difficulty==="medium"){
            setTimer(60000)
        }else{
            setTimer(30000)
        }
    }, [difficulty])

    const shuffleCards = (cards) => {
        let currentIndex = cards.length;
        let randomIndex;
        let temporaryValue;

        const shuffledCards = JSON.parse(JSON.stringify(cards));

        while (currentIndex !== 0) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;
            temporaryValue = shuffledCards[currentIndex];
            shuffledCards[currentIndex] = shuffledCards[randomIndex];
            shuffledCards[randomIndex] = temporaryValue;
        }

        return shuffledCards;
    };

    useEffect(() => {
        let shuffledCards = [...cardsData, ...cardsData];
        shuffledCards = shuffleCards(shuffledCards);
        setCards(shuffledCards);
    }, []);

    const flipCard = (index) => {
        if (lockBoard || cards[index].flipped) return;

        const updatedCards = [...cards];
        updatedCards[index].flipped = true;
        setCards(updatedCards);

        if (firstCard === null) {
            setFirstCard(index);
            return;
        }

        setSecondCard(index);
        setLockBoard(true);
    };

    useEffect(() => {
        if (firstCard !== null && secondCard !== null) {
            checkForMatch();
        }
    }, [firstCard, secondCard]);

    const checkForMatch = () => {
        const isMatch = cards[firstCard].name === cards[secondCard].name;
        if (isMatch) {
            disableCards();
            setScore((prevScore) => prevScore + 1);
        } else {
            unflipCards();
        }
    };

    const disableCards = () => {
        const updatedCards = [...cards];
        updatedCards[firstCard].flipped = true;
        updatedCards[secondCard].flipped = true;
        setCards(updatedCards);

        resetBoard();
    };

    const handleDifficultyChange = (event) => {
        setDifficulty(event.target.value);
        restart()
    };

    const unflipCards = () => {
        setTimeout(() => {
            const updatedCards = [...cards];
            updatedCards[firstCard].flipped = false;
            updatedCards[secondCard].flipped = false;
            setFirstCard(null);
            setSecondCard(null);
            setCards(updatedCards);

            resetBoard();
        }, 1000);
    };

    const resetBoard = () => {
        setFirstCard(null);
        setSecondCard(null);
        setLockBoard(false);
    };

    const restart = () => {
        setScore(0);
        let shuffledCards = [...cardsData, ...cardsData];
        shuffledCards = shuffleCards(shuffledCards);
        setCards(shuffledCards);
        resetBoard();
        setResetTimer(true)
        setTimerRunning(true)
        
    };

    useEffect(()=>{
        const res=confirm("Are you ready to start the Game, and earn interesting rewards")
        if(res){
            setTimerRunning(true)
        }else{
            navigate("/")
        }

    }, [])

    const onTimerComplete=()=>{
        const res= confirm(`The Time is up your total score is ${score}`)
        navigate('/rewards')
    }

    return (
        <div className="flex flex-col items-center py-10 bg-blue-950 ">
            <div className=" w-full max-w-7xl flex justify-between items-center">
                <div className="flex w-full justify-center items-center gap-5">
                    <h1 className="text-4xl font-bold text-white text-center">Memory Cards</h1>
                    <DigitalTimer initialTimeMs={timer} onTimerComplete={onTimerComplete} timerRunning={timerRunning} isReset={resetTimer} setIsReset={setResetTimer}/>
                </div>
                <div className="">
                    <label htmlFor="difficulty" className="block text-xl font-semibold mb-2 text-white">
                        Choose Difficulty:
                    </label>
                    <select
                        id="difficulty"
                        value={difficulty}
                        onChange={handleDifficultyChange}
                        className="w-full p-3 border border-gray-300 rounded-md text-gray-700 focus:ring-2 focus:ring-blue-400"
                    >
                        <option value="easy">Easy</option>
                        <option value="medium">Medium</option>
                        <option value="hard">Hard</option>
                    </select>
                </div>
                
            </div>
            <div
                ref={gridContainer}
                className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4"
                style={{ maxWidth: '900px' }}
            >
                {cards.map((card, index) => (
                    <div
                        key={index}
                        className="card-container"
                        onClick={() => flipCard(index)}
                    >
                        <div
                            className={`card ${card.flipped ? 'flipped' : ''}`}
                        >
                            {!card.flipped?
                            <div className="card-front">
                                <div className="back bg-blue-500 w-full h-full rounded-lg"></div>
                            </div>:

                            <div className="card-back">
                                <img className="w-20 h-20 object-contain" src={`../assets/${card.image}`} alt={card.name} />
                            </div>
                            }
                        </div>
                    </div>
                ))}
            </div>
            <p className="mt-4 text-xl text-white">Score: <span>{score}</span></p>
            <div className="mt-6">
                <button
                    onClick={restart}
                    className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-blue-600 transition-all duration-300"
                >
                    Restart
                </button>
            </div>
        </div>
    );
};

export default FlipCardGame;
