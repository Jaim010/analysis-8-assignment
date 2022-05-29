from zipfile import ZipFile
import os

__PATH = "./backups"

def create(filename: str) -> tuple[bool, str]:
  __create_dir()
  
  try:
    with ZipFile("{path}/{fn}.zip".format(fn=filename, path=__PATH), "w") as zipObj:
      zipObj.write("./db.sqlite")
      zipObj.write("./.log")
    return (True, "")
      
  except Exception as err:
    return (False, err)
    
def __create_dir() -> None:
  if not os.path.exists(__PATH):
    os.mkdir(__PATH)
  