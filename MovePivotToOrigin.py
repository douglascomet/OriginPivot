#!/usr/bin/env python
#title           :MovePivotToOrigin.py
#description     :Script used to move each object's pivot from a selection to the origin based on the current worldspace location of the each object's pivot
#author          :Doug Halley
#date            :20171029
#version         :2.0
#usage           :In Maya MovePivotToOrigin.MovePivotToOrigin()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def MovePivotToOrigin():
    
    #gets selection from scene
    meshes=cmds.ls( sl = True )

    if meshes:
        
        for x in meshes:

            #freeze transforms prior to moving object
            cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True )

            #gets the current world location of the mesh based on its pivot
            curPos = cmds.xform( x, q = True, ws = True, piv = True )

            #moves pivot to the bottom of the origin
            cmds.xform( meshes, piv = [ 0, 0, 0 ], ws=True )

            #freeze transforms after the move
            cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True ) 
        
    elif not meshes:

        cmds.confirmDialog( title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )