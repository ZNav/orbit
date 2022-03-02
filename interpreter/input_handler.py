from os.path import exists

defaultInputFile = 'input.orbit'

def openFile(fileName):
    with open(fileName, 'r') as f:
        return f.read()

def InputHandler(argv, fileName=None):
    if fileName != None and exists(fileName):
        return openFile(fileName)
    if len(argv) > 1 and exists(argv[1]):
        return openFile(argv[1])
    elif exists(defaultInputFile):
        return openFile(defaultInputFile)
    else:
        return
        # TODO Invalid input error
