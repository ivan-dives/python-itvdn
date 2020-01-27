def add_link_to(links):
    original_url = input('Enter url: ')
    short_name = None
    while not short_name or short_name in links:
        short_name = input('Enter short name: ')
        if short_name in links:
            print('This name already exists '
                  '(url: {})'.format(links[short_name]))

    links[short_name] = original_url


def get_link_from(links):
    name = input('Enter link name: ')
    url = links.get(name, None)

    if url:
        print(url)
    else:
        print('Link does not exist')


def main():
    links = {}

    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')

        choice = input('> ')
        if choice == '1':
            add_link_to(links)
        elif choice == '2':
            get_link_from(links)
        elif choice == '3':
            break
        else:
            print('Incorrect input')

        print()


if __name__ == '__main__':
    main()
