#!/usr/bin/env python
from lib import Fem
from lib import Run
from lib import Plot

import numpy as np


def main():
    robot = Fem.Model()
    gui = Plot.Plot(robot)


    print ("")
    robot.import_model("model.inp")
    print ("")

    #robot.node(6 , 10.0 , 10.0 , 0.0)
    #robot.element(2, 1, 2)

    robot.dumpNodes()
    print ("")
    robot.dumpElements()
    print ("")

    gui.plot_nodes()

    run = Run.Run(robot)

    vector = np.array([ 5.0 , 5.0 , 0.0 ])
    run.moveNode(1,vector)
    run.moveElem(1,vector)

    robot.dumpNodes()
    print ("")

    gui.plot_nodes()

    print ("")


    
if __name__ == "__main__":
    main()
