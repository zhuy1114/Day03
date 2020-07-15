import logging
import time

import pytest

from config import PUB_ARTICLE_TITLE, BASE_PATH
from page.mp.home_page import HomeProxy
from page.mp.pub_art_page import PubArtProxy
from utils import DriverUtils, is_element_exists, load_json_data


@pytest.mark.run(order=2)
class TestPubArticle:
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.pub_art_proxy = PubArtProxy()

    @pytest.mark.parametrize("art_content,art_channel", load_json_data(BASE_PATH + "/data/test_pub_article.json"))
    def test_pub_article(self, art_content, art_channel):
        art_title = PUB_ARTICLE_TITLE
        art_content = art_content
        art_channel = art_channel
        logging.info("发布的文章信息为：文章标题={}，文章内容={}，文章频道={}".format(art_title, art_content, art_channel))
        self.home_proxy.to_pub_art_page()
        self.pub_art_proxy.test_pub_art(art_title, art_content, art_channel)
        assert is_element_exists(self.driver, '新增文章成功')

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
