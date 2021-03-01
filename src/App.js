
import './App.css';
import React from 'react';

class App extends React.Component {
 constructor(){
   super();
  this.brand = "VOLVO";
 }
  render() {
   return <h1>My favourite car is {this.brand}</h1>;
}
}

export default App