import pdb
import numpy

class MyPyHenshinOctaveMLanguageLibrary(object):

    def buildStoichiometricMatrixWithModelTree(self,transformation_name,transformation_tree,model_tree):

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

            # Get the species symbol list -
            species_symbol_list = model_tree.mySpeciesSymbolList
            interaction_name_list = model_tree.myInteractionNameList

            # Create stochiometric array -
            number_of_species = len(species_symbol_list)
            number_of_reactions = len(interaction_name_list)
            stmatrix = numpy.empty((number_of_species,number_of_reactions))
            for reaction_index in range(0,number_of_reactions):

                local_reaction_name = interaction_name_list[reaction_index]

                for species_index in range(0,number_of_species):

                    local_species_symbol = species_symbol_list[species_index]
                    stmatrix[species_index, reaction_index] = 0.0

            return stmatrix

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Monkey"

    def buildMassActionDataFileForOctaveMWithModelTree(self,transformation_name,transformation_tree,model_tree):

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
            print filename

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")


        return "Monkey"

    def buildMassActionBalanceEquationsForOctaveMWithModelTree(self,transformation_name,transformation_tree,model_tree):

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
            print filename

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")



        return "Code stuff goes here ..."

    def buildMassActionSolveBalanceEquationsForOctaveMWithModelTree(self,transformation_name,transformation_tree,model_tree):

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
            print filename

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    def buildMassActionKineticsEquationsForOctaveMWithModelTree(self,transformation_name,transformation_tree,model_tree):

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
            print filename

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    def buildMassActionInputEquationsForOctaveMWithModelTree(self,transformation_name,transformation_tree,model_tree):

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
            print filename

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Code stuff goes here ..."