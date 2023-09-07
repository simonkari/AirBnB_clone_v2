#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Create a compressed archive of the 'web_static' folder.

    Returns:
        str: The path to the compressed archive if successful, None otherwise.
    """
    try:
        with lcd("versions"):
            local("mkdir -p versions")
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            archive_name = "web_static_{}.tgz".format(date)
            archive_path = "versions/{}".format(archive_name)
            local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("Error:", e)
        return None
