import gori
from tiny_bsky import Client


def main():
    client = Client(ini_file="bsky.ini")
    client.post(gori.gori())


if __name__ == "__main__":
    main()
