import dictionary as d
import richWord as rw

dz = d.Dictionary()


class MultiDictionary:

    def __init__(self):
        self._dizionari = {"italian": dz.loadDictionary("resources/Italian.txt"),
                           "english": dz.loadDictionary("resources/English.txt"),
                           "spanish": dz.loadDictionary("resources/Spanish.txt")}


    def printDic(self, language):
        print(self._dizionari[language.lower()])

    def searchWord(self, words, language):
        errate = []
        diz = self._dizionari[language.lower()]
        for word in words:
            if not word in diz:
                errate.append(word)
        print("Parole errate using contains: ")
        if len(errate) == 0:
            print("Nessuna parola errata rilevata")
        for word in errate:
            print(word)
        return errate

    def searchWordLinear(self, words, language):
        errate = []
        diz = self._dizionari[language.lower()]
        for word in words:
            for i in range(len(diz)):
                if diz[i] == word:
                    break
                if diz[i] != word and i == len(diz) - 1:
                    errate.append(word)
        print("Parole errate using linear search: ")
        if len(errate) == 0:
            print("Nessuna parola errata rilevata")
        for word in errate:
            print(word)
        return errate


    def searchWordDichotomic(self, words, language):
        errate = []
        diz = self._dizionari[language.lower()]
        l = len(diz)
        ref = diz[int(l / 2)]
        for word in words:
            if word > ref:
                for i in range(int(l / 2), l):
                    if diz[i] == word:
                        break
                    if diz[i] != word and i == l - 1:
                        errate.append(word)
            if word < ref:
                for i in range(0, int(l / 2)):
                    if diz[i] == word:
                        break
                    if diz[i] != word and i == int(l / 2) - 1:
                        errate.append(word)
            if word == ref:
                continue
        print("Parole errate using dichotomic search: ")
        if len(errate) == 0:
            print("Nessuna parola errata rilevata")
        for word in errate:
            print(word)
        return errate


if __name__ == "__main__":
    pass
