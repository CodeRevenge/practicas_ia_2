from PyQt5.QtCore import QThread, pyqtSignal
import time
import random
import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

class RBF(QThread):
    countChanged = pyqtSignal(int)
    def __init__(self, inputs = None, clusters_count= 5):
        super(QThread, self).__init__()

        if inputs is None:
            raise Exception('There is no inputs')

        if clusters_count > len(inputs):
            raise Exception('The algorithm need at least the same number of inputs and clusters')

        self.DIMENSIONS = len(inputs[0])

        self.inputs = np.array(inputs, dtype=np.float64)
        self.clusters_count = clusters_count


        self.clusters = []
        self.hidden_neurons = []

        self.isConverged = [False]*self.clusters_count

    def run(self):
        # range_inp = np.arange(len(self.inputs))
        # self.centroids = self.inputs[np.random.choice(range_inp,\
        #     self.clusters_count, replace=False)].copy()
        self.centroids = self.inputs[:self.clusters_count].copy()
        self.clusters = [[] for _ in self.centroids]

        while not all(self.isConverged):


            for pattern in self.inputs:
                menor = self.centroids[0]
                indx = 0
                for index, centroid in enumerate(self.centroids):
                    if la.norm(pattern.T - centroid)**2 < la.norm(pattern.T - menor)**2:
                        menor = centroid
                        indx = index
                if not self.isConverged[indx]:
                    self.clusters[indx].append(pattern)

            plot_centroids(self.clusters, self.centroids)

            for index, cluster in enumerate(self.clusters):
                mean = np.mean(cluster, axis= 0, dtype=np.float64)
                if (abs(mean - self.centroids[index]) <= 1e-10).all():
                    self.isConverged[index] = True
                else:
                    self.centroids[index] = mean
                    self.isConverged[index] = False
                    self.clusters[index] = []

        # plot_centroids(self.clusters, self.centroids)
        for index, cluster in enumerate(self.clusters):
            # if self.DIMENSIONS > 1:
            #     cov_matx = np.cov([np.array(cluster)[:,0], np.array(cluster)[:,1]])
            # else:
            #     cov_matx = np.std(cluster)
            
            # gaussian = np.exp(-0.5((cluster-self.centroids[index]).T * la.inv(cov_matx) * (cluster-self.centroids[index]))) \
            #     / (2 * np.pi())**(self.DIMENSIONS/2) * np.fabs(cov_matx)**(1/2)

            std_dev = np.std(cluster)

            gaussian = np.exp((-la.norm(pattern.T - self.centroids[index])**2) / 2 * std_dev**2)

            self.hidden_neurons.append(gaussian)

            print(1)

                

def plot_centroids(clusters, centroids):
    a = np.array(sum(clusters,[]))
    centroids = np.array(centroids)
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.scatter(a[:,0],a[:,1], c='r', s=15)
    plt.scatter(centroids[:,0],centroids[:,1], c='b', s=20)
    for index, cluster in enumerate(clusters):
        for pattern in cluster:
            plt.plot([pattern[0],centroids[index][0]], [pattern[1], centroids[index][1]], c='b')
    plt.axis(True)

    plt.show()
    
if __name__ == "__main__":
    try:
        # inputs = np.random.randint(-5,5,(8,2))
        inputs = [[-2,3],[-2,1],[-3,2],[2,-2],[3,-2],[3,-1],[-3,-3],[-2,-2],[-4,-1],[2,3],[3,2],[4,3],[-3.16,3.43],[-4.34,-2.87],[4.13,-2.16],[2.87,4.23]]
        random.shuffle(inputs)
        print(inputs)
        rbf = RBF(inputs,4)
        rbf.run()
        print(rbf.clusters)
        print(rbf.centroids)

        plot_centroids(rbf.clusters, rbf.centroids)

    except KeyboardInterrupt:
        print('The execution was interrupted')
        
        