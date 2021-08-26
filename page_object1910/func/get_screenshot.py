'''
截图方法    出现Bug以后截图， 预期结果与实际结果不一致需要截图
'''
import os
import time

def Get_Screenshot(driver,filename):
    # 获取当前文件的路径
    path = os.path.dirname(__file__)
    # 获取时间戳的方法    第一个时间戳需要年月日
    time_stamp1 = time.strftime('%Y%m%d')
                      # 获取时分秒
    time_stamp2 = time.strftime('%H-%M-%S')
      # 图片路径              # 替换文件夹
    image_path = path.replace('func','image')
    # 文件路径
    filepath = image_path + '/' + time_stamp1
    # 假如没有这个时间戳--就新建一个
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    # 全路径
    image_full_path = filepath + '/' + filename + time_stamp2 + '.png'
          # get_screenshot_as_file 获取截图的方法
    driver.get_screenshot_as_file(image_full_path)



