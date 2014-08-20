class MyPyHenshinAbstractTransformation:

    def __init__(self):
        print "Abstract transformation __init__method"

    def __del__(self):
        print "Abstract transformation __del__ method"

    def executeTransformationUsingIntermediateTree(self, model_tree):
        print "Abstract execute transformation method"