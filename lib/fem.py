# Klassendefinitionen fuer den FEM-analogen Bastelkram

class Node:
    def __init__(self, nid , x , y , z=0):
        self.nid = nid
        self.x   = x
        self.y   = y 
        self.z   = 0.0

class Element:
    def __init__(self, eid):
        self.eid = eid
        self.n   = {}
    

class Model:
    def __init__(self):
        self.n = {}
        self.e = {}

    def addNode(self,*args):
        if len(args) == 3:
            node = Node(args[0], args[1], args[2], 0.0)
            self.n.update({ node.nid : node})

        elif len(args) == 4:
            node = Node(args[0], args[1], args[2], args[3])
            self.n.update({ node.nid : node})
        else:
            print ("Wrong node definition.")

    def addElement(self,*args):
        if len(args) == 1:
            eid=args[0]
            elem = Element(eid)
            self.e.update({ elem.eid : elem})
        else:
            print ("Wrong Element definition.")

    def addNodeToElem(self,eid,*args):
        if len(args) < 1:
            print ("No nodes defined to connect to Element")
            return False
        else:
            for nid in args:
                self.e[eid].n.update({nid:self.n[nid]})


    def dumpElements(self):
        for eid, elem in self.e.items():
            print("EID: " + str(elem.eid) + " -- ", end='')
            for nid, node in elem.n.items():
                print ("N" + str(nid) + " " , end='')
            print ('')

    def dumpNodes(self):
        for nid, node in self.n.items():
            print ("NID: " + str(node.nid) + " -- (" + str(node.x) + " / " + str(node.y) + " / " + str(node.z) + " ) ")









