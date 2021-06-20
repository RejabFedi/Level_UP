from py2neo import Graph, Node, Relationship


class CreateTenseNodes:
    graph = Graph(host="localhost", user="neo4j", password="123", port=7687)



    def create_Tense( Tense_name):
        name = Tense_name
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
        Tense = Node("Tense", name=name)
        graph.create(Tense)
        return Tense

    def create_Tenses(Tences):
        name = Tences
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
        Tenses = Node("Tenses", name=name)
        graph.create(Tenses)
        return Tenses



