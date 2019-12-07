import unittest
from api.login_api import LoginApi
import requests

from utils import assert_common


class TestLogin(unittest.TestCase):


    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.session = requests.Session()
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    def test01_login_success(self):
        # 调用获取验证码接口
        response = self.login_api.get_verify(self.session)
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # print(resposne.text)
        # 调用自己封装的登陆接口
        response = self.login_api.login(self.session, "18600000000", "123456", "8888")
        print(response.json())

        assert_common(self, response, 200, 1, "登陆成功")

    def test02_username_is_error(self):
        # 调用获取验证码接口
        response = self.login_api.get_verify(self.session)
        # 断言返回的图片
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # 调用登陆接口
        response = self.login_api.login(self.session, "13900138006", "123456", "8888")
        print(response.json())

        # 断言
        assert_common(self, response, 200, -1, "账号不存在!")

    def test03_password_is_error(self):
        # 获取验证码
        response = self.login_api.get_verify(self.session)
        # 断言返回的图片
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # 调用登陆接口
        response = self.login_api.login(self.session, "13800138006", "error", "8888")
        print(response.json())

        # 断言
        assert_common(self, response, 200, -2, "密码错误!")
