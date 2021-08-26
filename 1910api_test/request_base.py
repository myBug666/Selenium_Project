import json

import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

base_url = 'http://httpbin.org'

# 一，四种请求
# r = requests.get(base_url + '/get')
# print(r.status_code)
# r = requests.post(base_url + '/post')
# print(r.status_code)
# r = requests.put(base_url + '/put')
# print(r.status_code)
# r = requests.delete(base_url + '/delete')
# print(r.status_code)

# 二，参数的传递
# param_data = {
#     'user':'tjc',
#     'password':'666666'}
# r = requests.get(base_url + '/get',params=param_data)
# print(r.url)

# 三、请求头定制
# form_data = {'user':'tjc','password':'666666'}
# user_header = {"Accept":"acc","Host":"tjc_localhost",
#           "user-agent":"Moailla/5.0 (Windows NT 10.0; Win64; x64)"}
# reg = requests.post(base_url + '/post',data=form_data,headers=user_header)
# print(reg.text)
# 不加请求头，会别反爬虫网站屏蔽

# 四、获取cookies，设置cookie的格式，超时设置
# cookie = {'user':'tjc'}
# reg = requests.get(base_url + '/get',cookies = cookie,timeout = 3)
# print(reg.text)
# print(reg.cookies)

# # 五、文件上传
# file = {'file':open('文件名字.txt','rb')}
# req = requests.post(base_url + '/post',files = file)
# # print(req.text)
# print(req.text.encode('utf-8').decode('uniconde_ecaape'))

# 六、会话对象
# req = requests.get(base_url + '/get','cookies/set/user/tjc')
# print(req.text)
# 用会话对象，做一些接口依赖的运用，利用session我们可以做到模拟同一个会话；
# 而且不用担心cookies的问题；
# 通过常用模拟登录成功之后再进行下一步的操作，生成会话对象
# session = requests.Session()
# req = session.get(base_url + '/cookies/set/user/tjc')
# # print(req.text)
# # 获取cookie
# req1 = session.get(base_url  + '/cookies')
# print(req1.text)

# 七、证书验证 若有验证证书需求：不想验证，则加verify=False，关闭验证SSL
# req = requests.get('https://www.12306.cn',verify=False)
# print(req.text)

# 八、设置代理ip
# proxies = {'http':'.......'}
# req = requests.get(base_url + '/get',proxies = proxies)

# 九、身份认证-BasicAuth
# req = requests.get(base_url + '/basic-auth/tjc/6666',auth = HTTPBasicAuth('tjc','6666'))
# print(req.text)
# print(req.status_code)
# 身份认证-DigestAuth
# requests.get(base_url+'digest-auth/auth/tjc/666666',auth = HTTPDigestAuth('tjc','666666'))

# 十、流式请求处理
req = requests.get(base_url + '/stream/10',stream=True)
print(req.text)
# 对响应结果进行迭代处理，line遍历每一组数据，req.响应的所有数据集 调用iter_lines方法
for line in req.iter_lines(decode_unicode=True):
    # 如果解析出来的数据不为空
    if line:
        # 解析位Json格式数据
        data = json.loads(line)
        print(data['id'])




