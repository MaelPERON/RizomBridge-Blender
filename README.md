<img src="./wiki/rizombridge_logo.png" height="128px" align="right">


# RizomBridge-Blender

Blender addon to fasten the UV unwrapping and packing through RizomUV back to Blender.

## Authors

- [@MaelPERON](https://www.github.com/MaelPERON) (maintainer)
- Alexandre RENAUX, [@sky-ark](https://www.github.com/sky-ark) (original creator)
## Installation

Multiple options are available to download this addon :

1. Official Releases
> Under [Releases](https://github.com/MaelPERON/RizomBridge-Blender/releases), download the latest .zip file compatible with your Blender version.

2. Github download
> * Checkout the github branch suiting your needs (e.g. [dev](https://github.com/MaelPERON/RizomBridge-Blender/tree/dev) for beta testing)
>
> * Under code, click "Download ZIP"

Once the .zip is download, drag-and-drop it on a blender window and click "Ok".
*You can also install it [from the preferences](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#add-on-settings) under "Add-ons > **Install from disk...**"*
## Documentation

### Setup

1. Fullfill the rizomuv executable path (e.g. "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe")
> The addon use this path to call a new rizomuv instance.

2. Fullfill the addon export folder (e.g. "C:/tmp/rizombridge/").
> It stores the .fbx files used for working under rizom and importing the data back.

### Settings

* Auto-save before export (default: True)
If you fear the export might crash blender, it saves before exporting the selected objects.

* Forward and Up axis (default: -Z Y)
Orient the exported geometry. Will not influence the importing orientation (as Blender will automatically restore the normal one).

### Usage

When working on models you want to unwrap and pack the UVs, select them and click on "Export to RizomUV". It should use the active object as a reference and open a new RizomUV window.

Once the work is done, you can import all the new data using "Import from RizomUV".

*Note that if you deselected all the objects, you might want to reselect the active object so the addon can tell what are the objects to reimport.*
## Badges

[![Blender](https://img.shields.io/badge/Blender-4.2.1%2B-E87D0D?logo=blender&logoColor=white)](https://www.blender.org/)
[![License](https://img.shields.io/badge/License-GPL--3.0--or--later-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![GitHub issues](https://img.shields.io/github/issues/MaelPERON/RizomBridge-Blender)](https://github.com/MaelPERON/RizomBridge-Blender/issues)
[![Latest release](https://img.shields.io/github/v/release/MaelPERON/RizomBridge-Blender?display_name=tag)](https://github.com/MaelPERON/RizomBridge-Blender/releases)
