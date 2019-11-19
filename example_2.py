#pip install neo4jrestclient
#Retirado do site: https://marcobonzanini.com/2015/04/06/getting-started-with-neo4j-and-python/

from neo4jrestclient.client import GraphDatabase 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="admin")
 
# Create some nodes with labels
user = db.labels.create("User")
u1 = db.nodes.create(name="Marco")
user.add(u1)
u2 = db.nodes.create(name="Daniela")
user.add(u2)
 
beer = db.labels.create("Beer")
b1 = db.nodes.create(name="Punk IPA")
b2 = db.nodes.create(name="Hoegaarden Rosee")
# You can associate a label with many nodes in one go
beer.add(b1, b2)

# User-likes->Beer relationships
u1.relationships.create("likes", b1)
u1.relationships.create("likes", b2)
u2.relationships.create("likes", b1)
# Bi-directional relationship?
u1.relationships.create("friends", u2)

#Rodar no browser a query:
#MATCH (n)-[r]->(m) RETURN n, r, m;