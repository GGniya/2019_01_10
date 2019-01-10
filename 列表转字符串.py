a = ['a','b','c','d']
#列表通过     .join()转字符串 中间用   -    连接
content = "-".join(a)    #注意:列表中只能说字符串,有数字会报错

print(content)
a = ['a','b','c','d','10']
content = "-".join(a)
print(content)

# a = ['a','b','c','d',10]
content = "-".join(a)
print(content)      #报错

a = ['a-e','b','c','d','10']
content = "-".join(a)       #列表中有 - 结果就不理想 需考虑
print(content)
