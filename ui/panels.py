"""UI panels for RizomBridge addon."""

import bpy
from ..utils.preferences import get_preferences


class RB_VIEW3D_PT_RizomBridge_Main(bpy.types.Panel):
    """Main RizomBridge tool panel in the 3D viewport."""

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "RizomBridge"
    bl_category = "RizomBridge"
    bl_order = 0

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the main tool panel."""
        layout = self.layout
        prefs = get_preferences()
        has_rizom_path = getattr(prefs, "rizom_path", "") != ""
        has_folder_path = getattr(prefs, "export_folder", "") != ""

        # Display configuration options
        layout.label(text="Configuration")
        #   Rizom Path
        row = layout.row()
        row.alert = not has_rizom_path
        row.prop(prefs, "rizom_path")
        #   Export folder
        row = layout.row()
        row.alert = not has_folder_path
        row.prop(prefs, "export_folder")
        # Save before export
        layout.prop(prefs, "save_before_export")

        # Display export settings
        layout.label(text="Export Settings")
        layout.prop(prefs, "forward_axis")
        layout.prop(prefs, "up_axis")

        # Display action buttons
        layout.separator()
        layout.label(text="Actions")
        row = layout.row()
        row.scale_y = 2
        #   Export
        subrow = row.row()
        subrow.enabled = has_rizom_path and has_folder_path
        subrow.operator("object.rizomuv_export", text="Export to RizomUV",
                        icon="EXPORT")
        #   Import
        subrow = row.row()
        subrow.enabled = has_folder_path
        subrow.operator("object.rizomuv_import", text="Import from RizomUV",
                        icon="IMPORT")

        # Link to project info
        layout.separator()
        layout.operator(
            "wm.url_open",
            text="Project Info"
        ).url = "https://github.com/MaelPERON/RizomBridge-Blender"
