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

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Initialize an empty buffer -
            buffer = ''

            # Get the function name -
            function_name = filename.split('.')[0]
            buffer += '#include <octave/oct.h>\n'
            buffer += '#include <ov-struct.h>\n'
            buffer += '#include <iostream>\n'
            buffer += '#include <Math.h>\n'
            buffer += '\n'
            buffer += '// Function prototypes - \n'
            buffer += 'void calculateKinetics(ColumnVector&,ColumnVector&,ColumnVector&);\n'
            buffer += 'void calculateInputs();\n'
            buffer += 'void calculateMassBalances(int,Matrix&,ColumnVector&,ColumnVector&,ColumnVector&);\n'
            buffer += '\n'
            buffer += '// Main function. Calls kinetics, inputs and balances. Returns the derivative - \n'
            buffer += 'DEFUN_DLD(ExtBalanceFunction,args,nargout,"Calculate the mass balances.")\n'
            buffer += '{\n'
            buffer += '}\n'
            buffer += '\n'
            buffer += '// Inputs function - \n'
            buffer += 'void calculateInputs()\n'
            buffer += '{\n'
            buffer += '\t // Add inputs code here...\n'
            buffer += '}\n'
            buffer += '\n'
            buffer += '// Kinetics function - \n'
            buffer += 'void calculateKinetics(ColumnVector& kV,ColumnVector& x,ColumnVector& rV)\n'
            buffer += '{\n'
            buffer += '\t // Add inputs code here...\n'
            buffer += '}\n'
            buffer += '\n'
            buffer += '// Balance equations function - \n'
            buffer += 'void calculateMassBalances(int NSTATES,Matrix& STMATRIX,ColumnVector& rV,ColumnVector& ds,ColumnVector& dx)\n'
            buffer += '{\n'
            buffer += '}\n'

            return buffer
        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Monkey spank ..."

