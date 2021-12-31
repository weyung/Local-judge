import subprocess
import random
import sys
from tqdm import tqdm

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
    # print(out_info,out_error)
    return out_info

if __name__ == '__main__':
    stdpath = "%s/标准代码/" % sys.path[0]      # 标准代码所在路径
    testpath = "%s/测试代码/" % sys.path[0]     # 测试代码所有路径
    #编译标准及测试代码
    result = subprocess.check_output("gcc -std=c99 -o std std.c", shell=True, cwd=stdpath)
    result = subprocess.check_output("gcc -std=c11 -o test test.c", shell=True, cwd=testpath)

    f = open('%s/测试结果.txt' % sys.path[0], 'w+', encoding='utf-8', newline="")
    print('随机测试中...')
    pas=0       # 通过次数
    freq=100    # 测试次数
    for index in tqdm(range(freq)):
        # 生成测试数据
        rtest = random_int_list(0, 99, 10)
        s = ''
        for i in rtest:
            s = "%s%s " % (s, i)
        s = "%s\n" % s
        # 进行测试
        output = iotest("./test", testpath, s)
        stdoutput = iotest("./std", stdpath, s)
        f.write("随机测试 - r,%d数据点\n"%index)
        f.write("标准输入\n%s" % s)
        f.write("实际输出\n%s\n" % output)
        f.write("期望输出\n%s\n\n" % stdoutput)
        if output==stdoutput:
            f.write('通过「随机测试 - r,%d数据点」测试点\n\n'%index)
            pas=pas+1
        else:
            f.write('未通过「随机测试 - r,%d数据点」测试点\n\n'%index)
    f.close()
    print('随机测试 %d/%d'%(pas,freq))
    print('测试完成')

