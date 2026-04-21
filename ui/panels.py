"""UI panels for RizomBridge addon."""

import bpy


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
        addon_name = __package__.split('.')[0]
        prefs = context.preferences.addons[addon_name].preferences

        # Display configuration options
        layout.label(text="Configuration")
        layout.prop(prefs, "rizom_path")
        layout.prop(prefs, "export_folder")
        layout.prop(prefs, "save_before_export")

        # Display export settings
        layout.label(text="Export Settings")
        layout.prop(prefs, "forward_axis")
        layout.prop(prefs, "up_axis")

        # Display action buttons
        layout.separator()
        layout.label(text="Actions")
        layout.operator("object.rizomuv_export", text="Export to RizomUV")
        layout.operator("object.rizomuv_import", text="Import from RizomUV")

        # Link to project info
        layout.separator()
        layout.operator(
            "wm.url_open",
            text="Project Info"
        ).url = "https://github.com/MaelPERON/RizomBridge-Blender"
