# A.I.T
from bot.main import web_driver
from config.data import nums
from time import sleep

class node:
    def __init__(self,data=None):
        self.data = data
        self.pointer = None
    
    def activate(self):
        for i in range(nums.iterations):
            func = web_driver()
            func.start_driver()
            func.start_browser()
            func.authorization()
            func.credentials()
            func.geolocation()
            func.date_of_birth()
            func.terms_and_conditions()
            func.register()
            sleep(25)
            func.rumble_logo()
            func.search_bar()
            func.profile_select()
            func.follow_acc()
            sleep(3)
            func.like_posts()
            sleep(3)
            func.close_browser()
            print(f'Executions: {i}')

    
class linked_list:
    def __init__(self):
        self.head: node = None
    
    def add_node(self,new_node):
        if not self.head:
            self.head = new_node
        else:
            current_node = new_node
            while current_node.pointer:
                current_node = current_node.pointer
            current_node.pointer = new_node

def quit_driver():
    print("Exiting gracefully...")
    func = web_driver()
    if func.driver is not None:
        func.close_browser()
    exit(0)


if __name__ == "__main__":
    instance = linked_list()
    instance.add_node(node(data=0))
    current_node = instance.head
    try:
        while current_node:
            for i in range(nums.num_nodes):
                current_node.activate()
            current_node = current_node.pointer
    except KeyboardInterrupt:
        quit_driver()