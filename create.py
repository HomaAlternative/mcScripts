import sys
import gen_bs

from te4lib import p, repAllMathes
from gen_bs import setNameSpace
from gen_bs import createBlockWith as block
from gen_bs import createItemOf as item

from shuffle_textues import genAllCombo
from cr_crafts import createCraft, withAdvUnlock


activeNms = None
curNms = "minecraft"


#устанавливает рабочее пространство
#и в случае необходимости минимизирует шаблон
#в режиме сессии это отключено, чтобы не было багов
#(по нормальному писать было лень так что так)
def setNms(nms, mini=True):
    global activeNms, curNms
    if(activeNms == None):
        setNameSpace(nms)
        curNms = nms
        activeNms = nms
        if(mini):
            def minimizeSize(jsonCode:str):
                jsonCode = jsonCode.strip()
                jsonCode = repAllMathes(jsonCode, [
                        ["\n", " "],
                        ["  ", " "],
                        [": ", ":"],
                        ["{ ", "{"],
                        [" }", "}"],
                        [", ", ","]
                    ]
                )
                return jsonCode

            from constants import transformAll
            transformAll(minimizeSize)


#патерн для генерации блоков
#T -> true, F -> false
#всего 3 аргумента (Block, Stairs, Slab)
#во время процесса создания шаблонов, будет сгенерировано только то, что указано
#по умолчанию TFF (только обычный блок)
class Patern():
    def __init__(self, data:str) -> None:
        def getV(i):
            if len(data)>i:
                return data[i].capitalize() == "T"
            else:
                return False

        self.genBlock  = getV(0)
        self.genStairs = getV(1)
        self.genSlabs  = getV(2)


#печатает помощь (думаю и сами поняли)
def printHelp():p(
'''args:
    -help : show this text
    -block: Create block
            block=block_id
    -item : Create item, lincked with block
            -item=item_id
            -texture=texture or -t (Default parent of block)
    -nms  : set namespace. Default "minecraft"
            or use -block=namespase:block_id
    -ptr  : patern (Block, Stairs, Slab).
            Default: TFF
    -sss  : Active session mode
    -ext  : Disable session
    -rm   : remove sellected block or item
    -mini : enable minimum json size
    -adv  : create craft advancements frame

    -combo: create multi-owerride model
            -item=main_model_path
            -parent=parent_model_path
            -shift=0 : shift CMD to value
            -textures=first,second+tx2_first,tx2_second
            
    -craft: create craft frame
            -craft=craft_name
            -d or -io: generate in-out frame
            -sh or -no-form: enable noform craft frame
            -adv: generate with craft advancements frame
''')


#создает всевозможные модели для указанного набора текстур (наследуя указанную)
#после чего создает item и помещает в него ссылки на сгенерированные модели
#
#-combo -item=test -parent=debuf -textures=va,vb,vc,vd+v_a,v_b,v_c,v_d
def combo(args:dict):
    
    global curNms
    if not ("item" in args and "parent" in args and "textures" in args):
        printHelp()
        return
    
    txMap = []
    for line in args["textures"].split("+"):
        txMap.append(line.split(","))
    remove = "rm" in args or "remove" in args

    parent = args["parent"]
    if ":" not in parent:
        parent = curNms+":"+parent

    item = args["item"]
    if ":" not in item:
        item = curNms+":"+item

    shift = 0
    if "shift" in args:
        shift = int(args["shift"])

    genAllCombo(item, parent, txMap, 
                gen_bs.__wdir__+"/models/", remove, shift)
    p("Combo created.")
    

def crafts(args:dict):
    global curNms
    name = args["craft"]
    remove = "rm" in args or "remove" in args
    double = "d" in args or "io" in args
    if not double and ("-sh" in args or "-no-form" in args):
        double = None

    genAdv = "adv" in args

    createCraft(gen_bs.__wdir__+"/", name, double, remove, nms=curNms, genAdv=genAdv)
    p("Craft template created.")


#генерирует шаблон ачивок
def advenchiments(args:dict):
    global curNms
    name = args["adv"]
    remove = "rm" in args or "remove" in args

    withAdvUnlock(gen_bs.__wdir__+"/", name=name, nms=curNms, remove=remove)
    p("Recepie unlock advancement template created.")


def prepareId(id, mini=True):
    if(":" in id):
        id = id.split(":")
        setNms(id[0])
        return id[1]
    else:
        if("nms" in args):
            setNms(args["nms"], mini)
        else:
            setNms("minecraft", mini)
        return id


#сам центральный скрипт
def main(args:dict , mini=True):
    if(args == {} or "help" in args):
        printHelp()
        return
    if("combo" in args):
        combo(args)
        return
    if("craft" in args):
        crafts(args)
        return
    if("adv" in args):
        advenchiments(args)
        return

    remove = "rm" in args or "remove" in args
    
    if("block" in args):
        patern = None
        if("ptr" in args):
            patern = Patern(args["prt"])
        else:
            patern = Patern("TFF")
        id = prepareId(args["block"], mini)
        if(remove):
            p("block removed")
        else:
            p("block created.")
        block(id, patern.genBlock, patern.genStairs, patern.genSlabs, remove=remove)
    elif "item" in args:
        id = prepareId(args["item"], mini)
        texture = None

        if "texture" in args: texture = args["texture"]
        elif "t" in args: texture = args["t"]

        if(remove):
            p("item removed.")
        else:
            p("item created.")
        item(id, remove=remove, texture=texture)
    else:
        printHelp()
    

debug = False
#запуск скриптов
if __name__ == "__main__":
    #преобразовывает аргументы
    #по синтаксису -arg=value
    def parse(args):
        fArgs = {}
        for a in args:
            if(a[0]!="-"):
                continue
            a = a[1:]
            if "=" in a:
                data = a.split("=")
                fArgs[data[0]] = data[1]
            else:
                fArgs[a] = True
        return fArgs
    args:dict = parse(sys.argv[1:])
    mini = not "normal-size" in args
    if("sss" in args) or debug:
        if("nms" in args):
            setNms(args["nms"], mini)
        else:
            setNms("minecraft", mini)
        
        p(f"Session create namespase = [{activeNms}], mini = {mini}")
        while True:
            args = parse(list(map(lambda a:a.strip(), input(">> ").split(" "))))
            if("ext" in args or "exit" in args):
                p("Session closed.")
                break
            else:
                main(args, mini)
    else:
        main(args, mini)