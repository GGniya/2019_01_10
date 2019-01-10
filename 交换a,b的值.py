# 在不创建第三个变量的情况下交换a和b的值
a = 10
b = 60

# 第一种
a = a + b  # a=70 b=60
b = a - b  # b=10 a=70
a = a - b  # a=60 b=10

# 第二种
a, b = b, a
print(a, b)
