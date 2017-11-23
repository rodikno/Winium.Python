from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        'app': r'C:\_executables\PortWin\Debug\PortWin.Client.Win.exe'
    })

time.sleep(3)
#Alt+Down -> down -> Enter
driver.find_element_by_name('Autentisering')

# Logging in

#Selecting EVRY user
driver.find_element_by_id('lueUser').send_keys('Evry')
driver.find_element_by_id('lueUser').click()
#Selecting test Bank
driver.find_element_by_id('lueCorporation').send_keys('Evry Testbank')
driver.find_element_by_id('lueCorporation').click()
#Typing password in
driver.find_element_by_id('txtPassword').send_keys('6150')
#Click on login button
driver.find_element_by_id('btnLogin').click()

#NEW SECTION
driver.find_element_by_id('teContractRefDirectSearch').click()
time.sleep(2)
#driver.find_element_by_name('Portefølje').click()
driver.find_element_by_name('IRS').click()

driver.close()


#click on ID lueCorporation
# send keys Evry Testbank
# click with mouse
#click name Portefølje
#click name IRS

# if passwordfield:
#     print('Password field is located')
# else:
#     print('Password field is NOT located')
# menu_bar.click()
# menu_bar.find_element_by_name('File').click()
# menu_bar.find_element_by_name('New').click()
# menu_bar.find_element_by_name('Project...').click()
#
# project_name = 'SpecialForHabrahabr-' + str(time.time())
# new_project_win = window.find_element_by_name('New Project')
# new_project_win.find_element_by_id('Windows Desktop').click()
# new_project_win.find_element_by_name('Console Application').click()
# new_project_win.find_element_by_id('txt_Name').send_keys(project_name)
# new_project_win.find_element_by_id('btn_OK').click()
#
# text_view = window.find_element_by_id('WpfTextView')
# text_view.send_keys('using System;{ENTER}{ENTER}')
#
# actions = ActionChains(driver)
# actions.send_keys('namespace Habrahabr{ENTER}')
# actions.send_keys('{{}{ENTER}')
# actions.send_keys('class Program{ENTER}')
# actions.send_keys('{{}{ENTER}')
# actions.send_keys('static void Main{(}string{[}{]} args{)}{ENTER}')
# actions.send_keys('{{}{ENTER}')
# actions.send_keys('Console.WriteLine{(}\"Hello Habrahabr\"{)};')
#
# actions.send_keys('^{F5}')
# actions.perform()d_element_by_id('MyTextBox').text