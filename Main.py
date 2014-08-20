import argparse
import sys
import json
import pdb
import numpy
from MyPyHenshinParserLibrary import *
from MyPyHenshinTransformationLibrary import *


def main(argv):

    # initialize -
    model_input_parser = None
    model_transformation_manager = None

    arg_parser = argparse.ArgumentParser(description='Generate simulation and optimization code using PyHenshin')
    arg_parser.add_argument('-i', '--transformation-input-path', type=str, required=True, help='Path to Henshin input file')
    arg_parser.add_argument('-o', '--transformation-output-path', type=str, required=True, help='Path to model output files')
    args_list = arg_parser.parse_args(argv[1:])

    # Ok, so we need to process the input file -
    input_file_path = args_list.transformation_input_path
    transformation_dictionary = processHenshinTransformationInputFileAtPath(input_file_path)

    # Match based upon input type, and build the correct parser -
    input_language_flag = transformation_dictionary.get("transformation_input_type")
    if input_language_flag == 'SBML':
        model_input_parser = MyPyHenshinSBMLParser()

    elif input_language_flag == 'VLFF':
        model_input_parser = MyPyHenshinVLFFParser()

    elif input_language_flag == 'VLNLFF':
        model_input_parser = MyPyHenshinVLNLFFParser()

    else:
        print "Unsupported input file type"
        exit(-1)

    # Next, we need to build the transformation manager -
    language_type_flag = transformation_dictionary.get("transformation_output_language_type")
    model_type_flag = transformation_dictionary.get("transformation_model_class")
    if model_type_flag == "MA":
        model_transformation_manager = MyPyHenshinMAModelTransformation()

    elif model_type_flag == "FBA":
        model_transformation_manager = MyPyHenshinFBAModelTransformation()

    elif model_type_flag == "HCFL":
        model_transformation_manager = MyPyHenshinHCFLModelTransformation()

    else:
        print "Unsupported model type"
        exit(-1)

    # execute the parser -
    input_file_url = transformation_dictionary['transformation_input_url']
    intermediate_model_tree = model_input_parser.buildModelTreeFromInputURL(input_file_url)

    pdb.set_trace()

    # hand the model tree to the transformation manager -
    model_componenent_dictionary = model_transformation_manager.executeTransformationUsingIntermediateTree(intermediate_model_tree)

    # write the model components to disk -
    path_to_model_components = args_list.model_output_path
    writeModelComponentsToDiskAtPath(path_to_model_components, model_componenent_dictionary)


def writeModelComponentsToDiskAtPath(path_to_model_components, model_component_dictionary):
    pass

def processHenshinTransformationInputFileAtPath(path_to_input_file):

    # Initialize -
    transformation_dictionary = {}

    # load json data -
    json_data = open(path_to_input_file)
    data = json.load(json_data)
    json_data.close()

    # process the transformation_type block -
    transformation_type_block = data['transformation_type']
    for (key, value) in transformation_type_block.iteritems():
        transformation_dictionary[key] = value


    # process the list_of_transformation_components block -
    list_of_transformation_components_block = data['list_of_transformation_components']
    number_of_transformations = len(list_of_transformation_components_block)
    transformation_block = []
    for transformation_index in range(0,number_of_transformations):
        local_dictionary = list_of_transformation_components_block[transformation_index]

        # local dictionary has a single key - dictionary linkage
        temp_dictionary = {}
        for (key, value) in local_dictionary.iteritems():
            temp_dictionary[key] = value

    transformation_block.append(temp_dictionary)

    # Store the block -
    transformation_dictionary['transformation_component_array'] = transformation_block

    # return -
    return transformation_dictionary

# Boiler plate code for launching main -
if __name__ == '__main__':
    main(sys.argv)