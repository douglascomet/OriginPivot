# ==============================================================================
# !/usr/bin/env python
# title           :MoveToOrigin.py
# description     :Script used to move selection to the origin based on the
#                   worldspace location of the selection's pivot
# author          :Doug Halley
# date            :2017-12-21
# version         :1.0
# usage           :In Maya move_to_origin.move_to_origin()
# notes           :
# python_version  :2.7.5
#==============================================================================

import maya.cmds as cmds

def move_to_origin():
    """Moves the selected objects, based on their pivot,
    to the origin.
    """

    # gets selection from scene
    meshes = cmds.ls(sl=True)

    if meshes:

        # freeze transforms prior to moving object
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

        # gets the current world location of the mesh based on its pivot
        current_position = cmds.xform(meshes, q=True, ws=True, piv=True)

        # determines the distance to the origin from the current location
        # in worldspace of the pivot
        distance_to_origin = [-(current_position[0]), -(current_position[1]), \
            -(current_position[2])]

        #moves the object to the origin
        cmds.xform(meshes, t=distance_to_origin, ws=True)

        #freeze transforms after the move
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

    elif not meshes:

        cmds.confirmDialog(title='Error', message='A mesh was not selected.\n \
            Select a mesh and re-run script', button=['OK'], \
                defaultButton='Yes', messageAlign="center")

