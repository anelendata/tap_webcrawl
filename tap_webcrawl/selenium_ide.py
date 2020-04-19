# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()

  def test_untitled(self):
    self.driver.get("https://nces.ed.gov/ccd/schoolsearch/school_list.asp?Search=1&InstName=&SchoolID=&Address=&City=&State=01&Zip=&Miles=&County=&PhoneAreaCode=&Phone=&DistrictName=&DistrictID=&SchoolType=1&SchoolType=2&SchoolType=3&SchoolType=4&SpecificSchlTypes=all&IncGrade=-1&LoGrade=-1&HiGrade=-1")
    # self.driver.get("https://nces.ed.gov/ccd/schoolsearch/school_list.asp?Search=1&InstName=&SchoolID=&Address=&City=&State=25&Zip=&Miles=&County=Plymouth&PhoneAreaCode=&Phone=&DistrictName=Abington&DistrictID=&SchoolType=1&SchoolType=2&SchoolType=3&SchoolType=4&SpecificSchlTypes=all&IncGrade=-1&LoGrade=-1&HiGrade=-1")
    self.driver.set_window_size(1680, 961)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".excelclass").click()
    self.vars["win9317"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win9317"])
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) a > font").click()