#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """
    Creates a tgz archive for deployment
    Return: returns archive path if created or None if failed
    """
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        name = f"versions/web_static_{datetime.now().\
                 strftime(%Y%m%d%H%M%S)}.tgz"
        local(f"tar -cvzf {name} web_static")
        return name
    except Exception:
        return None
