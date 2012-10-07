import numpy as np

class farm:
    def __init__(self, name, entries):
        self.n = name
        self.output = np.zeros((entries, 2))
        
    # def __call__(self, date, out):
    #     print date
    #     self.output.append(np.array([date, out]))
    def fill(self, i, date, out):
        self.output[i] = np.array([date, out])
        
    def __str__(self):
        return self.n + '\n' + str(self.output)

    def get_output(self):
        return self.output

    def output_on_date(self, d):
        for date, out in self.output:
            if date == d:
                return self.out
            
            
    
    
