#!/usr/bin/python3
""" This is a function that compresses a folder. """
from datetime import datetime
from fabric.api import local

def do_pack():
    """
    Compresses the 'web_static' folder and generates an
    archive with a timestamp.If successful, it returns
    the path to the archive; otherwise, it returns None.
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")
        
        # Generate a timestamp in the format YYYYMMDDHHMMSS
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Define the archive path with the timestamp
        archive_path = "versions/web_static_{}.tgz".format(date)
        
        # Use 'tar' to compress the 'web_static' folder into the archive
        _gzip = local("tar -cvzf {} web_static".format(archive_path))
        
        # Return the path to the generated archive
        return archive_path
    except Exception:
        # Return None if any exception occurs during the process
        return None
