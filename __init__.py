# Based on original work by Renaux Alexandre (@sky-ark)
# Forked and maintained by MaelPERON

from . import auto_load

bl_info = {
    "name": "ENSI Tool Addon",
    "description": "Bridge between Blender and RizomUV for efficient UV unwrapping",
    "author": "MaelPERON, sky-ark",
    "version": (1, 0, 0),
    "blender": (4, 2, 1),
    "category": "Import-Export",
    "location": "View3D > Sidebar",
    "doc_url": "https://github.com/MaelPERON/RizomBridge-Blender",
}

auto_load.init()


def register():
    auto_load.register()
    print("Blender_ensi registered.")


def unregister():
    auto_load.unregister()
