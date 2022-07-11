import re


def check_password(password: str) -> None | str:
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[*#+@])[a-zA-Z\d*#+@]{4,6}$"
    pat = re.compile(reg)
    mat = re.search(pat, password)
    return password if mat else None


def main():
    password_data = input('Enter password: ')
    list_password_true = []
    for password in password_data.split(','):
        result = check_password(password)
        if result:
            list_password_true.append(result)

    print(','.join(list_password_true))


if __name__ == '__main__':
    main()
