import React, { Component, Fragment } from 'react';
import Plotly from "plotly.js-basic-dist";
import axios from 'axios';
import createPlotlyComponent from "react-plotly.js/factory";
const Plot = createPlotlyComponent(Plotly);

class MainGraph extends Component {
  state = {
    class1: { x: [], y: []},
    class2: { x: [], y: []}
  };

  UNSAFE_componentWillUpdate() {
    if(!(this.state.class1.x.length === 0 && this.state.class2.x.length === 0) && this.props.reset) {
      this.resetPoints()
    }
  }

  setPoint = async (e) => {

    let selectedClass = this.props.selectedClass;

    if(this.props.trained) {
      console.log(this.props.trained);

      let data = {
        inputs: [e.points[0].x, e.points[0].y],
        weights: this.props.finalWeights,
        theta: this.props.finalTheta
      }
  
      let response = await axios.post("http://127.0.0.1:5000/testPerceptron", data);
  
      selectedClass = response.data.classified;
    }

    this.setState((prevState) => {
      if(selectedClass === 0) {
        let class1 = prevState.class1;
        class1.x.push(e.points[0].x)
        class1.y.push(e.points[0].y)
        this.props.setPoints(0, class1);
        return {class1}

      } else if (selectedClass === 1) {
          let class2 = prevState.class2;
          class2.x.push(e.points[0].x)
          class2.y.push(e.points[0].y)
          this.props.setPoints(1, class2);
          return {class2}
        }
      })
  }

  resetPoints = () => {
    this.setState({
      class1: { x: [], y: []},
      class2: { x: [], y: []}
    })
  }

  render() {

    let config = {modeBarButtonsToRemove: ['hoverCompareCartesian'], scrollZoom: false}
    let tipo = ''

    if (this.props.algorithmType === 'perceptron'){
      tipo = "Perceptrón"
    } else if(this.props.algorithmType === 'adaline'){
      tipo = "Adaline"
    }
    return(
      <Fragment>
        <Plot
          config={config}
          onClick={this.setPoint}
          data={[
            {
              x: [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5,-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
              y: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, ],
              type: 'points',
              mode: 'markers',
              marker: {color: 'white'},
            },
            {
              x: this.state.class1.x,
              y: this.state.class1.y,
              type: 'points',
              mode: 'markers',
              marker: {color: 'red'},
            },
            {
              x: this.state.class2.x,
              y: this.state.class2.y,
              type: 'points',
              mode: 'markers',
              marker: {color: 'blue'},
            },
            {
              x: [-5,5],
              y: [this.props.slope1, this.props.slope2],
              mode: 'lines',
              marker: {color: 'black'},
            }
          ]}
          layout = {
            {
              width: 654,
              height: 370,
              title: tipo,
              hovermode: 'closest',
              showlegend: false,
              xaxis:{
                autorange: false,
                range: [-5,5],
                zeroline: true
              },
              yaxis:{
                autorange: false,
                range: [-5,5],
                zeroline: true
              }
            }
          }
        />
      </Fragment>
    );
  };
};

export default MainGraph;