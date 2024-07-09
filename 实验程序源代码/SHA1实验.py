import hashlib
import time

def JMSHA1(path):
    sha1jiami = hashlib.sha1()
    try:
        a = open(fr'{path}', 'rb')
    except:
        print('文件路径有误，请输入正确的路径！')
        return main()
    while True:
        b = a.read(256000)  # 这里就是每次读取文件放入内存的大小，小心溢出！
        sha1jiami.update(b)
        if not b:
            break
    a.close()
    jiamijiegou = sha1jiami.hexdigest()
    return jiamijiegou

def SHAcompare():
    num = input('请输入已知的SHA1值：')
    path = input('请输入文件路径：')
    starttime = time.time()
    data = JMSHA1(path)
    print(f'{path}的SHA1值为：{data}')  
    if num == data:
        print(f'两个文件SHA1值相同\n花费时间：{time.time() - starttime}')
    else:
        print(f'两个文件SHA1值不相同\n花费时间：{time.time() - starttime}')

def filecompare():
    path1 = input('请输入文件1路径：')
    path2 = input('请输入文件2路径：')
    starttime = time.time()
    data = JMSHA1(path1)
    data2 = JMSHA1(path2)
    print(f'{path1}的SHA1值为：{data}')
    print(f'{path2}的SHA1值为：{data2}')
    if data2 == data:
        print(f'两个文件SHA1值相同\n花费时间：{time.time() - starttime}')
    else:
        print(f'两个文件SHA1值不相同\n花费时间：{time.time() - starttime}')

def justSHA1():
    path = input('请输入文件路径：')
    starttime = time.time()
    data = JMSHA1(path)
    print(f'{path}的SHA1值为：{data}\n花费时间：{time.time() - starttime}')

def main():
    while True:
        print('_'*20 + 'GetSHA1' + '_'*20)
        print(f'1.计算文件SHA1；\n2.已知SHA1值对比文件；\n3.比较两个文件SHA1值\n0.退出')
        a = input('请输入功能序号：')
        if a == '1':
            justSHA1()
        elif a == '2':
            SHAcompare()
        elif a == '3':
            filecompare()
        elif a == '0':
            print('程序已退出！')
            print('*' * 30 + 'GetSHA1' + '*' * 30)
            exit()
        else:
            print('输入有误，请重新输入！')
if __name__ == '__main__':
    main()
