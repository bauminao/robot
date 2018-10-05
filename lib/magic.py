import numpy as np

class Magic():
    def __init__(self,model):
        self.model = model
        self.t     = 0.0
        self.steps = 1.0

    def moveNode(self,nid,vector):
        n = self.model.n[nid].getxyz_np()
        self.model.n[nid].setxyz_np(n+vector)
        return n + vector

    def moveElem(self,eid,vector):
        for nid in self.model.e[eid].n:
            self.moveNode(nid , vector)




