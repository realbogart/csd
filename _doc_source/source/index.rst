%%%%%%%%%%%%%%%%%%%%%%%%%
Csound csd Python Package
%%%%%%%%%%%%%%%%%%%%%%%%%

.. toctree::
    :maxdepth: 2

    Installing csd <install.rst>
    CSD Modules <csd_sco_event.rst>
    PythonScore <pysco.rst>
    Demo Scripts <demo/index.rst>
    Command-Line <commandline.rst>
    bugs.rst
    glossary.rst

..
    A Pysco Score TOOTorial <pysco_toot.rst>

Mission Statement
-----------------

*"Enable users to process and generate Csound orchestras and scores
quickly, easily and efficiently."*

Download
--------

`Download Latest as Zip <https://github.com/jacobjoaquin/csd/zipball/master>`_

`Download Latest as TAR Ball <https://github.com/jacobjoaquin/csd/tarball/master>`_

About
-----

CSD provides core functions for building python scripts that can process
and generate Csound code.

As of this moment, the focus is on score manipulation.  CSD comes with
many functions that can parse, pull, push information in and out of
Csound scores.  In the future, there are plans to provide equivalent
functions for Csound orchestras.

This package ships with a few demo scripts that can be of great use to
anyone who writes Csound music the old fashion way, that is, with a text
editor. The ``sco_align`` script will save you from repeatedly typing
'space-down-left' by aligning Csound scores auto-magically.  If you need
to run a dozen or more pfields through a function, ``pfunc`` lets your
write your own function and choose which instruments and pfields to
operate on with a single command-line in a terminal window.  Or if you
are organizing your pfields, and decided that amp would work better on
pfield 4 and pitch on pfield 5, then ``swap_columns`` is just what you
need.

In order to use these demo scripts, you'll need to use a command-line
terminal.  However, using these scripts in applications may be possible
in the future.

If you are a developer of a Csound front-end, Csound based-app, or are
just looking to extend the capabilities of your favorites text editor,
let me know so we can start the process of figuring out our respective
needs to make this happen. I'm open to any and all ideas from anyone.

Csd is requires Python 2.7. And maybe Python 2.6.

Information
-----------

Csound csd Python Package

By Jacob Joaquin

jacobjoaquin@gmail.com

http://twitter.com/JacobJoaquin

copyright (c) Jacob Joaquin 2009


License
-------
GNU Lesser General Public License

Version 3, 29 June 2007

http://www.gnu.org/licenses/lgpl.html

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

