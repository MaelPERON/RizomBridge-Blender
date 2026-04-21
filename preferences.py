"""Addon preferences for RizomBridge."""

import bpy


class RB_Preferences(bpy.types.AddonPreferences):
    """RizomBridge addon preferences."""

    bl_idname = __package__

    rizom_path: bpy.props.StringProperty(  # type: ignore
        name="RizomUV Path",
        subtype="FILE_PATH",
        description="Path to the RizomUV executable",
        default="C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe"
    )

    export_folder: bpy.props.StringProperty(  # type: ignore
        name="Export Folder",
        subtype="DIR_PATH",
        description="Path to the export folder for RizomUV FBX files"
    )

    save_before_export: bpy.props.BoolProperty(  # type: ignore
        name="Auto-Save Before Export",
        description="Save the blend file before exporting to RizomUV",
        default=True
    )

    forward_axis: bpy.props.EnumProperty(  # type: ignore
        name="Forward Axis",
        description="Forward axis for the FBX export",
        items=[
            ("X", "X", "X"),
            ("Y", "Y", "Y"),
            ("Z", "Z", "Z"),
            ("-X", "-X", "-X"),
            ("-Y", "-Y", "-Y"),
            ("-Z", "-Z", "-Z"),
        ],
        default="-Z"
    )

    up_axis: bpy.props.EnumProperty(  # type: ignore
        name="Up Axis",
        description="Up axis for the FBX export",
        items=[
            ("X", "X", "X"),
            ("Y", "Y", "Y"),
            ("Z", "Z", "Z"),
            ("-X", "-X", "-X"),
            ("-Y", "-Y", "-Y"),
            ("-Z", "-Z", "-Z"),
        ],
        default="Y"
    )

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the preferences panel."""
        layout = self.layout
        layout.prop(self, "rizom_path")
        layout.prop(self, "export_folder")
        layout.prop(self, "save_before_export")
        layout.prop(self, "forward_axis")
        layout.prop(self, "up_axis")
