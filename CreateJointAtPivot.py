'''
==============================================================================
!/usr/bin/env python
title           :CreateJointAtPivot.py
description     :Script used to create a joint at the
                 world space coordinates of a selection's pivot
author          :Doug Halley
date            :2018-01-17
version         :3.0
usage           :In Maya CreateJointAtPivot.create_joint_at_pivot()
notes           :
python_version  :2.7.14
==============================================================================
'''

import maya.cmds as cmds


def create_joint_at_pivot():
    '''If there is a valid selection then get the world space
    position of the selection's pivot and create a joint to that
    position.
    '''

    # gets selection from scene
    meshes = cmds.ls(sl=True)

    # checks if there are selections
    # generates popup if there is no valid selction
    if meshes:

        # freeze transforms prior to moving object
        cmds.makeIdentity(apply=True, r=True, s=True, t=True, n=False, pn=True)

        # gets the current world location of the mesh based on its pivot
        cur_pos = cmds.xform(meshes, q=True, ws=True, sp=True)

        # sets joint position at the current position of the selection
        cmds.joint(position=cur_pos, r=True)

    elif not meshes:

        cmds.confirmDialog(
            title='Error',
            message='A mesh was not selected.\nSelect a mesh and re-run ' +
            'script',
            button=['OK'],
            defaultButton='Yes',
            messageAlign='center')
