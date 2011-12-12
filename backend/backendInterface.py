'''

Backend Interface

'''

import cursorhelpers as db
import operator

def search_query(word):
    """Returns pages that contain the word corresponding to word_id by descending
    page_rank.
    Return:
    ((doc_id, page_rank, frequency of word, url),...)
    or 
    (), if the query returns nothing"""
    word_id = db.Lexicon.get_word_id(word)
    
    if word_id == None:
        #no matches
        return ()
    
    results = db.Join.get_page_rank_urls_by_word(word_id)
    formatted_results = []
    for r in results:
        formatted_results.append((r[0],int(r[1]),r[2],r[3],r[4],r[5]))
    formatted_results = sorted(formatted_results, key=operator.itemgetter(1), reverse=True)
    
    print formatted_results

    return formatted_results

if __name__=="__main__":
    print search_query("alex") 
