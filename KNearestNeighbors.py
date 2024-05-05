import math

class K_NearestNeighbors:
    def __init__(self, idata: dict):
        self.data = idata

    def distance(self, points1, points2):
        if not (len(points1) == len(points2)):
            print("Image resolution is incorrect.")
            return 
        suma = 0
        for i in range(len(points1)):
            suma += pow(points1[i] - points2[i], 2)
        return math.sqrt(suma)

    def allEqual(self, lst):
        if len(lst) < 2:
            return True
        
        first = lst[0]
        for v in lst[1:]:
            if v != first:
                return False
        return True

    def getNearest(self, nearestNeighbors, nearestObj, points):
        dista = []
        for nr in nearestNeighbors:
            dista.append(self.distance(nr, points))
        min_dist = min(dista)
        min_ind = dista.index(min_dist)
        return nearestObj[min_ind]

    def predict(self, points: list, k: int):
        nearestNeighbors = []
        for key in self.data:
            dista = self.distance(points, key)
            if dista <= k:
                nearestNeighbors.append(key)
        nearestObj = []
        for near in nearestNeighbors:
            nearestObj.append(self.data[near])
        
        if len(nearestNeighbors) == 0:
            return None
        
        if len(nearestNeighbors) == 1:
            return nearestObj[0]
        if self.allEqual(nearestObj):
            return nearestObj[0]
        
        return self.getNearest(nearestNeighbors, nearestObj, points)
