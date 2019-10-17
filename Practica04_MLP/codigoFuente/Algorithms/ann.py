import random
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoidPrime(z):
    return np.exp(-z)/((1+np.exp(-z))**2)


class Neuron:
    def __init__(self, bias):
        self.bias = bias
        
        self.inputs = []
        self.weights = []
        self.net = 0
        self.output = 0
        self.delta = 0
    
    def calculate_net(self, inputs):
        # print("NET: {} o {} + {}".format(inputs, self.weights, self.bias))
        self.inputs = inputs
        self.net = np.dot(self.weights, inputs) + self.bias
        # print("net", self.net)
        return self.net
    
    def calculate_output(self):
        self.output = sigmoid(self.net)
        # print("output", self.output)
        return self.output
    

class NeuronLayer:
    def __init__(self, num_neurons, bias):
        self.bias = bias if bias else random.random()
        
        self.neurons = []
        for _ in range(num_neurons):
            self.neurons.append(Neuron(self.bias))
    
    def inspect(self):
        print('Neurons:', len(self.neurons))
        for neuron_index in range(len(self.neurons)):
            print(' Neuron', neuron_index+1)
            for weight_index in range(len(self.neurons[neuron_index].weights)):
                print('  Weight:', self.neurons[neuron_index].weights[weight_index])
            print('  Net: ', self.neurons[neuron_index].net)
            print('  Output: ', self.neurons[neuron_index].output)
            print('  Bias:', self.bias)

class NeuralNetwork:
    def __init__(self, inputs, layers_structure, bias, targets, learning_rate, min_error, max_epochs):  
        self.inputs = inputs
        self.min_error = min_error
        self.max_epochs = max_epochs

        self.input_layer = []
        self.hidden_layers = []
        self.output_layer = None
        self.targets = targets
        self.target = []
        self.learning_rate = learning_rate

        self.output = []
        self.globalError = 1000

        # One bias for all network
        if len(bias) == 1:
            for num_neurons in layers_structure[0:-1]:
                self.hidden_layers.append(NeuronLayer(num_neurons, bias[0]))

            self.output_layer = NeuronLayer(layers_structure[-1], bias[0])
        # One bias for each layer
        else:
            if len(bias) != len(layers_structure):
                # return print("Bias array length must be 1 or equal to structure length ({})".format(len(layers_structure)))
                pass
            for num_neurons, layer_bias in zip(layers_structure[0:-1], bias[0:-1]):
                self.hidden_layers.append(NeuronLayer(num_neurons, layer_bias))
            self.output_layer = NeuronLayer(layers_structure[-1], bias[-1])

        self.init_weights()

    def init_weights(self):
        # From inputs to first hidden layer
        for hidden_neuron in self.hidden_layers[0].neurons:
            for input in np.zeros(len(self.inputs[0])):
                hidden_neuron.weights.append(random.random())
        # From hidden layers to hidden layers
        if len(self.hidden_layers) > 1:
            # Start iterating from 2nd hidden layer
            for previous_hidden_layer_index, hidden_layer in enumerate(self.hidden_layers[1:]):
                for hidden_neuron in hidden_layer.neurons:
                    # Iterate previous layer index
                    for previous_layer_neuron in self.hidden_layers[previous_hidden_layer_index].neurons:
                            hidden_neuron.weights.append(random.random())
        # From last hidden layer to output layer
        for output_neuron in self.output_layer.neurons:
            for neuron in self.hidden_layers[-1].neurons:
                output_neuron.weights.append(random.random())

    def forward(self, test_input=None):
        input_layer = test_input if test_input else self.input_layer
        # print("Input: ", input_layer)
        self.output = []
        previous_layer_outputs = []
        layer_output = []
        for layer_index, layer in enumerate(self.hidden_layers):
            previous_layer_outputs = layer_output
            layer_output = []

            for neuron in layer.neurons:
                if layer_index == 0:
                    neuron.calculate_net(input_layer)
                else:
                    neuron.calculate_net(previous_layer_outputs)

                layer_output.append(neuron.calculate_output())
        
        for neuron in self.output_layer.neurons:
            neuron.calculate_net(layer_output)
            self.output.append(neuron.calculate_output())
    
    def calculateGlobalError(self):
        # print("Error: Target ({}) - Output ({})".format(self.target, self.output))
        self.globalError = np.sum(0.5 * (np.array(self.target) - np.array(self.output)) ** 2 )

    def backprop(self):
        output_layer_new_weights = []
        hidden_layers_new_weights = []
        # Start with the output layer deltas
        for neuron in self.output_layer.neurons:
            for input_, weight in zip(neuron.inputs, neuron.weights):
                delta = (neuron.output - self.target) * (sigmoidPrime(neuron.net))
                neuron.delta = delta
                weight_cost = delta * input_
                # Update and save new weight
                output_layer_new_weights.append((weight-self.learning_rate*weight_cost))
        
        # Proceed with hidden layer deltas
        for layer_index, layer in enumerate(reversed(self.hidden_layers)):
            for neuron_index, neuron in enumerate(layer.neurons):
                for weight_index, weight in enumerate(neuron.weights):
                    # Layer n-1
                    # La primera parte de tres, es el delta de la neurona siguiente por el peso que las conecta
                    error_wtr_output = 0 
                    
                    if layer_index == 0:
                        for next_neuron in self.output_layer.neurons:
                            error_wtr_output += next_neuron.delta * next_neuron.weights[neuron_index]
                            # print("next_neuron Delta: {}, Weight: {}".format(next_neuron.delta, next_neuron.weights[neuron_index]))
                    else:
                        # Other hidden layers
                        for next_neuron in self.hidden_layers[layer_index-1].neurons:
                            error_wtr_output += next_neuron.delta * next_neuron.weights[neuron_index]
                            # print("next_neuron Delta: {}, Weight: {}".format(next_neuron.delta, next_neuron.weights[neuron_index]))

                    delta = error_wtr_output * sigmoidPrime(neuron.net)
                    neuron.delta = delta
                    weight_input = neuron.inputs[weight_index]
                    weight_cost = delta * weight_input
                    # print("WEIGHT COST: ", weight_cost)
                    hidden_layers_new_weights.append((weight-self.learning_rate*weight_cost))
                    neuron.bias = neuron.bias - self.learning_rate * delta

        # print(hidden_layers_new_weights)
        # print(output_layer_new_weights)

        # Set new weights
        i = 0
        for layer in self.hidden_layers:
            for neuron in layer.neurons:
                for weight_index, weight in enumerate(neuron.weights):
                    neuron.weights[weight_index] = hidden_layers_new_weights[i]
                    i += 1
        
        # Output weights
        i = 0
        for neuron in self.output_layer.neurons:
                for weight_index, weight in enumerate(neuron.weights):
                    neuron.weights[weight_index] = output_layer_new_weights[i]
                    i += 1

    def train(self, progress_bar):
        epochs = 0
        progress = 100 / self.max_epochs
        progress_count = 0
        for input, target in zip(self.inputs, self.targets):
            self.globalError = 1000
            self.input_layer = input
            self.target = target
            while self.globalError > self.min_error and epochs < self.max_epochs:
                self.forward()
                self.calculateGlobalError()
                self.backprop()
                epochs += 1 
                progress_count += progress
                progress_bar.setValue(progress_count)
                # print("Epoch {}: {}".format(epochs, self.globalError))

    def inspect(self):
        print('------')
        print('* Inputs: {}'.format(self.input_layer))
        print('------\n')
        print('* Hidden Layers')
        for index, hidden_layer in enumerate(self.hidden_layers):
            print('Hidden Layer #{}:'.format(index+1))
            hidden_layer.inspect()
            print('\n')
        print('------')
        print('* Output Layer')
        self.output_layer.inspect()
        print('------')

# NN = NeuralNetwork(inputs=[[1,1],[2,2],[3,3]], layers_structure=[2,2,1], bias=[0.70], targets=[1, 2, 3], learning_rate = 0.8, min_error = 0.01, max_epochs = 1000000)
# NN.train()
# NN.forward(test_input=[1,1])