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
            stmatrix_buffer = ''
            for species_index in range(0, number_of_species):

                local_species_symbol = species_symbol_list[species_index]

                stmatrix_row = ""
                for reaction_index in range(0, number_of_reactions):

                    # get the reaction name -
                    local_reaction_name = interaction_name_list[reaction_index]

                    # look up reaction_stoichiometric_map
                    reaction_stoichiometric_map = model_tree.myDictionaryOfInteractionModels[local_reaction_name]

                    if local_species_symbol in reaction_stoichiometric_map:
                        value = reaction_stoichiometric_map[local_species_symbol]
                        stmatrix_row += " "+str(value)+" "
                    else:
                        stmatrix_row += " 0.0 "

                stmatrix_buffer += stmatrix_row + "\n"

            pdb.set_trace()
            return stmatrix_buffer

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