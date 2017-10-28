#!/usr/bin/env python
#title           :CreateJointAtPivot.py
#description     :Script used to create a joint at the world space coordinates of a selection's pivot
#author          :Doug Halley
#date            :20171028
#version         :1.0
#usage           :In Maya CreateJointAtPivot.CreateJointAtPivot()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def CreateJointAtPivot():
    
    #gets selection from scene
    meshes=cmds.ls(sl=True)

    if meshes:

        #freeze transforms prior to moving object
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True) 

        #gets the current world location of the mesh based on its pivot
        curPos = cmds.xform( meshes, q = True, ws = True, sp = True)

        cmds.joint(position=curPos, r = True)
        
    elif not meshes:

        cmds.confirmDialog( title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )