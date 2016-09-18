import os
import sys
import io
import re
import hachoir
from hachoir import core
from hachoir import metadata
from hachoir import parser
from hachoir import stream
from hachoir import subfile

# print(help(hachoir)) #查询模块具有哪些package

sourcedir = "../videosAndImages"  # 文件复制源路径
targetdir = "../newFiles"  # 文件复制目标路径
fileType = {
    'jpg': '.jpg',
    'png': '.png',
    'mp4': '.mp4',
    'mov': '.mov'
}

def getFiles(src,type):
    """
    遍历源文件目录，将所有符合类型的文件的路径放入filelist,返回filelist

    :param src: 源目录
    :param type: 文件类型
    :return selectfilelist: 文件列表
    """
    dirstack = [sourcedir]  # 遍历目录的目录栈
    filelist = []  # 读取到的文件列表
    selectfilelist = [] #筛选后的文件列表

    # 遍历源文件目录，将所有文件的路径放入filelist
    while (len(dirstack) > 0):
        parentdir = dirstack.pop()
        pathlist = os.listdir(parentdir)

        #赛选文件类型,并置于列表selectfilelist中
        for i in range(0,len(pathlist)):
            if (pathlist[i][-4:] == type):
                selectfilelist.append(pathlist[i])

        print("赛选后的file为: {}".format(selectfilelist))
    return selectfilelist

getFiles(sourcedir,fileType['mov'])


# #如果没有目录则新建一个
# if (not os.path.exists(targetdir)):
#     try:
#         os.mkdir(targetdir)
#     except Exception:
#         print('failed to create target directory.')
# copycount = 0
# totalcount = len(filelist)
# for file in filelist:
#     # 实现文件拷贝
#     srcfile = io.open(file, "rb")
#     # tarfile = io.open(targetdir+renameMyFiles(file,'jpg'), "wb")
#     # tarfile.write(srcfile.read())
#     # tarfile.close()
#     srcfile.close()
#     copycount += 1  # 计数器递增
#     sys.stdout.write("\r%8d of %8d " % (copycount, totalcount))  # 打印进度