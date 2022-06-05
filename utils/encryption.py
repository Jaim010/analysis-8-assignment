import json
import argparse

__settings_path = "./settings.json"

if __name__ == "__main__":
  import sys
  if sys.argv[0] ==  ".\encryption.py":
    __settings_path = "../settings.json"

with open(__settings_path) as file:
  __SETTINGS = json.load(file)
  
__SHIFT = __SETTINGS["encryption"]["shift"]
__ADD = lambda x,y: x + y
__SUBTRACT = lambda x,y: x - y

def __ceasar_cipher(func: callable) -> callable:
  def encryptor(text: str) -> str:
    result = ""
    for char in text:
      result += chr(
        func(ord(char), __SHIFT) % 0x110000
      )
  
    return result
  
  return encryptor

def encrypt(text: str) -> str:
  return __ceasar_cipher(__ADD)(text)

def decrypt(text: str) -> str:
  return __ceasar_cipher(__SUBTRACT)(text)

# Handles given arguments, if running file as __main__
# Example:
#   python utils/encryption.py [--command COMMAND] <TEXT>
#   python utils/encryption.py -c encrypt SomeText
__parser = argparse.ArgumentParser()

__parser.add_argument(
  "--command",
  "-c",
  help="command to run on given string",
)

__parser.add_argument(
  "text",
  type=str,
  help="text to perform the command over",
)

def __main(args):
  actions = {func.__name__: func for func in [encrypt, decrypt]}
  
  if args.command not in actions.keys():
    raise Exception(f"No such command exists: {args.command}")
  
  result = actions[args.command](args.text)
  print(result)

if __name__ == "__main__":
  __main(__parser.parse_args())  

  
  
  