# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#
#     @staticmethod
#     def static_method():
#         print(f"Called static_method.")

# example 2 ______________________________________

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if cls.MIN_COORD <= arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x, y):
        return x*x + y*y
