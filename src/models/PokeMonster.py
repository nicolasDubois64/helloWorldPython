class PokeMonster:

    def __init__(self, name, mainType):
        self.name = name
        self.mainType = mainType

    def printInfos(self):
        msg = "{0}: pokemon de type {1}.".format(self.name, self.mainType)
        print(msg)

