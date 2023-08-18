import time

from selenium import webdriver


def login():
    # 使用ChromePotions不自动退出浏览器
    driver = webdriver.ChromeOptions()
    driver.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=driver)

    url = 'https://youzy.cn/'
    # 打开优志愿
    driver.get(url)
    # 放大界面
    driver.maximize_window()
    # 选择省份
    driver.find_element('xpath', '//a[contains(@class, "js-selectProvince") and @title="湖南"]').click()
    # # 点击登录
    driver.find_element('xpath', '//div[@class="fleft" and @id="divLogin"]').click()
    time.sleep(2)
    # # 切换手机号登录
    driver.find_element('xpath', '//a[not(contains(@class,"hide")) and contains(@class,"js-login-type")]').click()
    time.sleep(2)
    # # 输入手机号
    mobile = driver.find_element('xpath', '//*[@id="uzy-form-login"]/div[2]/div[4]/div[1]/input')
    mobile.send_keys("19512287942")
    # # 输入密码
    password = driver.find_element('xpath', '//*[@id="uzy-form-login"]/div[2]/div[4]/div[2]/input[1]')
    password.send_keys('12345678')
    # # 提交登录
    driver.find_element('xpath', '//button[contains(@class,"js-login")]').click()
    time.sleep(3)

    # 隐性等待
    # driver.implicitly_wait(10)
    # 退出浏览器
    driver.quit()


def test_youzy():
    login()
