from selenium import webdriver
from time import sleep
import getpass
import sys
import random
import string
import io
from PIL import Image
import requests
from io import BytesIO

class TinderBot:
  def __init__(self):
    self.driver = webdriver.Chrome()

  def login(self, two_fa):
    self.driver.get('https://tinder.com')

    sleep(5)

    fb_btn = self.driver.find_element_by_xpath(
        '//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
    fb_btn.click()

    # select popup window
    base_window = self.driver.window_handles[0]
    self.driver.switch_to_window(self.driver.window_handles[1])

    # input email/username
    email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
    username = getpass.getpass('please input username\n')
    email_input.send_keys(username)

    # input password
    password_input = self.driver.find_element_by_xpath('//*[@id="pass"]')
    password = getpass.getpass('please input password\n')
    password_input.send_keys(password)

    sleep(3)

    login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
    login_btn.click()

    # if you use 2FA for fb
    if(two_fa):

        # input code
        code_input = self.driver.find_element_by_xpath('//*[@id="approvals_code"]')
        input_digits = getpass.getpass("please input code\n")
        code_input.send_keys(input_digits)

        continue_btn = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        continue_btn.click()

        # select don't save
        not_save_check = self.driver.find_element_by_xpath('//*[@id="u_0_3"]')
        not_save_check.click()

        # click continue button
        second_continue_btn = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        second_continue_btn.click()

    # for loading tinder web app
    sleep(10)

    # switch back to main window
    self.driver.switch_to_window(base_window)

    popup_1 = self.driver.find_element_by_xpath(
        '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    popup_1.click()
    popup_2 = self.driver.find_element_by_xpath(
        '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    popup_2.click()

    sleep(5)

  # swipe right
  def like(self):
      like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
      like_btn.click()

  # swipe left
  def not_like(self):
      not_like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
      not_like_btn.click()

  def close_popup(self):
      popup = self.driver.find_element_by_xpath(
          '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
      popup.click()

  def close_match(self):
      popup = self.driver.find_element_by_xpath(
          '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
      popup.click()

  def close_home(self):
      popup = self.driver.find_element_by_xpath(
          '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
      popup.click()

  def not_pay(self):
      popup = self.driver.find_element_by_xpath(
          '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
      popup.click()
      print('cannot swipe any more')
      print('will finish the program')

  def randomString(self, stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

  def take_screenshot(self):
      filename = self.randomString()+'.png'
      image = self.driver.find_element_by_xpath(
          '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div')
      image_url = image.value_of_css_property("background-image")
      raw_url = image_url.replace('url("', '').replace('")', '')
      # get webp
      # convert webp --> png
      resp = requests.get(raw_url)
      im = Image.open(BytesIO(resp.content)).convert("RGB")
      im.save(filename, "png")

  def auto_swipe(self, debug):
      while True:
        sleep(1)
        rand = random.random()
        if rand > 0.5:
          try:
            if debug:
              print('swipe like')
            self.take_screenshot()
            self.like()
          except Exception:
            try:
              self.close_popup()
            except Exception:
              try:
                  self.close_match()
              except Exception:
                  try:
                      self.close_home()
                  except Exception:
                      self.not_pay()
                      driver.close()
                      break
        else:
          if debug:
            print('swipe not like')
          self.not_like()

