import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from progress.bar import Bar

def sigmoid(Z):
    return 1/(1+np.exp(-Z))

def sigmoidPrime(out):
    return out * (1-out)

class NeuralNetwork(QThread):
    countChanged = pyqtSignal(int)
    def __init__(self, inputs, targets, learning_rate, structure, max_epochs, min_error, bias=np.random.rand()):
        super(QThread, self).__init__()
        self.inputs = inputs
        self.targets = targets
        self.learning_rate = learning_rate
        self.structure, self.bias = self.setWeights(inputs, structure, bias)

        self.max_epochs = max_epochs
        self.min_error = min_error

        # Outputs will be stored in here for backprop calculations
        self.outputs = []
    
    def setWeights(self, inputs, structure, bias):
        # Xavier Initialization
        weightsMatrix = []
        biasMatrix = []

        for nodes_idx, nodes in enumerate(structure[1:]):
            biasLayer = []
            layer = []
            for _ in range(nodes):
                layer.append(np.random.rand(structure[nodes_idx])*np.sqrt(1/(structure[nodes_idx]+nodes)))
                # layer.append(np.random.rand(structure[nodes_idx]))
                biasLayer.append(np.array(bias))

            biasMatrix.append(np.array(biasLayer))
            weightsMatrix.append(np.array(layer))

        try:
            weightsMatrix = np.array(weightsMatrix)
        except ValueError:
            weightsMatrix += weightsMatrix + [1]
            weightsMatrix = np.array(weightsMatrix)[:-1]
        return weightsMatrix, np.array(biasMatrix)

    def forwardPropagation(self, inputs):
        # The first "outputs" are actually the inputs, used in the last layer for backprop
        self.outputs = []
        self.outputs.append(np.array(inputs))

        forward = None
        for idx, (layer, bias) in enumerate(zip(self.structure, self.bias)):
            if idx == 0:
                forward = self.forwardLayer(layer, inputs, bias)
            else: 
                forward = self.forwardLayer(layer, forward, bias)

            # Store ouputs for backprop calculations
            self.outputs.append(forward)

        return forward
    
    def forwardLayer(self, weights, inputs, bias):
        # Separate function in case different activation functions are used
        return sigmoid(np.dot(weights, inputs) + bias)

    def calculateCostFunction(self, target, output):
        return np.sum(0.5 * (target - output) ** 2)

    def backwardPropagation(self, target):
        # Reverse outputs so it goes along reversed network for backprop
        self.outputs.reverse()

        layer_deltas = []
        network_deltas = []

        neuron_chains = []
        layer_neuron_chains = []
        network_chains = []

        for layer_idx, (layer, bias_layer) in enumerate(zip(self.structure[::-1], self.bias[::-1])):
            for neuron_idx, (neuron, bias) in enumerate(zip(layer, bias_layer)):
                # First hidden layer
                if layer_idx == 0:
                    error = self.outputs[layer_idx][neuron_idx] - target[neuron_idx]
                else:
                    error = 0
                    for weight, delta in zip(self.structure[::-1][layer_idx-1], network_deltas[layer_idx-1]):
                        error += delta * weight[neuron_idx]

                net_sigmoid_prime = sigmoidPrime(self.outputs[layer_idx][neuron_idx])

                neuron_delta = error * net_sigmoid_prime
                layer_deltas.append(neuron_delta)

                # Adjust bias weight 
                self.bias[::-1][layer_idx][neuron_idx] -= neuron_delta

                for weight_idx, weight in enumerate(neuron):
                    weight_input = self.outputs[layer_idx+1][weight_idx]

                    weight_chain = neuron_delta * weight_input
                    neuron_chains.append(weight_chain)

                layer_neuron_chains.append(neuron_chains)
                neuron_chains = []
            
            network_deltas.append(layer_deltas)
            layer_deltas = []

            network_chains.append(np.array(layer_neuron_chains))
            layer_neuron_chains = []

        # Clean epoch outputs
        self.outputs = []

        try:
            network_chains = np.array(network_chains)
        except ValueError:
            network_chains += network_chains + [1]
            network_chains = np.array(network_chains)[:-1]

        return network_chains[::-1]
    
    def updateWeights(self, weight_deltas):
        self.structure = self.structure - self.learning_rate * weight_deltas

    def train(self):
        progress = 80 / self.max_epochs
        progress_count = 0
        
        acumulated_error = 999
        acumulated_outputs = []
        epochs = 0

        # print(len(self.inputs))
        self.errors = []
        while acumulated_error > self.min_error and epochs < self.max_epochs:
            # with Bar("Inputs: ", max=len(self.inputs)) as bar:
            for idx, (inputs, targets)in enumerate(zip(self.inputs, self.targets)):
                forward = self.forwardPropagation(inputs)
                acumulated_outputs.append(forward)
                weight_deltas = self.backwardPropagation(targets)
                self.updateWeights(weight_deltas)
                    # bar.next()
                # bar.finish()

            # print(np.sum(abs((np.array(self.targets) - np.array(acumulated_outputs)))))
            acumulated_error = (np.sum(abs((np.array(self.targets) - np.array(acumulated_outputs))))) * 100 / (len(self.targets) * len(self.targets[0]))
            # print("Epoch: {} - Acumulated error: [{}] // Precision: {}%".format(epochs+1, acumulated_error, 100-acumulated_error))
            acumulated_outputs = []
            self.errors.append(acumulated_error)
            epochs += 1

            progress_count += progress
            if int(progress_count) % 10:
                # time.sleep(0.001)
                self.countChanged.emit(progress_count)


    def run(self):
        self.train()