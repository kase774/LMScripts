#!/usr/bin/python3
import os


def is_root():
    return os.geteuid() == 0

if not is_root():
    print("you're not executing this file as root, which you should probably do since most of them require "
          "commands that need sudo privileges..,")