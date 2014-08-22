import pdb
import numpy
import random

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

                if not local_species_symbol == '[]':
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

            # program buffer -
            buffer = ''

            # Get the file name (we need this to get the function name -
            filename = component_dictionary['file_name']

            # Get the function name -
            function_name = filename.split('.')[0]

            buffer += "function DF = "+function_name+"(TSTART,TSTOP,Ts,INDEX)\n"
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
                raw_reaction_string = model_tree.myDictionaryOfInteractionModels[reaction_name]['raw_interaction_string']

                value = 0.0
                if '_reverse' in reaction_name:
                    value = random.gauss(1.0, 0.1)

                else:
                    value = random.gauss(10.0, 1.0)

                buffer +='\t'+str(value)+';\t% '+str(reaction_counter)+' '+reaction_name+"::"+raw_reaction_string+"\n"
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
                    buffer += '\t0.0;\t% '+str(species_counter)+' '+species_symbol+'\n'
                    species_counter += 1

            buffer += '];\n'
            buffer += '\n'
            buffer += '% == DO NOT EDIT BELOW THIS LINE ================================== \n'
            buffer += 'DF.NUMBER_OF_REACTIONS = number_of_reactions;\n'
            buffer += 'DF.NUMBER_OF_SPECIES = number_of_species;\n'
            buffer += 'DF.KINETIC_PARAMETER_VECTOR = KPV;\n'
            buffer += 'DF.INITIAL_CONDITION_VECTOR = ICV;\n'
            buffer += '% ================================================================= \n'
            buffer += 'return;\n'

            return buffer
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

            # Initialize an empty buffer -
            buffer = ''

            # Get the function name -
            function_name = filename.split('.')[0]

            # Fill the buffer ...
            buffer += 'function dxdt = '+function_name+'(x,t,DF)\n'
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

            # Initialize an empty buffer -
            buffer = ''

            # Get the function name -
            function_name = filename.split('.')[0]

            # Fill the buffer ...
            buffer += 'function rV = '+function_name+'(t,x,DF)\n'
            buffer += '\n'
            buffer += '% Alias the species for debugging - \n'

            species_symbol_list = model_tree.mySpeciesSymbolList
            species_counter = 1
            for species_symbol in species_symbol_list:

                if not species_symbol == '[]':
                    buffer += species_symbol + ' = x('+str(species_counter)+',1);\n'
                    species_counter += 1

            buffer += '\n'
            buffer += '% Calculate the rate vector - \n'
            interaction_name_list = model_tree.myInteractionNameList
            reaction_counter = 1
            for local_reaction_name in interaction_name_list:

                buffer += 'rV('+str(reaction_counter)+',1) = kV('+str(reaction_counter)+',1)'

                # look up reaction_stoichiometric_map
                reaction_stoichiometric_map = model_tree.myDictionaryOfInteractionModels[local_reaction_name]
                for (local_species_symbol,stcoeff) in reaction_stoichiometric_map.iteritems():

                    if not local_species_symbol == 'raw_interaction_string' and not local_species_symbol == '[]':
                        if float(stcoeff)<0.0:
                            buffer += '*(('+local_species_symbol+')^'+str(-1*stcoeff)+')'


                buffer += ';\n'
                reaction_counter += 1

            buffer += '\n'
            buffer += 'return;\n'

            return buffer

        else:

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

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
            buffer += 'function uV = '+function_name+'(t,x,DF)\n'
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

            raise Exception("Error while executing "+str(__name__)+". Missing transformation component dictionary?")

        return "Code stuff goes here ..."