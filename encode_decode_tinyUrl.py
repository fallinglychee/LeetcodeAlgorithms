class Codec:
    
    chars = string.ascii_letters + string.digits
    
    def __init__(self):
        #create two dictionarys, one with original url as key value and the other with coded url as key value
        self.encrypt = {}
        self.decrypt = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        #if input is new, generate shortened url
        while longUrl not in self.encrypt:
            code = "".join(random.choice(Codec.chars) for length in range(0, 6))
        #establish key-value association between url and code in encrypt dict and vice versa for decrypt dict
            if code not in self.encrypt:
                self.decrypt[code] = longUrl
                self.encrypt[longUrl] = code
        return "http://tinyurl.com/" + self.encrypt[longUrl]
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        #return tinyUrl code by slicing shortUrl by 6 characters
        return self.decrypt[shortUrl[19:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))