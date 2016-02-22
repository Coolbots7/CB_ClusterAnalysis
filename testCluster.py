from ClusterAnalysis import ClusterAnalysis
import numpy as np

clus = ClusterAnalysis(3)

for i in range(50):
    x = np.random.uniform(0.0,1.0)
    y = np.random.uniform(0.0,1.0)
    z = np.random.uniform(0.0,1.0)
    
    clus.addPattern([x,y,z])

Done = False
prevError = 0
minError = np.inf
while not Done:
    clus.update()

    if clus.Error < minError:
        minError = clus.Error

    if np.abs(clus.Error-prevError) < (clus.Error*0.00001):
        Done = True
        print "Minimum Reached"
    prevError = clus.Error
            
    print clus.Error

print "Min Error: ",
print minError
print "Final Error: ",
print clus.Error
clus.draw()
