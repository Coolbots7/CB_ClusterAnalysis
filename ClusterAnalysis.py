import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Cluster:
    def __init__(self,pos):
        self.pos = pos
        self.deltaPos = [0,0,0]

        self.color = '#%02X%02X%02X' % (np.random.randint(100,256),np.random.randint(100,256),np.random.randint(100,256))

    def draw(self, ax):
        ax.scatter(self.pos[0], self.pos[1], self.pos[2], c='black')

class Pattern:
    def __init__(self,pos):
        self.pos = pos
        self.cluster = None

    def printCluster(self):
        print self.cluster

    def draw(self, ax, color):
        ax.scatter(self.pos[0], self.pos[1], self.pos[2], c=color)

class ClusterAnalysis:
    def __init__(self, numC):
        self.numClusters = numC
        self.clusters = []
        for i in range(numC):
            self.clusters.append(Cluster([np.random.uniform(0.0,1.0),np.random.uniform(0.0,1.0),np.random.uniform(0.0,1.0)]))

        self.numPatterns = 0
        self.patterns = []
        
        self.Error = 0

        self.learningRate = 0.1

    def normalize(self, array):
        maxVal = np.amax(array)

        return np.divide(array, float(maxVal))

    def addPattern(self,pos):
        self.patterns.append(Pattern(pos))
        self.numPatterns += 1

    def calcE(self):
        self.Error = 0
        for i in range(self.numPatterns):
            e=np.inf
            ji = -1
            for j in range(self.numClusters):
                diff = np.subtract(self.patterns[i].pos,self.clusters[j].pos)
                sqr = np.power(np.abs(diff),2)
                ei = np.sum(sqr)

                if ei < e:
                    e = ei
                    ji = j

            self.patterns[i].cluster = ji
            self.Error += e

    def minE(self):
        idx = np.random.randint(0,self.numPatterns)
        cluster = self.patterns[idx].cluster
        delta = np.multiply(np.subtract(self.patterns[idx].pos, self.clusters[cluster].pos), self.learningRate)
        if np.array_equal(delta, [0,0,0]):
            return True
        else:
            self.clusters[cluster].pos += delta
            return False

    def update(self):
        self.calcE()
        return self.minE()

    def printClusters(self):
        for i in self.patterns:
            i.printCluster()

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for i in self.patterns:
            i.draw(ax, self.clusters[i.cluster].color)

            ax.plot((i.pos[0],self.clusters[i.cluster].pos[0]),(i.pos[1],self.clusters[i.cluster].pos[1]),(i.pos[2],self.clusters[i.cluster].pos[2]), c=self.clusters[i.cluster].color)
            
        for i in self.clusters:
            i.draw(ax)

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
            

        plt.show()
