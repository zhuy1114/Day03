from utils import DriverUtils


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_app_driver()

    def find_elt(self, location):
        return self.driver.find_element(*location)


class BaseHandle:
    def input_text(self, element, text):
        """
        :param element: 模拟对象
        :param text: 模拟输入的文本
        :return:
        """
        element.clear()
        element.send_keys(text)
