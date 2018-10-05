#!/usr/bin/env python
from lib import fem
from lib import magic

import numpy as np


def main():
    robot = fem.Model()

    robot.node(0 , 10.0 , 5.0  , 0.0)
    robot.node(4 , 12.0 , 8.0  , 0.0)
    robot.node(6 , 14.0 , 10.0 , 0.0)
    robot.node(0 , 16.0 , 11.0 , 0.0)
    robot.node(2 , 18.0 , 15.0 , 0.0)
    robot.node(6 , 10.0 , 10.0 , 0.0)

    robot.element(0)
    robot.element(0)
    robot.element(3, 4)
    robot.element(2, 1, 2)

    robot.dumpNodes()
    robot.dumpElements()

    run = magic.Magic(robot)

    vector = np.array([ 1.0 , 0.0 , 0.0 ])
    run.MoveNode(1,vector)
    
if __name__ == "__main__":
    main()
