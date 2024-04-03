"""
Define schemas for posting/putting data to the database
Define Object structure for JSON data in request body
"""
from pydantic import BaseModel
from typing import Optional


class Add_Episode(BaseModel):
    """ Fields that must/can be included in a POST request """
    title: str
    date: str
    black_gesso: Optional[bool] = 0
    bright_red: Optional[bool] = 0
    burnt_umber: Optional[bool] = 0
    cadmium_yellow: Optional[bool] = 0
    dark_sienna: Optional[bool] = 0
    indian_red: Optional[bool] = 0
    indian_yellow: Optional[bool] = 0
    liquid_black: Optional[bool] = 0
    liquid_clear: Optional[bool] = 0
    midnight_black: Optional[bool] = 0
    phthalo_blue: Optional[bool] = 0
    phthalo_green: Optional[bool] = 0
    prussian_blue: Optional[bool] = 0
    sap_green: Optional[bool] = 0
    titanium_white: Optional[bool] = 0
    van_dyke_brown: Optional[bool] = 0
    yellow_ochre: Optional[bool] = 0
    alizarin_crimson: Optional[bool] = 0
    aurora_borealis: Optional[bool] = 0
    barn: Optional[bool] = 0
    beach: Optional[bool] = 0
    boat: Optional[bool] = 0
    bridge: Optional[bool] = 0
    building: Optional[bool] = 0
    bushes: Optional[bool] = 0
    cabin: Optional[bool] = 0
    cactus: Optional[bool] = 0
    cirrus: Optional[bool] = 0
    cliff: Optional[bool] = 0
    clouds: Optional[bool] = 0
    conifer: Optional[bool] = 0
    cumulus: Optional[bool] = 0
    deciduous: Optional[bool] = 0
    dock: Optional[bool] = 0
    farm: Optional[bool] = 0
    fence: Optional[bool] = 0
    fire: Optional[bool] = 0
    flowers: Optional[bool] = 0
    fog: Optional[bool] = 0
    grass: Optional[bool] = 0
    hills: Optional[bool] = 0
    lake: Optional[bool] = 0
    lighthouse: Optional[bool] = 0
    mill: Optional[bool] = 0
    moon: Optional[bool] = 0
    mountain: Optional[bool] = 0
    mountains: Optional[bool] = 0
    night: Optional[bool] = 0
    ocean: Optional[bool] = 0
    palm_trees: Optional[bool] = 0
    path: Optional[bool] = 0
    person: Optional[bool] = 0
    portrait: Optional[bool] = 0
    river: Optional[bool] = 0
    rocks: Optional[bool] = 0
    snow: Optional[bool] = 0
    snowy_mountain: Optional[bool] = 0
    structure: Optional[bool] = 0
    sun: Optional[bool] = 0
    tree: Optional[bool] = 0
    trees: Optional[bool] = 0
    waterfall: Optional[bool] = 0
    waves: Optional[bool] = 0
    windmill: Optional[bool] = 0
    winter: Optional[bool] = 0

    class Config:
        orm_mode = True


class Update_Episode(BaseModel):
    """ Fields that can be updated in a PUT request """
    title: Optional[str] = None
    date: Optional[str] = None
    black_gesso: Optional[bool] = 0
    bright_red: Optional[bool] = 0
    burnt_umber: Optional[bool] = 0
    cadmium_yellow: Optional[bool] = 0
    dark_sienna: Optional[bool] = 0
    indian_red: Optional[bool] = 0
    indian_yellow: Optional[bool] = 0
    liquid_black: Optional[bool] = 0
    liquid_clear: Optional[bool] = 0
    midnight_black: Optional[bool] = 0
    phthalo_blue: Optional[bool] = 0
    phthalo_green: Optional[bool] = 0
    prussian_blue: Optional[bool] = 0
    sap_green: Optional[bool] = 0
    titanium_white: Optional[bool] = 0
    van_dyke_brown: Optional[bool] = 0
    yellow_ochre: Optional[bool] = 0
    alizarin_crimson: Optional[bool] = 0
    aurora_borealis: Optional[bool] = 0
    barn: Optional[bool] = 0
    beach: Optional[bool] = 0
    boat: Optional[bool] = 0
    bridge: Optional[bool] = 0
    building: Optional[bool] = 0
    bushes: Optional[bool] = 0
    cabin: Optional[bool] = 0
    cactus: Optional[bool] = 0
    cirrus: Optional[bool] = 0
    cliff: Optional[bool] = 0
    clouds: Optional[bool] = 0
    conifer: Optional[bool] = 0
    cumulus: Optional[bool] = 0
    deciduous: Optional[bool] = 0
    dock: Optional[bool] = 0
    farm: Optional[bool] = 0
    fence: Optional[bool] = 0
    fire: Optional[bool] = 0
    flowers: Optional[bool] = 0
    fog: Optional[bool] = 0
    grass: Optional[bool] = 0
    hills: Optional[bool] = 0
    lake: Optional[bool] = 0
    lighthouse: Optional[bool] = 0
    mill: Optional[bool] = 0
    moon: Optional[bool] = 0
    mountain: Optional[bool] = 0
    mountains: Optional[bool] = 0
    night: Optional[bool] = 0
    ocean: Optional[bool] = 0
    palm_trees: Optional[bool] = 0
    path: Optional[bool] = 0
    person: Optional[bool] = 0
    portrait: Optional[bool] = 0
    river: Optional[bool] = 0
    rocks: Optional[bool] = 0
    snow: Optional[bool] = 0
    snowy_mountain: Optional[bool] = 0
    structure: Optional[bool] = 0
    sun: Optional[bool] = 0
    tree: Optional[bool] = 0
    trees: Optional[bool] = 0
    waterfall: Optional[bool] = 0
    waves: Optional[bool] = 0
    windmill: Optional[bool] = 0
    winter: Optional[bool] = 0

    class Config:
        orm_mode = True
