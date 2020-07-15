from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

        # 信息管理
        self.info_manage = (By.XPATH, "//*[text()='信息管理']")
        # 内容审核
        self.check_info = (By.XPATH, "//*[text()='内容审核']")

    def find_info_manage(self):
        return self.find_elt(self.info_manage)

    def find_check_info(self):
        return self.find_elt(self.check_info)


class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    def click_info_manage(self):
        self.home_page.find_info_manage().click()

    def click_check_info(self):
        self.home_page.find_check_info().click()


class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_check_page(self):
        self.home_handle.click_info_manage()
        self.home_handle.click_check_info()
