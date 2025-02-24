"""
    This example shows how to use visualize a heatmap in 2D
"""

from brainrender import settings

import brainglobe_heatmap as bgh

settings.SHOW_AXES = True
settings.SHADER_STYLE = "cartoon"

values = dict(  # scalar values for each region
    TH=1,
    RSP=0.2,
    AI=0.4,
    SS=-3,
    MO=2.6,
    PVZ=-4,
    LZ=-3,
    VIS=2,
    AUD=0.3,
    RHP=-0.2,
    STR=0.5,
    CB=0.5,
    FRP=-1.7,
    HIP=3,
    PA=-4,
)
 
position = 3000
orientation = "sagittal"
# orientation = "frontal"
# orientation = "horizontal"

bgh.plan(
    values,
    atlas_name="allen_mouse_25um",
    position=position, 
    orientation=orientation,
    thickness=1000, # thickness of the slices used for rendering (in microns)
    arrow_scale=750,
    vmin=-5,
    vmax=3,
).show()
 
bgh.Heatmap(
    values,
    atlas_name="allen_mouse_25um",
    position=position, 
    orientation=orientation,
    thickness=1000, # thickness of the slices used for rendering (in microns)
    vmin=-5,
    vmax=3,
    # format="2D",
).show()

bgh.Heatmap(
    values,
    atlas_name="allen_mouse_25um",
    position=position, 
    orientation=orientation,
    thickness=1000, # thickness of the slices used for rendering (in microns)
    vmin=-5,
    vmax=3,
    format="2D",
).show()