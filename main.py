# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys(audi):
    for value in audi.values():
      print(value, end = " ")

# def showObjectKeys(audi): # paprasciausias budas gauti zodyno values
#   print(list(audi.values()))

showObjectKeys(audi)


# audi_keys_value = audi.values() # pasitikrinu ar tikrai tokie value
# print(audi_keys_value)