import os
import sys
import numpy
import pandas

def hello(Name:str, age:int)->str:
    """
    brief description of how the package works and introduce thee user

    This docstring provides a more detailed description of the function, its
    parameters, return value, and any additional information that might be
    useful.

    Args:
        Name(str): The name of the user of the package
        Age(int): The age of the user
    
    Returns:
        Welcome the user and tell us how old he/she is
    
    Raises:
        ValueError: if the age of the user is negative 

    """
    if age<0:
        raise ValueError('Age cannot be negative value')
    
    return(f'hello {Name}, your age is {age}')

def DeltaCT(CT_Sample:float,CT_Ctrl:float)->float:
    """ This is a function to calculate the DeltaCT

    Args:
        CT_Sample (float): The mean of the CT value for the sample or experimental group
        CT_Ctrl (float): The mean of the CT value for the control group

    Returns:
        float: DeltaCT
    Raises:
        ValueError: The CT value is out of range 
    """    """
    """
    if CT_Ctrl>30:
        raise ValueError('The CT value is out of range')
    elif CT_Sample>30:
        raise ValueError('The CT value is out of range')
    return CT_Sample-CT_Ctrl    

print(hello('ccc', 18))
print(DeltaCT(25,21))
