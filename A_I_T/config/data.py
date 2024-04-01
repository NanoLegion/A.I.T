from dataclasses import dataclass

class urls:
    sign_up_url: str = 'https://rumble.com/register.php'

class nums:
    iterations: int = 3
    node_data: int = 0
    max_retries:int = 3 
    num_nodes: int = 50
    retry_delay: int = 0 
    retries: int = 0

class output_file:
    file_name: str = 'logs.txt'

class strings:
    password: str = 'superman2350'
    country:str = 'United States'
    profile_xpath: str = '/html/body/main/div/div/div[1]/div/ol/li/a'

class date_of_birth_elements:
    month_list = [
        'January','February','March','April',
        'May','June','July','August','September',
        'October','November','December',
    ]

class acc_names:
    acc_name = [
        'LeoVenice','WillCatonJr',
        'LGrady90','RiverSoundsInc'
        ]

@dataclass
class posts:
    post_dict = {
    1:'/html/body/main/section/ol/div[1]/div[1]/a',
    2:'/html/body/main/section/ol/div[2]/div[1]/a',
    3:'/html/body/main/section/ol/div[3]/div[1]/a',
    4:'/html/body/main/section/ol/div[4]/div[1]/a',
    5:'/html/body/main/section/ol/div[5]/div[1]/a',
    6:'/html/body/main/section/ol/div[6]/div[1]/a',
    }
    post_dict_2 = {
    7:'/html/body/main/section/ol/div[7]/div[1]/a',
    8:'/html/body/main/section/ol/div[8]/div[1]/a',
    9:'/html/body/main/section/ol/div[9]/div[1]/a',
    10:'/html/body/main/section/ol/div[10]/div[1]/a',
    11:'/html/body/main/section/ol/div[11]/div[1]/a',
    12:'/html/body/main/section/ol/div[12]/div[1]/a',
    13:'/html/body/main/section/ol/div[13]/div[1]/a',
    14:'/html/body/main/section/ol/div[14]/div[1]/a',
    15:'/html/body/main/section/ol/div[15]/div[1]/a',
    16:'/html/body/main/section/ol/div[16]/div[1]/a',
    }


class email_elements:
    email_list = [
        '@protonmail.com','@gmail.com','@yahoo.com','@mailfence.com',
        '@msn.com','@hotmail.com','@aol.com','@outlook.com',
    ]
@dataclass
class locators:
    name_xpath: str = '//*[@id="name"]'
    username_xpath: str = '//*[@id="username"]'
    password_xpath: str = '//*[@id="password"]'
    retype_password_xpath: str = '//*[@id="retype_password"]'
    email_xpath: str = '//*[@id="email"]'
    retype_email_xpath: str = '//*[@id="retype_email"]'
    country_xpath: str = '/html/body/main/div/div/div[1]/section/div[2]/div/div/form/div[2]/ul/li[7]/span/select'
    day_xapth: str = '//*[@id="birthday-day"]'
    month_xpath: str = '//*[@id="birthday-month"]'
    year_xpath: str = '//*[@id="birthday-year"]'
    search_bar_xpath: str = '/html/body/header/div/form/input'
    rumble_logo_xpath: str = '/html/body/header/div/a'
    terms_and_conditions_xpath: str = '/html/body/main/div/div/div[1]/section/div[2]/div/div/form/ul/li[2]/span/div/label'
    register_btn_xpath: str = '//*[@id="registerBtn"]'
    like_btn_xpath: str = '/html/body/main/article/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/button[1]'
    follow_btn_xpath: str = '/html/body/main/div/div[1]/div/div/div[3]/div/button[1]'


