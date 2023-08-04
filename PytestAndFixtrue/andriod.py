"""
=====================
Author：Tan
Time：2023/3/24 14:49
Project：python学习
=====================
"""
import time

from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui

from PytestAndFixtrue.pressed import Test

caps = {
    'platformName': 'Android',  # 平台
    'deviceName': 'YCPDU17510004756',
    # 设备名 在cmd输入adb devices 可查看   荣耀X30:A8NL6R2106005153  小米:d86bb73c   荣耀6X：YCPDU17510004756
    # 'app': r'D:\androidsdk\android-sdk-windows\build-tools\app-debug.apk',  # 安装包路径
    'noReset': True,
    'platformVersion': '8.0.0'  # 安卓手机版本
}
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)


# caps = {
#     'platformName': 'Android',  # 平台
#     'deviceName': 'BRNUT21B15032048',  # 设备名 在cmd输入adb devices 可查看
#     'appPackage': 'com.eagersoft.youzy.youzy',  # 配置aapt环境变量，然后输入aapt dump badging 包名路径 命令查看包名和activity
#     'appActivity': 'com.eagersoft.youzy.youzy.mvvm.ui.launch.LaunchActivity'
# }
# driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)

# 等待
# driver.implicitly_wait(10)


def psychology_evaluation():
    for f in range(44):
        if f == 43:
            break
        else:
            # driver.find_element(By.ID, 'com.eagersoft.youzy.youzy:id/click_parent').click()

            wait = ui.WebDriverWait(driver, 5)
            wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@text="中等"]'))
            driver.find_element(By.XPATH, '//*[@text="中等"]').click()


def learning_evaluation():
    for j in range(163):
        if j == 162:
            break
        else:
            driver.find_element(By.ID, 'com.eagersoft.youzy.youzy:id/tv_name').click()


def orientation_evaluation():
    for k in range(1200):
        if k == 1200:
            break
        else:
            driver.find_element(By.ID, 'com.eagersoft.youzy.youzy:id/simpleTransitionButton').click()
            driver.implicitly_wait(5)


def intelligence_evaluation():
    for f in range(61):
        if f == 59:
            break
        else:
            # driver.find_element(By.ID, 'com.eagersoft.youzy.youzy:id/click_parent').click()

            wait = ui.WebDriverWait(driver, 5)
            wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@text="4"]'))
            driver.find_element(By.XPATH, '//*[@text="4"]').click()


def swipe_huadong():
    size = driver.get_window_size()
    height = size["height"]
    width = size["width"]
    driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5)
    time.sleep(3)

    size = driver.get_window_size()
    height = size["height"]
    width = size["width"]
    driver.swipe(width * 0.1, height * 0.5, width * 0.9, height * 0.5)


def install():
    # 如果存在app删除，不存在则安装
    if driver.is_app_installed('com.eagersoft.youzy.youzy'):
        driver.remove_app('com.eagersoft.youzy.youzy')
        driver.install_app('D:/android APK/com.eagersoft.youzy.youzy_8.4.0_liqucn.com.apk')
    else:
        driver.install_app('D:/android APK/com.eagersoft.youzy.youzy_8.4.0_liqucn.com.apk')


def swipe_huadong2():
    driver.find_element(By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.TextView').click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[3]').click()


# 手机屏幕九宫格解锁
def unlock():
    size = driver.get_window_size()
    height = size["height"]
    width = size["width"]
    driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1)
    time.sleep(1)

    el = driver.find_element(By.ID, 'com.android.systemui:id/lockPatternView')
    action = el.rect
    start_x = action['x']
    start_y = action['y']
    width = action['width']
    height = action['height']

    position_1 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 6}
    position_2 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 1 / 6}
    position_3 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 6}
    position_4 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 1 / 2}
    position_5 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 1 / 2}
    position_6 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 1 / 2}
    position_7 = {'x': start_x + width * 1 / 6, 'y': start_y + height * 5 / 6}
    position_8 = {'x': start_x + width * 1 / 2, 'y': start_y + height * 5 / 6}
    position_9 = {'x': start_x + width * 5 / 6, 'y': start_y + height * 5 / 6}

    touch = TouchAction(driver)
    touch.press(**position_1).move_to(**position_2).move_to(**position_3).move_to(
        **position_5).move_to(**position_7).move_to(**position_8).move_to(
        **position_9).release().perform()

    # touch.press(x=start_x + width * 1 / 6, y=start_y + height * 1 / 6).move_to(x=start_x + width * 1 / 2, y=start_y + height * 1 / 6).move_to(
    #     x=start_x + width * 5 / 6, y=start_y + height * 1 / 6).release().perform()

    time.sleep(1)


# 根据keycode实现对按键的控制
# https://www.jianshu.com/p/f7ec856ff56f
def pressed13():
    driver.press_keycode(4)


# 多点触控 放大缩小屏幕
def ddck():
    fd = TouchAction(driver)
    fd1 = TouchAction(driver)
    action = driver.get_window_size()
    width = action['width']
    height = action['height']

    fd.press(x=width / 2, y=height / 2).move_to(x=width / 2, y=height * 2).release()
    fd1.press(x=width / 2, y=height / 2).move_to(x=width / 2, y=height * 0.125).release()
    m = MultiAction(driver)
    m.add(fd, fd1)
    m.perform()


def test_evaluation():
    # psychology_evaluation()  # 心理测评
    # learning_evaluation()  # 学习能力测评
    # intelligence_evaluation()  # 智力测评
    # orientation_evaluation()  # 专业定位五合一测评
    # swipe_huadong()  # 左右滑动切换效果
    # swipe_huadong2()  # 通过Xpath 点击切换效果
    # print("包名:{}".format(driver.current_package))
    # print("界面名:{}".format(driver.current_activity))
    # driver.start_activity('com.eagersoft.youzy.youzy', '.mvvm.ui.main.Main') # 跳转其他应用
    # install()  # 如果存在app删除，不存在则安装
    # unlock()  # 手机屏幕九宫格解锁
    # pressed()  # 根据keycode实现对按键的控制

    # tt = Test()
    # driver.press_keycode(tt.my_name) # 调用工具类变量

    ddck()  # 多点触控 放大缩小屏幕

    # driver.quit()
