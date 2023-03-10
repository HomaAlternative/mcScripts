from gen_bs import createOrIgnore as createFile


#создает модель, с переопределенными текстурами
def genModelOwerrided(parent, textures, nms="minecraft:"):
    st = '{"parent":"'+parent+'","textures":{'
    marker = 0
    for texture in textures:
        if(marker!=0):
            st+=','
        st += '"'+str(marker)+'":"'+nms+texture+'"'
        marker+=1
    return st+'}}'


#тупо перебор
def addAll(txMap):
    all = []
    for i in txMap[0]:
        all.append([i])

    for i in range(1, len(txMap)):
        temp = []
        for line in all:
            for item in txMap[i]:
                temp.append(line+[item])
        all = temp
    return all
    

#создает набор всевозможных моделей по набору текстур
def genAllOwModels(parent, txMap, nms="minecraft:"):
    allJsons = []
    for texCombo in addAll(txMap):
        allJsons.append(genModelOwerrided(parent, texCombo, nms=nms))
    return allJsons


#создает json со всеми путями
def prepareFrame(routes:list, parent:str, shift:int):
    num = 1
    st = '{"parent":"'+parent+'","overrides":[\n'

    def genLine(model,  num):
        return '{"predicate":{"cmd":'+str(num+shift)+'},"model":"'+model+'"}'
        
    for route in routes:
        if num != 1:
            st+=',\n'
        st += genLine(route, num)
        num+=1
    return st+'\n]}'


#создает всевозможные модели для указанного набора текстур (наследуя указанную)
#после чего создает item и помещает в него ссылки на сгенерированные модели
#
#использование
#genAllCombo("test/model", "parent",[["a1","a2"],["b1","b2"]])
def genAllCombo(selfName, parent:str, txMap, wdir="", remove=False, shift=0):
    
    routes = []
    pPath = selfName.split("/")
    prefix = "/".join(pPath[:-1])

    suffix = pPath[-1]

    nms = "minecraft:"
    if(":" in pPath[0]):
        nms = pPath[0].split(":")
        suffix = nms[1]
        nms = nms[0]+":"

    if ":" in selfName:
        selfName = selfName.split(":")[1]

    models = genAllOwModels(parent, txMap, nms=nms)

    def createFile0(model):
        num = len(routes)
        name = prefix+"vars/"+suffix+"/v"+str(num)
        routes.append(nms+name)
        createFile(wdir+name+".json", model, remove=remove)

    for model in models:
        createFile0(model)

    
    createFile(wdir+"item/"+selfName+".json", prepareFrame(routes, parent, shift), remove=remove)
