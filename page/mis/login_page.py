from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtils


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()

        # 查找用户名
        self.username = (By.NAME, "username")
        # 查找密码
        self.password = (By.NAME, "password")
        # 登录按钮
        self.submit_btn = (By.ID, "inp1")

    def find_username(self):
        return self.find_elt(self.username)

    def find_password(self):
        return self.find_elt(self.password)

    def find_sub_btn(self):
        return self.find_elt(self.submit_btn)


class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    def click_sub_btn(self):
        js_str = "document.getElementById('inp1').removeAttribute('disabled')"
        DriverUtils.get_mis_driver().execute_script(js_str)
        self.login_page.find_sub_btn().click()


class LoginProxy:
    def test_login(self, username, password):
        self.loing_handle = LoginHandle()
        self.loing_handle.input_username(username)
        self.loing_handle.input_password(password)
        self.loing_handle.click_sub_btn()
