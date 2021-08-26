import unittest
'''
依赖---需要用全局变量
'''
class unit_test(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('setUp-------1、打开浏览器 2、隐式等待 3、窗口最大化')  # 1、打开浏览器 2、隐式等待 3、窗口最大化

    def tearDown(self) -> None:
        print('tearDown-----------关闭浏览器')  # 关闭浏览器


if __name__ == '__main__':
    unittest.main()
