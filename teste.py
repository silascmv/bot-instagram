import utils as util

utilitario =  util.Utils()
listOfUsers = utilitario.getLastFileUsers('stechsolucoesdigitais')
print(utilitario.getListOfToComment(listOfUsers,10,4))



#print(listOfUsers)
""" qntDeComentarios = 10
qntUserPerComent = 2
totalList = qntUserPerComent * qntDeComentarios

i = 0
# MAP OF KEY-WHENEVER - VALUE QUANTIDADE DE USUÁRIOS POR COMENTÁRIO.
mapOfQntUserPerComment = {}
while i < totalList:
    x = i
    while x < i + qntUserPerComent:
        print(listOfUsers[x])
        if i in mapOfQntUserPerComment:
           listAux = mapOfQntUserPerComment.get(i)
           listAux.append(listOfUsers[x])
           mapOfQntUserPerComment[i] = listAux
        else: 
            mapOfQntUserPerComment[i] = [listOfUsers[x]]
        x += 1
        
    i += qntUserPerComent

print(mapOfQntUserPerComment) """