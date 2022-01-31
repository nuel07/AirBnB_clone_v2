#!/usr/bin/python3
# Fabric script that generates a .tgz archive of web_static content

from datetime import datetime
from fabric.api import *


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
