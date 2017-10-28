#!/usr/bin/env python
#title           :MovePivotToJoint.py
#description     :Script used to each object's pivot from a selection to the worldspace location of a selected joint
#author          :Doug Halley
#date            :20171028
#version         :1.0
#usage           :In Maya MovePivotToJoint.MovePivotToJoint()
#notes           :
#python_version  :2.7.5  
#==============================================================================

import maya.cmds as cmds

def MovePivotToJoint():
    
    #gets selection from scene
    selection = cmds.ls(sl=True)

    #get last object in selection which should be a joint
    joint = selection[-1]

    if cmds.objectType(joint, isType = 'joint'):
        
        #gets worldspace position of the joint
        jointPos = cmds.joint(joint, q = True, p = True)

        #removes joint from selection list
        selection.pop()

        errorList = []

        for x in selection:
            
            if cmds.objectType( x, isType = 'nurbsSurface' ) or cmds.objectType( x, isType = 'mesh' ) or cmds.objectType( x, isType = 'transform' ):
                
                #freeze transforms prior to moving object's pivot
                cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True )

                #move object's pivot to the worldspace location of a joint
                cmds.xform( x, piv = jointPos, ws = True)

                #freeze transforms after to moving object's pivot
                cmds.makeIdentity( apply = True, r = True, s = True, t = True, n = False, pn = True )

            else:
                
                errorList.append(x)
                continue

        if errorList:
            cmds.confirmDialog( title='Error', message='Error running script with these objects' + str(errorList), button=['OK'], defaultButton='Yes', messageAlign = "center" )


    else:
        cmds.confirmDialog( title='Error', message='A joint was not selected as the target worldspace position.\nEnsure a joint is selected last and re-run script', button=['OK'], defaultButton='Yes', messageAlign = "center" )
