from datetime import date
import utils.database as database
from utils.user import User

def log(activity: str, information: str, user: User, suspicious: bool = False):
	username = user.username if user != None else "" 
	
	database.execute_query("INSERT INTO logs (username, date, activity, information, suspicious) VALUES (?, ?, ?, ?, ?)", 
                        username, f"{date.today()}", activity, information, str(int(suspicious)))