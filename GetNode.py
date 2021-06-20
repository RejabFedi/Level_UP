from py2neo import Graph
from py2neo.matching import *


def Match_nodes(Type_node, Name_node):
    graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
    matcher = NodeMatcher(graph)
    a = matcher.match(Type_node, name=Name_node).first()

    return a

if __name__ == "__main__":
    print(Match_nodes('Tence','will future'))







