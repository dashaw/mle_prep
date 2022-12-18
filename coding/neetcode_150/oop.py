class TextEditor:

    def __init__(self):
        self.s = ''
        self.c = 0 

    def addText(self, text: str) -> None:
        self.s = self.s[:self.c]+text+self.s[self.c:]
        self.c += len(text)
        
    def deleteText(self, k: int) -> int:
        len_s = len(self.s)
        # are there enough characters?
        if k > self.c:
            self.s = self.s[self.c:]
            res = self.c
            self.c = 0
        else:
            self.c = self.c - k
            self.s = self.s[:self.c] + self.s[self.c + k:]
            res = k

        return res

    def _moveCursor(self, k: int) -> None:
        if self.c + k < 0:
            self.c = 0
        elif self. c + k > len(self.s):
            self.c = len(self.s)
        else:
            self.c += k

        self.left_characters = min(10,self.c)

    def cursorRight(self, k: int) -> str:
        self._moveCursor(k)
        return self.s[self.c-self.left_characters:self.c]

    def cursorLeft(self, k: int) -> str:
        self._moveCursor(-1*k)
        return self.s[self.c-self.left_characters:self.c]   
