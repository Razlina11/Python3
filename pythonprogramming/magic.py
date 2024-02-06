class message:
    def __init__(self,msg):  #magic method
        self.msg=msg
    def __repr__(self):     #for representation
        return 'object:{}'.format(self.msg)
    def __add__(self,other):    #concatenate
        return self.msg+other
        

if __name__=='__main__':
    obj=message("hello")
    print(obj+"World")


