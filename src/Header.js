import React, { Component } from "react";
import "./Style.css";
import { Link } from "react-router-dom";
import logo from "./logo.png";

export default class Header extends Component {
  render() {
    return (
      <div className="header">
        <img className="logo" src={logo} alt={"MinasCoders"} />
        <ul className="menu-ul">
          <li>
            <Link className="link" to="/">
              Home
            </Link>
          </li>
          <li>
            <Link className="link" to="/novoaarquivo">
              Novo Arquivo
            </Link>
          </li>
        </ul>
      </div>
    );
  }
}
