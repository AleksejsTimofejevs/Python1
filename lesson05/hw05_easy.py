# coding: utf-8

__author__ = 'Тимофеев Алексей'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import sys
import os
import shutil

def createdirs(n):
    try:
        for i in range(1,n):
            os.mkdir("dir_" + str(i))
    except OSError:
        print("Папки уже существуют!")

def deletedirs(n):
    try:
        for i in range(1,n):
            os.rmdir("dir_" + str(i))
    except OSError:
        print("Папки уже удалены!")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def showdir():
    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i):
            print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copycurfile():
    titlelist = os.path.basename(__file__).split(".")
    destdir = os.path.abspath(titlelist[0]) + "copy.py"
    shutil.copy(__file__, destdir)


def showall():
    for i in os.listdir(os.getcwd()):
        print(i)

def deletedir(n):
    try:
        os.rmdir(n)
    except OSError:
        print("Папки уже удалены!")

def createdir(n):
    try:
        os.mkdir(n)
    except OSError:
        print("Папки уже существуют!")