import requests


class LoginApi:

    def __init__(self):
        # self.session = requests.Session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
    def get_verify(self, obj):  # obj是外部传入的session实例
        # 返回获取验证码接口的信息
        return obj.get(self.verify_url)

    def login(self, obj, username, password, verify_code):  # obj是外部传入的session实例
        return obj.post(self.login_url,
                        data={"username": username, "password": password, "verify_code": verify_code})
