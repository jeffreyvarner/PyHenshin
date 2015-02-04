import pdb
from libsbml import *

class MyPyHenshinIntermediateModelObject(object):

    def __init__(self):
        self._myInteractionNameList = []
        self._mySpeciesSymbolList = None
        self._myDictionaryOfSpeciesModels = None
        self._myDictionaryOfInteractionModels = None
        self._myListOfRawReactionStrings = []

    def __del__(self):
        self._myInteractionNameList = None
        self._mySpeciesSymbolList = None
        self._myDictionaryOfSpeciesModels = None
        self._myDictionaryOfInteractionModels = None
        self._myListOfRawReactionStrings = None

    def __extractSpeciesFromVLVFFReactionString(self, reaction_string, direction_factor):

        # Split around the +
        species_list = reaction_string.split('+')
        new_species_list = []
        stoichiometry_dictionary = {}
        for raw_species in species_list:
            if '*' in raw_species:

                species_symbol = raw_species.split('*')[1]
                new_species_list.append(species_symbol)

                # grab the stoichoimetry -
                stoichiometry_dictionary[species_symbol] = direction_factor*float(raw_species.split('*')[0])

            else:
                new_species_list.append(raw_species)

                # grab the stoichoimetry -
                stoichiometry_dictionary[raw_species] = direction_factor


        return (new_species_list,stoichiometry_dictionary)

    def initilizeMyIntermediateModelObjectWithSBMLModelObject(self, model_object):

        # initialize -
        reaction_dictionary = {}
        reaction_name_array = []

        # Iterate through the species list -
        list_of_species = model_object.getListOfSpecies()
        for species_object in list_of_species:
            species_symbol = species_object.getId()
            self.addSpeciesSymbolToSpeciesSymbolList(species_symbol)

        # iterate through the list of reactions, and put into
        # the correct form -
        list_of_reactions = model_object.getListOfReactions()
        for reaction_object in list_of_reactions:

            # Get the reaction name -
            local_reaction_name = reaction_object.getName()
            reaction_name_array.append(local_reaction_name)

        # Set the list of reactions -
        self.myInteractionNameList = reaction_name_array

        pdb.set_trace()

    def initilizeMyIntermediateModelObjectWithVLFFModelDictionary(self, model_dictionary):

        # Iterate through reactions in natural order, before we do anything split the reversible steps -
        reaction_name_array = model_dictionary['reaction_name_array']
        local_reaction_name_array = []
        for reaction_name in reaction_name_array:

            # Get the reaction dictionary for this reaction name -
            reaction_component_dictionary = model_dictionary[reaction_name]

            # Is this reaction reversible?
            reversible_flag = reaction_component_dictionary['reaction_backward_flag']
            if reversible_flag == '-inf':
                # We have a reversible reaction .. need to split into two -

                # Update the names -
                reverse_name = reaction_name+'_reverse'
                local_reaction_name_array.append(reaction_name)
                local_reaction_name_array.append(reverse_name)

                # Create a new dictionary -
                reverse_reaction_component_dictionary = {}
                reverse_reaction_component_dictionary['reaction_name'] = reverse_name
                reverse_reaction_component_dictionary['reaction_left_side'] = reaction_component_dictionary['reaction_right_side']
                reverse_reaction_component_dictionary['reaction_right_side'] = reaction_component_dictionary['reaction_left_side']
                reverse_reaction_component_dictionary['reaction_backward_flag'] = '0'
                reverse_reaction_component_dictionary['reaction_forward_flag'] = reaction_component_dictionary['reaction_forward_flag']

                # update the original reaction -
                reaction_component_dictionary['reaction_backward_flag'] = '0'

                model_dictionary[reverse_name] = reverse_reaction_component_dictionary
            else:
                local_reaction_name_array.append(reaction_name)

        # Grad this order for later -
        self.myInteractionNameList = local_reaction_name_array
        for reaction_name in local_reaction_name_array:

            # Get the reaction dictionary for this reaction name -
            reaction_component_dictionary = model_dictionary[reaction_name]

            # reactant string -
            reactant_string = reaction_component_dictionary['reaction_left_side']
            (reactant_species_list, reactant_stoichiometric_dictionary) = self.__extractSpeciesFromVLVFFReactionString(reactant_string, -1.0)

            # product string -
            product_string = reaction_component_dictionary['reaction_right_side']
            (product_species_list, product_stoichiometric_dictionary) = self.__extractSpeciesFromVLVFFReactionString(product_string, 1.0)

            # build reaction model -
            reaction_model = dict(reactant_stoichiometric_dictionary.items()+product_stoichiometric_dictionary.items())
            reaction_model['raw_interaction_string'] = reactant_string+'-->'+product_string
            reaction_model['reactant_string'] = reactant_string
            self._myListOfRawReactionStrings.append(reactant_string+'-->'+product_string)
            self.addInteractionToInteractionDictionary(reaction_name, reaction_model)

            reactant_model = {}
            for symbol in reactant_species_list:

                if not symbol == "[]":
                    local_species_model = {}
                    local_species_model['symbol'] = symbol
                    local_species_model['compartment'] = 'model'
                    reactant_model[symbol] = local_species_model
                    self.addSpeciesSymbolToSpeciesSymbolList(symbol)

            product_model = {}
            for symbol in product_species_list:

                if not symbol == "[]":
                    local_species_model = {}
                    local_species_model['symbol'] = symbol
                    local_species_model['compartment'] = 'model'
                    product_model[symbol] = local_species_model

                self.addSpeciesSymbolToSpeciesSymbolList(symbol)

            species_model = dict(reactant_model.items()+product_model.items())
            for (key, value) in species_model.iteritems():
                self.addSpeciesSymbolToSpeciesDictionary(key, value)


    def addSpeciesSymbolToSpeciesSymbolList(self,species_symbol):

        if self._mySpeciesSymbolList is None:
            self._mySpeciesSymbolList = []

        if species_symbol not in self._mySpeciesSymbolList:
            self._mySpeciesSymbolList.append(species_symbol)

    def addInteractionToInteractionDictionary(self, interaction_key, interaction_model):

        if self._myDictionaryOfInteractionModels is None:
            self._myDictionaryOfInteractionModels = {}

        self._myDictionaryOfInteractionModels[interaction_key] = interaction_model


    def addSpeciesSymbolToSpeciesDictionary(self, species_key, species_model):

        if self._myDictionaryOfSpeciesModels is None:
            self._myDictionaryOfSpeciesModels = {}

        if species_key not in self._myDictionaryOfSpeciesModels:
            if not species_key == '[]':
                self._myDictionaryOfSpeciesModels[species_key] = species_model



    @property
    def myListOfRawReactionStrings(self):
        return self._myListOfRawReactionStrings


    @myListOfRawReactionStrings.setter
    def myListOfRawReactionStrings(self,interaction_list):
        self._myListOfRawReactionStrings = interaction_list

    @property
    def myInteractionNamelList(self):
        return self._myInteractionNameList

    @myInteractionNamelList.setter
    def myInteractionNameList(self, interaction_name_list):
        self._myInteractionNameList = interaction_name_list

    @property
    def mySpeciesSymbolList(self):
        return self._mySpeciesSymbolList

    @mySpeciesSymbolList.setter
    def mySpeciesSymbolList(self,species_list):
        self._mySpeciesSymbolList = species_list

    @property
    def myDictionaryOfInteractionModels(self):
        return self._myDictionaryOfInteractionModels

    @myDictionaryOfInteractionModels.setter
    def myDictionaryOfInteractionModels(self, interaction_list):
        self._myDictionaryOfInteractionModels = interaction_list

    @property
    def myDictionaryOfSpeciesModels(self):
        return self._myDictionaryOfSpeciesModels

    @myDictionaryOfSpeciesModels.setter
    def myDictionaryOfSpeciesModels(self, species_list):
        self._myDictionaryOfSpeciesModels = species_list
