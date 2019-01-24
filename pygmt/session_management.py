"""
Modern mode session management modules.
"""
from .clib import Session


def begin():
    """
    Initiate a new GMT modern mode session.

    Used in combination with :func:`pygmt.end`.

    Only meant to be used once for creating the global session.

    """
    prefix = "pygmt-session"
    with Session() as lib:
        lib.call_module("begin", prefix)


def end():
    """
    Terminate GMT modern mode session and optionally produce the figure files.

    Called after :func:`pygmt.begin` and all commands that you want included in a
    session. Will finalize any PostScript plots that were made in the
    background, convert them to the desired format (specified in
    ``pygmt.begin``), and bring the figures to the working directory.

    """
    with Session() as lib:
        lib.call_module("end", "")
