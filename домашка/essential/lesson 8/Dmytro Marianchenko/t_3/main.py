import func_mod


def main():
    try:
        import user
        user.user_input()
    except ModuleNotFoundError:
        print("Input link to get short link:\n>>  ")
        find_key = input()
        default_key = find_key
        find_key = func_mod.get_data(find_key)
        if find_key is None:
            temp = (default_key, f"{func_mod.URL_SHORT_LINK}/{find_key}")
            print(temp)


if __name__ == '__main__':
    main()
