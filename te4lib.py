#Урезанная версия моей либы, оставил только самое важное 
#Набор скриптов для работы с файлами и логированием
#Не буду это комментировать, там итак все понятно


import os, time, traceback

__mainPath__      = (__file__.replace("\\", "/")[0:__file__.rfind("/")+1])
__logField__ = ""
__basicPrinter__ = print
__basicInputer__ = input
__defFormat__ = " > {value}"
__canAdd__ = False


def setFormat(newFormat):
    global __defFormat__
    __defFormat__ = newFormat


def p(o):print(o)


def i(o):return input(o)
    

def print(o, __format__=__defFormat__):
    global __logField__
    __basicPrinter__(__format__.format(value=o))
    toPrint = "{0}\n".format(o)
    __logField__ = __logField__ +toPrint
    return toPrint


def input(o):
    global __logField__
    toPrint = "{0}\n".format(o)
    __logField__ = __logField__ +toPrint
    returnValue = __basicInputer__(toPrint)
    return returnValue


def currentTime():
    return round(time.time() * 1000)


def testTime(func, logf=True, msg="Time spent: "):
    tTime1 = currentTime()
    result = func()
    if(logf):
        time = currentTime()-tTime1
        ms =  time%1000
        sec = (time%60000)//1000
        min = (time//60000000)
        if(min<0):
            p(msg+str(sec)+"sec, "+str(ms)+"ms")
        else:
            p(msg+str(min)+"min, "+str(sec)+"sec, "+str(ms)+"ms")
        return result
    else: return currentTime()-tTime1


def editPath(path):
    global __mainPath__
    __mainPath__ = path.replace("\\", "/")


def logError():
    format = "------------------------------------------------------------------------------------"
    ermsg = "| "+traceback.format_exc().replace("\n", "\n| ")
    print(format+"\n"+ermsg+"\n"+format)
    

def saveLog(fileName="log.txt"):
    global __canAdd__, __logField__
    if len(__logField__)==0:
        return
    if __canAdd__:
        with open(fileName, "a") as file:
            file.write(__logField__)
            file.close()
    else:
        createFile(__mainPath__+fileName, __logField__)
    __logField__ = ""


__codecs__ = ["cp1252", "cp437", "utf-16be", "utf-16", "ascii", "utf-8"]


def replaceAll(string:str, old, new=""):
    while old in string:
        string = string.replace(old, new)
    return string


def removeComments(data, __sr1__="//", __sr2__="\n", __replacer__=lambda x: ""):
    index = 0
    index = data.find(__sr1__, index)
    while(index!=-1):
        index2 = data.find(__sr2__, index)
        if(index2==-1):
            break
        insert = __replacer__(data[index+len(__sr1__):index2])
        result = data[0:index] + insert + data[index2+len(__sr2__):]
        data = result
        index = data.find(__sr1__, index+len(insert))
    return data


def checkAll(string, mathes):
    for m in mathes:
        if m[0] in string:
            return True
    return False


def repAllMathes(string, mathes):
    while checkAll(string, mathes):
        for m in mathes:
            string = replaceAll(string, m[0], m[1])
    return string


def createForFileIfNeed(path):
    pt = path.split("/")
    del pt[len(pt)-1]
    pt2 = __mainPath__+("/".join(pt))
    if not os.path.exists(pt2+"/"):
        pass
        os.makedirs(pt2)


def createFile(path, value="", encoding=5):
    createForFileIfNeed(path)
    with open(__mainPath__+path, "w+", encoding=__codecs__[encoding]) as file:
        file.write(value)
        file.close()


def getConfigVar(var, fileName="config.cfg", default=None):
    value = default
    with open(fileName, "r") as file:
        for str1 in file.read().split("\n"):
            if str1.startswith(var):
                value = str1[str1.find("=")+1:].strip()
                break
        file.close()
    return value


def getDeepFiles(pth, prefix = "", ignore=[]):
    fls = os.listdir(pth)
    fls2 = []
    for f in fls:
        if f in ignore:
            continue
        if "." in (pth+f):
            fls2.append(prefix+f)
        else:
            newdir = (pth+"/"+f).replace("//", "/")
            if prefix+f+"/" in ignore:
                continue
            fls3 = getDeepFiles(newdir, prefix+f+"/")
            for ff in fls3:
                fls2.append(ff)
    return fls2


def getFileStr(fileName, encoding=5):
    try:
        file = open(__mainPath__+fileName, encoding=__codecs__[encoding])
        st = file.read().strip()
        file.close()
        return st
    except:
        p("ERROR in "+__mainPath__+" "+fileName)
        logError()
        return ""