#!/usr/bin/env python
#title           :originPivot.py
#description     :Script used to move selection and its pivot to the origin
#author          :Doug Halley
#date            :20170713
#version         :2.0
#usage           :In Maya originPivot.originPivot()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def originPivot():
    #gets selection from scene
    meshes=cmds.ls(sl=True)

    if meshes:

        #gets bounding box of selection and saves info of the bounding box into a list as xmin, ymin, zmin, xmax, ymax, zmax
        bbox = cmds.exactWorldBoundingBox(meshes)

        #freeze transforms prior to moving pivot
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True) 

        #checks if upAxis is y
        if cmds.upAxis( q=True, axis=True ) == 'y':
            #define that the selection's pivot should be at the bottom of the bounding box
            bottomPivot = [(bbox[0] + bbox[3])/2, bbox[1], (bbox[2] + bbox[5])/2]

            #moves pivot to the bottom of the bounding box
            cmds.xform(meshes, piv=bottomPivot, ws=True)

            #determines the distance to the origin from the current location in worldspace of the pivot
            distanceToOrigin = [-((bbox[0] + bbox[3])/2), -(bbox[1]), -((bbox[2] + bbox[5])/2)]

        #checks if upAxis is z
        elif cmds.upAxis( q=True, axis=True ) == 'z':
            #define that the selection's pivot should be at the bottom of the bounding box
            bottomPivot = [(bbox[0] + bbox[3])/2, (bbox[1] + bbox[4])/2, bbox[2]]

            #moves pivot to the bottom of the bounding box
            cmds.xform(meshes, piv=bottomPivot, ws=True)

            #determines the distance to the origin from the current location in worldspace of the pivot
            distanceToOrigin = [-((bbox[0] + bbox[3])/2), -((bbox[1] + bbox[4])/2), -(bbox[2])]

        #moves the object to the origin
        cmds.xform(meshes, t = distanceToOrigin,  ws=True) 

        #freeze transforms after the move
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True) 

    elif not meshes:

        cmds.confirmDialog( title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )

