class MyPyHenshinAbstractTransformation:

    def __init__(self):
        print "Abstract transformation __init__method"

    def __del__(self):
        print "Abstract transformation __del__ method"

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_flag, model_type_flag, output_language_type_flag):
        print "Abstract execute transformation method"