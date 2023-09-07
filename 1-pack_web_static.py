#!/usr/bin/python3
""" This is a function that compresses a folder. """
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    It should return the archive path if the archive has been
    generated correctly; otherwise, it should return None.
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        rout = "versions/web_static_{}.tgz".format(date)
        _gzip = local("tar -cvzf {} web_static".format(rout))
        return rout
    except Exception:

        return None
