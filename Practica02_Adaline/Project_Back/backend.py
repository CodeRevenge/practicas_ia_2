import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import os
import json

from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def question():
    return jsonify(
        api = 'Perceptron Backend',
        author = 'Wicho Flores'
    )


@app.route("/perceptron", methods=['POST'])
def perceptron():
    class Perceptron:
        def __init__(self, inputs, learningRate, expectedOutputs, maxEpochs, weights, theta):
            self._inputs = inputs
            self._learningRate = learningRate
            self._expectedOutputs = expectedOutputs
            self._weights = np.array(weights)
            self._theta = theta
            self._outputs = np.zeros(inputs.shape[0])
            self._maxEpochs = maxEpochs
            self.slope = []
            self.errors = []
            self.converged = False
        
        def train(self):
            activated = self.activation()
            results = self._expectedOutputs - activated
            print(activated)
            print(results)
            error = np.sum(results**2)

            if error == 0:
                self.graph(activated)
                self.errors.append(int(np.sum(results)))
                self.converged = True
            
            currentEpochs = 0
            while error != 0 and currentEpochs < self._maxEpochs:
                currentEpochs += 1
                i = 0
                for inputs in self._inputs:
                    self._weights = self._weights + (self._learningRate * results[i] * inputs)
                    self._theta = self._theta + (self._learningRate * results[i] * 1)
                    
                    i += 1
                    if(error == 0):
                        self.converged = True
                        break
                    
                    print('\n----------------------------\n')
                    print("Expected Output:", self._expectedOutputs)
                    print("Activated results:", activated)
                    print("Errors:", results)
                    print("Error:", error)
                    print("Theta:", self._theta)
                    
                activated = self.activation()
                results = self._expectedOutputs - activated
                error = np.sum(np.array(results**2))
                self.errors.append(int(error))

                self.graph(activated)

            if error == 0:
                self.converged = True
            print('\n-------------END--------------\n')
            print("Inputs: \n", self._inputs)
            print("Weights: \n", self._weights)
            print("Expected Output:", self._expectedOutputs)
            print("Activated results:", activated)
            print("Errors:", results)
            print("Error:", error)
            print("Theta:", self._theta)

        def activation(self):
            results = []
            dot = np.dot(self._inputs, self._weights) + self._theta

            for result in dot:
                if result > 0:
                    results.append(1)
                else:
                    results.append(0)

            r = np.array(results)
            r.sort()
            return np.array(results)
        
        def graph(self, results):
            for i,pattern in enumerate(self._inputs):
                
                if(results[i] == 0):
                    plt.plot([pattern.item(0)], [pattern.item(1)], 'ro')
                else:
                    plt.plot([pattern.item(0)], [pattern.item(1)], 'go')

                x = np.linspace(-5,5,2)
                print("Here's X")
                print(x)
                # https://medium.com/@thomascountz/calculate-the-decision-boundary-of-a-single-perceptron-visualizing-linear-separability-c4d77099ef38
                y = (-(self._theta / self._weights[1]) / (self._theta / self._weights[0]))*x + (-self._theta / self._weights[1])
                print("Here's Y")
                print(y)
                plt.title('AND') if self._expectedOutputs[1] == 0 else plt.title('OR')

                plt.xlabel('X')
                plt.ylabel('Y')
                plt.plot(x, y, color="black")

            
            self.slope.append([y[0],y[1]])
            # plt.draw()
            # plt.pause(1)
            # plt.cla()

    # plt.ion()
    # plt.plot()
    # plt.show()

    learningRate = 0.1

    #inputs = np.array([[0,0], [1,0], [0,1], [1,1]])
    req = request.get_json()
    inputs = np.array(req['inputs'])
    expectedOutputs = np.array(req['classes'])
    learningRate = req['learningRate']
    maxEpochs = req['maxEpochs']
    weights = req['weights']
    theta = req['theta']

    print(weights)
    print(theta)

    AND = Perceptron(inputs, learningRate, expectedOutputs, maxEpochs, weights, theta)
    AND.train()

    print(AND.errors)
    print(AND.slope)

    return jsonify(
        slopes = AND.slope,
        errors = AND.errors,
        converged = AND.converged,
        weights = [AND._weights[0],AND._weights[1]],
        theta = AND._theta
    )

    #expectedOutputs = np.array([0,1,1,1])

    #OR = Perceptron(inputs, learningRate, expectedOutputs)
    #OR.train()

@app.route("/testPerceptron", methods=['POST'])
def testPerceptron():
    req = request.get_json()
    # Inputs of the new point i.e. [3,4]
    inputs = np.array(req['inputs'])
    # Weights of trained perceptron i.e. [0.34532, 0.15923]
    weights = np.array(req['weights'])
    # Theta of trained perceptron i.e. 0.92379
    theta = req['theta']

    z = np.dot(weights, inputs) + theta*1

    if z > 0:
        classified = 1
    else:
        classified = 0
    
    return jsonify(
        classified = classified
    )

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
