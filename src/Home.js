import 'rc-collapse/assets/index.css';
import React, { Component } from 'react';
import './App.css';
import { Input, Collapse, Button } from 'antd';
import axios from 'axios';
const { Panel } = Collapse;

export default class Home extends Component {
  state = {
    dataSource: [],
    search: [],
    activeKey: []
  };

  postRequest = search => {
    axios
      .post('http://127.0.0.1:8000/search/', {
        pesquisa: search
      })
      .then(res => {
        console.log(res);
        this.setState({
          dataSource: res.data
        });
      })
      .catch(error => {
        console.error(error);
      });
  };
  onAccordionChange(activeKey) {
    this.setState({ activeKey });
  }
  render() {
    const { dataSource, search } = this.state;

    return (
      <div>
        <div className='titulo'>
          <h2>Digite uma pesquisa sobre Jogos</h2>
        </div>
        <div className='pesquisa'>
          <Input
            className='card'
            placeholder='Digite uma Pesquisa '
            onChange={e => this.setState({ search: e.target.value })}
          />
          <Button
            icon='search'
            onClick={() => {
              this.postRequest(search);
            }}
          />
        </div>
        <div className='comentarios'>
          <Collapse
            bordered={false}
            activeKey={this.state.activeKey}
            onChange={this.onAccordionChange.bind(this)}
          >
            {dataSource.map(item => {
              return (
                <Panel header={item.titulo} key={item.titulo}>
                  <p>{item.texto}</p>
                </Panel>
              );
            })}
          </Collapse>
        </div>
      </div>
    );
  }
}
