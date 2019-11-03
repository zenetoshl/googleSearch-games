import React from "react";
import "./App.css";
import { Button, Input } from "antd";
import axios from "axios";

class Comentarios extends React.PureComponent {
  state = {
    comments: [],
    comment: "",
    texts: [],
    text: ""
  };

  postRequest = search => {
    axios
      .post('http://127.0.0.1:8000/search/', {
        texto: search
      })
      .then(res => {
        console.log(res);
      })
      .catch(error => {
        console.error(error);
      });
  };

  render() {
    const { TextArea } = Input;
    const { comments, comment, text, texts } = this.state;
    return (
      <div className="divCard">
        <Input
          className="card"
          placeholder="Digite um Título"
          onChange={e => this.setState({ comment: e.target.value })}
        />
        <br></br>
        <TextArea
          rows={10}
          className="card"
          placeholder="Digite um Texto"
          onChange={e => this.setState({ text: e.target.value })}
        />
        <br></br>
        <Button
          className="button"
          type="primary"
          onClick={() => {
            const newComments = comments.concat(comment);
            const newText = texts.concat(text);
            this.postRequest(comment.concat('\n').concat(text))
            this.setState({
              comments: newComments,
              texts: newText,
              comment: "",
              text: "",
              visible: true
            });
          }}
        >
          Inserir
        </Button>
      </div>
    );
  }
}
export default Comentarios;
