from rapidfuzz import fuzz
import re
"""hangi fonksiyonlar olacak

similarty check benzer kelimeleri yakalayıp editleyecek
otofiller boşluklu yazılmış kelimeleri  birleştiricek
longformer take slangs from a dictiolnary and will change them with longer version

"""
choosens = [""]
slang_dictionaray={
    "no.":"numara"
}
def similarity_check(will_edited):
    for choosen in choosens:
        if fuzz.ratio(choosen,will_edited)>70:
            return choosen
        else: return will_edited

def otofiller(will_edited):
    for i in will_edited:
        pass
def longformer(will_edited): 
    for slang in slang_dictionaray:
        if will_edited==slang:
            return slang_dictionaray[slang]

print(longformer("no."))