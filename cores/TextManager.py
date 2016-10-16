from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter

class TextManager():

    def __init__(self):
        pass

    def readFile(self, fileName):
        print("read file")
        with open(fileName, 'r') as file:
            text = file.read()

        return text

    def save(self, fileName, text):
        file = open(fileName, 'w')
        file.write(text)
