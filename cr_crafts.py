import constants as cs
from gen_bs import createOrIgnore as createFile


#создает шаблон крафта
def createCraft(path:str, name:str, double, remove=False, nms="minecaft", genAdv=False):
    if double==True:
        createFile(path+"recipes/i_"+name+".json", cs.__fr_in_craft__, remove=remove)
        createFile(path+"recipes/o_"+name+".json", cs.__fr_out_craft__, remove=remove)
    elif double==False:
        createFile(path+"recipes/"+name+".json", cs.__fr_in_craft__, remove=remove)
    elif double==None:
        createFile(path+"recipes/"+name+".json", cs.__fr_out_craft__, remove=remove)

    if(genAdv): withAdvUnlock(path=path, name=name, nms=nms, remove=remove)


#добавляет шаблон ачивки
def withAdvUnlock(path:str, name:str, nms:str="minecraft", remove=False):
    fullRcpName = nms+":"+name
    result = cs.__fr_adv_recept__.replace(
        "%RECEPT_FULL_NAME%", fullRcpName).replace("%RECEPT_NAME%",name
    )
    createFile(path+"advancements/recipes/"+name+".json", result, remove=remove)