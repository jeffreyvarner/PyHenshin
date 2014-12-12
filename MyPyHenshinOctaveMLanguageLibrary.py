import pdb
import numpy
import random
from MyPyHenshinParserLibrary import *


class MyPyHenshinOctaveMLanguageLibrary(object):

    def buildStoichiometricMatrixWithModelTree(self, transformation_name, transformation_tree, model_tree):

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

                if not local_species_symbol == '[]':
                    stmatrix_row = ""
                    for reaction_index in range(0, number_of_reactions):

                        # get the reaction name -
                        local_reaction_name = interaction_name_list[reaction_index]

                        # look up reaction_stoichiometric_map
                        reaction_stoichiometric_map = model_tree.myDictionaryOfInteractionModels[local_reaction_name]

                        if local_species_symbol in reaction_stoichiometric_map:
                            value = reaction_stoichiometric_map[local_species_symbol]
                            stmatrix_row += " " + str(value) + " "
                        else:
                            stmatrix_row += " 0.0 "

                    stmatrix_buffer += stmatrix_row + "\n"

            return stmatrix_buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    # FLUX BALANCE ANALYSIS METHODS --------------------------------------------------------------------------------- #
    def buildFBAControlEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        if 'dependency' in component_dictionary:
            dependecy_list = component_dictionary['dependency']
            dependency_dictionary = dict()
            for dependency_key in dependecy_list:

                # Item index -
                for transformation_component in transformation_component_array:

                    if dependency_key in transformation_component:
                        dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']


        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # Initialize an empty buffer ...
            buffer = ''

            # Control file -
            if 'transformation_control_file_url' in transformation_tree:

                 # Get the control file url -
                path_to_control_file = transformation_tree['transformation_control_file_url']

                # Load the parser -
                parser = MyPyHenshinControlListParser()

                # Parse the control file -
                control_data_structure = parser.buildFBAControlFunctionListFromInputURL(path_to_control_file)

                # Process the control data structure -
                for control_data in control_data_structure:

                    # Extract data -
                    type_flag = control_data[0]
                    source_array = control_data[1]
                    target_array = control_data[2]

                    if type_flag == 'activates':

                        print('activates')

                    elif type_flag == 'inhibits':

                        print('inhibits')

                    elif type_flag == 'induces':

                        print('induces')

                    elif type_flag == 'represses':

                        print('represses')

            # return the filled buffer -
            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"


    def buildFBAFluxBoundsFileForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

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

            # program buffer -
            buffer = ''

            reaction_name_list = model_tree.myInteractionNamelList
            reaction_count = len(reaction_name_list)
            for reaction_index in range(0, reaction_count):
                buffer += '0\tinf\n'

            return buffer
        else:
            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    def buildFBADebugFluxFileForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

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

            # program buffer -
            buffer = ''

            # Get the list of raw reaction string -
            counter = 1
            raw_reaction_string_list = model_tree.myListOfRawReactionStrings
            for reaction_string in raw_reaction_string_list:
                buffer += str(counter) + '\t' + reaction_string
                buffer += '\n'
                counter += 1

            return buffer
        else:
            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    def buildFBADataFileForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        dependecy_list = component_dictionary['dependency']
        dependency_dictionary = dict()
        for dependency_key in dependecy_list:

            # Item index -
            for transformation_component in transformation_component_array:

                if dependency_key in transformation_component:
                    dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # program buffer -
            buffer = ''

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Get the function name -
            function_name = filename.split('.')[0]

            buffer += "function DF = " + function_name + "(TSTART,TSTOP,Ts,INDEX)\n"
            buffer += '\n'
            buffer += '% Load the stoichiometric matrix and flux bounds array - \n'

            # Do we have a make_stoichiometric_matrix key?
            if 'make_stoichiometric_matrix' in dependency_dictionary:
                stoichiometric_matrix_filename = dependency_dictionary['make_stoichiometric_matrix']
                buffer += 'stoichiometric_matrix = load(\''
                buffer += stoichiometric_matrix_filename
                buffer += '\');\n'
            else:
                buffer += 'stoichiometric_matrix = load(\'STMatrix.dat\');\n'


            # Do we have the flux bound key?
            if 'make_flux_bounds_file' in dependency_dictionary:
                flux_bounds_filename = dependency_dictionary['make_flux_bounds_file']
                buffer += 'flux_bounds_array = load(\''
                buffer += flux_bounds_filename
                buffer += '\');\n'
            else:
                buffer += 'flux_bounds_array = load(\'FB.dat\');\n'

            buffer += '[number_of_species,number_of_reactions] = size(stoichiometric_matrix);\n'
            buffer += '\n'

            # Build the free species list -
            extracellular_species_list = []
            if 'transformation_extracellular_species_url' in transformation_tree:

                # Get the extracellular url -
                path_to_extracellular_species_list = transformation_tree['transformation_extracellular_species_url']

                # Build the parser -
                input_file_parser = MyPyHenshinSpeciesListParser()

                # Load the file -
                extracellular_species_list = input_file_parser.buildSpeciesListFromInputURL(path_to_extracellular_species_list)


            buffer += '% Setup the free metabolite array - \n'
            buffer += 'IDX_FREE_METABOLITES = [\n'

            counter = 1
            model_species_list = model_tree.mySpeciesSymbolList
            for extracellular_species in extracellular_species_list:
                # Lookup the index of this species -
                extracellular_species_index = model_species_list.index(extracellular_species) + 1
                buffer += '\t' + str(extracellular_species_index)
                buffer += '\t' + str(counter)
                buffer += '\t;\t% ' + str(counter) + ' ' + extracellular_species
                buffer += '\n'
                counter += 1

            buffer += '];\n'

            buffer += '\n'
            buffer += '% Split the stoichiometric matrix - \n'
            buffer += 'IDX_BALANCED_METABOLITES = setdiff(1:number_of_species,IDX_FREE_METABOLITES(:,1));\n'
            buffer += 'N_IDX_BALANCED_METABOLITES = length(IDX_BALANCED_METABOLITES);\n'
            buffer += '\n'

            # Make the species bound array -
            buffer += '% Setup the bounds on species - \n'
            buffer += 'BASE_BOUND = 1;\n'
            buffer += 'SPECIES_BOUND = [\n'

            counter = 1
            for extracellular_species in extracellular_species_list:
                # Lookup the index of this species -
                extracellular_species_index = model_species_list.index(extracellular_species) + 1
                buffer += '\t' + str(extracellular_species_index)
                buffer += '\t0\tBASE_BOUND\t;\t% ' + str(counter) + ' ' + extracellular_species
                buffer += '\n'
                counter += 1

            buffer += '];\n'
            buffer += '\n'

            # Split the stoichiometric matrix -
            buffer += '% Split the stochiometrix matrix - \n'
            buffer += 'S	=	stoichiometric_matrix(IDX_BALANCED_METABOLITES,:);\n'
            buffer += 'SDB	=	stoichiometric_matrix(SPECIES_BOUND(:,1),:);\n'

            buffer += '\n'
            buffer += '% == DO NOT EDIT BELOW THIS LINE ================================== \n'
            buffer += 'DF.STOICHIOMETRIC_MATRIX = stoichiometric_matrix;\n'
            buffer += 'DF.FLUX_BOUNDS = flux_bounds_array;\n'
            buffer += 'DF.SPECIES_BOUND_ARRAY = SPECIES_BOUND;\n'
            buffer += 'DF.SPECIES_BOUNDS_INDEX = IDX_FREE_METABOLITES;\n'
            buffer += 'DF.BALANCED_MATRIX = S;\n'
            buffer += 'DF.SPECIES_CONSTRAINTS = SDB;\n'
            buffer += 'DF.NUMBER_OF_REACTIONS = number_of_reactions;\n'
            buffer += 'DF.NUMBER_OF_STATES = number_of_species;\n'
            buffer += '% ================================================================= \n'
            buffer += 'return;\n'

            return buffer
        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"
    # ----------------------------------------------------------------------------------------------------------------#

    # CELL FREE METHODS ----------------------------------------------------------------------------------------------#
    def buildCellFreeControlEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        dependecy_list = component_dictionary['dependency']
        dependency_dictionary = dict()
        for dependency_key in dependecy_list:

            # Item index -
            for transformation_component in transformation_component_array:

                if dependency_key in transformation_component:
                    dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # Initialize an empty buffer ...
            buffer = ''

            # Control file -
            if 'control_file_url' in transformation_tree:

                 # Get the control file url -
                path_to_control_file = transformation_tree['control_file_url']

                # Load the parser -
                parser = MyPyHenshinControlListParser()


            # return the filled buffer -
            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    def buildCellFreeKineticsEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        dependecy_list = component_dictionary['dependency']
        dependency_dictionary = dict()
        for dependency_key in dependecy_list:

            # Item index -
            for transformation_component in transformation_component_array:

                if dependency_key in transformation_component:
                    dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # Initialize an empty buffer ...
            buffer = ''


            # Check to see if we have an order file -
            extracellular_species_list = []
            if 'transformation_extracellular_species_url' in transformation_tree:

                # Get the extracellular url -
                path_to_extracellular_species_list = transformation_tree['transformation_extracellular_species_url']

                # Build the parser -
                input_file_parser = MyPyHenshinSpeciesListParser()

                # Load the file -
                extracellular_species_list = input_file_parser.buildSpeciesListFromInputURL(path_to_extracellular_species_list)


            # Reorder the species list -
            species_symbol_list = model_tree.mySpeciesSymbolList
            reordered_species_list = []
            for species_symbol in species_symbol_list:
                if not species_symbol == '[]':
                    if not species_symbol in extracellular_species_list:
                        reordered_species_list.append(species_symbol)

            for extracellular_species_symbol in extracellular_species_list:
                if not extracellular_species_symbol == '[]':
                    reordered_species_list.append(extracellular_species_symbol)


            # return the filled buffer -
            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"


    def buildCellFreeBalanceEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        dependecy_list = component_dictionary['dependency']
        dependency_dictionary = dict()
        for dependency_key in dependecy_list:

            # Item index -
            for transformation_component in transformation_component_array:

                if dependency_key in transformation_component:
                    dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # program buffer -
            buffer = ''

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Get the function name -
            function_name = filename.split('.')[0]

             # Fill the buffer ...
            buffer += 'function dxdt = ' + function_name + '(x,t,DF)\n'
            buffer += '\n'
            buffer += '% Get the stoichiometric matrix -\n'
            buffer += 'STM = DF.STOICHIOMETRIC_MATRIX;\n'
            buffer += '\n'

            # Check to see if we have a kinetics dependency -
            buffer += '% Calculate the kinetics -\n'
            if 'make_kinetics' in dependency_dictionary:

                # Get the name of the kinetics file -
                filename = dependency_dictionary['make_kinetics']

                # Get the function name -
                function_name = filename.split('.')[0]

                # Call the kinetics function -
                buffer += 'rV = '+function_name+'(t,x,DF);\n'
                buffer += '\n'

            else:
                buffer += 'rV = Kinetics(t,x,DF);\n'
                buffer += '\n'


            # Check to see if we have a control dependency -
            buffer += '% Calculate the control variables -\n'
            if 'make_control' in dependency_dictionary:

                # Get the name of the kinetics file -
                filename = dependency_dictionary['make_inputs']

                # Get the function name -
                function_name = filename.split('.')[0]

                # Call the kinetics function -
                buffer += 'vV = '+function_name+'(t,x,rV,DF);\n'
                buffer += '\n'
            else:

                buffer += 'vV = Control(t,x,rV,DF);\n'
                buffer += '\n'

            # Update the rate vector -
            buffer += '% Update the rate vector -\n'
            buffer += 'rV = rV*vV;\n'
            buffer += '\n'

            # Check to see if we have a kinetics dependency -
            buffer += '% Calculate the inputs -\n'
            if 'make_inputs' in dependency_dictionary:

                # Get the name of the kinetics file -
                filename = dependency_dictionary['make_inputs']

                # Get the function name -
                function_name = filename.split('.')[0]

                # Call the kinetics function -
                buffer += 'uV = '+function_name+'(t,x,DF);\n'
                buffer += '\n'

            else:
                buffer += 'uV = Input(t,x,DF);\n'
                buffer += '\n'

            buffer += '\n'
            buffer += '% Calculate the dxdt terms -\n'
            buffer += 'dxdt = STM*rV + uV;\n'
            buffer += '\n'
            buffer += 'return;\n'

            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    def buildCellFreeDataFileForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

        # First thing, we need to look up the specific block that is associated with this transformation
        component_dictionary = None
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                if key_value == transformation_name:
                    component_dictionary = transformation_dictionary[key_value]
                    break

        # Do we have a dependency?
        dependecy_list = component_dictionary['dependency']
        dependency_dictionary = dict()
        for dependency_key in dependecy_list:

            # Item index -
            for transformation_component in transformation_component_array:

                if dependency_key in transformation_component:
                    dependency_dictionary[dependency_key] = transformation_component[dependency_key]['file_name']

        # We should have the component dictionary - execute the code generation logic
        if component_dictionary is not None:

            # program buffer -
            buffer = ''

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Get the function name -
            function_name = filename.split('.')[0]

            buffer += "function DF = " + function_name + "(TSTART,TSTOP,Ts,INDEX)\n"
            buffer += '\n'
            buffer += '% Load the stoichiometric matrix and flux bounds array - \n'

            # Do we have a make_stoichiometric_matrix key?
            if 'make_stoichiometric_matrix' in dependency_dictionary:
                stoichiometric_matrix_filename = dependency_dictionary['make_stoichiometric_matrix']
                buffer += 'stoichiometric_matrix = load(\''
                buffer += stoichiometric_matrix_filename
                buffer += '\');\n'
            else:
                buffer += 'stoichiometric_matrix = load(\'Network.dat\');\n'

            buffer += '\n'
            buffer += '[number_of_species,number_of_reactions] = size(stoichiometric_matrix);\n'
            buffer += '\n'

            # List of parameter values -
            buffer += '% Kinetic parameter vector - \n'
            buffer += 'KPV = [\n'

            buffer += '];\n'
            buffer += '\n'

            # List the initial conditions -
            buffer += '\n'
            buffer += '% Initial condition vector - \n'
            buffer += 'ICV = [\n'

            # Check to see if we have an order file -
            extracellular_species_list = []
            if 'transformation_extracellular_species_url' in transformation_tree:

                # Get the extracellular url -
                path_to_extracellular_species_list = transformation_tree['transformation_extracellular_species_url']

                # Build the parser -
                input_file_parser = MyPyHenshinSpeciesListParser()

                # Load the file -
                extracellular_species_list = input_file_parser.buildSpeciesListFromInputURL(path_to_extracellular_species_list)


            # Reorder the species list -
            species_symbol_list = model_tree.mySpeciesSymbolList
            reordered_species_list = []
            for species_symbol in species_symbol_list:
                if not species_symbol == '[]':
                    if not species_symbol in extracellular_species_list:
                        reordered_species_list.append(species_symbol)

            for extracellular_species_symbol in extracellular_species_list:
                if not extracellular_species_symbol == '[]':
                    reordered_species_list.append(extracellular_species_symbol)

            # Populate the list of ICs w/0's -
            reaction_name_list = model_tree.myInteractionNameList
            species_counter = 1
            for species_symbol in reordered_species_list:

                if not species_symbol == '[]':
                    buffer += '\t0.0;\t% ' + str(species_counter) + ' ' + species_symbol + '\n'
                    species_counter += 1

            for reaction_symbol in reaction_name_list:

                if not species_symbol == '[]':
                    buffer += '\t1.0;\t% ' + str(species_counter) + ' E_' + reaction_symbol + '\n'
                    species_counter += 1

            buffer += '];\n'
            buffer += '\n'
            buffer += '% == DO NOT EDIT BELOW THIS LINE ================================== \n'
            buffer += 'DF.STOICHIOMETRIC_MATRIX = stoichiometric_matrix;\n'
            buffer += 'DF.NUMBER_OF_REACTIONS = number_of_reactions;\n'
            buffer += 'DF.NUMBER_OF_STATES = number_of_species;\n'
            buffer += 'DF.KINETIC_PARAMETER_VECTOR = KPV;\n'
            buffer += 'DF.INITIAL_CONDITION_VECTOR = ICV;\n'
            buffer += 'DF.MEASUREMENT_SELECTION_VECTOR = 1:number_of_species;\n'
            buffer += '% ================================================================= \n'
            buffer += 'return;\n'

            return buffer
        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"
    # ----------------------------------------------------------------------------------------------------------------#

    # MASS ACTION METHODS ------------------------------------------------------------------------------------------- #
    def buildMassActionDataFileForOctaveMWithModelTree(self, transformation_name, transformation_tree, model_tree):

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

            # program buffer -
            buffer = ''

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Get the function name -
            function_name = filename.split('.')[0]

            buffer += "function DF = " + function_name + "(TSTART,TSTOP,Ts,INDEX)\n"
            buffer += '\n'
            buffer += '% Load the stoichiometric matrix - \n'
            buffer += 'stoichiometric_matrix = load(\'STMatrix.dat\');\n'
            buffer += '[number_of_species,number_of_reactions] = size(stoichiometric_matrix);\n'
            buffer += '\n'
            buffer += '% Kinetic parameter vector - \n'
            buffer += 'KPV = [\n'

            # Populate a list w/random parameters -
            interaction_name_list = model_tree.myInteractionNameList
            reaction_counter = 1
            for reaction_name in interaction_name_list:

                # Get raw interaction string -
                raw_reaction_string = model_tree.myDictionaryOfInteractionModels[reaction_name][
                    'raw_interaction_string']

                value = 0.0
                if '_reverse' in reaction_name:
                    value = random.gauss(1.0, 0.1)

                else:
                    value = random.gauss(10.0, 1.0)

                buffer += '\t' + str(value) + ';\t% ' + str(
                    reaction_counter) + ' ' + reaction_name + "::" + raw_reaction_string + "\n"
                reaction_counter += 1

            buffer += '];\n'
            buffer += '\n'
            buffer += '% Initial condition vector - \n'
            buffer += 'ICV = [\n'

            # Populate the list of ICs w/0's -
            species_symbol_list = model_tree.mySpeciesSymbolList
            species_counter = 1
            for species_symbol in species_symbol_list:

                if not species_symbol == '[]':
                    buffer += '\t0.0;\t% ' + str(species_counter) + ' ' + species_symbol + '\n'
                    species_counter += 1

            buffer += '];\n'
            buffer += '\n'
            buffer += '% == DO NOT EDIT BELOW THIS LINE ================================== \n'
            buffer += 'DF.STOICHIOMETRIC_MATRIX = stoichiometric_matrix;\n'
            buffer += 'DF.NUMBER_OF_REACTIONS = number_of_reactions;\n'
            buffer += 'DF.NUMBER_OF_STATES = number_of_species;\n'
            buffer += 'DF.KINETIC_PARAMETER_VECTOR = KPV;\n'
            buffer += 'DF.INITIAL_CONDITION_VECTOR = ICV;\n'
            buffer += 'DF.MEASUREMENT_SELECTION_VECTOR = 1:number_of_species;\n'
            buffer += '% ================================================================= \n'
            buffer += 'return;\n'

            return buffer
        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Monkey"

    def buildMassActionBalanceEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree,
                                                               model_tree):

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

            # Fill the buffer ...
            buffer += 'function dxdt = ' + function_name + '(x,t,DF)\n'
            buffer += '\n'
            buffer += '% Get the stoichiometric matrix -\n'
            buffer += 'STM = DF.STOICHIOMETRIC_MATRIX;\n'
            buffer += '\n'
            buffer += '% Calculate the kinetics -\n'
            buffer += 'rV = Kinetics(t,x,DF);\n'
            buffer += '\n'
            buffer += '% Calculate the inputs -\n'
            buffer += 'uV = Input(t,x,DF);\n'
            buffer += '\n'
            buffer += '% Calculate the dxdt terms -\n'
            buffer += 'dxdt = STM*rV + uV;\n'
            buffer += '\n'
            buffer += 'return;\n'

            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    def buildMassActionSolveBalanceEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree,
                                                                    model_tree):

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
            buffer += 'function [TSIM,X,OUTPUT] = ' + str(function_name) + '(pDataFile,TSTART,TSTOP,Ts,DFIN)\n'
            buffer += '\n'
            buffer += '% Check to see if I need to load the datafile \n'
            buffer += 'if (~isempty(DFIN))\n'
            buffer += '\tDF = DFIN;\n'
            buffer += 'else\n'
            buffer += '\tDF = feval(pDataFile,TSTART,TSTOP,Ts,[]);\n'
            buffer += 'end;\n'
            buffer += '\n'
            buffer += '% Get reqd stuff from data struct - \n'
            buffer += 'IC = DF.INITIAL_CONDITION_VECTOR;\n'
            buffer += 'TSIM = TSTART:Ts:TSTOP;\n'
            buffer += 'MEASUREMENT_INDEX_VECTOR = DF.MEASUREMENT_SELECTION_VECTOR;\n'
            buffer += '\n'
            buffer += '% Call the ODE solver - the default is ODE15s\n'
            buffer += 'pMassBalances = @(x,t)BalanceEquations(x,t,DF);\n'
            buffer += 'X = lsode(pMassBalances,IC,TSIM);\n'
            buffer += '\n'
            buffer += '% Calculate the output - \n'
            buffer += 'OUTPUT = X(:,MEASUREMENT_INDEX_VECTOR);\n'
            buffer += '\n'
            buffer += '% return to caller -\n'
            buffer += 'return;\n'

            return buffer

        else:
            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    def buildMassActionKineticsEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree,
                                                                model_tree):

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

            # Fill the buffer ...
            buffer += 'function rV = ' + function_name + '(t,x,DF)\n'
            buffer += '\n'
            buffer += '% Get the parameter vector - \n'
            buffer += 'kV = DF.KINETIC_PARAMETER_VECTOR;\n'
            buffer += '\n'
            buffer += '% Alias the species for debugging - \n'

            species_symbol_list = model_tree.mySpeciesSymbolList
            species_counter = 1
            for species_symbol in species_symbol_list:

                if not species_symbol == '[]':
                    buffer += species_symbol + ' = x(' + str(species_counter) + ',1);\n'
                    species_counter += 1

            buffer += '\n'
            buffer += '% Calculate the rate vector - \n'
            interaction_name_list = model_tree.myInteractionNameList
            reaction_counter = 1
            for local_reaction_name in interaction_name_list:

                buffer += 'rV(' + str(reaction_counter) + ',1) = kV(' + str(reaction_counter) + ',1)'

                # look up reaction_stoichiometric_map
                reaction_stoichiometric_map = model_tree.myDictionaryOfInteractionModels[local_reaction_name]
                for (local_species_symbol, stcoeff) in reaction_stoichiometric_map.iteritems():

                    if not local_species_symbol == 'raw_interaction_string' and not local_species_symbol == '[]':
                        if float(stcoeff) < 0.0:
                            buffer += '*((' + local_species_symbol + ')^' + str(-1 * stcoeff) + ')'

                buffer += ';\n'
                reaction_counter += 1

            buffer += '\n'
            buffer += 'return;\n'

            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    def buildMassActionInputEquationsForOctaveMWithModelTree(self, transformation_name, transformation_tree,model_tree):

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

            # Fill the buffer ...
            buffer += 'function uV = ' + function_name + '(t,x,DF)\n'
            buffer += '\n'
            buffer += '% Get the number of states - \n'
            buffer += 'number_of_states = DF.NUMBER_OF_STATES;\n'
            buffer += '\n'
            buffer += '% Default is to return a vector of zeros - \n'
            buffer += 'uV = zeros(number_of_states,1);\n'
            buffer += '\n'
            buffer += 'return;\n'

            return buffer

        else:

            raise Exception("Error while executing " + str(__name__) + ". Missing transformation component dictionary?")

        return "Code stuff goes here ..."

    # ----------------------------------------------------------------------------------------------------------------#