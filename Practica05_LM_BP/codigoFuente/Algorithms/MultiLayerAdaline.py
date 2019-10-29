import numpy as np
import matplotlib.pyplot as plt

class MLP:
    def __init__(self, classes_count, inputs, architecture, learning_rate, min_error, max_ephocs):
        self.classes_count = classes_count
        self.inputs = inputs
        self.inputs.insert(0,np.random.rand())
        self.architecture = architecture
        self.learning_rate = learning_rate
        self.min_error = min_error
        self.max_ephocs = max_ephocs

        self.errors = []

    def init_weights(self):
        self.weights = []
        # Set layers
        for m in range(len(self.architecture)):
            self.weights.append([])
            # Set neurons
            for i in range(self.architecture[m]):
                self.weights[m].append([])
                # Set weights
                for _ in range(len(self.inputs)):  
                    self.weights[m][i].append(np.random.rand())

    def train(self, progressBar):
        # progress = 100 / self.max_ephocs
        # progressCount = 0

        # self.init_weights()
        
        # self.a_vectors = [[self.inputs]]
        # self.net_vectos = []

        # for ephoc in range(self.max_ephocs):
        #     progressBar.setValue(progressCount)
        #     progressCount += progress
        #     for m in range(len(self.architecture)):
        #         for i in range(self.architecture[m]):
        #             for j in range(len(self.inputs)):
        #                 for input in self.inputs:
        #                     pass
        
        self.errors = np.random.rand(self.max_ephocs)*15
