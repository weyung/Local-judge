import subprocess
import random
import os
import shutil
import chardet
import os.path
import sys

def detectCode(path):
	with open(path, 'rb') as file:
		data = file.read(200000)
		dicts = chardet.detect(data)
	return dicts["encoding"]
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (
        int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
def iotest(filename, path, data):
    obj = subprocess.Popen([filename], stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path, encoding="utf-8")
    obj.stdin.write(data)
    out_info, out_error = obj.communicate()  # 简单写法，out_info：标准输出
    #print(out_info,out_error)
    if(out_error):
        print('hhsdkfj')
    return out_info
def getpathsuffix(path):
    return path.split('/')[-1]


if __name__ == '__main__':
    stdpath = "%s/标准代码/" % sys.path[0]
    testpath = "%s/测试代码/" % sys.path[0]
    result = subprocess.check_output(
        "gcc -std=c99 -o std std.c", shell=True, cwd=stdpath)

    f = open('%s/测试结果.txt' % sys.path[0], 'w+', encoding='utf-8', newline="")
    rootdir = './hw.atpyyds.xyz/upload'     # 作业存放的文件夹
    list = os.listdir(rootdir)              # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        print('%d\t%s'%(i+1,getpathsuffix(path)))
        orifile='%s/第1题.cpp'%path
        if((os.path.isfile(orifile))==False):
            orifile='%s/第1题.c'%path
        shutil.copyfile(orifile,'%s/raw.c'%testpath)
        #替换
        rawfile=open('%sraw.c'%testpath, 'r', encoding=detectCode('%sraw.c'%testpath))
        testfile=open('%stest.c'%testpath,"w+", encoding='utf-8')
        lines=rawfile.readlines()
        for line in lines:
            line=line.replace('"stdafx.h"',"<stdio.h>")
            line=line.replace('<iostream>',"<stdio.h>")
            line=line.replace('scanf_s',"scanf")
            line=line.replace('printf_s',"printf")
            testfile.write(line)
        rawfile.close()
        testfile.close()
        #编译
        try:
            result = subprocess.check_output(
        "gcc -std=c99 -o test test.c", shell=True, cwd=testpath)
        except:
            f.write('%s\n'%path.split('/')[-1])
            f.write('编译失败\n\n')
            print('编译失败')
            continue
        for count in range(1):
            rtest = random_int_list(0, 20, 10)
            s = ''
            for i in rtest:
                s = "%s%s " % (s, i)
            s = "%s\n" % s
            output = iotest("./test", testpath, s)
            stdoutput = iotest("./std", stdpath, s)
            f.write('%s\n'%getpathsuffix(path))
            f.write("随机测试 - %d数据点\n"%count)
            f.write("标准输入\n%s" % s)
            f.write("输出\n%s\n" % output)
            f.write("期望输出\n%s\n\n" % stdoutput)
    f.close()
