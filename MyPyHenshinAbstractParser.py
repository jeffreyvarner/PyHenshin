
class MyPyHenshinAbstractParser:

    def __init__(self):
        print "Parser init method was called"

    def __del__(self):
        print "Parser del method was called"

    def buildModelTreeFromInputURL(self, path_to_input_file):

        # This will need to be overriden -
        print "This method must be overridden in subclass of parser - "+str(path_to_input_file)

