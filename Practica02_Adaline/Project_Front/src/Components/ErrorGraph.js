import React, { Component, Fragment } from 'react';
import Plotly from "plotly.js-basic-dist";

import createPlotlyComponent from "react-plotly.js/factory";
const Plot = createPlotlyComponent(Plotly);

class ErrorGraph extends Component {
  state = {

  };

  render() {
    let config = {modeBarButtonsToRemove: ['hoverCompareCartesian'], scrollZoom: true}
    let x = this.props.errors.map((e, i) => i+1);
    let y = this.props.errors.map(e => e);
    
    return(
      <Fragment>
         <Plot
          config={config}
          onClick={this.setPoint}
          data={[
            {
              x: x,
              y: y,
              type: 'scatter',
              marker: {color: 'black'},
            }
          ]}
          layout = {
            {
              width: 654,
              height: 250,
              title: 'Errores',
              hovermode: 'closest',
              showlegend: false
            }
          }
        />
      </Fragment>
    );
  };
};

export default ErrorGraph;