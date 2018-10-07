import matplotlib.pyplot as plt

class Plot():
    def __init__(self,model):
        self.model = model

    def plot_nodes(self):
        x = []
        y = []
        z = []
        nlist = []
        for nid,node in self.model.n.items():
            nlist.append(nid)
            x.append(node.x)
            y.append(node.y)
            z.append(node.z)
        plt.xlim(-20,20)
        plt.ylim(-20,20)
        plt.title('model - Nodes @ t=x.y')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.scatter(x,y,s=60, c='blue', marker='x')

        plt.show()
        return True

    def plot_elems(self):
        return True

