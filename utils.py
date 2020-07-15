import json

import selenium.webdriver
import appium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 读取json数据文件的方法
def load_json_data(file_path):
    case_data = []
    # 打开数据文件
    with open(file_path, encoding="utf-8")as f:
        # 读取json数据
        data = json.load(f)
        # 遍历键值
        for data_value in data.values():
            # 以列表形式呈现
            case_data.append(list(data_value.values()))
    return case_data


def choose_channel(driver, channel_keywords, expect_name):
    css_string = "[placeholder*='{}']".format(channel_keywords)
    driver.find_element_by_css_selector(css_string).click()
    # 获取所有频道选项
    option_list = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    # 是否找到标识
    is_element = False
    for channel_name in option_list:
        if channel_name.text == expect_name:
            channel_name.click()
            is_element = True
            break
        else:
            ActionChains(driver).move_to_element(channel_name).send_keys(Keys.DOWN).perform()
            is_element = False
    if is_element is False:
        NoSuchElementException("can't find this {} option".format(expect_name))


def is_element_exists(driver, text):
    xpath_string = "//*[contains(text(),'{}')]".format(text)
    try:
        is_suc = driver.find_element_by_xpath(xpath_string)
    except Exception as e:
        is_suc = False
        raise
    return is_suc


# 根据元素的属性值判断元素是否存在
def is_element_by_att_exists(driver, attr_name, attr_value):
    xpath_string = "//*[contains(@{},'{}')]".format(attr_name, attr_value)
    try:
        is_suc = driver.find_element_by_xpath(xpath_string)
    except Exception as e:
        is_suc = False
        raise
    return is_suc


class DriverUtils:
    # 定义私有属性
    # 自媒体
    __mp_driver = None

    # 后台管理
    __mis_driver = None

    # app
    __app_driver = None

    # 自媒体开关
    __mp_key = True

    # 后台管理系统开关
    __mis_key = True

    # 自媒体驱动
    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(10)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    # 修改mp开关的方法
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 后台管理系统驱动
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(10)
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    # 修改mis开关的方法
    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # app驱动
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            cap = {
                "platformName": 'android',
                'deviceName': 'huawei',
                'appPackage': 'com.itcast.toutiaoApp',
                'appActivity': '.MainActivity',
                'noReset': True
            }
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)

        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None
