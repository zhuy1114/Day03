import threading
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def get_driver(browsername):
    if browsername == 'chrome':
        caps = DesiredCapabilities.CHROME.copy()
        caps['platform'] = 'WINDOWS'
    elif browsername == 'firefox':
        caps = DesiredCapabilities.FIREFOX.copy()
        caps['platform'] = 'WINDOWS'
    else:
        caps = DesiredCapabilities.CHROME.copy()
        caps['platform'] = 'WINDOWS'
    # 创建驱动对象
    driver = webdriver.Remote("http://192.168.1.101:4444/wd/hub", caps)
    return driver


def do_test(driver):
    # 执行业务操作
    driver.maximize_window()
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("kw").send_keys("test")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    browserName = ['chrome', 'firefox']
    for i in browserName:
        driver = get_driver(i)
        threading.Thread(target=do_test, args=(driver,)).start()
