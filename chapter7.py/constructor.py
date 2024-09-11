
class rectangle :
    
    
    def __init__(self, height, width):
        
         print(f"The height and width of recatangle is height: {height} and width: {width}")
         self.height = height
         self.width = width
         
    def set_dimensions(self, height, width):
        self.height = height
        self.width = width
    
        
    def area(self):
        area = self.height * self.width
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.height + self.width)
        return(perimeter)
    
#creating objects

rectangle1 = rectangle(4, 3)
rectangle2 = rectangle(4, 7)
rectangle3 = rectangle(7, 9) 

