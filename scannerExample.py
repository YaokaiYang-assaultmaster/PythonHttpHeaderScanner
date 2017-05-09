import HTTPHeaderScanner as hscanner


def main():
    target_website = 'http://www.google.com'

    new_scanner = hscanner.HttpHeaderScanner()
    new_scanner.connect_server(target_website)
    header_dict = new_scanner.get_headers()
    for ele in header_dict:
        # do whatever we want here
        # I will just print them out as an example
        print(str(ele) + ': ' + str(header_dict[ele]))

    header_count = new_scanner.get_header_count()
    print('There is %d different header fields in total from HTTP response of website %s'
          % (header_count, target_website))


if __name__ == '__main__':
    main()
