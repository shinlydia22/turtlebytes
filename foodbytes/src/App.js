import logo from './food_icon.png';
import './App.css';
import axios from 'axios';
import React, { Component } from 'react';
import { useState } from 'react';

// const header_comp = {
//   imgURL: 'https://shorturl.at/emzMT'
// };

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

// // function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <h> Welcome to FoodBytes! </h>
//       </header>
      
//       <p> Please upload an image to be processed. </p>
//       <MyButton />
//     </div>
//   );
// // }


class App extends Component {

  state = {

      // Initially, no file is selected
      selectedFile: null
  };

  // On file select (from the pop up)
  onFileChange = event => {

      // Update the state
      this.setState({ selectedFile: event.target.files[0] });

  };

  // On file upload (click the upload button)
  onFileUpload = () => {

      // Create an object of formData
      const formData = new FormData();

      // Update the formData object
      formData.append(
          "myFile",
          this.state.selectedFile,
          this.state.selectedFile.name
      );

      // Details of the uploaded file
      console.log(this.state.selectedFile);

      // Request made to the backend api
      // Send formData object
      axios.post("http://localhost:5000/uploadfile", formData)
      .then(response => {
        // Handle the response, e.g., show a success message to the user
        const res = response.data
        // setProfileData(({
        //   profile_name: res.name,
        //   about_me: res.about}))
        console.log("File uploaded successfully.");
      })
      .catch(error => {
        if (error.response && error.response.status === 404) {
          console.error('Resource not found');
        } else {
          console.error('An error occurred:', error.message);
        }

      });

  };

  // File content to be displayed after
  // file upload is complete

  render() {
    return (
        <div>
          <header className="App-header">
             <img src={logo} className="App-logo" alt="logo" />
             <h> Welcome to FoodBytes! </h>
           </header>
            <h1>
                FoodBytes
            </h1>
            <h3>
                File Upload Here!
            </h3>
            <div>
                <input type="file" onChange={this.onFileChange} />
                <button onClick={this.onFileUpload}>
                    Submit
                </button>

                {/* <p>To get your profile details: </p><button onClick={getData}>Click me</button>
                {profileData && <div>
                      <p>Profile name: {profileData.profile_name}</p>
                      <p>About me: {profileData.about_me}</p>
                    </div>
                } */}
            </div>
            {this.fileData()}
        </div>
    );
  }
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
