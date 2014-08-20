import pdb
from MyPyHenshinAbstractParser import MyPyHenshinAbstractParser
from MyPyHenshinIntermediateModelObject import MyPyHenshinIntermediateModelObject


class MyPyHenshinVLNLFFParser(MyPyHenshinAbstractParser):

    def buildModelTreeFromInputURL(self, path_to_input_file):
        print "In VLNFF subclass - "+str(path_to_input_file)


class MyPyHenshinSBMLParser(MyPyHenshinAbstractParser):

    def buildModelTreeFromInputURL(self, path_to_input_file):
        print "In SBML subclass - "+str(path_to_input_file)


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
                if not line.startswith('#'):

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
                    local_array = []
                    local_array.append(reaction_name)
                    local_array.append(reaction_left_side)
                    local_array.append(reaction_right_side)
                    local_array.append(reaction_backward_flag)
                    local_array.append(reaction_forward_flag)
                    reaction_dictionary[reaction_name] = local_array

        input_text_file.close()
        reaction_dictionary['reaction_name_array'] = reaction_name_array

        # ok, so we have the reaction dictionary, we need to convert this into the model tree
        model_object = MyPyHenshinIntermediateModelObject()
        model_object.initilizeMyIntermediateModelObjectWithVLFFModelDictionary(reaction_dictionary)

        # return -
        return model_object