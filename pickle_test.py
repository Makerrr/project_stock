import pickle as pkl
file = open('/Data/Embedding/rel.voc.pickle','rb')  # 以二进制读模式（rb）打开pkl文件
data =pkl.load(file)  # 读取存储的pickle文件
print(type(data))   # 查看数据类型
for i, (k, v) in enumerate(data.items()):   # 读取字典中前十个键值对
    if i in range(0, 10):
        print(k, v)
