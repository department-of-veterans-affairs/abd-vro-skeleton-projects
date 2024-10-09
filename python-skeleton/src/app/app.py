from app.config import DEBUG, ENV


def main() -> tuple[str, bool]:
    print(f'Hello World env={ENV} debug={DEBUG}')
    return ENV, DEBUG


if __name__ == '__main__':
    main()
