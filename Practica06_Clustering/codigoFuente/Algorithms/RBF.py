import numpy as np
import matplotlib.pyplot as plt


class RBF(object):
    """Implementation of a Radial Basis Function Network"""
    def __init__(self, hidden_neurons=2, learning_rate=0.01, max_ephochs=100, min_error = 0.01):
        self.hidden_neurons = hidden_neurons
        self.learning_rate = learning_rate
        self.max_ephochs = max_ephochs
        self.min_eror = min_error
 
        self.w = np.random.randn(hidden_neurons)
        self.bias = np.random.randn(1)

        self.errors = []

    def fit(self, X, y):
        # Training hidden layer
        self.centroids, self.std_dev = self.kmeans(X, self.hidden_neurons)

        # Training output layer
        acumulated_error = 999
        errors = []
        ephoc = 0
        while ephoc < self.max_ephochs:
            self.acumulated_outputs = []
            for i in range(X.shape[0]):
                outputs_rbf = np.array([self.gaussian(X[i], c, s) for c, s, in zip(self.centroids, self.std_dev)])
                net = outputs_rbf.T.dot(self.w) + self.bias
                self.acumulated_outputs.append(net)

    
                error = -(y[i] - net).flatten()
                errors.append(error)
    
                self.w = self.w - self.learning_rate * error * outputs_rbf
                self.bias = self.bias - self.learning_rate * error
            acumulated_error = (np.sum(abs((np.array(y) - np.array(self.acumulated_outputs))))) / (len(y)**2)
            self.errors.append(acumulated_error)
            ephoc += 1

    def predict(self, X):
        y_pred = []
        for i in range(X.shape[0]):
            outputs_rbf = np.array([self.gaussian(X[i], c, s) for c, s, in zip(self.centroids, self.std_dev)])
            net = outputs_rbf.T.dot(self.w) + self.bias
            y_pred.append(net)
        return np.array(y_pred)

    def gaussian(self, x, c, s):
        return np.exp(-1 / (2 * s**2) * (x-c)**2)

    def kmeans(self, X, hidden_neurons):
        '''
        Clustering
        '''
        # Choice random elements
        clusters = np.random.choice(np.squeeze(X), size=hidden_neurons)
        prev_clusters = clusters.copy()
        std_dev = np.zeros(hidden_neurons)
        converged = False

        while not converged:

            distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))

            closestCluster = np.argmin(distances, axis=1)

            for i in range(hidden_neurons):
                pointsForCluster = X[closestCluster == i]
                if len(pointsForCluster) > 0:
                    clusters[i] = np.mean(pointsForCluster, axis=0)

            converged = np.linalg.norm(clusters - prev_clusters) < 1e-6
            prev_clusters = clusters.copy()

        distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))
        closestCluster = np.argmin(distances, axis=1)

        clustersWithNoPoints = []
        for i in range(hidden_neurons):
            pointsForCluster = X[closestCluster == i]
            if len(pointsForCluster) < 2:
                clustersWithNoPoints.append(i)
                continue
            else:
                std_dev[i] = np.std(X[closestCluster == i])

        if len(clustersWithNoPoints) > 0:
            pointsToAverage = []
            for i in range(hidden_neurons):
                if i not in clustersWithNoPoints:
                    pointsToAverage.append(X[closestCluster == i])
            pointsToAverage = np.concatenate(pointsToAverage).ravel()
            std_dev[clustersWithNoPoints] = np.mean(np.std(pointsToAverage))

        return clusters, std_dev


if __name__ == "__main__":
    # sample inputs and add noise
    NUM_SAMPLES = 100
    X = np.random.uniform(0., 1., NUM_SAMPLES)
    X = np.sort(X, axis=0)
    noise = np.random.uniform(-0.1, 0.1, NUM_SAMPLES)
    y = np.sin(2 * np.pi * X)  + noise
    
    rbfnet = RBF(learning_rate=1e-2, hidden_neurons=2)
    rbfnet.fit(X, y)
    
    y_pred = rbfnet.predict(X)
    
    plt.plot(X, y, '-o', label='true')
    plt.plot(X, y_pred, '-o', label='RBF-Net')
    plt.legend()
    
    plt.tight_layout()
    plt.show()