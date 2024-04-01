from config.data import email_elements, date_of_birth_elements
from config.wordlist import name_list
from random import choices,randint

class unit_test:
        
        def test_function(self):
            # test
            for i in choices(name_list.list_of_names):
                self.name_value_get = i
                print(self.name_value_get)
                print('\n')
                break

        def test_function1(self):
            # name
            for i in choices(name_list.list_of_names):
                self.username_value = i
                for j in range(1):
                    self.user_num = j
                    self.concat_value = self.name_value_get 
                    self.var = str(randint(self.user_num,1000))
                    print(self.concat_value + self.var)
                    break
                break
                

        def test_function2(self):
            # username
            
            for j in range(1):
                username_num = j
                self.user_number = randint(int(username_num),1000)
                full_username = self.name_value_get + str(self.user_number)
                print('\n')
                print(full_username)
                break
                

        def test_function3(self):
                # email
                for j in choices(email_elements.email_list):
                    username_email = self.username_value
                    user_email = j
                    full_email = self.name_value_get + str(self.var) + str(user_email)
                    added_email = full_email
                    break
                print('\n')
                print(added_email)

        @staticmethod
        def test_function4():
            # dob
            year = randint(1990,2001)
            day = randint(1,31)
            for month in choices(date_of_birth_elements.month_list):
                break
            print('\n')
            print(year)
            print('\n')
            print(day)
            print('\n')
            print(month)



if __name__ == "__main__":
     func = unit_test()
     func.test_function()
     func.test_function1()
    # func.test_function2()
     func.test_function3()
    # func.test_function4()