"""
发布文章页面
"""

# 对象库层：将测试用例中需要用到的元素全部定位回来
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, choose_channel


class PubArtPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章名称
        self.art_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # 表单
        self.con_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.art_content = (By.CSS_SELECTOR, "body")
        # 文章封面
        self.art_cover = (By.XPATH, "//*[text()='自动']")
        # 文章频道
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表按钮
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    # 查找文章名称
    def find_art_title(self):
        return self.find_elt(self.art_title)

    # 查找表单
    def find_con_iframe(self):
        return self.find_elt(self.con_iframe)

    # 查找文章内容
    def find_art_content(self):
        return self.find_elt(self.art_content)

    # 查找文章封面
    def find_art_cover(self):
        return self.find_elt(self.art_cover)

    # 查找文章频道
    def find_channel(self):
        return self.find_elt(self.channel)

    # 查找频道选项
    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    # 查找发表按钮
    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层：通过调用对象库层的实例方法拿到元素对象，再定义对应的操作方法
class PubArtHandle(BaseHandle):
    def __init__(self):
        # 实例化对象库层
        self.pub_art_page = PubArtPage()

    # 输入文章名称
    def input_art_title(self, title):
        self.input_text(self.pub_art_page.find_art_title(), title)

    # 输入内容
    def input_art_content(self, content):
        # 先切换表单
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_art_page.find_con_iframe())
        # 输入内容
        self.input_text(self.pub_art_page.find_art_content(), content)
        # 切回默认页面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def choose_art_cover(self):
        self.pub_art_page.find_art_cover().click()

    # 选择频道
    def choose_channel_option(self, expect_channel):
        choose_channel(DriverUtils.get_mp_driver(), '请选择', expect_channel)

    # 点击发表
    def click_pub_btn(self):
        self.pub_art_page.find_pub_btn().click()


# 业务层：调用操作层的多个方法，形成连贯的业务操作
class PubArtProxy:
    def __init__(self):
        self.pub_art_handle = PubArtHandle()

    # 发布文章
    def test_pub_art(self, title, content, channel_name):
        # 输入标题
        self.pub_art_handle.input_art_title(title)
        # 输入内容
        self.pub_art_handle.input_art_content(content)
        # 选择封面
        self.pub_art_handle.choose_art_cover()
        # 选择频道
        self.pub_art_handle.choose_channel_option(channel_name)
        # 发布文章
        self.pub_art_handle.click_pub_btn()
