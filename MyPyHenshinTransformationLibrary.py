from MyPyHenshinAbstractTransformation import MyPyHenshinAbstractTransformation
from MyPyHenshinOctaveMLanguageLibrary import MyPyHenshinOctaveMLanguageLibrary
from MyPyHenshinOctaveCLanguageLibrary import MyPyHenshinOctaveCLanguageLibrary
from MyPyHenshinPythonLanguageLibrary import MyPyHenshinPythonLanguageLibrary
import pdb

class MyPyHenshinMAModelTransformation(MyPyHenshinAbstractTransformation):

    def __init__(self, rule_tree):
        self.model_class = 'MA'
        self.rule_tree = rule_tree

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):

        program_dictionary = {}
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                component_dictionary = transformation_dictionary[key_value]
                transformation_class = component_dictionary['transformation_class']
                file_name = component_dictionary['file_name']

                # We need to figure out what method to execute -
                model_language_array = (self.rule_tree[self.model_class])
                number_of_languages = len(model_language_array)
                for language_index in range(0, number_of_languages):

                    language = model_language_array[language_index].keys()[0]
                    if language == output_language_type_flag:

                        # Lookup the methods name -
                        method_name = model_language_array[language_index][output_language_type_flag][0][transformation_class]

                        # lookup the correct library -
                        if output_language_type_flag == 'Octave-M':
                            library_instance = MyPyHenshinOctaveMLanguageLibrary()
                            method = getattr(library_instance, method_name)

                            if not method:
                                raise Exception("Method %s not implemented" % method_name)

                            # Execute method -
                            program_buffer = method(key_value, transformation_tree, model_tree)
                            program_dictionary[file_name] = program_buffer

                        elif output_language_type_flag == 'Octave-C':
                            library_instance = MyPyHenshinOctaveCLanguageLibrary()
                            method = getattr(library_instance, method_name)

                            if not method:
                                raise Exception("Method %s not implemented" % method_name)

                            # Execute method -
                            program_buffer = method(key_value, transformation_tree, model_tree)
                            program_dictionary[file_name] = program_buffer

                        elif output_language_type_flag == 'Python':
                            library_instance = MyPyHenshinPythonLanguageLibrary()
                            method = getattr(library_instance, method_name)

                            if not method:
                                raise Exception("Method %s not implemented" % method_name)

                            # Execute method -
                            program_buffer = method(key_value, transformation_tree, model_tree)
                            program_dictionary[file_name] = program_buffer

        return program_dictionary

class MyPyHenshinFBAModelTransformation(MyPyHenshinAbstractTransformation):

    def __init__(self, rule_tree):
        self.model_class = 'FBA'
        self.rule_tree = rule_tree

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):

        program_dictionary = {}
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                component_dictionary = transformation_dictionary[key_value]
                transformation_class = component_dictionary['transformation_class']
                file_name = component_dictionary['file_name']

                # We need to figure out what method to execute -
                model_language_array = (self.rule_tree[self.model_class])
                number_of_languages = len(model_language_array)
                for language_index in range(0, number_of_languages):

                    language = model_language_array[language_index].keys()[0]
                    if language == output_language_type_flag:

                        # Lookup the methods name -
                        method_name = model_language_array[language_index][output_language_type_flag][0][transformation_class]

                        # lookup the correct library -
                        if output_language_type_flag == 'Octave-M':
                            library_instance = MyPyHenshinOctaveMLanguageLibrary()
                            method = getattr(library_instance, method_name)

                            if not method:
                                raise Exception("Method %s not implemented" % method_name)

                            # Execute method -
                            program_buffer = method(key_value, transformation_tree, model_tree)
                            program_dictionary[file_name] = program_buffer

        return program_dictionary

class MyPyHenshinCellFreeModelTransformation(MyPyHenshinAbstractTransformation):

    def __init__(self, rule_tree):
        self.model_class = 'CELL_FREE'
        self.rule_tree = rule_tree

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):

        program_dictionary = {}
        transformation_component_array = transformation_tree['transformation_component_array']
        for transformation_dictionary in transformation_component_array:
            for key_value in transformation_dictionary:
                component_dictionary = transformation_dictionary[key_value]
                transformation_class = component_dictionary['transformation_class']
                file_name = component_dictionary['file_name']

                # We need to figure out what method to execute -
                model_language_array = (self.rule_tree[self.model_class])
                number_of_languages = len(model_language_array)
                for language_index in range(0, number_of_languages):

                    language = model_language_array[language_index].keys()[0]
                    if language == output_language_type_flag:

                        # Lookup the methods name -
                        method_name = model_language_array[language_index][output_language_type_flag][0][transformation_class]

                        # lookup the correct library -
                        if output_language_type_flag == 'Octave-M':
                            library_instance = MyPyHenshinOctaveMLanguageLibrary()
                            method = getattr(library_instance, method_name)

                            if not method:
                                raise Exception("Method %s not implemented" % method_name)

                            # Execute method -
                            program_buffer = method(key_value, transformation_tree, model_tree)
                            program_dictionary[file_name] = program_buffer

        return program_dictionary


class MyPyHenshinHCFLModelTransformation(MyPyHenshinAbstractTransformation):

    def executeTransformationUsingIntermediateTree(self, transformation_tree, model_tree, input_language_type_flag, model_type_flag, output_language_type_flag):
        print "MyPyHenshinHCFLModelTransformation execute transformation method"