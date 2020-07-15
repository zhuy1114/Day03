"""
自媒体主页
"""

# 对象库层：将测试用例中需要用到的元素全部定位回来
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 内容管理
        self.content_manage = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章
        self.pub_article_manage = (By.XPATH, "//*[contains(text(),'发布文章')]")

    # 查找内容管理
    def find_con_mage(self):
        return self.find_elt(self.content_manage)

    # 查找发布文章
    def find_pub_art_mage(self):
        return self.find_elt(self.pub_article_manage)


# 操作层：通过调用对象库层的实例方法拿到元素对象，再定义对应的操作方法
class HomeHandle(BaseHandle):
    def __init__(self):
        # 实例化对象库层
        self.home_page = HomePage()

    # 点击文章管理
    def click_con_mage(self):
        self.home_page.find_con_mage().click()

    # 点击发布文章
    def click_pub_art_mage(self):
        self.home_page.find_pub_art_mage().click()


# 业务层：调用操作层的多个方法，形成连贯的业务操作
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_pub_art_page(self):
        self.home_handle.click_con_mage()
        self.home_handle.click_pub_art_mage()
