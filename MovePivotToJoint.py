'''
==============================================================================
!/usr/bin/env python
title           :MovePivotToJoint.py
description     :Script used to each object's pivot from a selection to the
                worldspace location of a selected joint
author          :Doug Halley
date            :2018-01-17
version         :3.0
usage           :In Maya move_pivot_to_joint.move_pivot_to_joint()
notes           :
python_version  :2.7.14
==============================================================================
'''

import maya.cmds as cmds


def move_pivot_to_joint():
    '''Moves the pivots of selected objects to a selected joint.

    Select the objects and then select a joint. As long as the
    joint is last object selected then the script can continue.
    The script will then move the pivots of the selected objects
    to the joint.
    '''

    # gets selection from scene
    selection = cmds.ls(sl=True)

    # get last object in selection which should be a joint
    joint = selection[-1]

    if cmds.objectType(joint, isType='joint'):

        # gets worldspace position of the joint
        joint_pos = cmds.joint(joint, q=True, p=True)

        # removes joint from selection list
        selection.pop()

        # list used to collect objects that aren't accounted for
        error_list = []

        for selected in selection:

            # check for valid object type otherwise populate error_list
            if cmds.objectType(selected, isType='nurbsSurface') or \
                cmds.objectType(selected, isType='mesh') or \
                    cmds.objectType(selected, isType='transform'):

                # freeze transforms prior to moving object's pivot
                cmds.makeIdentity(
                    apply=True,
                    r=True,
                    s=True,
                    t=True,
                    n=False,
                    pn=True)

                # move object's pivot to the worldspace location of a joint
                cmds.xform(selected, piv=joint_pos, ws=True)

                # freeze transforms after to moving object's pivot
                cmds.makeIdentity(
                    apply=True,
                    r=True,
                    s=True,
                    t=True,
                    n=False,
                    pn=True)

            else:
                error_list.append(selected)
                continue

        if error_list:
            cmds.confirmDialog(
                title='Error',
                message='Error running script with these objects' +
                str(error_list),
                button=['OK'],
                defaultButton='Yes',
                messageAlign='center')

    else:
        cmds.confirmDialog(
            title='Error',
            message='A joint was not selected as the target worldspace ' +
            'position.\nEnsure a joint is selected last and re-run script',
            button=['OK'],
            defaultButton='Yes',
            messaeAlign='center')
