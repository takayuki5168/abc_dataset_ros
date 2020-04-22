#!/usr/bin/env python

from PySide import QtCore
import sys, os
sys.path.append("/usr/lib/freecad/lib")
import FreeCAD, Part, MeshPart
#import FreeCAD, Part, Mesh

path = os.path.dirname(os.path.abspath(__file__)) + '/../models/step_test/'
dirs = os.listdir(path)

# for i in range(len(dirs)):
#     dir_path = path + dirs[i]
#     for f in [dir_path + '/' + j for j in os.listdir(dir_path)]:
#         if '.step' in f:
#             file_path = f
#     #print(file_path)

#     shape = Part.Shape()
#     shape.read(file_path)

#     doc = App.newDocument('Doc')
#     pf = doc.addObject("Part::Feature","MyShape")
#     pf.Shape = shape
#     #print(file_path.split('.step')[0] + '.stl')
#     Mesh.export([pf], dir_path + '/model.stl')







for i in range(len(dirs)):
    dir_path = path + dirs[i]
    for f in [dir_path + '/' + j for j in os.listdir(dir_path)]:
        if '.step' in f:
            file_path = f

    file = file_path
    FreeCAD.newDocument()
    FreeCAD.setActiveDocument("Unnamed")
    doc = FreeCAD.getDocument("Unnamed")
    FreeCAD.ActiveDocument = doc
    Part.insert(file,"Unnamed")

    # before converting to mesh we need to merge all shapes in the document
    if len(doc.Objects) > 1:
        FreeCAD.activeDocument().addObject("Part::MultiFuse","Fusion")
        FreeCAD.activeDocument().Fusion.Shapes = [doc.Objects[k] for k in range(len(doc.Objects) - 1)]
        FreeCAD.ActiveDocument.recompute()
        mesh = doc.addObject("Mesh::Feature","Mesh")
        mesh.Mesh = MeshPart.meshFromShape(doc.getObject("Fusion").Shape,5,0,0,0.5)
    else:
        mesh = doc.addObject("Mesh::Feature","Mesh")
        mesh.Mesh = MeshPart.meshFromShape(doc.getObject(doc.Objects[0].Name).Shape,5,0,0,0.5)

    del doc, mesh

    # saving the stl file
    file_stl = file.replace(".step", ".stl")
    FreeCAD.ActiveDocument.getObject("Mesh").Mesh.write(file_stl,"STL")
    FreeCAD.closeDocument("Unnamed")

    # using meshlab to convert stl files to dae
    file_dae = file.replace(".step", ".dae")
    convert = "meshlabserver -i " + file_stl + " -o " + file_dae
    os.system(convert)
    #os.system("rm " + file_stl)
    #if not os.path.exists(cwd + "done_step/"):
    #    os.makedirs(cwd + "done_step/")
    #os.system("mv " + file + " " + cwd + "done_step/")
