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
        self.inputs = inputs
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
    def __init__(self, layers_structure, bias, learning_rate):        
        self.input_layer = [1,2]
        self.hidden_layers = []
        self.output_layer = None
        self.target = []
        self.learning_rate = learning_rate

        self.output = []
        self.globalError = 10

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

    def init_weights(self):
        weight = .15
        # From inputs to first hidden layer
        for hidden_neuron in self.hidden_layers[0].neurons:
            for input in self.input_layer:
                hidden_neuron.weights.append(weight)
                weight+=.05
        # From hidden layers to hidden layers
        if len(self.hidden_layers) > 1:
            # Start iterating from 2nd hidden layer
            for previous_hidden_layer_index, hidden_layer in enumerate(self.hidden_layers[1:]):
                for hidden_neuron in hidden_layer.neurons:
                    # Iterate previous layer index
                    for previous_layer_neuron in self.hidden_layers[previous_hidden_layer_index].neurons:
                            hidden_neuron.weights.append(random.random())
        # From last hidden layer to output layer
        weight = .40
        for output_neuron in self.output_layer.neurons:
            for neuron in self.hidden_layers[-1].neurons:
                output_neuron.weights.append(weight)
                weight+=.05

    def forward(self):
        self.output = []
        previous_layer_outputs = []
        layer_output = []
        for layer_index, layer in enumerate(self.hidden_layers):
            previous_layer_outputs = layer_output
            layer_output = []
            for neuron in layer.neurons:
                if layer_index == 0:
                    neuron.calculate_net(self.input_layer)
                else:
                    neuron.calculate_net(previous_layer_outputs)

                layer_output.append(neuron.calculate_output())
        
        for neuron in self.output_layer.neurons:
            neuron.calculate_net(layer_output)
            self.output.append(neuron.calculate_output())
        
        return self.output
        # print("Output:", self.output)
    
    def calculateGlobalError(self):
        # print("Error: Target ({}) - Output ({})".format(self.target, self.output))
        self.globalError = np.sum(0.5 * (np.array(self.target) - np.array(self.output)) ** 2 )
        # self.globalError = abs(np.sum(np.array(self.target) - np.array(self.output)))
        # print("Error: ", self.globalError)

    def backprop(self):
        output_layer_new_weights = []
        hidden_layers_new_weights = []
        # Start with the output layer deltas

        for neuron, target in zip(self.output_layer.neurons, self.target):
            for input_, weight in zip(neuron.inputs, neuron.weights):
                delta = (neuron.output - target) * (sigmoidPrime(neuron.net))
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

    def inspect(self):
        # print('------')
        # print('* Inputs: {}'.format(self.input_layer))
        # print('------\n')
        # print('* Hidden Layers')
        for index, hidden_layer in enumerate(self.hidden_layers):
            # print('Hidden Layer #{}:'.format(index+1))
            hidden_layer.inspect()
            # print('\n')
        # print('------')
        # print('* Output Layer')
        self.output_layer.inspect()
        # print('------')

def train(all_inputs, all_targets, min_error, max_epochs, NN, progress_bar):
    # print(all_inputs)
    # print(all_targets)
    acumulated_error = 999
    acumulated_outputs = []
    progress = 80 / max_epochs
    progress_count = 0
    epochs = 0
    errors = []
    while acumulated_error > min_error and epochs < max_epochs:
        for inputs, targets in zip(all_inputs, all_targets):
            NN.input_layer = inputs
            NN.target = targets 

            # Every forward appends a new output
            # Which is used to calculate the acumulated error after each input
            acumulated_outputs.append(NN.forward())
            NN.backprop()
            
        # Get acumulated error
        acumulated_error = np.sum(abs((np.array(all_targets) - np.array(acumulated_outputs))))
        errors.append(acumulated_error)
        # print("Acumulated error", acumulated_error)
        acumulated_outputs = []
        epochs += 1
        progress_count += progress
        progress_bar.setValue(progress_count)

    return errors
        

# NN = NeuralNetwork(layers_structure=[2,4], bias=[0.35], learning_rate = 0.5)

# all_inputs = [[1,1],[2,2],[4,4]]
# all_targets = [[1,0,0,0],[0,1,0,0],[0,0,0,1]]
# min_error = 0.984321
# max_epochs = 7124

# train(all_inputs=all_inputs, all_targets=all_targets, min_error=min_error, max_epochs=max_epochs)  

# print("---------------")
# #Test 1
# NN.input_layer = [1,1]
# print(NN.forward())

# #Test 2
# NN.input_layer = [2,2]
# print(NN.forward())

# #Test 3
# NN.input_layer = [3,3]
# print(NN.forward())
