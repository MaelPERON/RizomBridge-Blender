"""Operators for RizomUV import/export."""

import bpy
from subprocess import Popen
from typing import Set

from ..utils.export import (
    get_ruv_filename,
    ensure_file_saved,
    export_to_fbx
)
from ..utils.preferences import get_preferences


class RB_RizomUV_Export(bpy.types.Operator):
    """Export the selected object to RizomUV."""

    bl_idname = "object.rizomuv_export"
    bl_label = "Export to RizomUV"
    bl_description = "Export the selected object to RizomUV"
    bl_options: Set[str] = {"REGISTER"}

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        """Check if export is possible."""
        return context.active_object is not None

    def execute(self, context: bpy.types.Context) -> Set[str]:
        """Execute the export operation."""
        if not ensure_file_saved(self.report):
            return {'CANCELLED'}

        export_file = get_ruv_filename(self.report)
        if not export_file:
            return {'CANCELLED'}

        if not export_to_fbx(export_file):
            self.report({'ERROR'}, "Failed to export FBX file.")
            return {'CANCELLED'}

        prefs = get_preferences()
        rizom_path = prefs.rizom_path

        if not rizom_path:
            self.report({'ERROR'}, "RizomUV path is not configured.")
            return {'CANCELLED'}

        try:
            Popen([rizom_path, str(export_file)])
        except Exception as e:
            self.report({'ERROR'}, f"Failed to open RizomUV: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}


class RB_RizomUV_Import(bpy.types.Operator):
    """Import UV maps from RizomUV."""

    bl_idname = "object.rizomuv_import"
    bl_label = "Import from RizomUV"
    bl_description = "Import UV maps from RizomUV"
    bl_options: Set[str] = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context: bpy.types.Context) -> bool:
        """Check if import is possible."""
        object = context.active_object
        return (
            object is not None and object.type == 'MESH'
        )

    def execute(self, context: bpy.types.Context) -> Set[str]:
        """Execute the import operation."""
        obj_selected = context.active_object

        if not obj_selected:
            self.report({'ERROR'}, "No active object selected.")
            return {'CANCELLED'}

        import_file = get_ruv_filename(self.report)
        if not import_file:
            return {'CANCELLED'}

        if not import_file.exists():
            self.report({'ERROR'}, f"Import file not found: {import_file}")
            return {'CANCELLED'}

        try:
            objects_selected = bpy.context.selected_objects
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
            bpy.ops.import_scene.fbx(filepath=str(import_file))

            objects_imported = bpy.context.selected_objects

            for obj_in in objects_imported:
                obj_out = context.scene.objects.get(
                    obj_in.name.replace(SUFFIX, "")
                )
                if not obj_out:
                    self.report({"WARNING"}, f"Object {obj_in.name} not found in the scene.")  # noqa: E501
                    continue

                # Deselect all
                bpy.ops.object.select_all(action='DESELECT')
                # Select both objects
                obj_in.select_set(True)
                obj_out.select_set(True)
                # Set obj_in as active
                bpy.context.view_layer.objects.active = obj_in

                # Join UVs
                bpy.ops.object.join_uvs()

                # Deselect obj_in, select only obj_out for deletion
                obj_out.select_set(False)
                bpy.context.view_layer.objects.active = obj_out
                bpy.ops.object.delete()

            bpy.ops.object.select_all(action='DESELECT')
            for obj in objects_selected:
                obj.select_set(True)

            bpy.ops.object.mode_set(mode='EDIT', toggle=False)
            bpy.ops.uv.seams_from_islands(mark_seams=True, mark_sharp=False)
            bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {e}")
            return {'CANCELLED'}
