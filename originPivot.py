'''
===============================================================================
!/usr/bin/env python
title           :originPivot.py
description     :Script used to move selection and its pivot to the origin
author          :Doug Halley
date            :2018-01-17
version         :4.0
usage           :In Maya originPivot.obj_and_piv_to_origin()
notes           :
python_version  :2.7.14
===============================================================================
'''

import maya.cmds as cmds


def obj_and_piv_to_origin():
    '''Move an object and its pivot to the origin.

    Script Steps:
    1. Determines the bounding box of a selection
    2. Finds the bottom center of the selection's bounding box
    3. Moves the pivot to that point in worldspace
    4. Determines the distance between the new position of the pivot and the
        origin
    5. Moves the selection to the origin
    '''

    # gets selection from scene
    meshes = cmds.ls(sl=True)

    if meshes:

        # gets bounding box of selection and saves info of the bounding box
        # into a list as xmin, ymin, zmin, xmax, ymax, zmax
        bounding_box = cmds.exactWorldBoundingBox(meshes)

        # freeze transforms prior to moving pivot
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

        # checks if upAxis is y
        if cmds.upAxis(q=True, axis=True) == 'y':

            # define that the selection's pivot should be at the bottom of the
            # bounding box
            bottom_pivot = [
                (bounding_box[0] + bounding_box[3]) / 2,
                bounding_box[1],
                (bounding_box[2] + bounding_box[5]) / 2]

            # moves pivot to the bottom of the bounding box
            cmds.xform(meshes, piv=bottom_pivot, ws=True)

            # determines the distance to the origin from the current location
            # in worldspace of the pivot
            distance_to_origin = [
                -((bounding_box[0] + bounding_box[3]) / 2),
                -(bounding_box[1]),
                -((bounding_box[2] + bounding_box[5]) / 2)]

        # checks if upAxis is z
        elif cmds.upAxis(q=True, axis=True) == 'z':

            # define that the selection's pivot should be at the bottom of the
            # bounding box
            bottom_pivot = [
                (bounding_box[0] + bounding_box[3]) / 2,
                (bounding_box[1] + bounding_box[4]) / 2,
                bounding_box[2]]

            # moves pivot to the bottom of the bounding box
            cmds.xform(meshes, piv=bottom_pivot, ws=True)

            # determines the distance to the origin from the current location
            # in worldspace of the pivot
            distance_to_origin = [
                -((bounding_box[0] + bounding_box[3]) / 2),
                -((bounding_box[1] + bounding_box[4]) / 2),
                -(bounding_box[2])]

        # moves the object to the origin
        cmds.xform(meshes, t=distance_to_origin, ws=True)

        # freeze transforms after the move
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

    elif not meshes:

        cmds.confirmDialog(
            title='Error',
            message='A mesh was not selected.\nSelect a mesh and re-run cript',
            button=['OK'],
            defaultButton='Yes',
            messageAlign='center')
