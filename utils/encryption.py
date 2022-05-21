import json

with open("./settings.json") as file:
  __SETTINGS = json.load(file)
  
__SHIFT = __SETTINGS["encryption"]["shift"]
__ADD = lambda x,y: x + y
__SUBTRACT = lambda x,y: x - y

def __ceasar_cipher(func: callable):
  def encryptor(text: str) -> str:
    result = ""
    for char in text:
      result += chr(
        func(ord(char), __SHIFT)
      )
  
    return result
  
  return encryptor

def encrypt(text: str) -> str:
  return __ceasar_cipher(__ADD)(text)

def decrypt(text: str) -> str:
  return __ceasar_cipher(__SUBTRACT)(text)
