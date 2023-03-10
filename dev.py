import te4lib
from te4lib import p, createFile


def getFileStr(st):
    return te4lib.getFileStr("src/"+st)


def getBlockStr(st, parent="minecraft:block/cube_all"):
    return getFileStr(st).replace("%PARENT%",parent)


def exportConstants():

    __fr_bl_state__      = getFileStr("0frame.json")
    __fr_item_model__    = getFileStr("0Iframe.json")
    __fr_si_item_model__ = getFileStr("1IFrame.json")
    __fr_block_model__   = getBlockStr("0Bframe.json")

    __fr_slab_frame__    = getFileStr("0SlabFrame.json")
    __fr_slab_model_up__ = getFileStr("0SlabUp.json")
    __fr_slab_model_dn__ = getFileStr("0SlabDn.json")

    __fr_stairs_state__      = getFileStr("stairs/0StairsFrame.json")
    __fr_stairs_model_main__ = getFileStr("stairs/0StairsMfrm.json")
    __fr_stairs_model_outh__ = getFileStr("stairs/0StairsOfrm.json")
    __fr_stairs_model_innr__ = getFileStr("stairs/0StairsINfrm.json")

    __fr_pane_item__                  = getFileStr("pane/0IPaneFrame.json")
    __fr_pane_frame__                 = getFileStr("pane/0PaneFrame.json")
    __fr_pane_model_pane_post__       = getBlockStr("pane/0MPaneBlock.json","block/pane_post")
    __fr_pane_model_pane_side__       = getBlockStr("pane/0MPaneBlock.json","block/pane_side")
    __fr_pane_model_pane_side_alt__   = getBlockStr("pane/0MPaneBlock.json","block/pane_side_alt")
    __fr_pane_model_pane_noside__     = getBlockStr("pane/0MPaneBlock.json","block/pane_noside")
    __fr_pane_model_pane_noside_alt__ = getBlockStr("pane/0MPaneBlock.json","block/pane_noside_alt")

    __fr_in_craft__   = getFileStr("crafts/in_frame.json")
    __fr_out_craft__  = getFileStr("crafts/out_frame.json")
    __fr_adv_recept__ = getFileStr("acv/AcvFrame.json")

    data = locals()

    toWrite = ""
    allWars = ""
    allWars2 = ""
    flag = False

    ignore = ["__fr_in_craft__", "__fr_out_craft__","__fr_adv_recept__"]

    for key in data:
        toWrite += (key + " = ''' "+data[key]+"'''\n")
        
        if key in ignore: continue

        if(flag):
            allWars += (", "+key)
            allWars2 += (', "'+key+'"')
        else:
            allWars += (key)
            allWars2 += ('"'+key+'"')
            flag = True

    createFile("constants.py", f'''
#импортируй это и используй
#
#from constants import {allWars}


def transformAll(func):
    gl = globals()
    for var in {allWars2}:
        gl[var] = func(gl[var])

{toWrite}
''')
    p("Completed.")


#Утилита для слияния шаблонов json из src в constants.py
#может быть полезно, если вдруг захочется собрать с помощью нуитки в 1 exe-шник
#чтобы не таскать за собой папку с шаблонами
if __name__=="__main__":
    exportConstants()