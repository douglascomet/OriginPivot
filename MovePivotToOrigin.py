#!/usr/bin/env python
#title           :MovePivotToOrigin.py
#description     :Script used to move each object's pivot from a selection to the origin based on the current worldspace location of the each object's pivot
#author          :Doug Halley
#date            :20171028
#version         :1.0
#usage           :In Maya MovePivotToOrigin.MovePivotToOrigin()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def MovePivotToOrigin():
    
    #gets selection from scene
    meshes=cmds.ls( sl = True )

    if meshes:

        #freeze transforms prior to moving object
        cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True )

        #gets the current world location of the mesh based on its pivot
        curPos = cmds.xform( meshes,q = True, ws = True, piv = True )

        #determines the distance to the origin from the current location in worldspace of the pivot
        distanceToOrigin = [ - ( curPos[ 0 ] ), - ( curPos[ 1 ] ), - ( curPos[ 2 ] ) ]

        #moves pivot to the bottom of the bounding box
        cmds.xform( meshes, piv = distanceToOrigin, ws=True )

        #freeze transforms after the move
        cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True ) 
        
    elif not meshes:

        cmds.confirmDialog( title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )