from os.path import expanduser
import glob
import os.path
import json

class Utils:
    def __init__(self):
        print('Init Utils')

    def getLastFileUsers(self,username):
        home = expanduser("~")
        pathOfLogs = (home + '\\' + 'InstaPy\\logs\\'+ username + '\\relationship_data\\' + username + '\\following\\')
        fileType = '\\*json'
        files = glob.glob(pathOfLogs + fileType)
        max_file = max(files,key=os.path.getctime)
        print(max_file)
        jsonFile = open(max_file,'r')
        jsonConverted = json.load(jsonFile)
        return jsonConverted

    def getListOfToComment(self,json,qtdUsers,qtdUserPerComment):
        listOfUsers = json
        totalList = qtdUsers * qtdUserPerComment
        i = 0
        mapOfQntUserPerComment = {}
        while i < totalList:
            x = i
            while x < i + qtdUserPerComment:
                if i in mapOfQntUserPerComment:
                    listAux = mapOfQntUserPerComment.get(i)
                    listAux.append('@{' + listOfUsers[x]+'}')
                    mapOfQntUserPerComment[i] = listAux
                else: 
                    mapOfQntUserPerComment[i] = ['@{' + listOfUsers[x]+'}']
                x += 1
                
            i += qtdUserPerComment

        return mapOfQntUserPerComment

        #print(jsonConverted)
        #for x in jsonConverted:
        #    print(x)

        """   def getListOfToComment(self,json,qtdUsers,qtdUserPerComment):
        listOfUsers = json
        totalList = qtdUsers * qtdUserPerComment
        i = 0
        mapOfQntUserPerComment = {}
        while i < totalList:
            x = i
            while x < i + qtdUserPerComment:
                if i in mapOfQntUserPerComment:
                    listAux = mapOfQntUserPerComment.get(i)
                    listAux.append(listOfUsers[x])
                    mapOfQntUserPerComment[i] = listAux
                else: 
                    mapOfQntUserPerComment[i] = [listOfUsers[x]]
                x += 1
                
            i += qtdUserPerComment

        return mapOfQntUserPerComment """


    