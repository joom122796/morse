from alphabet import alph as alph
from alphabet import list as list
from alphabet import m as m

def morseEncode(str):
  str = str.lower()
  for x in str:
    if x in alph:
      pos = alph.index(x)
      morse = list[pos]
      m.extend(morse+' ')
  encode = ''.join(m)
  print(encode)

string = input('Enter string to convert to morse code: ')
morseEncode(string)
