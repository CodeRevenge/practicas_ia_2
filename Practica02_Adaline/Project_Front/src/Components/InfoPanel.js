import React, { Component} from 'react';

class InfoPanel extends Component {
    state = {

    };

    render(){
        let panel = 'info-panel'
        let info = 'info'
        let tipo = ''

        if (this.props.response){
            panel = 'activate-panel '+ panel
        }

        if (this.props.algorithmType === 'perceptron'){
            info = 'activate-panel ' + info
            tipo = "Perceptrón"
        } else if(this.props.algorithmType === 'adaline'){
            info = 'activate-panel ' + info
            tipo = "Adaline"
        }

        let error = 0
        for(let x=0;x<this.props.errors.length;x++){
            error += this.props.errors[x]
        }

        return (
            <div className = {panel}>
                <div className="info-title">Información</div>
                <div className = {info}>
                    {tipo}<br/>
                    Épocas: {this.props.finalEpochs}<br/>
                    Convergencia: {this.props.converged ? "Afirmativo" : "Negativo"}<br/>
                    Error acumulado: {error}<br/>
                </div>
                
            </div>
        );
    }
}

export default InfoPanel;