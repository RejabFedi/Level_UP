from py2neo import Graph, Node, Relationship
import createListOfWords

class Create:
    graph = Graph(host="localhost", user="neo4j", password="123", port=7687)

    def create_level_node(id_level, level_name):
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
        level_name = Node("Level", name=level_name, id=id_level)
        graph.create(level_name)
        return level_name

    def create_word_node(word_name):
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
        word_name = Node("Word", name=word_name)
        graph.create(word_name)
        return word_name

    def create_relationship(a, b):
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687)
        Relation = Relationship(a, "Contains", b)
        graph.create(Relation)


    def creation (listWord):
        levels = ["A1", "A2", "B1", "B2","C"]
        idLevel = 0


        for k in range(len(levels)):
            if k < 4:
                firstWord = listWord.index(levels[k])
                lastWord = listWord.index(levels[k+1])
                levelWords = listWord[firstWord + 1:lastWord]
                a = Create.create_level_node(idLevel, levels[k])
                for i in range(len(levelWords)):
                    b = Create.create_word_node(levelWords[i])
                    Create.create_relationship(a, b)
                    idLevel += 1


            else:
                firstWord = listWord.index(levels[k])
                levelWords = listWord[firstWord + 1:]
                a = Create.create_level_node(idLevel, levels[k])

                for i in range(len(levelWords)):
                    b = Create.create_word_node(levelWords[i])
                    Create.create_relationship(a, b)
                    idLevel += 1








