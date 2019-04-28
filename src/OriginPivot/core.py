def create_joint_at_pivot():
    """
    If there is a valid selection then get the world space
    position of the selection's pivot and create a joint to that
    position.
    """

    import pymel.core as pm

    meshes = pm.cmds.ls(sl=True)

    # checks if there are selections
    # generates popup if there is no valid selection
    if meshes:
        pm.cmds.makeIdentity(
            translate=True, rotate=True, scale=True,
            apply=True, normal=False, pn=True)

        # freeze transforms prior to moving object

        # gets the current world location of the mesh based on its pivot
        cur_pos = pm.cmds.xform(meshes, q=True, ws=True, sp=True)

        # sets joint position at the current position of the selection
        pm.cmds.joint(position=cur_pos, rotate=True)

    else:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_pivot_to_bottom():
    """
    Move an object and its pivot to the origin.

    Script Steps:
    1. Determines the bounding box of a selection
    2. Finds the bottom center of the selection's bounding box
    3. Moves the pivot to that point in worldspace
    4. Determines the distance between the new position of the pivot and the origin
    5. Moves the selection to the origin
    """

    import pymel.core as pm

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

    else:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\nSelect a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_pivot_to_joint():
    """
    Moves the pivots of selected objects to a selected joint.

    Select the objects and then select a joint. As long as the
    joint is last object selected then the script can continue.
    The script will then move the pivots of the selected objects
    to the joint.
    """

    import pymel.core as pm

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
    """
    Iterates over a selection of objects and moves their pivot to the origin.
    """

    import pymel.core as pm

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

    else:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\n Select a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def move_to_origin():
    """
    Moves the selected objects, based on their pivot,
    to the origin.
    """

    import pymel.core as pm

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
                -(current_position[2])
            ]

            # moves the object to the origin
            pm.cmds.xform(mesh, translate=distance_to_origin, ws=True)

            # freeze transforms after the move
            pm.cmds.makeIdentity(
                translate=True, rotate=True, scale=True,
                apply=True, normal=False, pn=True)

    else:
        pm.cmds.confirmDialog(
            title='Error', message='A mesh was not selected.\n Select a mesh and re-run script',
            button=['OK'], defaultButton='Yes', messageAlign='center')

def create_pivot_bone():
    """
    Copy of Randall Hess's repo:
        https://techanimator.blogspot.com/2018/04/maya-create-bone-at-custom-pivot.html

    Create a bone from the custom pivot context
    """

    import pymel.core as pm

    # get these values
    loc_xform = None
    loc_rp = None

    # Get manipulator pos and orient
    manip_pin = pm.cmds.manipPivot(pinPivot=True)
    manip_pos = pm.cmds.manipPivot(q=True, p=True)[0]
    manip_rot = pm.cmds.manipPivot(q=True, o=True)[0]

    # delete existing temp objs
    temp_joint = None
    temp_loc = None
    temp_cluster = None
    temp_joint_name = 'temp_joint'
    temp_loc_name = 'temp_loc'
    temp_cluster_name = 'temp_cluster'
    temp_objs = [temp_joint_name, temp_loc_name]

    # get the selectMode
    sel_mode_obj = pm.cmds.selectMode(q=True, o=True)
    sel_mode_component = pm.cmds.selectMode(q=True, co=True)

    # store and clear selection
    selection = pm.ls(sl=True)

    if selection:
        sel = selection[0]

        # create temp joint and set pos/rot
        pm.cmds.select(cl=True)
        temp_joint = pm.joint(n=temp_joint_name)
        temp_loc = pm.spaceLocator(n=temp_loc_name)

        # get transform from the selected object
        if isinstance(sel, pm.nt.Transform):
            # snap loc to position
            const = pm.pointConstraint(sel, temp_loc, mo=False, w=1.0)
            pm.delete(const)
            const = pm.orientConstraint(sel, temp_loc, mo=False, w=1.0)
            pm.delete(const)

        elif isinstance(sel, pm.nt.Mesh):
            parent = sel.getParent()
            if parent:
                const = pm.pointConstraint(parent, temp_loc, mo=False, w=1.0)
                pm.delete(const)
                const = pm.orientConstraint(parent, temp_loc, mo=False, w=1.0)
                pm.delete(const)

                # get the transforms
                loc_xform = pm.xform(temp_loc, q=True, m=True, ws=True)
                loc_rp = pm.xform(temp_loc, q=True, ws=True, rp=True)

        # rotate the temp_loc if manip rot has been modified
        if not manip_rot == (0.0, 0.0, 0.0):
            pm.rotate(temp_loc, manip_rot)

        # move position to the cluster position
        if not manip_pos == (0.0, 0.0, 0.0):
            pm.xform(temp_loc, ws=True, t=manip_pos)

        # get the transforms
        loc_xform = pm.xform(temp_loc, q=True, m=True, ws=True)
        loc_rp = pm.xform(temp_loc, q=True, ws=True, rp=True)

        # get the position from the component selection
        if not isinstance(sel, pm.nt.Transform):
            pm.select(selection, r=True)
            pm.ConvertSelectionToVertices()
            try:
                cluster = pm.cluster(n=temp_cluster_name)[1]
            except:
                pm.cmds.warning('You must select a mesh object!')
                pm.delete(temp_joint)
                pm.delete(temp_loc)
                return

            # get the cluster position
            pm.cmds.select(cl=True)
            pos = pm.xform(cluster, q=True, ws=True, rp=True)

            # snap to the cluster
            const = pm.pointConstraint(cluster, temp_loc, mo=False, w=1.0)
            pm.delete(const)

            pm.delete(cluster)

            # rotate the temp_loc if manip rot has been modified
            if not manip_rot == (0.0, 0.0, 0.0):
                pm.rotate(temp_loc, manip_rot)

            # move position to the cluster position
            if not manip_pos == (0.0, 0.0, 0.0):
                pm.xform(temp_loc, ws=True, t=manip_pos)

            # get the transforms
            loc_xform = pm.xform(temp_loc, q=True, m=True, ws=True)
            loc_rp = pm.xform(temp_loc, q=True, ws=True, rp=True)

        # remove temp loc
        pm.delete(temp_loc)

    else:
        pm.cmds.warning('You must have a selection!')
        return

    # modify the joint and stu
    if temp_joint:
        if loc_xform and loc_rp:
            pm.xform(temp_joint, m=loc_xform, ws=True)
            pm.xform(temp_joint, piv=loc_rp, ws=True)

        # freeze orient
        pm.select(temp_joint)
        pm.makeIdentity(apply=True, translate=True, rotate=True, scale=True, n=False)

    # unpin pivot
    pm.cmds.manipPivot(pinPivot=False)
