f = open("1.csv","w")
f.write("hello,world")     #hello 在一个格   world在一个格
f.close()
f = open("2.csv","w")
f.write('"hello,world"')     # hello,world  在一个格
f.close()




