"""
=====================
Author：Tan
Time：2023/3/24 14:49
Project：python学习
=====================
"""
from appium.webdriver import Remote
from selenium.webdriver.common.by import By

caps = {
    'platformName': 'Android',  # 平台
    'deviceName': 'd86bb73c',  # 设备名 在cmd输入adb devices 可查看
    # 'app': r'D:\androidsdk\android-sdk-windows\build-tools\app-debug.apk',  # 安装包路径
    'noReset': True
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
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, 'android.widget.TextView').click()
# driver.find_element(By.ID, 'com.eagersoft.youzy.youzy:id/iv_logo').click()

driver.quit()
