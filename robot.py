#!/usr/bin/env python

import numpy
from lib.fem import Model
from lib.fem import Node

from lib.magic import Magic


def main():
    robot = Model()
    node=Node(1 , 0.0 , 0.0 )

    robot.addNode(2, 10.0 , 5.0)
    robot.addNode(4, 12.0 , 8.0)
    robot.addNode(6, 14.0 , 10.0)
    robot.addNode(8, 16.0 , 11.0)
    robot.addNode(2, 18.0 , 15.0)

    robot.addElement(1)

    robot.addNodeToElem(1,8,2,6)

    robot.dumpNodes()
    robot.dumpElements()

    run = Magic(robot)

    vector = (1 , 1 , 0)
    run.MoveNode(1,vector)
    
if __name__ == "__main__":
    main()
