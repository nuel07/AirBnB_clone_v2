#!/usr/bin/python3
"""Fabfile that creates and distributes archive to web servers"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["3.239.76.17", "34.229.62.150"]
env.user = "ubuntu"


def do_pack():
    """
    Return archive path if correctly generated,
    otherwise Return None
    """
    local("mkdir -p versions")
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static.{}.tgz".format(dt)
    tgzip = local("tar -cvzf {} web_static".format(file_path))

    if tgzip.succeeded:
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes archive to my web servers.
    Args:
       archive_path: path to the archive to be distributed
    Return:
       False, if file doesn't exist at archive_path
       True, otherwise
    """
    if os.path.exists(archive_path):
        file_archive = archive_path[9:]
        new_version = "/data/web_static/releases/" + file_archive[:-4]
        file_archive = "/tmp/" + file_archive
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_version))
        run("sudo tar -xzf {} -C {}/".format(file_archive, new_version))
        run("sudo rm {}".format(file_archive))
        run("sudo mv {}/web_static/* {}".format(new_version, new_version))
        run("sudo rm -rf {}/web_static".format(new_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_version))
        return True
    return False


def deploy():
    '''Create and distribute an archive to my web servers.'''
    path = do_pack()
    if path:
        do_deploy(path)
    return False
