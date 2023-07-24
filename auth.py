from models import User


def sign_in(username: str, password: str) -> bool | User:
    """Return User if username and password match an User. Return False if not User match"""
    query = User.select().where(
            User.username == username,
            User.password == password
        )

    if len(query) == 0:
        return False

    return query[0]

def main():

    result = sign_in("dev", "dev")

    print(repr(result))

if __name__ == "__main__":
    main()
