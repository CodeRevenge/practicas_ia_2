import random
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoidPrime(z):
    return np.exp(-z)/((1+np.exp(-z))**2)


class Neuron:
    def __init__(self, bias):
        self.bias = bias
        self.weights = []
        self.net = 0
        self.output = 0
    
    def calculate_net(self, inputs):
        print("Weights: ", self.weights)
        print("Inputs: ", inputs)
        self.net = np.dot(self.weights, inputs) + self.bias
        return self.net
    
    def calculate_output(self):
        self.output = sigmoid(self.net)
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
    def __init__(self, inputs, layers_structure, bias):        
        self.input_layer = inputs

        self.hidden_layers = []

        # One bias for all network
        if len(bias) == 1:
            for num_neurons in layers_structure[0:-1]:
                self.hidden_layers.append(NeuronLayer(num_neurons, bias[0]))

            self.output_layer = NeuronLayer(layers_structure[-1], bias[0])
        # One bias for each layer
        else:
            if len(bias) != len(layers_structure):
                return print("Bias array length must be 1 or equal to structure length ({})".format(len(layers_structure)))
            for num_neurons, layer_bias in zip(layers_structure[0:-1], bias[0:-1]):
                self.hidden_layers.append(NeuronLayer(num_neurons, layer_bias))
            self.output_layer = NeuronLayer(layers_structure[-1], bias[-1])

        self.init_weights()
        self.inspect()


    def init_weights(self):
        # From inputs to first hidden layer
        for hidden_neuron in self.hidden_layers[0].neurons:
            for input in self.input_layer:
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

    def forward(self):
        previous_layer_outputs = []
        layer_output = []
        for layer_index, layer in enumerate(self.hidden_layers):
            for neuron in layer.neurons:
                if layer_index == 0:
                    neuron.calculate_net(self.input_layer)
                else:
                    previous_layer_outputs = layer_output
                    layer_output = []
                    neuron.calculate_net(previous_layer_outputs)

                layer_output.append(neuron.calculate_output())
        
        for neuron in self.output_layer.neurons:
            neuron.calculate_net(layer_output)
            neuron.calculate_output()



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

NN = NeuralNetwork(inputs=[0.5, .10], layers_structure=[2,2], bias=[0.35, .6])
NN.forward()
NN.inspect()