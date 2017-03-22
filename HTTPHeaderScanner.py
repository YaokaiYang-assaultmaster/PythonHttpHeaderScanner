import urllib2

class HttpHeaderScanner:

    __headers = {}

    def connect_server(self, website):
        """Connect a server of which the header fields we want to check
        
        Args:
            website (String): The website whose server we want to check 
        
        """
        req = urllib2.Request(website)

        try:
            response = urllib2.urlopen(req)

            info = response.info()
            info_list = info.items()

            for ele in info_list:
                self.__headers[ele[0]] = ele[1]

        except Exception as e:

            print('Warning: Connection Error!!!')
            print(e)

    def get_server_field(self):
        """Return the server fields in the HTTP header
        
        Returns:
            String: The value of the server field, if not exists, return "None".
        """

        if 'server' in self.__headers:
            return ('server', self.__headers['server'])
        else:
            return 'None'

    def show_headers(self):
        """Print out all the fields of the http header
        
        """
        for ele in self.__headers:
            print(str(ele) + ': ' + str(self.__headers[ele]))

    def get_headers(self):
        """Return a dictionary of headers fields in (fieldname, value) pair
        
        Returns:
            Dict: A dictionary of (field name, corresponding value) pairs
        """
        tmp = dict()

        for key in self.__headers:
            tmp[key] = self.__headers[key]

        return tmp


    def get_header_count(self):
        """Return the total number of different fields in the header
        
        Returns:
            int: number of the header fields
        """
        return len(self.__headers)