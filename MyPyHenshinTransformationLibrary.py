from MyPyHenshinAbstractTransformation import MyPyHenshinAbstractTransformation

class MyPyHenshinMAModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):

        if input_language_type_flag == 'VLFF':
            pass

        else:
            error_string = "Exception: think about this ..."
            raise Exception(error_string)


class MyPyHenshinFBAModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):
        print "MyPyHenshinFBAModelTransformation execute transformation method"

class MyPyHenshinHCFLModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):
        print "MyPyHenshinHCFLModelTransformation execute transformation method"