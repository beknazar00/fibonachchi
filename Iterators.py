class Fibonachchi:
    def __init__(self,step):
        self.a = 0
        self.b = 1
        self.step = step

    def __next__(self):
        if self.step < 0:
            print('iltimos musbat son kiriting 😊')
        elif self.step == 1:
            print('yo yo yo yo qaytar qaytat...')
            print(self.a)
        else:
            print('fibonachchi ketma ketligi')
            count = 0
            while self.step > count:
                print(self.a)
                result = self.a + self.b
                self.a = self.b
                self.b = result
                count += 1    
    
step = int(input('Enter a number; '))
fibo = Fibonachchi(step)
fibo.__next__()