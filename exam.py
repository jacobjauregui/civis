class Calculator:
    def __init__(self, number):
        self.n = number
        self.data = [0 for i in range(number)]

    def add(self, number):
       self.data = [int(input('Enter a number: '+ str(i+1) + '= ')) for i in range(self.n)]

class basics(Calculator):
    def __init__(self, number):
        Calculator.__init__(self, number)
    
        
    def suma(self):
        a,b = self.data
        s = a + b
        print('The sum is: ', s)
    
    
    def resta(self):
        a,b = self.data
        r = a - b
        print('The rest is: ', r)