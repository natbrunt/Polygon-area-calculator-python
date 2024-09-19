class Rectangle:
    def __init__(self, *args):
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        if len(args) == 2:
            self.width = args[0]
            self.height = args[1]
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,_width):
        self.width = _width
    
    def set_height(self,_height):
        self.height = _height
    
    def get_area(self):
        return self.width* self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        # create a multi line string
        my_shape = ""
        i = 0 
        while i < self.height:
            row = ""
            for _ in range(self.width):
                row += "*"
            my_shape += row + "\n"
            i += 1
        return my_shape
    
    def get_amount_inside(self,shape):
        area_b = self.width * self.height
        area_a = shape.width * shape.height

        if area_a <= area_b:
            return area_b // area_a  
            # Integer division to get the maximum number of full fits
        else:
            return 0  
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side)
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, _side):
        self.width = _side
        self.height = _side
    
    def set_width(self,_width):
        self.width = _width
        self.height = _width
    
    def set_height(self,_height):
        self.height = _height
        self.width = _height

rect = Rectangle(15,10)
sq = Square(5)
print(rect)
print(rect.get_picture())
print(sq)
print(sq.get_picture())
