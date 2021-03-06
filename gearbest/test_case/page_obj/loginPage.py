from selenium.webdriver.common.by import By
from .base import BasePage
from time import sleep


class Login(BasePage):

    # 登录用户名的定位
    login_username_loc = (By.ID, 'email')
    # 登录密码的定位
    login_password_loc = (By.ID, 'password')
    # 登录按钮的定位
    login_button_loc = (By.ID, 'js-btnSubmit')
    # 登录错误提示的定位
    login_error_loc = (By.CSS_SELECTOR, "div.authForm_item>p")
    # 登录成功用户名信息
    login_user_success_loc = (By.CLASS_NAME, 'siteHeader_userAccountLink')

    # 登录页面
    url = "https://login.gearbest.com/m-users-a-sign.htm?type=1"
    title = "Sign In | GearBest.com"

    def __init__(self, selenium_driver):
        BasePage.__init__(self, selenium_driver, self.url,self.title)

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, username="testuser01", password="testgood001"):
        # 获取用户名和页面登录
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    # 登录错误提示信息
    def login_error_hint(self):
        return self.find_element(self.login_error_loc).text

    # 登录成功用户名信息
    def login_user_success(self):
        username = self.find_element(*self.login_user_success_loc).text
        username = username.strip('您好：')
        return username
