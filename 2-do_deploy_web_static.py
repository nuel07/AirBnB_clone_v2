#!/usr/bin/python3
"""Fabfile that distributes archive to web servers."""

from fabric.api import *
import os

env.hosts = ["3.239.76.17", "34.229.62.150"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distribute archive to web servers path if correctly generated,
    otherwise Return False
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
        run("sudo ln -s {} /data/web_static/current"
            .format(new_version))
        return True
    return False
