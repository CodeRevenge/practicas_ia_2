import React, { Component, Fragment } from 'react';
import './App.css';
import axios from 'axios';
import Swal from 'sweetalert2'

import NavBar from './Components/Navbar';
import MainGraph from './Components/MainGraph';
import ErrorGraph from './Components/ErrorGraph';
import ControlPanel from './Components/ControlPanel';

class App extends Component {
  state = {
    class1points: {},
    class2points: {},
    selectedClass: 0,
    learningRate: 0.5,
    maxEpochs: 10,
    minError: 0.05,
    finalEpochs: 0,
    errors: [],
    slopes: [],
    perceptronSlopes: [],
    adalineSlopes: [],
    converged: false,
    weights: [],
    theta: 0,
    finalWeights: [],
    finalTheta: "",
    initialized: false,
    trained: false
  };

  setClass = (c) => {
    this.setState({selectedClass: c})
  }

  setPoints = async (classType, points) => {    
    if(classType === 0) {
      this.setState({class1points: points})
    } else if(classType === 1) {
      this.setState({class2points: points})
    }
  }

  sendPoints = async (e) => {

    if((!this.state.initialized)) {
      console.log('not initialized // invalid epochs');
      Swal.fire({
        title: 'Error',
        text: 'No se han inicializado los pesos',
        type: 'error',
        showConfirmButton: false,
        timer: 1700
      })
      return;
    }

    if(this.state.maxEpochs === 0) {
      console.log('not initialized // invalid epochs');
      Swal.fire({
        title: 'Error',
        text: 'Las Épocas no pueden ser 0',
        type: 'error',
        showConfirmButton: false,
        timer: 1700
      })
      return;
    }

    if(this.state.learningRate === 0 || this.state.learningRate === 1) {
      console.log('not initialized // invalid epochs');
      Swal.fire({
        title: 'Error',
        text: 'El Learning Rate no puede ser 0',
        type: 'error',
        showConfirmButton: false,
        timer: 1700
      })
      return;
    }

    if(Object.values(this.state.class1points).length === 0 || Object.values(this.state.class2points).length === 0) {
      console.log('not initialized // invalid epochs');
      Swal.fire({
        title: 'Error',
        text: 'Faltan puntos en la gráfica',
        type: 'error',
        showConfirmButton: false,
        timer: 1700
      })
      return;
    }

    let data = {
      inputs: [],
      classes: [],
      maxEpochs: Number(this.state.maxEpochs),
      learningRate: Number(this.state.learningRate),
      minError: Number(this.state.minError),
      weights: this.state.weights,
      theta: this.state.theta
    }
    
    this.state.class1points.x.forEach((point, i) => {
      let pair = [point, this.state.class1points.y[i]]
      data.inputs.push(pair)
      data.classes.push(0)
    })

    this.state.class2points.x.forEach((point, i) => {
      let pair = [point, this.state.class2points.y[i]]
      data.inputs.push(pair)
      data.classes.push(1)
    })

    console.log(data);

    let response;

    if (e.target.value === "Perceptrón") {
      response = await axios.post("http://127.0.0.1:5000/perceptron", data)
      await this.setState({
        perceptronSlopes: response.data.slopes
      });

    } else if (e.target.value === "Adaline") {
      response = await axios.post("http://127.0.0.1:5000/adaline", data)
      await this.setState({
        adalineSlopes: response.data.slopes
      });

    }
    console.log(response.data);

    await this.setState({
      errors: response.data.errors,
      finalEpochs: response.data.errors.length,
      converged: response.data.converged,
      finalWeights: response.data.weights,
      finalTheta: response.data.theta,
      trained: response.data.converged
    });

    if(this.state.trained) {
      Swal.fire({
        title: 'Entrenamiento Exitoso',
        text: 'Ahora puedes agregar puntos para probar el modelo',
        type: "success",
        confirmButtonText: "Aceptar"
      })
    }
  }

  resetData = async () => {
    await this.setState({
      class1points: {},
      class2points: {},
      finalEpochs: 0,
      errors: [],
      slopes: [],
      perceptronSlopes: [],
      adalineSlopes: [],
      converged: false,
      reset: true,
      initialized: false,
      finalWeights: [],
      finalTheta: "",
      trained: false
    })

    await this.setState({
      reset: false
    })
  }

  onRateInput = (e) => {
    this.setState({learningRate: e.target.value})
  }

  onEpochsInput = (e) => {
    this.setState({maxEpochs: e.target.value})
  }

  onMinErrorInput = (e) => {
    this.setState({minError: e.target.value})
  }

  initialize = () => {

    let weights = [Math.random(), Math.random()]
    let theta = Math.random()

    let y2 = (-(theta / weights[1]) / (theta / weights[0]))*-5 + (-theta / weights[1])
    let y1 = (-(theta / weights[1]) / (theta / weights[0]))*5 + (-theta / weights[1])
    
    this.setState({
      weights,
      theta,
      initialized: true,
      slopes: [[y1, y2]]
    })
  }

  render() {
    return (
      <Fragment>
        <NavBar />
        <div className="main-container">
          <div className="container-left">
            <MainGraph finalWeights={this.state.finalWeights} finalTheta={this.state.finalTheta} trained={this.state.trained} reset={this.state.reset} converged={this.state.converged} finalEpochs={this.state.finalEpochs} selectedClass={this.state.selectedClass} setPoints={this.setPoints} slope1={this.state.slopes.length > 0 ? this.state.slopes[this.state.slopes.length-1][0] : null} slope2={this.state.slopes.length > 0 ? this.state.slopes[this.state.slopes.length-1][1] : null} 
              perceptronSlope1={this.state.perceptronSlopes.length > 0 ? this.state.perceptronSlopes[this.state.perceptronSlopes.length-1][0] : null} perceptronSlope2={this.state.perceptronSlopes.length > 0 ? this.state.perceptronSlopes[this.state.perceptronSlopes.length-1][1] : null}
              adalineSlope1={this.state.adalineSlopes.length > 0 ? this.state.adalineSlopes[this.state.adalineSlopes.length-1][0] : null} adalineSlope2={this.state.adalineSlopes.length > 0 ? this.state.adalineSlopes[this.state.adalineSlopes.length-1][1] : null}
            />
            <ErrorGraph errors={this.state.errors} />
          </div>
          <div className="container-right">
            <ControlPanel trained={this.state.trained} initialize={this.initialize} onMinErrorInput={this.onMinErrorInput} errorInput={this.state.minError} onEpochsInput={this.onEpochsInput} onRateInput={this.onRateInput} epochsInput={this.state.maxEpochs} rateInput={this.state.learningRate} resetData={this.resetData} setClass={this.setClass} sendPoints={this.sendPoints} />
          </div>
        </div>
      </Fragment>
    );
  }
}

export default App;
