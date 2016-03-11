import  threading
import time
class refresh(threading.Thread):

    def __init__(self, name=''):
        threading.Thread.__init__(self, name=name)


    def run(self):

        while True:
            try:
                #########
                time.sleep(3)
            except:
                break



class new_window(threading.Thread):

    def __init__(self, func, name=''):
        threading.Thread.__init__(self, name=name)
        self.func = func

    def run(self):
        self.func()


#need to complete