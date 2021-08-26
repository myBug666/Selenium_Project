

import sys

print(sys.path)
import unittest


sys.path.append('D:\\Project\\test\\selenlum1910\\page_object1910')
sys.path.append('D:\\Project\\test\\selenlum1910')
sys.path.append('E:\\tool\\PyCharm 2019.3.1\\plugins\\python\\helpers\\pycharm_display')
sys.path.append('D:\\huanjing\\test2\\Scripts\\python38.zip')
sys.path.append('D:\\huanjing\\test2\\DLLs')
sys.path.append('D:\\huanjing\\test2\\lib')
sys.path.append('D:\\huanjing\\test2\\Scripts')
sys.path.append('d:\\t\\python3\\Lib')
sys.path.append('d:\\t\\python3\\DLLs')
sys.path.append('D:\\huanjing\\test2')
sys.path.append('D:\\huanjing\\test2\\lib\\site-packages')
sys.path.append('D:\\huanjing\\test2\\lib\\site-packages\\pip-19.0.3-py3.8.egg')
sys.path.append('E:\\tool\\PyCharm 2019.3.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend')



if __name__ == '__main__':
#     # 测试用例集
    suite = unittest.defaultTestLoader.discover('testCase/smokeTesCase',pattern="*test.py")
#     # 测试用例加载器
    unittest.TextTestRunner().run(suite)


