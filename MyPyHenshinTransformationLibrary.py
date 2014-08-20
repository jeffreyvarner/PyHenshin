from MyPyHenshinAbstractTransformation import MyPyHenshinAbstractTransformation

class MyPyHenshinMAModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, model_tree):
        print "MyPyHenshinMAModelTransformation execute transformation method"

class MyPyHenshinFBAModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, model_tree):
        print "MyPyHenshinFBAModelTransformation execute transformation method"

class MyPyHenshinHCFLModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, model_tree):
        print "MyPyHenshinHCFLModelTransformation execute transformation method"