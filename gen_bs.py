from te4lib import createFile, p, __mainPath__

import shutil
import os.path
import constants as cs


__wdir__ = __mainPath__+"assets/te4blocks"

def setNameSpace(nmsps:str):
    setWorkDir("assets/"+nmsps)
    def edit(st:str):
        return st.replace("te4blocks:", nmsps+":")
    cs.transformAll(edit)
    

def setWorkDir(dir:str):
    global __wdir__
    __wdir__ = dir


def formateBlock(b:str, name): return b.replace("%BLOCK%", name)


#очищает все сгенерированное
def clearAll():
    shutil.rmtree(__wdir__+"/blockstates")
    shutil.rmtree(__wdir__+"/models")


#создает файл если его не существует и заполняет, иначе игнорируется
#в режиме удаления просто удаляет файл, если существует
#
#ты уже мог заметить, что аргумент remove протаскивается через много функций
#прежде чем дойдет до сюда и выполнит свою работу
#может быть несколько неоптимально по скорости, но мне пофиг
#тк это позволяет быстро расширять функцианал
def createOrIgnore(path, data, ignore=True, remove=False):
    if(remove):
        if(os.path.exists(path)):
            os.remove(path)
    else:
        if(ignore and os.path.exists(path)):
            return
        createFile(path, data)


#главная функция создания блока
def createBlockWith(name, block=True, stairs=False, slabs=False, ignore=True, remove=False):
    if(block):
        #генерация обычногго блока
        formated = cs.__fr_bl_state__.replace("%BLOCK%", name)
        formated2 = cs.__fr_block_model__.replace("%BLOCK%", name)
        createOrIgnore(__wdir__+"/blockstates/"+name+".json", formated, ignore, remove)
        createOrIgnore(__wdir__+"/models/block/"+name+".json", formated2, ignore, remove)
        createItemOf(name, remove)

    if(stairs):
        createStairsFor(name, remove=remove)
    if(slabs):
        createSlabsFor(name, remove=remove)
        

#создает модель предмета для блока
#если есть текстура, то создает простой предмет
#если в аргументе текстуры true - берет текстуру по имени файла
def createItemOf(name, remove=False, texture=None):
    formated3 = None
    if texture==None:
        formated3 = cs.__fr_item_model__.replace("%BLOCK%", name)
    elif texture==True:
        formated3 = cs.__fr_si_item_model__.replace("%TEXTURE%", name)
    else:
        formated3 = cs.__fr_si_item_model__.replace("%TEXTURE%", texture)

    createOrIgnore(__wdir__+"/models/item/"+name+".json", formated3, False, remove=remove)


#генерация ступенек
def createStairsFor(name, suffix="_stairs", suffix_outh="_outer_stairs", suffix_inn="_inner_stairs", remove=False):
    formated = cs.__fr_stairs_state__.replace("%BLOCK%", name)
    formated2 = cs.__fr_stairs_model_main__.replace("%BLOCK%", name)
    formated3 = cs.__fr_stairs_model_outh__.replace("%BLOCK%", name)
    formated4 = cs.__fr_stairs_model_innr__.replace("%BLOCK%", name)
    createOrIgnore(__wdir__+"/blockstates/"+name+suffix+".json", formated, remove=remove)
    createOrIgnore(__wdir__+"/models/block/"+name+suffix+".json", formated2, remove=remove)
    createOrIgnore(__wdir__+"/models/block/"+name+suffix_outh+".json", formated3, remove=remove)
    createOrIgnore(__wdir__+"/models/block/"+name+suffix_inn+".json", formated4, remove=remove)
    createItemOf(name+suffix)


#генерация плит
def createSlabsFor(name, suffix="_slab", suffix_up="_slab_top", suffix_dn="_slab_bottom", texture="", remove=False):
    cr = createOrIgnore; fb = formateBlock
    if texture == "" or texture == None:
        texture = name
    else:
        def func(b, name):
            return formateBlock(b.replace("te4blocks:block","minecraft:blocks"), name)
        fb = func

    cr(__wdir__+"/blockstates/"+name+suffix+".json", formateBlock(cs.__fr_slab_frame__, name), remove=remove)

    cr(__wdir__+"/models/block/"+name+suffix_up+".json", fb(cs.__fr_slab_model_up__, texture), remove=remove)
    cr(__wdir__+"/models/block/"+name+suffix_dn+".json", fb(cs.__fr_slab_model_dn__, texture), remove=remove)
    cr(__wdir__+"/models/item/"+name+suffix+".json", formateBlock(cs.__fr_item_model__, name+suffix_dn), False, remove=remove)


#генерация стекло-подобных ,,сущностей,,
def createPaneFor(name, suffix="_pane"):
    cr = createOrIgnore; fb = formateBlock

    cr(__wdir__+"/blockstates/"+name+suffix+".json", fb(cs.__fr_pane_frame__, name))

    cr(__wdir__+"/models/block/"+name+suffix+"_post.json", fb(cs.__fr_pane_model_pane_post__, name))
    cr(__wdir__+"/models/block/"+name+suffix+"_side.json", fb(cs.__fr_pane_model_pane_side__, name))
    cr(__wdir__+"/models/block/"+name+suffix+"_side_alt.json", fb(cs.__fr_pane_model_pane_side_alt__, name))
    cr(__wdir__+"/models/block/"+name+suffix+"_noside.json", fb(cs.__fr_pane_model_pane_noside__, name))
    cr(__wdir__+"/models/block/"+name+suffix+"_noside_alt.json", fb(cs.__fr_pane_model_pane_noside_alt__, name))

    cr(__wdir__+"/models/item/"+name+suffix+".json", fb(cs.__fr_pane_item__, name), False)


'''
Устарело
Раньше использовалось это для генерации конкретного массива блоков

def main():
    def mod_vanilla():
        createSlabsFor("granite", texture="stone_granite")


    def metall():
        for i in range(0, 13):
            createBlockWith("metall_"+str(i), True, True, True)
        createPaneFor("metall_0")
        createPaneFor("metall_1")
        createPaneFor("metall_12")


    def beton():
        for i in range(0, 4):
            createBlockWith("beton_"+str(i), True, True, True)


    def lab():
        for i in range(0, 2):
            createBlockWith("lab_block_"+str(i), True, True, True)


    def construct():
        for i in range(0, 1):
            createBlockWith("construct_"+str(i), True, True, True)
            createPaneFor("construct_"+str(i))


    metall()
    beton()
    lab()
    construct()
    mod_vanilla()
    p("Completed.")


if __name__=="__main__":
    main()
'''