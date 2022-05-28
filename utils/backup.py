from zipfile import ZipFile


def create(filename: str) -> tuple[bool, str]:
  try:
    with ZipFile("./{fn}.zip".format(fn=filename), "w") as zipObj:
      zipObj.write("./db.sqlite")
      zipObj.write("./.log")
    return (True, "")
      
  except Exception as err:
    return (False, err)
    