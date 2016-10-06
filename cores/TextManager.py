class TextManager():

    def __init__(self):
        pass

    def readFile(self, fileName):
        print("read file")
        with open(fileName, 'r') as file:
            text = file.read()
#            print (text)

        return text