import React from 'react'
import Lottie from 'react-lottie';
import animationData from './heart1.json';

export default function Heart() {

    const defaultOptions = {
        loop: true,
        autoplay: true,
        animationData: animationData,
        rendererSettings: {
          preserveAspectRatio: "xMidYMid slice"
        }
      };


    return (
    <div className='flex flex-wrap justify-center'>
        <div className='flex-grow gap-x-2'></div>
        <h2 className='mt-16  text-gray-900 font-sarif font-semibold tracking-wide'>Made With</h2>
      <Lottie 
	    options={defaultOptions}
        height={150}
        width={55}
      />
      <h2 className='mt-16 text-gray-900 font-sarif font-semibold tracking-wide'>By JDRanpariya</h2>
      <div className='flex-grow'>
      
      </div>
    </div>
    )
}
