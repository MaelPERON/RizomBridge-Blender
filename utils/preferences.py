"""Preference helpers for the RizomBridge addon."""

import bpy


def get_addon():
    return bpy.context.preferences.addons[__package__.split('.')[0]]


def get_preferences() -> "bpy.types.AddonPreferences":
    """
    Retrieve the addon preferences instance.

    Returns:
        bpy.types.AddonPreferences: The addon preferences object.
    """
    return get_addon().preferences
