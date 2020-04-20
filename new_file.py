import re

# PATRON = 'Hola' # None
# PATRON = '.*Hola' # <re.Match object; span=(0, 10), match='Amigo Hola'> * == numero de veces incluido zero
# PATRON = '.*Hola$' # None, porque $ significa que acabe ayi
# TEXTO='Amigo Hola Amigo'

# PATRON = '.*Hola$' # Process finished with exit code 0, porque $ significa que acabe alli
# TEXTO='Amigo Hola'

# TEXTO='Amigo Hola Amigo'
# PATRON = '.+Hola' # <re.Match object; span=(0, 10), match='Amigo Hola'> + == al menos una vez, pero tiene q haber un caracter previo

# TEXTO='Hola Amigo'
# PATRON = '.+Hola' # None + == al menos una vez, pero tiene q haber un caracter previo

# TEXTO='Hola'
# PATRON = '.?Hola' # <re.Match object; span=(0, 4), match='Hola'> ? == puede o no aparecer, pero si aparece solo al menos una vez


# TEXTO='aHola'
# PATRON = '.?Hola' # <re.Match object; span=(0, 5), match='aHola'> ? == puede o no aparecer, pero si aparece solo al menos una vez

# TEXTO='aaHola'
# PATRON = '.?Hola' # None ? == puede o no aparecer, pero si aparece solo al menos una vez

# [] va a parecer un caracter dentro de los corchetes
# PATRON = '[a-z]' # <re.Match object; span=(0, 1), match='a'>, busca un caracter dentro de los corchetes
# TEXTO='amigos'

# PATRON = '[a-z]+' # <re.Match object; span=(0, 6), match='amigos'>,
# TEXTO='amigos'

# PATRON = '[a-z]+' # <re.Match object; span=(0, 2), match='am'>
# TEXTO='amIgos'

# PATRON = '[a-zA-Z]+' # <re.Match object; span=(0, 6), match='amIgos'>
# TEXTO='amIgos'

# PATRON = '[a-zA-Z]+' # <re.Match object; span=(0, 4), match='amIg'>
# TEXTO='amIg0s'

# | == significa O
# PATRON = 'a|b' # <re.Match object; span=(0, 1), match='a'>
# TEXTO='amIg0s'

# con () se agrupan
# PATRON = '(w|q)|m' # None
# TEXTO='amIg0s'

# PATRON = '(w|q)|a' # <re.Match object; span=(0, 1), match='a'>

TEXTO='amIg0s+'
# PATRON = 'a|[+]' # <re.Match object; span=(0, 1), match='a'>, que tiene la a o el mas

PATRON = 'z|[+]' # None

result = re.match(PATRON, TEXTO)

print(result)