import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
  "--command",
  "-c",
  help="command to run on given string",
)

parser.add_argument(
  "text",
  type=str,
  help="Text to perform the command over",
)

with open("./settings.json") as file:
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



def main(args):
  actions = {
    "encrypt": encrypt,
    "decrypt": decrypt
  }
  
  if args.command not in actions.keys():
    raise Exception(f"No such command exists: {args.command}")
  
  result = actions[args.command](args.text)
  print(result)

if __name__ == "__main__":
  main(parser.parse_args())  

  
  
  