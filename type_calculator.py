import sys
from copy import deepcopy

from type_names import *
from type_dicts import *


def calculate_ineffective_against(type: str):
    validate_type(type)
    print(f'Type {type} is ineffective against: {ineffective_against[type]}')

def calculate_super_effective_against(type: str):
    validate_type(type)    
    print(f'Type {type} is super effective against: {super_effective_against[type]}')

def calculate_not_very_effective_against(type: str):
    validate_type(type)
    print(f'Type {type} is not very effective against: {not_very_effective_against[type]}')

def calculate_weak_to(type: str):
    validate_type(type)
    weak_to = compile_weak_to()
    print(f'Type {type} is weak to: {weak_to[type]}')

def calculate_strong_to(type: str):
    validate_type(type)
    strong_to = compile_strong_to()
    print(f'Type {type} is strong to: {strong_to[type]}')

def calculate_immune_to(type: str):
    validate_type(type)
    immune_to = compile_immune_to()
    print(f'Type {type} is immune to: {immune_to[type]}')


# Helper Methods
def validate_type(type: str):
    if (type not in type_tuple):
        print(f'Type {type} not supported!')
        exit() 

def compile_weak_to():
    weak_to = deepcopy(DEFAULT_TYPE_DICT)

    for type in type_tuple:
        for type_super_effective_against in super_effective_against[type]:
            weak_to[type_super_effective_against].add(type)
    
    return weak_to

def compile_strong_to():
    strong_to = deepcopy(DEFAULT_TYPE_DICT)

    for type in type_tuple:
        for type_not_very_effective_against in not_very_effective_against[type]:
            strong_to[type_not_very_effective_against].add(type)
    
    return strong_to

def compile_immune_to():
    immune_to = deepcopy(DEFAULT_TYPE_DICT)

    for type in type_tuple:
        for type_ineffective_against in ineffective_against[type]:
            immune_to[type_ineffective_against].add(type)
    
    return immune_to

def calculate_type_summary(type: str):
    calculate_ineffective_against(type)
    calculate_super_effective_against(type)
    calculate_not_very_effective_against(type)
    calculate_weak_to(type)
    calculate_strong_to(type)
    calculate_immune_to(type)

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")

    if (len(sys.argv) > 1):
        type = sys.argv[1].upper()
        if type in type_tuple:
            calculate_type_summary(type)
        else:
            print(f"ERROR: type {type} is not a supported type!")

    else:
        for type in type_tuple:
            calculate_type_summary(type)
            print('-----------------------------------')
