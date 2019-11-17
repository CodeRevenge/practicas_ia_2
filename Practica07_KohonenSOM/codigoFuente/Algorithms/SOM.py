from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import patches as patches

class SOM(QThread):
    countChanged = pyqtSignal(int)
    def __init__(self, k_neighborhood='Cuatro', k_distance= 'Euclidea', mesh_size= 20, max_ephocs= 500, learning_rate= 0.5):
        super(QThread, self).__init__()

        self.training_set = self.load_data()
        self.k_neighborhood = k_neighborhood
        self.k_distance = k_distance
        self.mesh_dimensions = np.array([mesh_size,mesh_size])
        self.max_ephocs = max_ephocs
        self.learning_rate = learning_rate
        self.acumulated_errors = list()
        


    def load_data(self):
        try:
            data_file = open('poker-hand-training-true.data','r')
        except FileNotFoundError:
            try:
                data_file = open('codigoFuente/Algorithms/poker-hand-training-true.data','r')
            except FileNotFoundError:
                data_file = open('Algorithms/poker-hand-training-true.data','r')
        data = []
        for line in data_file.readlines():
            a = line.split(',')
            a = list(map(int,a))[:-1]
            data.append(a)
        data_file.close()
        return np.array(data).T

    def run(self):
        self.train()
    
    def train(self):
        m = self.training_set.shape[0]
        n = self.training_set.shape[1]

        # initial neighbourhood radius
        init_radius = max(self.mesh_dimensions[0], self.mesh_dimensions[1]) / 2
        # radius decay parameter
        time_constant = self.max_ephocs / np.log(init_radius)

        # check if data needs to be normalised
        # normalise along each column
        col_maxes = self.training_set.max(axis=0)
        self.training_set = self.training_set / col_maxes[np.newaxis, :]


        # setup random weights between 0 and 1
        # weight matrix needs to be one m-dimensional vector for each neuron in the SOM
        self.net = np.random.random((self.mesh_dimensions[0], self.mesh_dimensions[1], m))

        progress = 100 / self.max_ephocs
        progress_count = 0

        for i in range(self.max_ephocs):
            error = []
            # print('Iteration %d' % i)
            
            # select a training example at random
            t = self.training_set[:, np.random.randint(0, n)].reshape(np.array([m, 1]))
            
            # find its Best Matching Unit
            bmu, bmu_idx = self.find_bmu(t, self.net, m)
            
            # decay the SOM parameters
            r = self.decrese_radius(init_radius, i, time_constant)
            l = self.decrese_learning_rate(self.learning_rate, i, self.max_ephocs)
            
            # now we know the BMU, update its weight vector to move closer to input
            # and move its neighbours in 2-D space closer
            # by a factor proportional to their 2-D distance from the BMU
            for x in range(self.net.shape[0]):
                for y in range(self.net.shape[1]):
                    w = self.net[x, y, :].reshape(m, 1)
                    # get the 2-D distance (again, not the actual Euclidean distance)
                    if self.k_distance == 'Euclidea':
                        w_dist = np.sum((np.array([x, y]) - bmu_idx) ** 2)
                    elif self.k_distance == 'Coseno':
                        w_dist = np.sum(1- ((np.array([x, y]) * bmu_idx) / (np.sqrt((np.array([x, y]) * bmu_idx) ** 2))))
                    elif self.k_distance == 'Manhattan':
                        w_dist = np.sum(np.fabs(np.array([x, y])-bmu_idx))
                    # if the distance is within the current neighbourhood radius
                    if self.k_neighborhood == 'Cuatro' and w_dist <= r**2:
                            # calculate the degree of influence (based on the 2-D distance)
                            influence = self.calculate_influence(w_dist, r)
                            # now update the neuron's weight using the formula:
                            # new w = old w + (learning rate * influence * delta)
                            # where delta = input vector (t) - old w
                            new_w = w + (l * influence * (t - w))
                            # commit the new weight
                            self.net[x, y, :] = new_w.reshape(1, m)
                            dist = abs(bmu.reshape(m)-np.mean(self.training_set, axis=1))
                            error.append(np.sqrt(np.dot(dist, dist.T)))
                    elif self.k_neighborhood == 'Estrella' and w_dist <= r**4:
                            # calculate the degree of influence (based on the 2-D distance)
                            influence = self.calculate_influence(w_dist, r)
                            # now update the neuron's weight using the formula:
                            # new w = old w + (learning rate * influence * delta)
                            # where delta = input vector (t) - old w
                            new_w = w + (l * influence * (t - w))
                            # commit the new weight
                            self.net[x, y, :] = new_w.reshape(1, m)
                            dist = abs(bmu.reshape(m)-np.mean(self.training_set, axis=1))
                            error.append(np.sqrt(np.dot(dist, dist.T)))
            self.acumulated_errors.append(float(sum(error) / float(len(self.training_set.T))))
            
            progress_count += progress
            if int(progress_count % 5):
                self.countChanged.emit(progress_count)

    def calculate_error(self):
        errs = list()
        for vector in self.training_set.T:
            print(vector)
            indx = np.argmin(np.sum((self.net - vector) ** 2, axis=2))
            w = np.array([int(indx / self.net.shape[0]), indx % self.net.shape[1]])
            dist = self.net[w[0], w[1]] - vector
            errs.append(np.sqrt(np.dot(dist, dist.T)))
        return float(sum(errs) / float(len(self.training_set.T)))

    def decrese_radius(self, initial_radius, i, time_constant):
        return initial_radius * np.exp(-i / time_constant)

    def decrese_learning_rate(self, initial_learning_rate, i, max_ephocs):
        return initial_learning_rate * np.exp(-i / max_ephocs)

    def calculate_influence(self, distance, radius):
        return np.exp(-distance / (2* (radius**2)))

    def find_bmu(self, t, net, m):
        """
            Find the best matching unit for a given vector, t, in the SOM
            Returns: a (bmu, bmu_idx) tuple where bmu is the high-dimensional BMU
                    and bmu_idx is the index of this vector in the SOM
        """
        bmu_idx = np.array([0, 0])
        # set the initial minimum distance to a huge number
        min_dist = np.iinfo(np.int).max    
        # calculate the high-dimensional distance between each neuron and the input
        for x in range(net.shape[0]):
            for y in range(net.shape[1]):
                w = net[x, y, :].reshape(m, 1)
                # don't bother with actual Euclidean distance, to avoid expensive sqrt operation
                # Choose the kind of distance operation
                if self.k_distance == 'Euclidea':
                    sq_dist = np.sum((w - t) ** 2)
                elif self.k_distance == 'Coseno':
                    sq_dist = np.sum(1 - ((w * t) / (np.sqrt((w * t) ** 2))))
                elif self.k_distance == 'Manhattan':
                    sq_dist = np.sum(np.fabs(w-t))
                if sq_dist < min_dist:
                    min_dist = sq_dist
                    bmu_idx = np.array([x, y])
        # get vector corresponding to bmu_idx
        bmu = net[bmu_idx[0], bmu_idx[1], :].reshape(m, 1)
        # return the (bmu, bmu_idx) tuple
        return (bmu, bmu_idx)

    def crate_graph(self):
        fig = plt.figure()
        # setup axes
        ax = fig.add_subplot(111, aspect='equal')
        ax.set_xlim((0, self.net.shape[0]+1))
        ax.set_ylim((0, self.net.shape[1]+1))
        ax.set_title('Self-Organising Map after %d iterations' % self.max_ephocs)

        # plot the rectangles
        for x in range(1, self.net.shape[0] + 1):
            for y in range(1, self.net.shape[1] + 1):
                face_color = self.net[x-1,y-1,:]
                face_color = [sum(face_color[:3])/3,sum(face_color[3:6])/3, sum(face_color[6:])/4]
                ax.add_patch(patches.Rectangle((x-0.5, y-0.5), 1, 1,
                            #  facecolor=net[x-1,y-1,:],
                            facecolor=face_color,
                            edgecolor='none'))
        plt.show()

if __name__ == "__main__":
    som = SOM(max_ephocs=5000)
    som.train()
    som.crate_graph()