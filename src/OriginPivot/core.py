import pymel.core as pm

def create_joint_at_pivot():
    '''If there is a valid selection then get the world space
    position of the selection's pivot and create a joint to that
    position.
    '''

    # gets selection from scene
    meshes = pm.cmds.ls(sl=True)

    # checks if there are selections
    # generates popup if there is no valid selction
    if meshes:
        pm.cmds.makeIdentity(
            translate=True, rotate=True, scale=True,
            apply=True, normal=False, pn=True)

        # freeze transforms prior to moving object

        # gets the current world location of the mesh based on its pivot
        cur_pos = pm.cmds.xform(meshes, q=True, ws=True, sp=True)

        # sets joint position at the current position of the selection
        pm.cmds.joint(position=cur_pos, rotate=True)

    elif not meshes:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_pivot_to_bottom():
    """Move an object and its pivot to the origin.

        Script Steps:
        1. Determines the bounding box of a selection
        2. Finds the bottom center of the selection's bounding box
        3. Moves the pivot to that point in worldspace
        4. Determines the distance between the new position of the pivot and the origin
        5. Moves the selection to the origin
        """

    # gets selection from scene
    meshes = pm.cmds.ls(sl=True)

    if meshes:

        # gets bounding box of selection and saves info of the bounding box
        # into a list as xmin, ymin, zmin, xmax, ymax, zmax
        bounding_box = pm.cmds.exactWorldBoundingBox(meshes)
        pm.cmds.makeIdentity(
            translate=True, rotate=True, scale=True,
            apply=True, normal=False, pn=True)

        # freeze transforms prior to moving pivot

        # checks if upAxis is y
        if pm.cmds.upAxis(q=True, axis=True) == 'y':

            # define that the selection's pivot should be at the bottom of the
            # bounding box
            bottom_pivot = [
                (bounding_box[0] + bounding_box[3]) / 2,
                bounding_box[1],
                (bounding_box[2] + bounding_box[5]) / 2]

            # moves pivot to the bottom of the bounding box
            pm.cmds.xform(meshes, piv=bottom_pivot, ws=True)

        # checks if upAxis is z
        elif pm.cmds.upAxis(q=True, axis=True) == 'z':

            # define that the selection's pivot should be at the bottom of the
            # bounding box
            bottom_pivot = [
                (bounding_box[0] + bounding_box[3]) / 2,
                (bounding_box[1] + bounding_box[4]) / 2,
                bounding_box[2]
            ]

            # moves pivot to the bottom of the bounding box
            pm.cmds.xform(meshes, piv=bottom_pivot, ws=True)

        # freeze transforms after the move
        pm.cmds.makeIdentity(
            translate=True, rotate=True, scale=True,
            apply=True, normal=False, pn=True)

    elif not meshes:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_pivot_to_joint():
    '''Moves the pivots of selected objects to a selected joint.

    Select the objects and then select a joint. As long as the
    joint is last object selected then the script can continue.
    The script will then move the pivots of the selected objects
    to the joint.
    '''

    # gets selection from scene
    selection = pm.cmds.ls(sl=True)

    # get last object in selection which should be a joint
    joint = selection[-1]

    if pm.cmds.objectType(joint, isType='joint'):

        # gets worldspace position of the joint
        joint_pos = pm.cmds.joint(joint, q=True, p=True)

        # removes joint from selection list
        selection.pop()

        # list used to collect objects that aren't accounted for
        error_list = []

        for selected in selection:

            # check for valid object type otherwise populate error_list
            if (
                    pm.cmds.objectType(selected, isType='nurbsSurface') or
                    pm.cmds.objectType(selected, isType='mesh') or
                    pm.cmds.objectType(selected, isType='transform')
                ):

                # freeze transforms prior to moving object's pivot
                pm.cmds.makeIdentity(
                    translate=True, rotate=True, scale=True,
                    apply=True, normal=False, pn=True)

                # move object's pivot to the worldspace location of a joint
                pm.cmds.xform(selected, piv=joint_pos, ws=True)

                # freeze transforms after to moving object's pivot
                pm.cmds.makeIdentity(
                    translate=True, rotate=True, scale=True,
                    apply=True, normal=False, pn=True)

            else:
                error_list.append(selected)
                continue

        if error_list:
            pm.cmds.confirmDialog(
                title='Error',
                message='Error running script with these objects {0}'.format(str(error_list)),
                button=['OK'], defaultButton='Yes', messageAlign='center')

    else:
        pm.cmds.confirmDialog(
            title='Error',
            message=(
                'A joint was not selected as the target worldspace ' +
                'position.\nEnsure a joint is selected last and re-run script'
            ),
            button=['OK'], defaultButton='Yes', messaeAlign='center')

def move_pivot_to_origin():
    '''Iterates over a selection of objects and moves their
    pivot to the origin.
    '''

    # gets selection from scene
    meshes = pm.cmds.ls(sl=True)

    if meshes:
        for mesh in meshes:
            # freeze transforms prior to moving object
            pm.cmds.makeIdentity(
                translate=True, rotate=True, scale=True,
                apply=True, normal=False, pn=True)

            # moves pivot to the bottom of the origin
            pm.cmds.xform(mesh, piv=[0, 0, 0], ws=True)

            # freeze transforms after the move
            pm.cmds.makeIdentity(
                translate=True, rotate=True, scale=True,
                apply=True, normal=False, pn=True)

    elif not meshes:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\n Select a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_to_origin():
    '''Moves the selected objects, based on their pivot,
    to the origin.
    '''

    # gets selection from scene
    meshes = pm.cmds.ls(sl=True)

    if meshes:
        for mesh in meshes:
            # freeze transforms prior to moving object
            pm.cmds.makeIdentity(
                translate=True, rotate=True, scale=True,
                apply=True, normal=False, pn=True)

            # gets the current world location of the mesh based on its pivot
            current_position = pm.cmds.xform(mesh, q=True, ws=True, piv=True)

            # determines the distance to the origin from the current location
            # in worldspace of the pivot
            distance_to_origin = [
                -(current_position[0]),
                -(current_position[1]),
                -(current_position[2])]

            # moves the object to the origin
            pm.cmds.xform(mesh, translate=distance_to_origin, ws=True)

            # freeze transforms after the move
            pm.cmds.makeIdentity(
                translate=True, rotate=True, scale=True,
                apply=True, normal=False, pn=True)

    elif not meshes:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\n Select a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')
