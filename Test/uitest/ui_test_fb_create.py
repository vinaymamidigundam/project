"""
 this file is create for flowing operations
"""
from Pageactions.commonfunctions import Create_New_Account
from PageObject.facebook_obj import Facebook_create
import time
import yaml

with open('../TestData/create_creads.yaml', 'r') as file:
    create_creads = yaml.full_load(file)

cfuntion = Create_New_Account()
g_objects = Facebook_create()

cfuntion.open_url('https://www.facebook.com/')
cfuntion.maximize()
time.sleep(3)
cfuntion.click_on_elements(g_objects.createnew_xpath)
time.sleep(3)
cfuntion.click_on_inputs_send_keys(g_objects.firstname_xpath, create_creads['firstname'])
cfuntion.click_on_inputs_send_keys(g_objects.surename_xpath, create_creads['surname'])
cfuntion.click_on_inputs_send_keys(g_objects.mobileno_xpath, create_creads['mobileno'])
cfuntion.click_on_inputs_send_keys(g_objects.newpassword_xpath, create_creads['password'])
cfuntion.click_on_inputs_send_keys(g_objects.day_xpath, create_creads['date'])
cfuntion.click_on_inputs_send_keys(g_objects.mounth_xpath, create_creads['month'])
cfuntion.click_on_inputs_send_keys(g_objects.year_xpath, create_creads['year'])
cfuntion.click_on_elements(g_objects.gender_xpath)

cfuntion.click_on_elements(g_objects.sigin_xpath)
