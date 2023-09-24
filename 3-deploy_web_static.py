#!/usr/bin/python3
"""Fabric script to generates a .tgz"""


from fabric.api import *
import os.path
from os import path
from datetime import datetime
from os.path import exists, isfile


env.hosts = ['3.94.185.2', '100.26.132.107']
env.user = 'ubuntu'


def do_pack():
    """ creates tar archive"""
    if path.exists("versions") is False:
        local("mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    pathfile = "versions/web_static" + date + ".tgz"
    local('tar cvfz ' + pathfile + ' web_static')
    if exists(pathfile):
        return (pathfile)
    return None


def do_deploy(archive_path):
    """ deploy a file to web servers"""
    if path.isfile(archive_path) is False:
        return False
    try:
        upload = put(archive_path, '/tmp')
        name = archive_path.split('/')[1][:-4]
        run('sudo mkdir -p /data/web_static/releases/' + name + '/')
        run('tar -xzf /tmp/' + name + '.tgz'
            ' -C /data/web_static/releases/' + name + '/')
        run('rm /tmp/' + name + '.tgz')
        run('mv /data/web_static/releases/' + name + '/web_static/* ' +
            '/data/web_static/releases/' + name + '/')
        run('rm -rf /data/web_static/releases/' + name + '/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/' + name + '/ ' +
            '/data/web_static/current')
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """full deployment"""
    pathfile = do_pack()
    if pathfile:
        return do_deploy(pathfile)
    return False
