from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

class TextManager():

    def __init__(self):
        pass

    def readFile(self, fileName):
        print("read file")
        with open(fileName, 'r') as file:
            text = file.read()
            lexer = get_lexer_for_filename(fileName)
            formatter = HtmlFormatter(lineos = True, cssclass = 'source')
            code = highlight(text, lexer, formatter)
            code = '<style>' + HtmlFormatter().get_style_defs() + '</style>' + code

        print(text)
        return code