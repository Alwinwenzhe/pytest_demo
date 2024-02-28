import requests

class AllRequest:

    session = requests.session()  # 在跨请求时自动保存和管理登录接口获取到的cookies信息，而不用手动处理这类信息了，比如login后，正常使用其它接口登录，不用特殊处理cookies

    def all_send_request(self,method,url,data,**kwargs):
        # 数据可能有params，data，json，files
        method = str(method).lower()
        if method == 'get':
            res = self.session.request(method=method,url=url,params=data,**kwargs)
        elif method== 'post':
            res = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            print('不支持得请求方式')
        return res
