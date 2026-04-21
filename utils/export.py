"""Export utilities for RizomUV FBX export."""

import bpy
from pathlib import Path
from typing import Optional

from .preferences import get_preferences


def get_ruv_export_path() -> Optional[Path]:
    """
    Get the RizomUV export folder path, creating it if necessary.

    Returns:
        Optional[Path]: The absolute export path, or None if not configured.
    """
    prefs = get_preferences()
    export_folder = prefs.export_folder

    if not export_folder:
        return None

    _export_path = Path(bpy.path.abspath(export_folder))
    _export_path.mkdir(parents=True, exist_ok=True)

    return _export_path


def get_ruv_filename(report_func=None) -> Optional[Path]:
    """
    Generate the RizomUV export filename for the active object.

    Args:
        report_func: Optional function to call for error
            reporting (e.g., self.report).

    Returns:
        Optional[Path]: The full export filepath, or None on error.
    """
    if not bpy.context.active_object:
        if report_func:
            report_func({'ERROR'}, "No active object selected.")
        return None

    _object_name = bpy.context.active_object.name
    _export_path = get_ruv_export_path()

    if not _export_path:
        if report_func:
            report_func({'ERROR'}, "Export folder is not set.")
        return None

    return _export_path / f"{_object_name}_ruv.fbx"


def ensure_file_saved(report_func=None) -> bool:
    """
    Ensure the blend file is saved before export.

    Args:
        report_func: Optional function to call for error
            reporting (e.g., self.report).

    Returns:
        bool: True if saved or auto-save disabled, False on error.
    """
    prefs = get_preferences()

    if not prefs.save_before_export:
        return True

    if not bpy.data.is_saved:
        if report_func:
            report_func({'ERROR'}, "Please save the file before exporting.")
        return False

    try:
        bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
        return True
    except Exception as e:
        if report_func:
            report_func({'ERROR'}, f"Failed to save the file: {e}")
        return False


def export_to_fbx(filepath: Path) -> bool:
    """
    Export the selected object to FBX with RizomUV settings.

    Args:
        filepath (Path): The destination FBX file path.

    Returns:
        bool: True if export succeeded, False otherwise.
    """
    prefs = get_preferences()

    try:
        bpy.ops.export_scene.fbx(
            filepath=str(filepath),
            use_selection=True,
            axis_forward=prefs.forward_axis,
            axis_up=prefs.up_axis,
            filter_glob="*.fbx",
            global_scale=1.0,
            apply_unit_scale=True,
            bake_space_transform=False,
            object_types={'MESH'},
            use_mesh_modifiers=False,
            mesh_smooth_type='OFF',
            use_mesh_edges=False,
            use_tspace=False,
            use_custom_props=False,
            add_leaf_bones=False,
            primary_bone_axis='Y',
            secondary_bone_axis='X',
            use_armature_deform_only=False,
            bake_anim=True,
            bake_anim_use_all_bones=True,
            bake_anim_use_nla_strips=True,
            bake_anim_use_all_actions=True,
            bake_anim_force_startend_keying=True,
            bake_anim_step=1.0,
            bake_anim_simplify_factor=1.0,
            path_mode='AUTO',
            embed_textures=False,
            batch_mode='OFF',
            use_batch_own_dir=True,
            use_metadata=True
        )
        return True
    except Exception as e:
        print(f"FBX export failed: {e}")
        return False
