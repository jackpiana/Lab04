class Dictionary:
    def __init__(self):
        self._diz = None

    def loadDictionary(self, path):
        diz = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parole = line.strip().split()
                if len(parole) == 1:
                    diz.append(parole[0])
        self._diz = diz
        return diz

    def printAll(self):
        print(self._diz)

    @property
    def dict(self):
        return self._dict
