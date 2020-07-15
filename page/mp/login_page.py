"""
自媒体登录页面
"""

# 对象库层：将测试用例中需要用到的元素全部定位回来
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 手机号
        self.phone_num = (By.CSS_SELECTOR, "[placeholder*='手机号']")
        # 验证码
        self.verify_code = (By.CSS_SELECTOR, "[placeholder*='验证码']")
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 查找手机号
    def find_phone_num(self):
        return self.find_elt(self.phone_num)

    # 查找验证码
    def find_verify_code(self):
        return self.find_elt(self.verify_code)

    # 查找登录按钮
    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层：通过调用对象库层的实例方法拿到元素对象，再定义对应的操作方法
class LoginHandle(BaseHandle):
    def __init__(self):
        # 实例化对象库层
        self.login_page = LoginPage()

    # 输入手机号
    def input_phone_num(self, phone_num):
        self.input_text(self.login_page.find_phone_num(), phone_num)

    # 输入验证码
    def input_verify_code(self, verify_code):
        self.input_text(self.login_page.find_verify_code(), verify_code)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 业务层：调用操作层的多个方法，形成连贯的业务操作
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 定义登录的方法
    def test_login(self, phone_num, verify_code):
        # 输入手机号
        self.login_handle.input_phone_num(phone_num)
        # 输入验证码
        self.login_handle.input_verify_code(verify_code)
        # 点击登录
        self.login_handle.click_login_btn()
