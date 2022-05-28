from zipfile import ZipFile

def create():
  with ZipFile("./backup.zip", "w") as zipObj:
    zipObj.write("./db.sqlite")
    zipObj.write("./.log")