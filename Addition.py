class Addition:
    def __init__(self):
        print("Addition object created")
        
    def operation(self, a, b):
        res = int(a)+int(b)
        print("Addition:" + str(res))