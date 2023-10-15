import React from 'react'
import './Popup.css'

function Popup(props) {
  return (props.trigger)?(
    <div className='Popup'>
        <div className='Inner'>
            <p>
                Carcinogen: yellow 6
            </p>
            <p>
                Hidden Sugar: maltodextrin
            </p>
            <button className='Close' onClick={()=> props.setTrigger(false)}>
                Close
            </button>
            {props.children}
        </div>
    </div>
  ): "";
}

export default Popup