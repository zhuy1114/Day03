"""
    审核文章页面
"""
# 对象库层
from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import choose_channel, DriverUtils


class EditPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章名称输入框
        self.art_title = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 查询按钮
        self.query_btn = (By.XPATH, "//*[text()='查询']")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 确认按钮
        self.confirm_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_art_title(self):
        return self.find_elt(self.art_title)

    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    def find_confirm_btn(self):
        return self.find_elt(self.confirm_btn)


# 操作层
class EditHandle(BaseHandle):
    def __init__(self):
        self.aduit_page = EditPage()

    # 输入文章标题
    def input_art_title(self, title):
        self.input_text(self.aduit_page.find_art_title(), title)

    # 选择状态栏
    def choose_status(self, status):
        choose_channel(DriverUtils.get_mis_driver(), '请选择状态', status)

    # 点击查询按钮
    def click_query_btn(self):
        self.aduit_page.find_query_btn().click()

    # 点击通过按钮
    def click_pass_btn(self):
        self.aduit_page.find_pass_btn().click()

    # 点击确定按钮
    def click_confirm_btn(self):
        self.aduit_page.find_confirm_btn().click()


# 业务层
class EditProxy:
    def __init__(self):
        self.edit_handle = EditHandle()

    def pass_article(self, title):
        # 输入文章标题
        self.edit_handle.input_art_title(title)
        # 选择状态为待审核
        self.edit_handle.choose_status('待审核')
        # 点击查询
        self.edit_handle.click_query_btn()
        # 点击通过
        self.edit_handle.click_pass_btn()
        # 点击确定
        self.edit_handle.click_confirm_btn()
        # 修改状态为审核通过状态
        self.edit_handle.choose_status('审核通过')
        # 点击查询按钮
        self.edit_handle.click_query_btn()
