import time

from page.app.home_page import HomeProxy
from utils import DriverUtils, is_element_by_att_exists


class TestQueryArticle:
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.home_proxy = HomeProxy()

    def test_query_article(self):
        channel_name = '推荐'
        self.home_proxy.query_article(channel_name)
        assert is_element_by_att_exists(self.driver, "text", "猜你喜欢")

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_app_driver()
