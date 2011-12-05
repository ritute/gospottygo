import cursorhelpers as db
'''

Step #5: PageRank

Uses the Links database table to generate rankings of pages.

'''

class Node(object):
    #self.doc_id
    #self.outgoing_links (list)
    #self.num_outgoing
    #self.score

    def __init__(self,doc_id,outgoing_links=[], score =0):
        self.doc_id = doc_id
        self.outgoing_links = outgoing_links
        self.num_outgoing = len(outgoing_links)
        self.score = score
    
def load_graph():
    #tuples of (id,url)
    raw_data = db.Document.get_all_words()
    nodes = {tup[0]:Node(tup[0],tup[1]) for tup in raw_data}

    return data

def get_seed_nodes():
    pass

def compute_page_rank():
    nodes = load_all_nodes() 

    seed_nodes = get_seed_nodes()

    for node in seed_nodes:
        recursively_propagate_rank(node)

def recursively_propagate_rank(node, depth_remaining=3):
    if (depth_remaining == 0):
        return

    num_outgoing = len(node.outgoing_links)
    outgoing_score = node.score/num_outgoing

    for outnode in node.outgoing_links:
        outnode.score += outgoing_score
        recursively_propagate_rank(outnode,depth_remaining-1)

def populate_page_rank():
    return load_graph()
