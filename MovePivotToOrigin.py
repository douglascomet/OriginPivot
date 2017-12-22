# ==============================================================================
# !/usr/bin/env python
# title           :MovePivotToOrigin.py
# description     :Script used to move each object's pivot from a selection
#                   to the origin based on the current worldspace location
#                   of the each object's pivot
# author          :Doug Halley
# date            :2017-12-21
# version         :3.0
# usage           :In Maya move_pivot_to_origin.move_pivot_to_origin()
# notes           :
# python_version  :2.7.5
#==============================================================================

import maya.cmds as cmds

def move_pivot_to_origin():
    """Iterates over a selection of objects and moves their
    pivot to the origin.
    """

    #gets selection from scene
    meshes = cmds.ls(sl=True)

    if meshes:

        for mesh in meshes:

            #freeze transforms prior to moving object
            cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

            #moves pivot to the bottom of the origin
            cmds.xform(mesh, piv=[0, 0, 0], ws=True)

            #freeze transforms after the move
            cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

    elif not meshes:

        cmds.confirmDialog(title='Error', message='A mesh was not selected.\n \
            Select a mesh and re-run script', button=['OK'], defaultButton='Yes', \
                messageAlign='center')
