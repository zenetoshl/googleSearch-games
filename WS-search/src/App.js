import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./App.css";
import Home from "./Home";
import NovoArquivo from "./NovoArquivo";
import Header from "./Header";
class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Header />
          <Route exact path="/" component={Home} />
          <Route path="/novoaarquivo" component={NovoArquivo} />
        </div>
      </Router>
    );
  }
}

export default App;
