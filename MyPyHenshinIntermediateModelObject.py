import pdb

class MyPyHenshinIntermediateModelObject(object):

    def __init__(self):
        self._myListOfSpeciesModels = None
        self._myDictionaryOfInteractionModels = None

    def __del__(self):
        self._myListOfSpeciesModels = None
        self._myDictionaryOfInteractionModels = None

    def extractSpeciesFromVLVFFReactionString(self, reaction_string, direction_factor):

        # Split around the +
        species_list = reaction_string.split('+')
        new_species_list = []
        stoichiometry_dictionary = {}
        for raw_species in species_list:
            if '*' in raw_species:

                species_symbol = raw_species.split('*')[1]
                new_species_list.append(species_symbol)

                # grab the stoichoimetry -
                stoichiometry_dictionary[species_symbol] = direction_factor*raw_species.split('*')[0]

            else:
                new_species_list.append(raw_species)

                # grab the stoichoimetry -
                stoichiometry_dictionary[raw_species] = direction_factor


        return (new_species_list,stoichiometry_dictionary)

    def initilizeMyIntermediateModelObjectWithVLFFModelDictionary(self, model_dictionary):

        reaction_name_array = model_dictionary['reaction_name_array']
        for reaction_name in reaction_name_array:

            # Get the reaction dictionary for this reaction name -
            reaction_component_array = model_dictionary[reaction_name]

            # reactant string -
            reactant_string = reaction_component_array[1]
            (reactant_species_list, reactant_stoichiometric_dictionary) = self.extractSpeciesFromVLVFFReactionString(reactant_string, -1.0)

            # product string -
            product_string = reaction_component_array[2]
            (product_species_list, product_stoichiometric_dictionary) = self.extractSpeciesFromVLVFFReactionString(product_string, 1.0)

            # build reaction model -
            reaction_model = dict(reactant_stoichiometric_dictionary.items()+product_stoichiometric_dictionary.items())
            self.addInteractionToInteractionDictionary(reaction_name, reaction_model)

            for symbol in reactant_species_list:
                self.addSpeciesSymbolToSpeciesList(symbol)

            for symbol in product_species_list:
                self.addSpeciesSymbolToSpeciesList(symbol)


    def addInteractionToInteractionDictionary(self, interaction_key, interaction_model):

        if self._myDictionaryOfInteractionModels is None:
            self._myDictionaryOfInteractionModels = {}

        self._myDictionaryOfInteractionModels[interaction_key] = interaction_model


    def addSpeciesSymbolToSpeciesList(self, species_model):

        if self._myListOfSpeciesModels is None:
            self._myListOfSpeciesModels = []

        if species_model not in self._myListOfSpeciesModels:
            if not species_model == '[]':
                self._myListOfSpeciesModels.append(species_model)


    @property
    def myDictionaryOfInteractionModels(self):
        return self._myDictionaryOfInteractionModels

    @myDictionaryOfInteractionModels.setter
    def myDictionaryOfInteractionModels(self, interaction_list):
        self._myDictionaryOfInteractionModels = interaction_list

    @property
    def myListOfSpeciesModels(self):
        return self._myListOfSpeciesModels

    @myListOfSpeciesModels.setter
    def myListOfSpeciesModels(self, species_list):
        self._myListOfSpeciesModels = species_list
