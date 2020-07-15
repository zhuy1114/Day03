# 对象库层
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle
from utils import DriverUtils


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

        # 频道区域
        self.channel_area = (By.XPATH, "//*[class='android.widget.HorizontalScrollView']")
        # 频道
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        # 第一条文章信息
        self.article_info = (By.XPATH, "//*[contains(@text,'评论')]")

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    def find_channel_option(self, channel_name):
        return self.driver.find_element(self.channel_option[0], self.channel_option[1].format(channel_name))

    def find_article_info(self):
        return self.find_elt(self.article_info)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 选择频道
    def choose_channel(self, channel_name):
        # 获取区域的范围
        area = self.home_page.find_channel_area()
        # 获取区域的左上角起点
        x = area.location['x']
        y = area.location['y']
        # 获取区域的长和宽
        w = area.size['width']
        h = area.size['height']
        # 滑动的位置
        # 开始x坐标
        start_x = x + w * 0.8
        # 开始y坐标
        start_y = y + h * 0.5

        # 结束x坐标
        end_x = x + w * 0.2
        # 结束y坐标
        end_y = start_y

        # 在当前区域根据频道的名称来查找对应元素
        while True:
            # 获取当前页面信息
            page_old = DriverUtils.get_app_driver().page_source
            # 如果找到元素就点击
            try:
                self.home_page.find_channel_option(channel_name).click()
                break
            # 没有找到则继续滑动
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y)
                # 获取滑动之后的页面信息
                page_new = DriverUtils.get_app_driver().page_source
                # 判断滑动之前和之后的信息是否相等
                if page_old == page_new:
                    raise NoSuchElementException("not find {} channel".format(channel_name))

    # 点击文章
    def click_article_info(self):
        self.home_page.find_article_info().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 根据频道查询文章
    def query_article(self, channel_name):
        self.home_handle.choose_channel(channel_name)
        self.home_handle.click_article_info()
