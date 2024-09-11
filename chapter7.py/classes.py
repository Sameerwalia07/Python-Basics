
'''class student:
    def set_name(self, name):
        self.name = name
        
        
    def get_name(self):
        return(self.name)
    
    
student1 = student()
student1.set_name("Sameer Walia")
print(student1.get_name()) 

student2 = student()
student2.set_name("Ekta Walia")
print(student2.get_name())'''



#question 2

class rectangle:
    def set_dimensions( self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        area = self.width * self.height
        return area
    
    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    
    
#creating objects
rectangle1 = rectangle()
width = int(input("Enter the height of rectangle :"))
height = int(input("Enter the width of the rectangle: "))
rectangle1.set_dimensions(height, width)
print("The width and height of rectangle is :", rectangle1.width, rectangle1.height)
print("The area of rectangle is :",rectangle1.area())
print("The perimeter of rectangle is :", rectangle1.perimeter())
        
        
        