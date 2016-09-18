import re
import os
import sys
import io
import hachoir
from hachoir import core
from hachoir import metadata
from hachoir import parser
from hachoir import stream
from hachoir import subfile


# print(help(hachoir)) #查询模块具有哪些package


recursive = False  # 递归获取源目录的子目录文件
sourcedir = "./videosAndImages"  # 文件复制源路径
targetdir = "./newFiles"  # 文件复制目标路径
dirstack = [sourcedir]   # 遍历目录的目录栈，使用栈结构实现目录树遍历
filelist = []            # 读取到的文件列表

print('source dir: ' + sourcedir)
print('target dir: ' + targetdir)

# 遍历源文件目录，将所有文件的路径放入filelist
while ( len(dirstack) > 0 ):
	parentdir = dirstack.pop()
	pathlist = os.listdir(parentdir)
	for path in pathlist:
		filepath = os.path.join(parentdir, path)
		isdir = os.path.isdir(filepath)
		if ( isdir and recursive):
			dirstack.append(filepath)
		elif ( not isdir):
			filelist.append(filepath)
print("There are {} files to be renamed.".format(len(filelist)))
print("filelist: {}".format(filelist))


#如果没有目录则新建一个
if (not os.path.exists(targetdir)):
    try:
        os.mkdir(targetdir)
    except Exception:
        print('failed to create target directory.')

copycount = 0
totalcount = len(filelist)
for file in filelist:
    # 实现文件拷贝
    srcfile = io.open(file, "rb")
    # tarfile = io.open(targetdir+renameMyFiles(file,'jpg'), "wb")
    # tarfile.write(srcfile.read())
    # tarfile.close()
    srcfile.close()
    copycount += 1  # 计数器递增
    sys.stdout.write("\r%8d of %8d " % (copycount, totalcount))  # 打印进度