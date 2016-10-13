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
            code = self.highLightText(text)

        print(text)
        return code

    def save(self, fileName, text):
        file = open(fileName, 'w')
        file.write(text)

    def highLightText(self, text):
        lexer = guess_lexer(text)
        formatter = HtmlFormatter(lineos=True, cssclass='source')
        code = highlight(text, lexer, formatter)
        code = '<style>' + HtmlFormatter().get_style_defs() + '</style>' + code

        return code