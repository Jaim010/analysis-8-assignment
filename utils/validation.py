from typing import Callable, List
import re

class __bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Result:
    
    valid: bool
    message: str
    
    def __init__(self, valid: bool, message: str) -> None:
        self.valid = valid
        self.message = message
        
class InvalidResult(Result):
    
    def __init__(self, message: str) -> None:
        super().__init__(False, message)
        
class ValidResult(Result):
    
    def __init__(self) -> None:
        super().__init__(True, "")

def get_user_input(question: str, validators: List[Callable[[str], Result]]) -> str:
    print()
    user_input = input(question)
    
    for validator in validators:
        result = validator(user_input)
        
        if not result.valid:
            print(f"{__bcolors.FAIL}{result.message}{__bcolors.ENDC}")
            
            return get_user_input(question, validators)
    
    return user_input

def check_length(min_length: int = 0, max_length: int = 20):
    def validator(input: str) -> Result:
        if len(input) < min_length:
            return InvalidResult("The input you entered is too short.")
        
        if len(input) > max_length:
            return InvalidResult("The input you entered is too long.")
        
        return ValidResult()
    
    return validator

def check_format(regex: str):
    def validator(input: str) -> Result:
        if re.fullmatch(regex, input) == None:
            return InvalidResult("The input does not match the format.")
        
        return ValidResult()
    
    return validator

def check_options(options: list[any]):
    def validator(input: str) -> Result:
        for option in options:
            if str(option) == input:
                return ValidResult()
        
        return InvalidResult("The input does not match the available options.")
    
    return validator

def is_email():
    return check_format("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}")

def is_valid_username():
    return check_format("^[A-Za-z]{1}[_'.A-Za-z0-9]{5,9}$")

def is_valid_password():
    return check_format("^[~!@#$%&_\-+=`|\\(){}[\]:;'<>,.?/A-Za-z0-9]{8,30}$")

# TODO - maybe needs to be expanded a bit.
def is_phone_number():
    def validator(input: str):
        if not check_format("^(\s?|-)([0-9]\s{0,3}){8}$")(input).valid:
            return InvalidResult("The input does not match the format.")
        
        # TODO
        
        return ValidResult()
    
    return validator

def is_number():
    return check_format("[0-9]+")