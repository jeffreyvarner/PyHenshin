import pdb

class MyPyHenshinIntermediateModelObject(object):

    def __init__(self):
        self._myDictionaryOfSpeciesModels = None
        self._myDictionaryOfInteractionModels = None

    def __del__(self):
        self._myDictionaryOfSpeciesModels = None
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

            reactant_model = {}
            for symbol in reactant_species_list:
                local_species_model = {}
                local_species_model['symbol'] = symbol
                local_species_model['compartment'] = 'model'

                reactant_model[symbol] = local_species_model

            product_model = {}
            for symbol in product_species_list:
                local_species_model = {}
                local_species_model['symbol'] = symbol
                local_species_model['compartment'] = 'model'

                product_model[symbol] = local_species_model

            species_model = dict(reactant_model.items()+product_model.items())
            for (key, value) in species_model.iteritems():
                self.addSpeciesSymbolToSpeciesDictionary(key, value)


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
