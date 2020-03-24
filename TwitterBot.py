from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.user = username
        self.pwd = password
        self.bot = webdriver.Chrome()

    def login(self, tweet_data):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')

        email.clear()
        password.clear()

        email.send_keys(self.user)
        password.send_keys(self.pwd)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        tweet_box_XPATH= '//*[@id="react-root"]/div/div/div[2]/main/'\
                         'div/div/div/div[1]/div/div[2]/div/div[2]/div[1]'\
                         '/div/div/div/div[2]/div[1]/div/div/div/div/div/div'\
                         '/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        tweet_box = bot.find_element_by_xpath(tweet_box_XPATH)
        tweet_box.clear()
        tweet_box.send_keys(tweet_data)

        tweet_box_tweet_button_XPATH = '//*[@id="react-root"]/div/div/div[2]'\
                                     '/main/div/div/div/div[1]/div/div[2]/div/div[2]'\
                                     '/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]'
        tweet_button = bot.find_element_by_xpath(tweet_box_tweet_button_XPATH)
        tweet_button.click()

opj = TwitterBot('YOUR USERNAME OR EMAIL','PASSWORD')
opj.login()
