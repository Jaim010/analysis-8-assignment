import json

with open("./settings.json") as file:
  settings = json.load(file)
  
__SHIFT = settings["encryption"]["shift"]
__ADD = lambda x,y: x + y
__SUBTRACT = lambda x,y: x - y

def __ceasar_cipher(func: callable):
  def encryptor(text: str):
    result = ""
    for char in text:
      result += chr(
        func(ord(char), __SHIFT)
      )
  
    return result
  
  return encryptor

def encrypt(text: str):
  return __ceasar_cipher(__ADD)(text)

def decrypt(text: str):
  return __ceasar_cipher(__SUBTRACT)(text)
