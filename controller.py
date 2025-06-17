import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        if txtIn is None or language is None or modality is None:
            self._view.create_alert("inserire tutti i parametri!")
            return
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                errate = self._multiDic.searchWord(words, language)
                t2 = time.time()
                tempo = (t2 - t1)
                self._view.add_output(tempo, errate)

            case "Linear":
                t1 = time.time()
                errate = self._multiDic.searchWordLinear(words, language)
                t2 = time.time()
                tempo = (t2 - t1)
                self._view.add_output(tempo, errate)


            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                t2 = time.time()
                tempo = (t2 - t1)
                self._view.add_output(tempo, parole)



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
