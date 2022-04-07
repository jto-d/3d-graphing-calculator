import numpy as np

class Equation:

    def __init__(self, equation : str):
        self.equation = equation

        self.equation = self.equation.replace('x', '(x)')
        self.equation = self.equation.replace('y', '(y)')
        # self.equation = self.equation.replace('z', '(z)')
        self.equation = self.equation.replace('^', '**')


        self.x_coords, self.y_coords, self.z_coords = [], [], []

    def get_z_coords(self, x_min, x_max, y_min, y_max, z_min, z_max):
        x_range = np.arange(x_min, x_max+.1, .1)
        y_range = np.arange(y_min, y_max+.1, .1)
        
        for x in x_range:
            for y in y_range:
                

                equation = self.equation
                equation = equation.replace('x', str(x))
                equation = equation.replace('y', str(y))

                z = eval(equation)
                
                if z > z_min and z < z_max:
                    self.x_coords.append(x)
                    self.y_coords.append(y)
                    self.z_coords.append(z)



    def __str__(self):
        return self.equation