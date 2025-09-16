
def check_password_strength(password: str) -> str:
    """Simple password strength checker."""
    if len(password) < 8:
        return " Weak: too short (minimum 8 characters)."
    if password.isdigit() or password.isalpha():
        return " Weak: must mix letters, numbers, or symbols."
    if password.lower() == password or password.upper() == password:
        return " Medium: add both upper and lower case letters."
    return " Strong password!"


def main():
    """CLI entrypoint for the password checker."""
    pwd = input("Enter a password: ")
    print(check_password_strength(pwd))


if __name__ == "__main__":
    main()
