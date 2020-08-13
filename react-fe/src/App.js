import React, { Component } from 'react';
import ReactPlayer from 'react-player'
import logo from './logo.svg';
import './App.css';

const intialState = {
  nowPlayingUrl: '',
  errorMsg: '',
}

class App extends Component {

  constructor() {
    super();
    this.state = intialState;
  }

  onPlayButton = () => {
    fetch('http://127.0.0.1:3000/application/podcast_episode', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
      .then((response) => {
        if (response != null) {
          if (response.result.length > 1) {
            console.log("~~~~~~");
            console.log(response.src);
            this.setState({
              nowPlayingUrl: '',
            })
          }
        }
      }).catch(() => {
        this.setState({
          errorMsg: 'notfound',
        })
      })
  }

  render() {
    return (
      <div className="App" >
        <header className="App-header">
          <ReactPlayer onClick={this.onPlayButton}
            url={this.state.nowPlayingUrl} playing />
          {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        </header>
      </div>
    );
  }
}

export default App;
