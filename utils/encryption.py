import json

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


if __name__ == "__main__":
  """
  Windows: 
    python ./utils/encryption.py [-d] <INPUT_STRING>
    python ./utils/encryption.py [-e] <INPUT_STRING>
    
    Example:
      python ./utils/encryption.py -e HelloWorld!
    
  Unix:
    python3 ./utils/encryption.py [-d] <INPUT_STRING>
    python3 ./utils/encryption.py [-e] <INPUT_STRING>
    
    Example:
      python ./utils/encryption.py -d q^È^Ê^Ò^ÖZYXH
  """
  import sys
  if len(sys.argv) > 3:
    raise f"Too many arguments. Expected 2, got {len(sys.argv)}" 
  
  action: callable
  
  if sys.argv[1] == "-d":
    action = decrypt
  elif sys.argv[1] == "-e":
    action = encrypt
  else:
    raise f"Invalid flag"  
  
  result = action(sys.argv[2])
  print(result)
  
  