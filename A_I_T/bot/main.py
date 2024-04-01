from config.data import urls, locators, strings, date_of_birth_elements, email_elements, posts, acc_names
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common import action_chains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config.wordlist import name_list
from random import choices,randint
from urllib.error import HTTPError
from seleniumbase import Driver 
from config.data import nums
import logging
import os

class web_driver:
    def __init__(self):
        self.driver = None
    
    def start_driver(self):
        self.driver = Driver(uc=True)

    def start_browser(self):
        while nums.retries < nums.max_retries:
            try:
                self.driver.get(urls.sign_up_url)
                WDW(self.driver, 10).until(EC.url_to_be(urls.sign_up_url))
                break 
            except HTTPError as err:
                if err.code != 200:
                    logging.error(f"HTTP error occurred: {err}")
                    logging.info(f"Retrying in {nums.retry_delay} seconds...")
                    nums.retry_delay = self.fibonacci(nums.retry_delay)
                    nums.retries += 1
    
    def authorization(self):
        # name ✅
        try:
            for i in choices(name_list.list_of_names):
                self.name_value = i
                for j in range(1):
                    self.user_num = j
                    self.concat_value = self.name_value 
                    self.var = str(randint(self.user_num,1000))
                    self.driver.find_element(
                    By.XPATH,locators.name_xpath).send_keys(self.name_value)
                    break
                break
        except ElementNotInteractableException as err:
            logging.error(err)
            
                

        #username ✅
        try:
            for j in range(1):
                username_num = j
                self.user_number = randint(int(username_num),10000)
                self.full_username = self.name_value + str(self.user_number)
                self.driver.find_element(By.XPATH,locators.username_xpath).send_keys(self.full_username)
                break
        except ElementNotInteractableException as err:
            logging.error(err)


        # password ✅
        try:
            self.driver.find_element(
                By.XPATH,locators.password_xpath).send_keys(strings.password)
        except NoSuchElementException as err:
            logging.error(err)
        # retype password ✅
        try:
            self.driver.find_element(
                By.XPATH,locators.retype_password_xpath).send_keys(strings.password)
        except NoSuchElementException as err:
            logging.error(err)
        
    
    def credentials(self):
        # email ✅
        try:
            for j in choices(email_elements.email_list):
                    username_email = self.name_value
                    user_email = j
                    full_email = username_email + str(self.user_number) + str(user_email)
                    added_email = full_email

                    self.driver.find_element(
                    By.XPATH,locators.email_xpath).send_keys(full_email)
                    added_email = full_email
                    break
        except ElementNotInteractableException as err:
            logging.error(err)


        # retype email ✅
        try:
            self.driver.find_element(
            By.XPATH,locators.retype_email_xpath).send_keys(added_email)
        except ElementNotInteractableException as err:
            logging.error(err)

      
    
    def geolocation(self):
        # country ✅
        try:
            self.driver.find_element(
                By.XPATH,locators.country_xpath).send_keys(strings.country)
        except NoSuchElementException as err:
            logging.error(err)


        
    
    def date_of_birth(self):
        # day ✅
        
        try:
            day_value = randint(1,28)
            self.driver.find_element(
                By.XPATH,locators.day_xapth).send_keys(day_value)
        except ElementNotInteractableException as err:
            logging.error(err)
        

        # month ✅
        try:
            for month_value in choices(date_of_birth_elements.month_list):
                try:
                    self.driver.find_element(
                        By.XPATH,locators.month_xpath).send_keys(month_value)
                except ElementNotInteractableException as err:
                    logging.error(err)
        except ElementNotInteractableException as err:
            logging.error(err)

        # year ✅
        try:
            year_value = randint(1990,2000)
            self.driver.find_element(
                By.XPATH,locators.year_xpath).send_keys(year_value)
        except ElementNotInteractableException as err:
            logging.error(err)

        
    def terms_and_conditions(self):
        # terms ✅
        try:
            self.driver.execute_script("window.scrollBy(0, 750);")
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.terms_and_conditions_xpath
                )))
            self.driver.find_element(By.XPATH,locators.terms_and_conditions_xpath).click()
            
        except ElementNotVisibleException and JavascriptException as err:
            logging.error(err)
        
    
    def register(self):
        # register user ✅
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.register_btn_xpath
                )))
            self.driver.find_element(By.XPATH,locators.register_btn_xpath).click()
        except ElementNotVisibleException as err:
            logging.error(err)
    
    def rumble_logo(self):
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.rumble_logo_xpath
                )))
            self.driver.find_element(
                By.XPATH,locators.rumble_logo_xpath).click()
        except NoSuchElementException as err:
            logging.error(err)
    
    def search_bar(self):
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.search_bar_xpath
            )))
            import traceback
            for i in choices(acc_names.acc_name):
                self.driver.find_element(
                By.XPATH, locators.search_bar_xpath).send_keys(i)
                break
            actions = AC.ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        except NoSuchElementException as err:
            traceback.print_exc(limit=None,file=None,chain=True)
            logging.error(err)

    def profile_select(self):
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,strings.profile_xpath
            )))
            self.driver.find_element(
                By.XPATH,strings.profile_xpath).click()
        except NoSuchElementException as err:
            logging.error(err)

    def follow_acc(self):
        try:
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.follow_btn_xpath
            )))
            self.driver.find_element(
                By.XPATH,locators.follow_btn_xpath).click()
        except NoSuchElementException as err:
            logging.error(err)
    
    def like_posts(self):
        for i in posts.post_dict:
            value = posts.post_dict[i]
            self.driver.find_element(By.XPATH,value).click()
            WDW(
                self.driver,10).until(
                    EC.presence_of_element_located((
                        By.XPATH,locators.like_btn_xpath
                    )))
            self.driver.find_element(By.XPATH,locators.like_btn_xpath).click()
            break

    








    def account_logs(self):
        try:
            file_data = 'text'
            logs_directory = '/Users/administrator/Desktop/Projects/SeleniumProjects/test_linkedlist_/logs'
            file_path = os.path.join(logs_directory,'logs.txt')
            with open(file_path, 'w') as file:
                file.writelines(file_data)
        except IOError as err:
            logging.error(err)

    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            sequence = [0, 1]
            for i in range(2, n):
                random_increment = randint(1, 5)
                next_number = sequence[-1] + sequence[-2] + random_increment
                sequence.append(next_number)
            return sequence
    n = 10  
    fibonacci_sequence = fibonacci(n)

    def close_browser(self):
        self.driver.quit()