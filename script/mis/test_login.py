import time

import pytest

from page.mis.login_page import LoginProxy
from utils import DriverUtils, is_element_exists


@pytest.mark.run(order=11)
class TestLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_proxy = LoginProxy()

    def test_login(self):
        username = 'testid'
        password = 'testpwd123'
        self.login_proxy.test_login(username, password)
        assert is_element_exists(self.driver, '管理员')

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()
