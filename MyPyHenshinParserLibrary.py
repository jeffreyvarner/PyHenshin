import pdb
from MyPyHenshinAbstractParser import MyPyHenshinAbstractParser
from MyPyHenshinIntermediateModelObject import MyPyHenshinIntermediateModelObject

class MyPyHenshinVLNLFFParser(MyPyHenshinAbstractParser):

    def buildModelTreeFromInputURL(self, path_to_input_file):
        print "In VLNFF subclass - "+str(path_to_input_file)

class MyPyHenshinSBMLParser(MyPyHenshinAbstractParser):

    def buildModelTreeFromInputURL(self, path_to_input_file):
        print "In SBML subclass - "+str(path_to_input_file)

class MyPyHenshinControlListParser(MyPyHenshinAbstractParser):

    def buildFBAControlFunctionListFromInputURL(self,path_to_input_file):

        input_text_file = open(path_to_input_file, "r")
        data_array = []
        for line_raw in input_text_file:

            # Strip the line -
            control_line = line_raw.rstrip('\n')

            # Check - is this an activate line?
            if 'activates' in control_line:

                # Split string to get source and targets -
                fragments = control_line.split('activates')

                # Source and targets -
                data_structure = []
                data_structure.append('activates')
                data_structure.append(fragments[0])
                data_structure.append(fragments[1])

                # Add data structure to array -
                data_array.append(data_structure)

            elif 'inhibits' in control_line:

                # Split string to get source and targets -
                fragments = control_line.split('inhibits')

                # Source and targets -
                data_structure = []
                data_structure.append('inhibits')
                data_structure.append(fragments[0])
                data_structure.append(fragments[1])

                # Add data structure to array -
                data_array.append(data_structure)

            elif 'induces' in control_line:

                # Split string to get source and targets -
                fragments = control_line.split('induces')

                # Source and targets -
                data_structure = []
                data_structure.append('induces')
                data_structure.append(fragments[0])
                data_structure.append(fragments[1])

                # Add data structure to array -
                data_array.append(data_structure)

            elif 'represses' in control_line:

                # Split string to get source and targets -
                fragments = control_line.split('represses')

                # Source and targets -
                data_structure = []
                data_structure.append('represses')
                data_structure.append(fragments[0])
                data_structure.append(fragments[1])

                # Add data structure to array -
                data_array.append(data_structure)

        return data_array


class MyPyHenshinSpeciesListParser(MyPyHenshinAbstractParser):

    def buildSpeciesListFromInputURL(self,path_to_input_file):

        input_text_file = open(path_to_input_file, "r")
        extracellular_species_list = []
        for line_raw in input_text_file:
            extracellular_species_list.append(line_raw.rstrip('\n'))

        return extracellular_species_list

class MyPyHenshinVLFFParser(MyPyHenshinAbstractParser):

    def buildModelTreeFromInputURL(self, path_to_input_file):

        # initialize -
        reaction_dictionary = {}
        reaction_name_array = []
        input_text_file = open(path_to_input_file, "r")
        for line_raw in input_text_file:

            # strip the spaces -
            line = line_raw.strip()

            # if not zero, or a comment -
            if not len(line) == 0:
                if not line.startswith('#') and not line.startswith('//'):

                    fragment_array = line.split(",")
                    number_of_fragments = len(fragment_array)
                    reaction_name = ""
                    reaction_left_side = ""
                    reaction_right_side = ""
                    reaction_backward_flag = ""
                    reaction_forward_flag = ""
                    for fragment_index in range(0, number_of_fragments):

                        value = fragment_array[fragment_index]
                        if fragment_index == 0:
                            reaction_name = value
                        elif fragment_index == 1:
                            reaction_left_side = value
                        elif fragment_index == 2:
                            reaction_right_side = value
                        elif fragment_index == 3:
                            reaction_backward_flag = value
                        elif fragment_index == 4:
                            reaction_forward_flag = value

                    # grab the name array -
                    reaction_name_array.append(reaction_name)

                    # build a reaction dictionary -
                    local_dictionary = {}
                    local_dictionary['reaction_name'] = reaction_name
                    local_dictionary['reaction_left_side'] = reaction_left_side
                    local_dictionary['reaction_right_side'] = reaction_right_side
                    local_dictionary['reaction_backward_flag'] = reaction_backward_flag
                    local_dictionary['reaction_forward_flag'] = reaction_forward_flag
                    reaction_dictionary[reaction_name] = local_dictionary

        input_text_file.close()
        reaction_dictionary['reaction_name_array'] = reaction_name_array

        # ok, so we have the reaction dictionary, we need to convert this into the model tree
        model_object = MyPyHenshinIntermediateModelObject()
        model_object.initilizeMyIntermediateModelObjectWithVLFFModelDictionary(reaction_dictionary)

        # return -
        return model_object