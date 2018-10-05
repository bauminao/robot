# Klassendefinitionen fuer den FEM-analogen Bastelkram
class Node:
    def __init__(self):
        self.nid = 0
        self.x   = 0.0
        self.y   = 0.0
        self.z   = 0.0

    def add (self, nid, x , y , z):
        self.nid = nid
        self.x = x
        self.y = y
        self.z = z

class Element:
    def __init__(self):
        self.eid = 0
        self.n   = dict()

    def add (self, eid):
        self.eid = eid

    def connect(self,node):
        self.n.update({node.nid:node})

    
class Model:
    def __init__(self):
        self.n = dict()
        self.e = dict()

    def node(self,nid,x,y,z):
        if nid==0:
            if len(self.n) == 0:
                nid = 1
            else:
                maxnid = sorted(self.n)[len(self.n)-1]
                nid=maxnid+1

        node = Node()
        node.add(nid, x,y,z)
        self.n.update({node.nid:node})
        return nid

    def checknode(self,nid):
        return nid in self.n

    def element(self,eid,*args):
        if eid==0:
            if len(self.e) == 0:
                eid = 1
            else:
                maxeid = sorted(self.e)[len(self.e)-1]
                eid=maxeid+1
        elem = Element()
        elem.add(eid)
        self.e.update({elem.eid:elem})

        for nid in args:
            if self.checknode(nid):
                node=self.n[nid]
                elem.connect(node)
        return eid

    def dumpElements(self):
        for eid, elem in self.e.items():
            print("EID: " + str(elem.eid) + " -- ", end='')
            for nid, node in elem.n.items():
                print ("N" + str(nid) + " " , end='')
            print ('')

    def dumpNodes(self):
        for nid, node in self.n.items():
            print ("NID: " + str(node.nid) + " -- (" + str(node.x) + " / " + str(node.y) + " / " + str(node.z) + " ) ")









