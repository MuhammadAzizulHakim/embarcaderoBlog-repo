from graph_tool.all import *
 
g = Graph()
ug = Graph(directed=False)
 
ug = Graph()
ug.set_directed(False)
assert ug.is_directed() == False
 
g1 = Graph()
g2 = Graph(g1)
 
v1 = g.add_vertex()
v2 = g.add_vertex()
 
e = g.add_edge(v1, v2)
graph_draw(g, vertex_text=g.vertex_index, output="two-nodes.png")

# Use the "football" dataset
g = graph_tool.collection.data["football"]
print(g)
print(g.gp.readme)
print(g.gp.description)

state = graph_tool.inference.minimize_blockmodel_dl(g)
state.draw(pos=g.vp.pos, output="football-sbm-fit.svg")