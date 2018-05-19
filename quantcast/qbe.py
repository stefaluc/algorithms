#!/usr/bin/python
from sys import stdin
import json

documents = []

def docDoesMatch(document, getRequest):
    propsToMatch = getRequest.keys()
    isValidDoc = True
    for prop in propsToMatch:
        if prop in document:
            if type(document[prop]) is list and type(getRequest[prop]) is list:
                for listItem in getRequest[prop]:
                    if listItem not in document[prop]:
                        isValidDoc = False
                        break
            elif type(document[prop]) is dict and type(getRequest[prop]) is dict:
                # recurse through nested json
                if not docDoesMatch(document[prop], getRequest[prop]):
                    isValidDoc = False
                    break
                # propsToMatch2 = getRequest[prop].keys()
                # isValidDoc2 = True
                # for prop2 in propsToMatch2:
                #     if prop2 in document[prop]:
                #         if not document[prop][prop2] == getRequest[prop][prop2]:
                #             isValidDoc2 = False
                #             break
                #     else:
                #         isValidDoc2 = False
                #         break
                # if not isValidDoc2:
                #     isValidDoc = False
                #     break
            else:
                if not document[prop] == getRequest[prop]:
                    isValidDoc = False
                    break
        else:
            isValidDoc = False
            break
    return isValidDoc

def deleteFromDocuments(deleteRequest):
    global documents
    # print 'delete request'
    # for document in documents:
    #     print document
    #     print deleteRequest
    #     if docDoesMatch(document, deleteRequest):
    #         print 'reached delete'
    #         documents.remove(document)
    documents[:] = [document for document in documents if not docDoesMatch(json.loads(document), deleteRequest)]

def getFromDocuments(getRequest):
    global documents
    for document in documents:
        if docDoesMatch(json.loads(document), getRequest):
            print document
            #return

def addToDocuments(document):
    documents.append(document)

def process(command, data):
    jsonData = json.loads(data)
    if command == 'add':
        addToDocuments(data)
    elif command == 'get':
        getFromDocuments(jsonData)
    elif command == 'delete':
        deleteFromDocuments(jsonData)
    else:
        print 'shouldn\'t reach'

def main():
    for line in stdin:
        input = line.split(' ', 1)
        process(input[0], input[1].replace('\n', ''))
    
main()
