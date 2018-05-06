===============================
OriginPivot
===============================


'Maya methods to manipulate pivots'

# OriginPivot
This is a Python script designed to move a mesh and its pivot to the origin.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=bphMRwqRSNE
" target="_blank"><img src="http://img.youtube.com/vi/bphMRwqRSNE/0.jpg"
alt="Demo Video" width="240" height="180" border="10" /></a>


I made the script after a request came in from level designers that the pivots of all the 3d models were always different. Modelers can be inconsistent with how they finalize and prep a mesh before being imported into a game engine.

The way it works is that script accesses the bounding box information of the selected mesh, gets the center of the overall selection, moves the pivot to the bottom of the bounding box, determines the difference between the new pivot location and the origin, and moves the mesh to the origin. The script adapts and determines the boudning box based on the up axis being Y or Z.

The function to call to execute the script is originPivot.originPivot()


Installation
============

::

    pip install OriginPivot

    or

    git clone https://github.com/douglascomet/OriginPivot.git
    python setup.py install

Tests
=====
    python setup.py test


Documentation
=============

https://github.com/douglascomet/OriginPivot


Development
===========

To set up `OriginPivot` for local development:

1. Clone the repo locally::

    git clone https://github.com/douglascomet/OriginPivot.git

2. Switch into the environment you want to test in::

    source /tools/maya/bin/activate

3. Install the module in development mode

    make dev


Use the `make` command for a reference of the available development tools in this project.


Tips
----

To run a subset of tests::

    tox -e envname -- py.test -k test_myfeature

To run all the test environments in *parallel* (you need to ``pip install detox``)::

    detox
