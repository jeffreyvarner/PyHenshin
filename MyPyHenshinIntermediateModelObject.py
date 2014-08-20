import pdb

class MyPyHenshinIntermediateModelObject(object):

    def __init__(self):
        self._myListOfSpecies = None

    def __del__(self):
        self._myListOfSpecies = None

    def extractSpeciesFromVLVFFReactionString(self, reaction_string):

        # Split around the +
        species_list = reaction_string.split('+')
        new_species_list = []
        for raw_species in species_list:
            if '*' in raw_species:

                species_symbol = raw_species.split('*')[1]
                new_species_list.append(species_symbol)

            else:
                new_species_list.append(raw_species)

        return new_species_list

    def initilizeMyIntermediateModelObjectWithVLFFModelDictionary(self, model_dictionary):

        reaction_name_array = model_dictionary['reaction_name_array']
        for reaction_name in reaction_name_array:

            # Get the reaction dictionary for this reaction name -
            reaction_component_array = model_dictionary[reaction_name]

            # reactant string -
            reactant_string = reaction_component_array[1]
            reactant_species_list = self.extractSpeciesFromVLVFFReactionString(reactant_string)

            # product string -
            product_string = reaction_component_array[2]
            product_species_list = self.extractSpeciesFromVLVFFReactionString(product_string)

            for symbol in reactant_species_list:
                self.addSpeciesSymbolToSpeciesList(symbol)

            for symbol in product_species_list:
                self.addSpeciesSymbolToSpeciesList(symbol)

    def addSpeciesSymbolToSpeciesList(self, species_model):

        if self._myListOfSpecies == None:
            self._myListOfSpecies = []

        if species_model not in self._myListOfSpecies:
            if not species_model == '[]':
                self._myListOfSpecies.append(species_model)

    @property
    def myListOfSpecies(self):
        return self._myListOfSpecies

    @myListOfSpecies.setter
    def myListOfSpecies(self, species_list):
        self._myListOfSpecies = species_list
