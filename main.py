from alphabet import alph as alph
from alphabet import list as list
m = []
def strToMorse(str):
  for x in str:
    if x in alph:
      pos = alph.index(x)
      morse = list[pos]
      m.extend(morse)
  string2 = ''
  print(string2.join(m))

string = input('Enter string to convert to morse code: ')
string = string.lower()
strToMorse(string)
