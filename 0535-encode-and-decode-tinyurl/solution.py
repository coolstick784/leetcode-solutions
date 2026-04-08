class Codec:

    def __init__(self):
        self.max_id = 0
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.url_to_id = {} # maps long urls to their id
        self.id_to_url = {} # maps ids to long urls
    
    def encode_id (self, max_id):
        cur = max_id
        out = ""
        while cur > 0:
            out.append(self.chars[cur%62])
            cur //= 62
        return out.rjust(7, "0")

    
    def decode_id(self, end):
        out = 0
        cur_pow = 0
        as_list = [self.chars.index(ch) for ch in end]
        as_list.reverse()
        for idx, n in enumerate(as_list):
            out += 62 **idx * n 
        return out
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """


        if longUrl in self.url_to_id:
            return "http://tinyurl.com/" + self.id_to_url[self.url_to_id[longUrl]]
        
        end = self.encode_id(self.max_id)
        
        
        self.url_to_id[longUrl] = self.max_id
        self.id_to_url[self.max_id] = longUrl
        self.max_id += 1
        return "http://tinyurl.com/" + end
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        end = shortUrl.split("/")[-1]
        id = self.decode_id(end)
        return self.id_to_url[id]

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
