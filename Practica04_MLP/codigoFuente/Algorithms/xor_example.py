from ann_new import NeuralNetwork
from timeit import default_timer as timer

inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
targets = [[1, 0],[0, 1],[0, 1],[1, 0]]
learning_rate = 1.5

# Input layer (1 per input) - Hidden Layers - Output Layer (1 per class)
structure = (len(inputs[0]), 8, len(targets[0]))

start = timer()

NN = NeuralNetwork(inputs=inputs, learning_rate=learning_rate, structure=structure,  bias=.35)
NN.train(training_inputs=inputs, training_targets=targets, max_epochs=10000, min_error=5)

def getBiggestIndex(array):
    return list(array).index(max(array))

print(NN.forwardPropagation(inputs[0]))
print(getBiggestIndex(NN.forwardPropagation(inputs[0])))

print(NN.forwardPropagation(inputs[1]))
print(getBiggestIndex(NN.forwardPropagation(inputs[1])))

print(NN.forwardPropagation(inputs[2]))
print(getBiggestIndex(NN.forwardPropagation(inputs[2])))

print(NN.forwardPropagation(inputs[3]))
print(getBiggestIndex(NN.forwardPropagation(inputs[3])))

end = timer()
print("Time:", end - start)