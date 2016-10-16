import re

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

    def findText(self, keyword, text):
        results = []
        lastIndex = 0
        found = re.search(keyword, text[lastIndex:])
        while (found):
            results.append({
                'start' : found.start() + lastIndex,
                'end'   : found.end() + lastIndex
            })

            lastIndex = found.end() + lastIndex
            found = re.search(keyword, text[lastIndex:])

        return results