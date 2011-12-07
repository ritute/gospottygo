import cursorhelpers as db
'''

Step #5: PageRank

Uses the Links database table to generate rankings of pages.

'''

class Node(object):
    def __init__(self,doc_id,url,outgoing_links=None, score =0):
        self.doc_id = doc_id
        self.url = url
        if outgoing_links==None:
            self.outgoing_links = [] 
        else:
            self.outgoing_links = outgoing_links
        self.num_outgoing = len(self.outgoing_links)
        self.score = score

    def add_outgoing_link(self,outnode):
        self.outgoing_links.append(outnode)
        self.num_outgoing=len(self.outgoing_links)
    
def load_graph():
    #tuples of (id,url)
    raw_nodes = db.Document.get_all_words()
    nodes = {tup[0]:Node(tup[0],tup[1]) for tup in raw_nodes}

    #tuples of (from, to, frequency)
    raw_edges = db.Link.get_all_edges()

    num_from = set([edge[0] for edge in raw_edges])
    num_to = set([edge[1] for edge in raw_edges])
    for edge in raw_edges:
        node1 = nodes[edge[0]]
        node2 = nodes[edge[1]]
        for i in range(edge[2]):
            node1.add_outgoing_link(node2)

    return nodes

def get_seed_nodes_and_set_seeds(nodes):
    """Identifies the seed nodes. Sets their seed values
    Returns a tuple of seed the nodes. Param nodes
    is a dictionary of """
    seed_file = open("../db/urllist.txt")
    seed_data = ( line.split("|") for line in seed_file)

    #list of seed nodes
    node_seed_list = []
    for node_url, seed_value in seed_data:
        try:
            node = nodes[db.Document.get_word_id(node_url)]
        except:
            #for whatever reason, the url in the 
            #urllist is not in our database
            continue
        node.score = int(seed_value)
        node_seed_list.append(node)

    return node_seed_list

def populate_page_rank():
    nodes_dict = compute_page_rank()
    nodes = nodes_dict.values()
    for node in nodes:
        db.PageRank.insert_page_rank(node.doc_id,node.score)

def compute_page_rank():
    nodes = load_graph() 
    seed_nodes = get_seed_nodes_and_set_seeds(nodes)
    #print_nodes(seed_nodes)

    for node in seed_nodes:
        recursively_propagate_rank(node)

    #print_nodes(nodes)

    return nodes

def recursively_propagate_rank(node, depth_remaining=3):
    if (depth_remaining == 0):
        return

    num_outgoing = len(node.outgoing_links)
    if (num_outgoing==0):
        return

    outgoing_score = int(node.score)/int(num_outgoing)

    for outnode in node.outgoing_links:
        if outnode == node: continue
        outnode.score += outgoing_score
        recursively_propagate_rank(outnode,depth_remaining-1)

def print_nodes(nodes):
    print "print_nodes"
    if isinstance(nodes,dict):
        nodes = nodes.values() #make nodes a list of nodes
    #instead of a dict of nodes

    for node in nodes:
        print "s"+str(node.score)+" "+str(node.doc_id)+"->",
        print "#%d"%len(node.outgoing_links) 
