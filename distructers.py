#create class
class employee:
    #initializing
    def __init__(self):
        print('employee created')
    #calling distructer
    def __del__(self):
        print("distructer called")
    def create_obj():
        print('making object...')
        obj = employee()
        print('function end ...')
        return obj
    print('calling create_obj( function...)')
    obj = crete_obj()
    print('program end ...')       