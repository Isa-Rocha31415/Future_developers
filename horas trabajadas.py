# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:33:56 2020

@author: IsaUnicorn
"""

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 4   )
print("Tu paga es " + str(paga))

