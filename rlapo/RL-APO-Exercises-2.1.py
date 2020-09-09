"""(1) Create a Bookmark class, which contains strings (URLs) you might
    want to view later on.  Adding one new URL will return a new
    instance of Bookmark with the new URL in it.  Using += will modify
    the existing instance of Bookmark.  Note that if a bookmark has
    already been stored, you shouldn't store it.

b = Bookmark()
b = b + 'https://lerner.co.il'  
b += ['https://lerner.co.il'  , 'https://google.com']
print(b) 
"""


class Bookmark(object):
    def __init__(self):
        self.urls = []

    def __add__(self, new_url):
        b = Bookmark()
        b.urls = self.urls.copy()
        if new_url not in b.urls:
            b.urls.append(new_url)
        return b

    def __iadd__(self, new_urls):
        for one_url in new_urls:
            if one_url not in self.urls:
                self.urls.append(one_url)
        return self

    def __repr__(self):
        return "\n".join(one_url for one_url in self.urls)


if __name__ == "__main__":
    b = Bookmark()
    b = b + "https://lerner.co.il"
    b = b + "https://google.com"
    b = b + "https://google.com"
    b += ["https://lerner.co.il", "https://google.com", "https://python.org"]

    print(b)
