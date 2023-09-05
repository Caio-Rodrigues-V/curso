from datetime import datetime

dataANI = datetime.strptime(input('quand é seu aniversario ? '),'%d/%m/%Y')
print(dataANI)

data_atual = datetime.now()

quanto_falta = dataANI - data_atual 

print(quanto_falta.days)