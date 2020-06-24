import os
import datetime
import shutil

dir = 'C:\\Users\Jan-Intel\Desktop'
os.chdir(dir)

def casovnaRazlika(info):
    return (datetime.datetime.now() - datetime.datetime.fromtimestamp(info)).days

def tipDatoteke(name):
    fullName = name
    mesto = name.rfind(".")
    if mesto != -1:
        name = name[mesto+1:]
    else:
        return
    name = name.lower()
    slike = ['jpeg', 'jpg', 'gif', 'png', 'jfif', 'webp']
    dokumenti = ['docx', 'doc', 'odt', 'pdf', 'ods']
    besedila = ['txt']
    koda = ['php', 'htm', 'html', 'js', 'css', 'sql', 'cpp', 'c']

    startDir = dir + '\\' + fullName
    endDir = ""

    if name in slike:
        print(name + ' slika')
        endDir = dir + '\\Slike\\' + fullName
    elif name in dokumenti:
        print(name + ' dokument')
        endDir = dir + '\\Dokumenti\\' + fullName
    elif name in besedila:
        print(name + ' besedilo')
        endDir = dir + '\\Besedila\\' + fullName
    elif name in koda:
        print(name + ' koda')
        endDir = dir + '\\Koda\\' + fullName
    else:
        print(name + ' ni ustrezen')
    
    if endDir != "":
        shutil.move(startDir, endDir)

def preberiDatoteke():
    for entry in os.scandir():
        info = entry.stat()
        if casovnaRazlika(info.st_mtime) > 7:
            tipDatoteke(entry.name)

preberiDatoteke()
# shutil.move(dir + '\Vaje_seznami_1.del.docx', dir + '\Dokumenti\Vaje_seznami_1.del.docx')
# os.close()