#!/usr/bin/python3
"""
A Fabric script that distributes an archive to the web servers,
built upon the file 1-pack_web_static.py.
"""

from fabric.api import put, run, env
from os.path import exists

# Define the list of remote hosts
env.hosts = ['54.87.157.153', '52.91.124.211']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    # Check if the specified archive_path exists on the local system
    if exists(archive_path) is False:
        return False
    try:
        # Extract necessary information from the archive_path
        file_n = archive_path.split("/")[-1]  # Extract the file name
        no_ext = file_n.split(".")[0]         # Remove the file extension
        path = "/data/web_static/releases/"

        # Upload the archive to the remote /tmp/ directory
        put(archive_path, '/tmp/')

        # Create a directory for the new release and extract the archive into it
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        # Remove the uploaded archive from the remote /tmp/ directory
        run('rm /tmp/{}'.format(file_n))

        # Move the contents of the web_static directory to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))

        # Remove the now empty web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Update the symbolic link to the new release
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        return True
    except Exception as e:
        # Return False if any exception occurs during the process
        print(e)
        return False
