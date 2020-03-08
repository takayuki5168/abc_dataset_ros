#!/usr/bin/env python

from PySide import QtCore
import sys, os
sys.path.append("/usr/lib/freecad/lib")
import FreeCAD, Part, Mesh

path = os.path.dirname(os.path.abspath(__file__)) + '/../models/step_test/'
dirs = os.listdir(path)

for i in range(len(dirs)):
    dir_path = path + dirs[i]
    for f in [dir_path + '/' + j for j in os.listdir(dir_path)]:
        if '.step' in f:
            file_path = f
    #print(file_path)

    shape = Part.Shape()
    shape.read(file_path)

    doc = App.newDocument('Doc')
    pf = doc.addObject("Part::Feature","MyShape")
    pf.Shape = shape
    #print(file_path.split('.step')[0] + '.stl')
    Mesh.export([pf], dir_path + '/model.stl')
