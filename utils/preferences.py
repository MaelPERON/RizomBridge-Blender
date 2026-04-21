"""Preference helpers for the RizomBridge addon."""

import bpy


def get_addon():
    name = __package__.split('.')[:3]
    name = '.'.join(name)
    return bpy.context.preferences.addons[name]


def get_preferences() -> "bpy.types.AddonPreferences":
    """
    Retrieve the addon preferences instance.

    Returns:
        bpy.types.AddonPreferences: The addon preferences object.
    """
    return get_addon().preferences
