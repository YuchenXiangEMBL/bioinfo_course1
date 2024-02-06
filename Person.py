import os
import sys
import numpy
import pandas

class Person:
    def __init__(self,name:str,age:int) -> None:
        """Constructor method to initialize attributes."""
        self.name=name
        self.age=age
    def greet(self):
        """methods to greet person
        """        
        print(f'hello, my name is {self.name} and I am {self.age} years old')

Alice=Person('Alice',24)
Bob=Person('Bob',30)

Alice.greet()
Bob.greet()