from py2neo import Graph

def findWord (word):


         graph = Graph(host="localhost",user="neo4j", password="123",port=7687)
         #result = graph.run("""MATCH (word:Word {})-[:Contains]-(p)RETURN p.name""".format('{name:"'+word+'"}'))
         re = graph.run("""MATCH (n1)-[:Contains]->(n2) WHERE n2.name='{}'RETURN  n1.name""".format(word))
         try:
             p = re.data()[-1]
             return p['n1.name']
         except IndexError:
             p = 'null'
             return p

         print(p)



if __name__ == "__main__":
    print(findWord('Present Perfect'))