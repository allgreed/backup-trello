import browser_cookie3
import requests
import datetime
import pathlib


def main():
    cookiejar = browser_cookie3.chrome(domain_name="trello.com")
    fname = f"trello-{datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y')}.json"
    with open(pathlib.Path.home() / "Keys" / "main-board-id") as f:
        board_id = f.read().rstrip()

    with open(pathlib.Path.home() / "Backup" / fname, "x") as f:
        resp = requests.get(f"https://trello.com/b/{board_id}.json", cookies=cookiejar).text
        f.write(resp)

    print("Done!")

if __name__ == "__main__":
    main()
