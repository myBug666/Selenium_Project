import unittest
'''
unittest默认加载脚本的顺序是：根据ASCII码的顺序加载，数字与字母的顺序为：0-9，A-Z，a-z

@classmethod  全局变量修饰器
'''
class unit_test(unittest.TestCase):
    def setUp(self):
        print('setUp---------------------------') #1、打开浏览器 2、隐式等待 3、窗口最大化
    def tearDown(self) -> None:
        print('tearDown------------------------') # 关闭浏览器
# 用例 定义方法名，必须以test开头
    def test_1(self):
        print('test_1')

    def test_a(self):
        print('test_a')

    def test_B(self):
        print('test_B')

# 执行顺序
# 数字---大写字母---“_”符号---小写字母



