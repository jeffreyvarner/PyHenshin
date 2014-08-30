class MyPyHenshinPythonLanguageLibrary(object):

    def __init__(self):
        pass

    def __del__(self):
        pass


    def buildMassActionBalanceEquationsForPythonWithModelTree(self, transformation_name, transformation_tree, model_tree):

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
            buffer += 'import numpy as np\n'
            buffer += '\n'
            buffer += 'def calculateKinetics(x,t,PROBLEM_DICTIONARY):\n'
            buffer += '\n'
            buffer += '\n'
            buffer += 'def calculateInputs(x,t,PROBLEM_DICTIONARY):\n'
            buffer += '\n'
            buffer += '\n'
            buffer += 'def '+function_name+'(x,t,PROBLEM_DICTIONARY):\n'
            buffer += '\n'
            buffer += '\t# Call the kinetics function - \n'
            buffer += '\trV = calculateKinetics(x,t,PROBLEM_DICTIONARY)\n'
            buffer += '\n'
            buffer += '\t# Call the inputs function - \n'
            buffer += '\tuV = calculateInputs(x,t,PROBLEM_DICTIONARY)\n'
            buffer += '\n'
            buffer += '\t# Call the input function - \n'
            buffer += '\treturn dxdt\n'

            return buffer

        else:
            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "What the what? This shouldn't have happend!"


    def buildMassActionSolveBalanceEquationsForPythonWithModelTree(self,transformation_name,transformation_tree,model_tree):
        pass


    def buildMassActionDataFileForPythonWithModelTree(self,transformation_name,transformation_tree,model_tree):
        pass




