#!/usr/bin/env python
from lib import fem
from lib import magic

import numpy as np


def main():
    robot = fem.Model()


    print ("")
    robot.import_model("model.inp")
    print ("")

    #robot.node(6 , 10.0 , 10.0 , 0.0)
    #robot.element(2, 1, 2)

    robot.dumpNodes()
    print ("")
    robot.dumpElements()
    print ("")

    run = magic.Magic(robot)

    vector = np.array([ 5.0 , 5.0 , 0.0 ])
    run.moveNode(1,vector)
    run.moveElem(1,vector)

    robot.dumpNodes()
    
if __name__ == "__main__":
    main()
