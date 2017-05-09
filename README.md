# PythonHttpHeaderScanner
A small python module that could get _HTTP headers_ from server response.

![example result](https://github.com/YaokaiYang-assaultmaster/PythonHttpHeaderScanner/blob/master/example_result.png)

## Usage
- First initialize a instance of the HttpHeaderScanner class by `new_scanner = HttpHeaderScanner()`
- Then connect to the server of which the responding header we want to check by `new_scanner.connect_server([website domain])`. `[website domain]`is the string domain name of the website , either with or without protocol (i.e. `http(s)://`).
- After connecting, we could get the header fields as a dictionary object by calling `header_fields = new_scanner.get_headers()`.
- Additionally, we could also get only the cound of the different header fields by calling `header_count = new_scanner.get_header_count()`
- Or, if you only want to check all the headers by printing them out, using `new_scanner.show_headers()`

## Example code
An example usage case is showed in `scannerExample.py`.
