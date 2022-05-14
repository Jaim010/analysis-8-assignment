class LoginResponse:
  def __init__(self, is_valid:bool, username:str, authorization_level:int) -> None:
    self.is_valid: bool = is_valid
    self.username: str = username
    self.authorization_level: int = authorization_level