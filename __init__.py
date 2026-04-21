# Based on original work by Renaux Alexandre (@sky-ark)
# Forked and maintained by MaelPERON

bl_info = {
    "name": "ENSI Tool Addon",
    "description": "A simple tool to export objects to RizomUV",
    "author": "MaelPERON",
    "version": (0, 1, 0),
    "blender": (4, 2, 1),
    "category": "Import-Export",
    "location": "View3D > Sidebar",
    "doc_url": "https://github.com/MaelPERON/RizomBridge-Blender",
}

import bpy
from . import operators, panels, preferences

def register():
    operators.register()
    panels.register()
    preferences.register()

def unregister():
    operators.unregister()
    panels.unregister()
    preferences.unregister()

if __name__ == "__main__":
    register()
