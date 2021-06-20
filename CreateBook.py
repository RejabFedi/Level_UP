from py2neo import Graph, Node, Relationship


class Create:
    graph = Graph(host="localhost", user="neo4j", password="123", port=7687 )

    def create_Book(id_Book, Book_name):
        name = Book_name
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687 )
        Book_name = Node("Book", id=id_Book, name=name)
        graph.create(Book_name)
        return Book_name

    def create_unit(id_unit, unit_name):
        name = unit_name
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687 )
        Unit_name = Node("Unit", id=id_unit, name=name)
        graph.create(Unit_name)
        return Unit_name

    def create_activity(id_activity, unit_name):
        name = unit_name
        graph = Graph(host="localhost", user="neo4j", password="123", port=7687 )
        activity_name = Node("Activity", id=id_activity, name=name)
        graph.create(activity_name)
        return activity_name



