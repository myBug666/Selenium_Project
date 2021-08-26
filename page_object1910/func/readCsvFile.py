import csv
import os

# 不同的测试用例，读取不同的文件，所以在公共方法中，需要接受文件名作为参数
def read(filename):
    # 使用相对路径
    # __file__ 是Python的内置函数，表示当前代码文件
    # os 表示操作系统，path 表示操作系统中的路径
    # dirname 表示当前的路径，不包含文件名
    base_path = os.path.dirname(__file__)   # 通过系统获取当前文件夹的路径
    # print(base_path)
    path = base_path.replace('func','data/'+filename)  # 找到data里面的文件
    list = []
    with open(path) as content:
        data = csv.reader(content)
        for row in data:
            list.append(row)
    # 测试数据库不包含第一行表头，加上[1:]
    return list[1:]

if __name__ == '__main__':
    # list = read('reg_normal.csv')
    list = read('add_goods.csv')
    print(list)

