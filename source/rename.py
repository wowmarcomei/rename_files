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

sourceDir = "../videosAndImages"  # 文件复制源路径
targetDir = "../newFiles"  # 文件复制目标路径
fileType = {
    'jpg': '.jpg',
    'png': '.png',
    'mp4': '.mp4',
    'mov': '.mov'
}

def FilesFilter(src,type):
    """
    遍历源文件目录，将所有符合类型的文件的路径放入selectfilelist,返回selectfilelist

    :param src: 源目录
    :param type: 文件类型
    :return selectfilelist: 文件列表
    """
    dirStack = [sourceDir]  # 遍历目录的目录栈
    fileList = []  # 读取到的文件列表
    selectFileList = [] #筛选后的文件列表

    # 遍历源文件目录，将所有文件的路径放入filelist
    while (len(dirStack) > 0):
        parentDir = dirStack.pop()
        pathlist = os.listdir(parentDir)

        #筛选文件类型,并置于列表selectfilelist中
        for i in range(0,len(pathlist)):
            if (pathlist[i][-4:] == type):
                # selectFileList.append(src)
                selectFileList.append(src+'/'+pathlist[i])

        print("Selected files are: {}".format(selectFileList))

    return selectFileList

def decodeMyFiles(file,filetype,myChar='Creation date',timePosition=8):
    """解析音频或者照片文件,

    :param file: 解析文件
    :param filetype: 待解析文件的类型
    :param myChar: 解析字符
    :param timePosition: 解析出来的字符添加下划线的位置,如:20161212161616,变成20161212_161616
    :return fileFinalTime: 解析出的文件创始时间
    """
    parserFile = parser.createParser(file) #解析文件
    if not parserFile:
        print("Unable to parse file!\n")
        exit(1)

    try:
        metadataDecode = metadata.extractMetadata(parserFile)  # 获取文件的metadata
    except ValueError:
        print('Metadata extraction error.')
        metadataDecode = None

    if not metadataDecode:
        print("Unable to extract metadata.")
        exit(1)

    myList = metadataDecode.exportPlaintext(line_prefix="") # 将文件的metadata转换为list,且将前缀设置为空

    for i in range(1,len(myList)+1):
        #如果字符串在列表中,则提取数字部分,即为文件创建时间
        if myChar in myList[i-1]:
            fileTime = re.sub(r"\D",'',myList[i-1])    #使用正则表达式将列表中的非数字元素剔除
            a=list(fileTime)                           #将文件创建时间字符串转为列表list
            a.insert(timePosition,'_')                 #将列表插入下划线分割date与time
            fileFinalTime = "".join(a)                 #重新将列表转为字符串

            print("The {0} is: {1}".format(myChar,fileFinalTime))
            return fileFinalTime

    print("Unable to get the creation time of {}\n".format(file))

def RenameFiles(src,type,dst='../videosAndImages'):
    files = FilesFilter(src,type)
    for i in range(0,len(files)):
        print("i is: {}".format(i))
        a=decodeMyFiles(files[i],type)
        os.rename(files[i], dst+'/'+a+type)

RenameFiles(sourceDir,fileType['mov'])

