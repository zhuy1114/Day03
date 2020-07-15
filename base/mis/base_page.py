from utils import DriverUtils


# 对象库层基类
class BasePage:
    def __init__(self):
        # 获取后台管理系统的浏览器驱动对象
        self.driver = DriverUtils.get_mis_driver()

    # 公用定位元素方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 操作层基类
class BaseHandle:
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
