
#импортируй это и используй
#
#from constants import __fr_bl_state__, __fr_item_model__, __fr_si_item_model__, __fr_block_model__, __fr_slab_frame__, __fr_slab_model_up__, __fr_slab_model_dn__, __fr_stairs_state__, __fr_stairs_model_main__, __fr_stairs_model_outh__, __fr_stairs_model_innr__, __fr_pane_item__, __fr_pane_frame__, __fr_pane_model_pane_post__, __fr_pane_model_pane_side__, __fr_pane_model_pane_side_alt__, __fr_pane_model_pane_noside__, __fr_pane_model_pane_noside_alt__


def transformAll(func):
    gl = globals()
    for var in "__fr_bl_state__", "__fr_item_model__", "__fr_si_item_model__", "__fr_block_model__", "__fr_slab_frame__", "__fr_slab_model_up__", "__fr_slab_model_dn__", "__fr_stairs_state__", "__fr_stairs_model_main__", "__fr_stairs_model_outh__", "__fr_stairs_model_innr__", "__fr_pane_item__", "__fr_pane_frame__", "__fr_pane_model_pane_post__", "__fr_pane_model_pane_side__", "__fr_pane_model_pane_side_alt__", "__fr_pane_model_pane_noside__", "__fr_pane_model_pane_noside_alt__":
        gl[var] = func(gl[var])

__fr_bl_state__ = ''' {"variants": {"normal": { "model": "te4blocks:%BLOCK%" }}}'''
__fr_item_model__ = ''' {"parent": "te4blocks:block/%BLOCK%"}'''
__fr_si_item_model__ = ''' {"parent": "item/generated","textures": {"layer0":"items/%TEXTURE%"}}'''
__fr_block_model__ = ''' {"parent": "minecraft:block/cube_all","textures": {"all": "te4blocks:block/%BLOCK%"}}'''
__fr_slab_frame__ = ''' {"variants": {
"half=bottom": { "model": "te4blocks:%BLOCK%_slab_bottom" },
"half=top": { "model": "te4blocks:%BLOCK%_slab_top" }
}}'''
__fr_slab_model_up__ = ''' {"parent": "block/upper_slab","textures": {
"bottom": "te4blocks:block/%BLOCK%",
"top": "te4blocks:block/%BLOCK%",
"side": "te4blocks:block/%BLOCK%"
}}'''
__fr_slab_model_dn__ = ''' {"parent": "block/half_slab","textures": {
"bottom": "te4blocks:block/%BLOCK%",
"top": "te4blocks:block/%BLOCK%",
"side": "te4blocks:block/%BLOCK%"
}}'''
__fr_stairs_state__ = ''' {
    "variants": {
        "facing=east,half=bottom,shape=straight":  { "model": "te4blocks:%BLOCK%_stairs" },
        "facing=west,half=bottom,shape=straight":  { "model": "te4blocks:%BLOCK%_stairs", "y": 180, "uvlock": true },
        "facing=south,half=bottom,shape=straight": { "model": "te4blocks:%BLOCK%_stairs", "y": 90, "uvlock": true },
        "facing=north,half=bottom,shape=straight": { "model": "te4blocks:%BLOCK%_stairs", "y": 270, "uvlock": true },
        "facing=east,half=bottom,shape=outer_right":  { "model": "te4blocks:%BLOCK%_outer_stairs" },
        "facing=west,half=bottom,shape=outer_right":  { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 180, "uvlock": true },
        "facing=south,half=bottom,shape=outer_right": { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 90, "uvlock": true },
        "facing=north,half=bottom,shape=outer_right": { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 270, "uvlock": true },
        "facing=east,half=bottom,shape=outer_left":  { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 270, "uvlock": true },
        "facing=west,half=bottom,shape=outer_left":  { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 90, "uvlock": true },
        "facing=south,half=bottom,shape=outer_left": { "model": "te4blocks:%BLOCK%_outer_stairs" },
        "facing=north,half=bottom,shape=outer_left": { "model": "te4blocks:%BLOCK%_outer_stairs", "y": 180, "uvlock": true },
        "facing=east,half=bottom,shape=inner_right":  { "model": "te4blocks:%BLOCK%_inner_stairs" },
        "facing=west,half=bottom,shape=inner_right":  { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 180, "uvlock": true },
        "facing=south,half=bottom,shape=inner_right": { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 90, "uvlock": true },
        "facing=north,half=bottom,shape=inner_right": { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 270, "uvlock": true },
        "facing=east,half=bottom,shape=inner_left":  { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 270, "uvlock": true },
        "facing=west,half=bottom,shape=inner_left":  { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 90, "uvlock": true },
        "facing=south,half=bottom,shape=inner_left": { "model": "te4blocks:%BLOCK%_inner_stairs" },
        "facing=north,half=bottom,shape=inner_left": { "model": "te4blocks:%BLOCK%_inner_stairs", "y": 180, "uvlock": true },
        "facing=east,half=top,shape=straight":  { "model": "te4blocks:%BLOCK%_stairs", "x": 180, "uvlock": true },
        "facing=west,half=top,shape=straight":  { "model": "te4blocks:%BLOCK%_stairs", "x": 180, "y": 180, "uvlock": true },
        "facing=south,half=top,shape=straight": { "model": "te4blocks:%BLOCK%_stairs", "x": 180, "y": 90, "uvlock": true },
        "facing=north,half=top,shape=straight": { "model": "te4blocks:%BLOCK%_stairs", "x": 180, "y": 270, "uvlock": true },
        "facing=east,half=top,shape=outer_right":  { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 90, "uvlock": true },
        "facing=west,half=top,shape=outer_right":  { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 270, "uvlock": true },
        "facing=south,half=top,shape=outer_right": { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 180, "uvlock": true },
        "facing=north,half=top,shape=outer_right": { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "uvlock": true },
        "facing=east,half=top,shape=outer_left":  { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "uvlock": true },
        "facing=west,half=top,shape=outer_left":  { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 180, "uvlock": true },
        "facing=south,half=top,shape=outer_left": { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 90, "uvlock": true },
        "facing=north,half=top,shape=outer_left": { "model": "te4blocks:%BLOCK%_outer_stairs", "x": 180, "y": 270, "uvlock": true },
        "facing=east,half=top,shape=inner_right":  { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 90, "uvlock": true },
        "facing=west,half=top,shape=inner_right":  { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 270, "uvlock": true },
        "facing=south,half=top,shape=inner_right": { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 180, "uvlock": true },
        "facing=north,half=top,shape=inner_right": { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "uvlock": true },
        "facing=east,half=top,shape=inner_left":  { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "uvlock": true },
        "facing=west,half=top,shape=inner_left":  { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 180, "uvlock": true },
        "facing=south,half=top,shape=inner_left": { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 90, "uvlock": true },
        "facing=north,half=top,shape=inner_left": { "model": "te4blocks:%BLOCK%_inner_stairs", "x": 180, "y": 270, "uvlock": true }
    }
}'''
__fr_stairs_model_main__ = ''' {"parent": "block/stairs","textures": {
"bottom": "te4blocks:block/%BLOCK%",
"top": "te4blocks:block/%BLOCK%",
"side": "te4blocks:block/%BLOCK%"
}}'''
__fr_stairs_model_outh__ = ''' {"parent": "block/outer_stairs","textures": {
"bottom": "te4blocks:block/%BLOCK%",
"top": "te4blocks:block/%BLOCK%",
"side": "te4blocks:block/%BLOCK%"
}}'''
__fr_stairs_model_innr__ = ''' {"parent": "block/inner_stairs","textures": {
"bottom": "te4blocks:block/%BLOCK%",
"top": "te4blocks:block/%BLOCK%",
"side": "te4blocks:block/%BLOCK%"
}}'''
__fr_pane_item__ = ''' {
    "parent": "item/generated",
    "textures": {
        "layer0": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_pane_frame__ = ''' {
    "multipart": [
        {   "apply": { "model": "te4blocks:%BLOCK%_pane_post" }},
        
        {   "when": { "north": true },
            "apply": { "model": "te4blocks:%BLOCK%_pane_side" }
        },
        {   "when": { "east": true },
            "apply": { "model": "te4blocks:%BLOCK%_pane_side", "y": 90 }
        },
        {   "when": { "south": true },
            "apply": { "model": "te4blocks:%BLOCK%_pane_side_alt" }
        },
        {   "when": { "west": true },
            "apply": { "model": "te4blocks:%BLOCK%_pane_side_alt", "y": 90 }
        },
        {   "when": { "north": false },
            "apply": { "model": "te4blocks:%BLOCK%_pane_noside" }
        },
        {   "when": { "east": false },
            "apply": { "model": "te4blocks:%BLOCK%_pane_noside_alt" }
        },
        {   "when": { "south": false },
            "apply": { "model": "te4blocks:%BLOCK%_pane_noside_alt", "y": 90 }
        },
        {   "when": { "west": false },
            "apply": { "model": "te4blocks:%BLOCK%_pane_noside", "y": 270 }
        }
    ]
}'''
__fr_pane_model_pane_post__ = ''' {
    "parent": "block/pane_post",
    "textures": {
        "edge": "te4blocks:block/%BLOCK%",
        "pane": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_pane_model_pane_side__ = ''' {
    "parent": "block/pane_side",
    "textures": {
        "edge": "te4blocks:block/%BLOCK%",
        "pane": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_pane_model_pane_side_alt__ = ''' {
    "parent": "block/pane_side_alt",
    "textures": {
        "edge": "te4blocks:block/%BLOCK%",
        "pane": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_pane_model_pane_noside__ = ''' {
    "parent": "block/pane_noside",
    "textures": {
        "edge": "te4blocks:block/%BLOCK%",
        "pane": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_pane_model_pane_noside_alt__ = ''' {
    "parent": "block/pane_noside_alt",
    "textures": {
        "edge": "te4blocks:block/%BLOCK%",
        "pane": "te4blocks:block/%BLOCK%"
    }
}'''
__fr_in_craft__ = ''' {
    "type": "minecraft:crafting_shaped",
    "pattern": [
      "LLL",
      "LLL",
      "LLL"
    ],
    "key": {
      "L": {"item": "te4_spships:copper_ingot"}
    },
    "result": {
      "item": "te4_spships:copper_block",
      "count": 1
    }
}'''
__fr_out_craft__ = ''' {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
      {"item": "te4_spships:copper_block"}
    ],
    "result": {
      "item": "te4_spships:copper_ingot",
      "count": 9
    }
}'''
__fr_adv_recept__ = ''' {"parent": "minecraft:recipes/root",
"requirements": [["has_the_recipe","has_item"]],
"rewards": {"recipes": [
    "%RECEPT_FULL_NAME%"
]},
"criteria": {
    "has_the_recipe": {"trigger": "minecraft:recipe_unlocked",
        "conditions": {"recipe": "%RECEPT_NAME%"}
    },
    "has_item": {"trigger": "minecraft:inventory_changed",
        "conditions": {"items": [{
                "item": "%RECEPT_FULL_NAME%"
        }]}
    }
}}'''

