import time

import pytest

from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_element_exists


@pytest.mark.run(order=2)
class TestLogin:
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.login_proxy = LoginProxy()

    def test_login(self):
        phone_num = "13911111111"
        verify_code = "246810"
        self.login_proxy.test_login(phone_num, verify_code)
        # 断言
        assert is_element_exists(self.driver, '传智播客')

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
