import sys
import urllib.request

sys.setrecursionlimit(10000000)





class Bst:
    def __init__(self, path:str, **kwargs):
        self.right = None
        self.word = None
        self.left = None
        get_from_url = False
        get_from_file = False
        #print(kwargs)
        #print(kwargs.items())
        for key, value in kwargs.items():
            if key == "url":
                get_from_url = value
            elif key == "file":
                get_from_file = value

        #print(get_from_url)
        #print(get_from_file)
        if not get_from_url and not get_from_file:
            return

        words:list[str] = []
        #print(path)
        if get_from_file:
            words = Bst.read_dictionary_(path)
        else:
            words = Bst.read_from_url_(path)
            #print(words[:100])



        set_children(self, words)

    def autocomplete(self, prefix: str) -> list:
        #print(self.word, "prefix:", prefix)
        if self.word is None:
            return []
        if self.word.startswith(prefix):
            return [*self.left.autocomplete(prefix), *[self.word], *self.right.autocomplete(prefix)]
        # if self.word < prefix:
        #     return [*self.right.autocomplete(prefix)]
        # if self.word > prefix:
        #     return [*self.left.autocomplete(prefix)]
        return [*self.left.autocomplete(prefix), *self.right.autocomplete(prefix)]

    def print(self) -> None:
        if self.word is None:
            print("empty")
        else:
            #print("word", self.word)
            print("left\n", self.left.print(), "word", self.word, "right\n", self.right.print())

    def print_list(self):
        if not self.left is None:
            self.left.print_list()
        if not self.word is None:
            print(self.word)
        if not self.right is None:
            self.right.print_list()

    def read_from_url_(url: str) -> list[str]:
        return urllib.request.urlopen(url).read().decode("utf-8")

    def read_dictionary_(filename: str) -> list[str]:
        with open(filename) as f:
            return f.readlines()
            
            
def set_children(b:Bst, l:list[str]):
    len_ = len(l)
    print("len = ",len_)
    if len_ == 0:
        b.word = None
        b.left = None
        b.right = None
    else:
        m = int(len_ // 2)
        b.word = l[m]
        b.left = Bst("")
        b.right = Bst("")
        set_children(b.left, l[0:m])
        set_children(b.right, l[m + 1:len_])
    pass