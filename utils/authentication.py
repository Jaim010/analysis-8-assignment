def to_name(authorization_level: int) -> str:
    if authorization_level == 1:
        return "Advisor"
    if authorization_level == 2:
        return "System Administrator"
    if authorization_level == 3:
        return "Super Administrator"
    return ""