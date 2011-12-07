'''

Backend Interface

'''

import cursorhelpers as db

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

    return results

if __name__=="__main__":
    print search_query("alex") 
