import logo from './food_icon.png';
import './App.css';

const header_comp = {
  imgURL: 'https://shorturl.at/emzMT'
};

function MyButton() {
  function handleClick() {
    alert('You clicked me!');
  }

  return (
    <button onClick={handleClick}>
      Upload Image
    </button>
  );
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h> Welcome to FoodBytes! </h>
      </header>
      
      <p> Please upload an image to be processed. </p>
      <MyButton />
    </div>
  );
}

export default App;


// use for additional resources
{/* <a
  className="App-link"
  href="https://reactjs.org"
  target="_blank"
  rel="noopener noreferrer"
>
  Learn React
</a> */}