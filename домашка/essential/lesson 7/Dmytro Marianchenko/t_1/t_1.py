container = {"https://docs.python.org/3/library/index.html": "https://goo-gl.su/python"}
URL_SHORT_LINK = "http//srt.lnk."


def main():
    try:
        import link_
        link_.user_input()
    except ModuleNotFoundError:
        print("Input link to get short link:\n>>  ")
        find_key = input()
        default_key = find_key
        find_key = container.get(find_key)
        if find_key is None:
            container.setdefault(default_key, f"{URL_SHORT_LINK}/{default_key}")
            print(container.get(default_key))


if __name__ == '__main__':
    main()
