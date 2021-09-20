# Necessario instalar o pyshorteners - disponivel em https://pypi.org/project/pyshorteners/ 

import pyshorteners

# Carrega lib
s = pyshorteners.Shortener()

# Recebe a URL original
url = input("Digite ou cole a URL a ser encurtada: ")

# Gera URL encurtada
short_url = s.tinyurl.short(url)

# Mostra resultado
print(f"\nURL Encurtada: {short_url}")