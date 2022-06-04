from utils.user import User
import utils.encryption as enc
from datetime import datetime

__LOG_PATH = "./.log"

def log(activity: str, information: str, user: User, suspicious: bool = False) -> None:
  username = user.username if user != None else "" 

  separator = "\t"
  with open(__LOG_PATH, "a+", encoding="utf-8") as f:
    f.seek(0)
    
    lines = f.readlines()
    lines = decrypt_log(lines)

    log_number = len(lines)
    
    now = datetime.now()

    content = f"{str(log_number)}{separator}{username}{separator}{now.date()}{separator}{now.time().strftime('%H:%M:%S')}{separator}{activity}{separator}{information}{separator}{suspicious}\n"
    
    ## Debug ##
    with open("./plain.log", "a+", encoding="utf-8") as pf:
      pf.write(content)
    
    f.write(enc.encrypt(content))
    
#! Maybe not needed, not sure how it will behave when a char converts to \n
def decrypt_log(encrypted_content: list[str]) -> list[str]:
  content = ""
  for line in encrypted_content:
    content += line
    
  decrypted_content = enc.decrypt(content)
  decrypted_content = decrypted_content.split("\n")
  
  return decrypted_content
  
  
def get_log_content() -> list[str]:
  with open(__LOG_PATH, "r", encoding="utf-8") as f:
    encrypted_content = f.readlines()
  return encrypted_content