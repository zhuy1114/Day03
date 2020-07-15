import pytest

from utils import DriverUtils


@pytest.mark.run(order=19)
class TestEnd:
    def test_end(self):
        # 修改关闭浏览器的开关值为False
        DriverUtils.change_mis_key(True)
        DriverUtils.quit_mis_driver()
