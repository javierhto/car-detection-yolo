from math import sqrt
import numpy as np

class Detection:
    def __init__(self, id, cls, box):
        self.id = id
        self.cls = cls
        self.box = box
        self.center = (int(box[0]+(box[2]-box[0])/2) , int(box[1]+(box[3]-box[1])/2))
        self.waiting = 0
        self.undetected = 0

    def update(self, box):
        threshold = 5
        if not(np.array_equal(self.box, box)):
            # Se calcula el nuevo centro
            new_center = (int(box[0]+(box[2]-box[0])/2) , int(box[1]+(box[3]-box[1])/2))
            # Se calcula la distancia entre los centros
            dist = sqrt((self.center[0] - new_center[0])**2 + (self.center[1] - new_center[1])**2)
            #print('dist:')
            #  print(dist)
            # Si la distancia es inferior al threshold, se incrementa el contador de espera
            if dist < threshold:
                self.waiting += 1
            else:
                self.waiting = 0
            # Se actualizan los datos de la caja, del centro y el contador de indetectado
            self.box = box
            self.center = new_center
        else:
            self.waiting += 1
        self.undetected = 0

        #if self.waiting > 50:
        #    print(f"Vehiculo {self.id} en espera")

    def notDetected(self):
        self.undetected += 1

    def __str__(self):
        return f"Detección: {self.id}, class: {self.cls}, box: {self.box}, center: {self.center}, wait count: {self.waiting}, undetected: {self.undetected}"