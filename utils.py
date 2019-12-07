# 自定义工具类


def assert_common(self, response, http_code, status,
                  msg):  # response:外部传入的Response对象，http_code：200，status：预期结果的status，msg：预期的msg
    # 断言响应数据中的响应状态码是否为200
    self.assertEqual(http_code, response.status_code)
    # 断言status
    self.assertEqual(status, response.json().get("status"))
    # 断言msg
    self.assertEqual(msg, response.json().get("msg"))
