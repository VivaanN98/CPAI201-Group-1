import React, { useEffect, useState } from 'react';
import PlaceCardItem from './PlaceCardItem';

function PlacesToVisit({ trip }) {
    const [tripData, setTripData] = useState(trip);

    useEffect(() => {
        if (trip?.tripData) {
            setTripData(trip.tripData);
        }
    }, [trip]);

    // Debugging: Log the itinerary object to inspect the structure.
    useEffect(() => {
        console.log("Itinerary Days:", tripData?.itinerary);
    }, [tripData]);

    // Sort days based on the numeric value extracted from "dayX" format.
    const sortedDays = tripData?.itinerary ? Object.keys(tripData.itinerary).sort((a, b) => {
        // Extract the numeric part of the day string
        const numA = parseInt(a.replace('day', ''), 10);
        const numB = parseInt(b.replace('day', ''), 10);

        return numA - numB; // Sort numerically based on the extracted number
    }) : [];

    return (
        <div>
            <h2 className='font-bold text-lg'>Places to Visit</h2>
            <div>
                {sortedDays.map((day) => (
                    <div key={day} className='mt-5'>
                        <h2 className='font-medium text-lg'>{day}</h2>
                        <div className='grid md:grid-cols-2 gap-5'>
                            {tripData?.itinerary[day].plan?.map((place, index) => (
                                <div key={index}>
                                    <h2 className='font-medium text-sm text-orange-600'>{place.time}</h2>
                                    <PlaceCardItem place={place} />
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default PlacesToVisit;
