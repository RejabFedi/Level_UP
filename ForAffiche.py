from py2neo import Graph, Node, Relationship
import listOfLevelsOP

def totalWordsInLevel (nameLevel) :
    graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
    result = graph.run(
        "MATCH (:Level{A1})-->(n:Word ) RETURN count(n) as count".format(A1="{name:'"+nameLevel+"'}")
    ).evaluate()
    return result

def usedUnusedWOrdsInLevel (nameLevel,list) :
    used =0
    for i in list :
        if i == nameLevel :
           used+=1
    unused=totalWordsInLevel(nameLevel)-used
    return [unused,used]
