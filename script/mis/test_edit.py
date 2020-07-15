# 定义测试类
import time

import pytest

from config import PUB_ARTICLE_TITLE
from page.mis.edit_page import EditProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, is_element_exists


@pytest.mark.run(order=12)
class TestEdit:
    # 定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.home_proxy = HomeProxy()
        self.edit_proxy = EditProxy()

    # 定义测试方法--文案的测试步骤
    def test_edit(self):
        article_title = PUB_ARTICLE_TITLE
        self.home_proxy.to_check_page()
        self.edit_proxy.pass_article(article_title)

        # 断言
        assert is_element_exists(self.driver, PUB_ARTICLE_TITLE)

    # 定义销毁的方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()
