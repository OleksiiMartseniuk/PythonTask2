import re


def check_password(password: str) -> None | str:
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[*#+@])[a-zA-Z\d*#+@]{4,6}$"
    pat = re.compile(reg)
    mat = re.search(pat, password)
    return password if mat else None


if __name__ == '__main__':
    pass
