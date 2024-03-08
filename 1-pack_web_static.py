#!/usr/bin/python3
"""Compressing."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """compressing."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
    except Exception:
        output = None
    return output
