class Rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        response = ""
        for i in range(self.height):
            response += f"{'*' * self.width}\n"
        return response

    def get_amount_inside(self, otherObj):
        return self.get_area() // otherObj.get_area()

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __repr__(self):
        return f"Square(side={self.height})"


