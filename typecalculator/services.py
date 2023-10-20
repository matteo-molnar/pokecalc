import json

from copy import deepcopy

from typecalculator.types import *


def calculate_ineffective_against(type: str):
    validate_type(type)
    return f"Type {type} is ineffective against: {ineffective_against[type]}"


def calculate_super_effective_against(type: str):
    validate_type(type)
    return f"Type {type} is super effective against: {super_effective_against[type]}"


def calculate_not_very_effective_against(type: str):
    validate_type(type)
    return (
        f"Type {type} is not very effective against: {not_very_effective_against[type]}"
    )


def calculate_weak_to(type: str):
    validate_type(type)
    weak_to = compile_weak_to()
    return f"Type {type} is weak to: {weak_to[type]}"


def calculate_strong_to(type: str):
    validate_type(type)
    strong_to = compile_strong_to()
    return f"Type {type} is strong to: {strong_to[type]}"


def calculate_immune_to(type: str):
    validate_type(type)
    immune_to = compile_immune_to()
    return f"Type {type} is immune to: {immune_to[type]}"


def calculate_summary():
    output = {}
    for type in type_tuple:
        output[type] = {}
        output[type]["ineffective_against"] = calculate_ineffective_against(type)
        output[type]["super_effective_against"] = calculate_super_effective_against(
            type
        )
        output[type][
            "not_very_effective_against"
        ] = calculate_not_very_effective_against(type)
        output[type]["weak_to"] = calculate_weak_to(type)
        output[type]["strong_to"] = calculate_strong_to(type)
        output[type]["immune_to"] = calculate_immune_to(type)
    return json.dumps(output)


# Helper Methods
def validate_type(type: str):
    if type not in type_tuple:
        print(f"Type {type} not supported!")
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
