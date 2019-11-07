import numpy as np
import matplotlib.pyplot as plt


class RBFNet(object):
    """Implementation of a Radial Basis Function Network"""
    def __init__(self, hidden_neurons=2, lr=0.01, epochs=100, inferStds=True):
        self.hidden_neurons = hidden_neurons
        self.lr = lr
        self.epochs = epochs
        self.inferStds = inferStds
 
        self.w = np.random.randn(hidden_neurons)
        self.b = np.random.randn(1)

        self.errors = []

    def fit(self, X, y):

        self.centers, self.stds = self.kmeans(X, self.hidden_neurons)

    
        # training
        for epoch in range(self.epochs):
            errors = 0
            for i in range(X.shape[0]):
                a = np.array([self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)])
                F = a.T.dot(self.w) + self.b
    
                loss = (y[i] - F).flatten() ** 2
                # print('Loss: {0:.2f}'.format(loss[0]))
    
                error = -(y[i] - F).flatten()
                errors += error[0]
    
                self.w = self.w - self.lr * a * error
                self.b = self.b - self.lr * error
            self.errors.append(errors)

    def predict(self, X):
        y_pred = []
        for i in range(X.shape[0]):
            a = np.array([self.rbf(X[i], c, s) for c, s, in zip(self.centers, self.stds)])
            F = a.T.dot(self.w) + self.b
            y_pred.append(F)
        return np.array(y_pred)

    def rbf(self, x, c, s):
        return np.exp(-1 / (2 * s**2) * (x-c)**2)

    def kmeans(self, X, hidden_neurons):

        clusters = np.random.choice(np.squeeze(X), size=hidden_neurons)
        prevClusters = clusters.copy()
        stds = np.zeros(hidden_neurons)
        converged = False

        while not converged:

            distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))

            closestCluster = np.argmin(distances, axis=1)

            for i in range(hidden_neurons):
                pointsForCluster = X[closestCluster == i]
                if len(pointsForCluster) > 0:
                    clusters[i] = np.mean(pointsForCluster, axis=0)

            converged = np.linalg.norm(clusters - prevClusters) < 1e-6
            prevClusters = clusters.copy()

        distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))
        closestCluster = np.argmin(distances, axis=1)

        clustersWithNoPoints = []
        for i in range(hidden_neurons):
            pointsForCluster = X[closestCluster == i]
            if len(pointsForCluster) < 2:
                clustersWithNoPoints.append(i)
                continue
            else:
                stds[i] = np.std(X[closestCluster == i])

        if len(clustersWithNoPoints) > 0:
            pointsToAverage = []
            for i in range(hidden_neurons):
                if i not in clustersWithNoPoints:
                    pointsToAverage.append(X[closestCluster == i])
            pointsToAverage = np.concatenate(pointsToAverage).ravel()
            stds[clustersWithNoPoints] = np.mean(np.std(pointsToAverage))

        return clusters, stds


if __name__ == "__main__":
    # sample inputs and add noise
    NUM_SAMPLES = 100
    X = np.random.uniform(0., 1., NUM_SAMPLES)
    X = np.sort(X, axis=0)
    noise = np.random.uniform(-0.1, 0.1, NUM_SAMPLES)
    y = np.sin(2 * np.pi * X)  + noise
    
    rbfnet = RBFNet(lr=1e-2, hidden_neurons=2)
    rbfnet.fit(X, y)
    
    y_pred = rbfnet.predict(X)
    
    plt.plot(X, y, '-o', label='true')
    plt.plot(X, y_pred, '-o', label='RBF-Net')
    plt.legend()
    
    plt.tight_layout()
    plt.show()