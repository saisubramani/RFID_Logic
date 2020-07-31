class a():
    def __init__(self):
        self.flag = True
        self.limit=10
    def loadcell(self):
        print(self.flag)
        i =0 
        while(self.flag):
            
            if i > self.limit:
                break
            else:
                print(i)
                i=i+1
            
        #self.flag = False

ob = a()
data = ob.loadcell()
