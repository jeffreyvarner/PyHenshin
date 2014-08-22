from MyPyHenshinOctaveMLanguageLibrary import MyPyHenshinOctaveMLanguageLibrary

class MyPyHenshinOctaveCLanguageLibrary(object):

    def __init__(self):
        pass

    def __del__(self):
        pass


    def buildStoichiometricMatrixWithModelTree(self,transformation_name, transformation_tree, model_tree):

        language_library = MyPyHenshinOctaveMLanguageLibrary()
        buffer = language_library.buildStoichiometricMatrixWithModelTree(transformation_name, transformation_tree, model_tree)
        return buffer

    def buildMassActionSolveBalanceEquationsForOctaveCWithModelTree(self, transformation_name, transformation_tree,model_tree):

        language_library = MyPyHenshinOctaveMLanguageLibrary()
        buffer = language_library.buildMassActionSolveBalanceEquationsForOctaveMWithModelTree(transformation_name, transformation_tree, model_tree)
        return buffer

    def buildMassActionDataFileForOctaveCWithModelTree(self, transformation_name, transformation_tree, model_tree):

        language_library = MyPyHenshinOctaveMLanguageLibrary()
        buffer = language_library.buildMassActionDataFileForOctaveMWithModelTree(transformation_name, transformation_tree, model_tree)
        return buffer

    def buildMassActionBalanceEquationsForOctaveCWithModelTree(self,transformation_name,transformation_tree,model_tree):

        return "Monkey spank ..."

