#!/usr/bin/env python
#title           :MoveToOrigin.py
#description     :Script used to move selection to the origin based on the worldspace location of the selection's pivot
#author          :Doug Halley
#date            :20171028
#version         :1.0
#usage           :In Maya MoveToOrigin.MoveToOrigin()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def MoveToOrigin():
    
    #gets selection from scene
    meshes=cmds.ls(sl=True)

    if meshes:

        #freeze transforms prior to moving object
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True) 

        #gets the current world location of the mesh based on its pivot
        curPos = cmds.xform(meshes,q = True, ws = True, piv = True)

        #determines the distance to the origin from the current location in worldspace of the pivot
        distanceToOrigin = [-(curPos[0]), -(curPos[1]), -(curPos[2])]

        #moves the object to the origin
        cmds.xform(meshes, t = distanceToOrigin,  ws=True) 

        #freeze transforms after the move
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True) 
        
    elif not meshes:

        cmds.confirmDialog( title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )