import React, { Component } from 'react';

import circle from '../Assets/circle.png'
import rectangle from '../Assets/rect.png';


class ControlPanel extends Component {
  state = {
    activeClass: 0
  };

  setActive = async (e) => {

    if(e.target.classList.contains('red')) {
      this.redClass.classList.add('active');
      this.blueClass.classList.remove('active');
      await this.setState({activeClass: 0})
    } else {
      this.blueClass.classList.add('active');
      this.redClass.classList.remove('active'); 
      await this.setState({activeClass: 1})
    }

    this.props.setClass(this.state.activeClass);
  }

  render() {
    return(
      <div className="control-panel">
        <div className="classes-container" >
          <div className="class1">
            <p>Clase 1</p>
            <div ref={(redClass) => {this.redClass = redClass}} className="class red active" onClick={this.setActive} >
              <img className="class-image red" width="150" height="150" src={rectangle}></img>
            </div>
          </div>
          <div className="class2">
            <p>Clase 2</p>
            <div ref={(blueClass) => {this.blueClass = blueClass}} className="class blue" onClick={this.setActive} >
              <img className="class-image blue" width="150" height="150" src={circle}></img>
            </div>
          </div>
        </div>
        <div className="inputs-container">
          <div className="rate-input">
            <p>Learning Rate</p>
            <input type="text" onChange={this.props.onRateInput} value={this.props.rateInput} placeholder="0.5"></input>
          </div>
          <div className="epochs-input">
            <p>Max Epochs</p>
            <input type="text" onChange={this.props.onEpochsInput} value={this.props.epochsInput} placeholder="20"></input>
          </div>
        </div>
        <div className="buttons-container">
          <div className="set-buttons-container">
          <input onClick={this.props.initialize} className="button-inicializar" type="submit" value="Inicializar"></input>
          <input onClick={this.props.resetData} className="button-resetear" type="submit" value="Resetear"></input>
          </div>
          <div className="inicializar-container">
            <input onClick={this.props.sendPoints} className="button-entrenar" type="submit" value="Entrenar"></input>
          </div>
        </div>
      </div>
    );
  };
};

export default ControlPanel;