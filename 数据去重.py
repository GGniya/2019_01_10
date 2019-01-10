#   3  布隆去重   推荐
#布隆过滤存储的是状态  0 / 1
# 优点: 内存占有量低 ,可以持久化存储
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



#   1   列表去重
#优点:逻辑/代码简单易懂
# 缺点 1)如果数据量巨大电脑吃不消(内存)
#      2)只对当前运行有效 ,不能停
result = ['zhangsan','lisi']
keyword = 'wangwu'
if 'zhangsan' in result:
    print("数据已存在")
else:
    #数据存储
    print("新数据,开始存储")
    result.append(keyword)

result = []
while True:
    keyword = input("请输入数据")
    if keyword in result:
        print("数据已存在")
    else:
        print("数据不存在!开始处理")
        result.append(keyword)


# python 生成随机字符串
import uuid
result = []
while True:
    key = uuid.uuid1()
    if keyword in result:
        print("数据已存在")
    else:
        print("数据不存在!开始处理")
        result.append(keyword)


import sys , uuid
result = []
while True:
    key = uuid.uuid1()
    if key in result:
        print("数据已存在")
    else:
        print("数据不存在!开始处理")
        result.append(key)
        print("内存占用:",sys.getsizeof(result))



#      2  列表去重  列表存储加密后的数据
#常用的加密算法    md5 (推荐)  /                不推荐    aes   /  des  /
import hashlib
md5str ="要去重加密的数据"
m1 = hashlib.md5()
m1.update(md5str.encode("utf-8"))
token = m1.hexdigest()
print(token)


