'''
执行测试用例的一个入口，通过这个文件可以执行指定测试用例，或全部测试用例
'''
import os
import time
import unittest

# from page_object1910.lib.BSTestRunner import BSTestRunner
from page_object1910.lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 1、找出所需执行的测试用例，TestLoader执行测试用例的加载器

                                            # *test 是匹配test结尾
    suite = unittest.defaultTestLoader.discover('testCase/smokeTesCase', pattern='*test.py')
                                            # test* 是匹配test开头
    # suite = unittest.defaultTestLoader.discover('testCase',pattern='test*.py')

    # 2-1、通过unittest执行测试用例集
    # unittest.TextTestRunner().run(suite)
    # 2-2、通过HTMLTestRunner文件执行测试用例集
    file_path = os.path.dirname(__file__)  # 先找到本文件的路径
                   # 获取时间戳
    time_stamp = time.strftime('%Y%m%d_%H-%M-%S')  # strftime
        # 先找到本文件 放到report下面 加上文件名  加上时间戳
    all_path = file_path + "/report/" + "测试报告" + time_stamp + ".html"
    file = open(all_path,'wb') # w写 b二进制
    HTMLTestRunner(stream=file,verbosity=1,title='1910自动化测试报告',
                   description='测试环境：win10、i7、8G、SSD500G', tester = '田建朝').run(suite)
    # BSTestRunner(stream=file,verbosity=1,title='1910自动化测试报告',
    #                description='测试环境：win10、i7、8G、SSD500G', tester = '田建朝').run(suite)
    file.close() # 关闭文件




