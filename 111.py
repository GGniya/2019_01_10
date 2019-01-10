from bloomfilter import Bloomfilter
import os
#  参数1:       n位  或者  文件路径
if os.path.exists("state.txt"):
    print("文件存在直接加载状态")
    bloom = Bloomfilter("state.txt")
else:
    print("文件不存在设置大小为100000")
    bloom = Bloomfilter(100000)

bloom =Bloomfilter(100000)
# 如果程序是第一次使用填数字    如果不是第一次 用文件路径
# bloom =Bloomfilter("state.txt")
while True:
    key = input("请输入数据")
    if bloom.test(key):    #测试
        print("数据存在",key)
    else:
        print("数据不存在!",key)
        bloom.add(key)        #添加
        bloom.save("state.txt")   #状态保存