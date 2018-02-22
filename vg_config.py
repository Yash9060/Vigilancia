"""Initiate and perfrom necessary environment setup for Vigilancia."""
import sys
import os

import vgconf

def _add_extras_path(module_name):
    sys.path.insert(0, os.path.join(vgconf.EXTRAS_PATH, module_name))
    return

def init():
    _add_extras_path(vgconf.DARKFLOW_MODULE_NAME)
    return
