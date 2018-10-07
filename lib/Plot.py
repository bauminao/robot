import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from time import sleep


class Plot():
    def __init__(self,model):
        self.model = model

        plt.ion()

        self.fig = plt.figure()

        self.ax = plt.axes(projection='3d')
        #self.ax = self.fig.add_subplot(111)

        self.plot_init()


    def plot_init(self):
        plt.xlim(-20,20)
        plt.ylim(-20,20)
        plt.title('model - Nodes @ t=x.y')
        plt.xlabel('X')
        plt.ylabel('Y')



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

        self.ax.plot3D(x,y,z,'r+')

        self.fig.canvas.draw()

        plt.waitforbuttonpress()
        sleep(1)

        return True

    def plot_elems(self):
        return True

