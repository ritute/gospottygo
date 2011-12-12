import __init__
import random
import unittest
from backend.cursorhelpers import *

class TestDocLexBaseDB(unittest.TestCase):
    def setUp(self):
        DataBase.drop_tables()
        DataBase.create_tables()
        
    def test_get_all_words(self):
        """Make sure that get_all_words returns a list"""
        self.assertEqual(type(Document.get_all_words()), type([]))
        self.assertEqual(type(Lexicon.get_all_words()), type([]))
        
    def test_document_insert(self):
        """Make sure we can insert a word into the database table"""
        if Document.get_word_id("WORD") == None: # if not already existing, try adding it
            self.assertTrue(Document.insert("WORD"))
        else:
            assert Document.insert("WORD") == False # don't insert since already existing
            
    def test_document_get_word_id(self):
        """Make sure that value is returned"""
        if Document.get_word_id("TEST") == None: # if not already existing, try adding it
            Document.insert("TEST") #insert first
            self.assertTrue(Document.get_word_id("TEST")) #now try obtaining word id
            
    def test_lexicon_insert(self):
        """Make sure we can insert a word into the database table"""
        if Lexicon.get_word_id("WORD") == None: # if not already existing, try adding it
            self.assertTrue(Lexicon.insert("WORD"))
        else:
            assert Lexicon.insert("WORD") == False # don't insert since already existing
            
    def test_lexicon_get_word_id(self):
        """Make sure that value is returned"""
        if Lexicon.get_word_id("TEST") == None: # if not already existing, try adding it
            Lexicon.insert("TEST") #insert first
            self.assertTrue(Lexicon.get_word_id("TEST")) #now try obtaining word id
            
    def test_document_get_word_id_add(self):
        """Make sure we can get word id"""
        if Document.get_word_id_add("ADD") == None: # if not already existing, try adding it
            self.assertEqual(type(Document.get_word_id_add("ADD")), type(1)) #ensure integer returned
        else:
            self.assertEqual(type(Document.get_word_id_add("ADD")), type(1)) #ensure integer returned
            
    def test_lexicon_get_word_id_add(self):
        """Make sure we can get word id"""
        if Lexicon.get_word_id_add("ADD") == None: # if not already existing, try adding it
            self.assertEqual(type(Lexicon.get_word_id_add("ADD")), type(1)) #ensure integer returned
        else:
            self.assertEqual(type(Lexicon.get_word_id_add("ADD")), type(1)) #ensure integer returned
            
    def test_document_get_all_words(self):
        """Make sure we get list of words since we already added some"""
        self.assertEqual(type(Document.get_all_words()), type([])) #make sure list returned
        
    def test_lexicon_get_all_words(self):
        """Make sure we get list of words since we already added some"""
        self.assertEqual(type(Lexicon.get_all_words()), type([])) #make sure list returned


class TestLinkWordIndexBaseDB(unittest.TestCase):
    def setUp(self):
        pass #don't need to do anything here
        
    def test_link_get_all_edges(self):
        """Make sure nothing returned"""
        #since we have nothing in table yet relating to page rank, this should return nothing
        assert len(Link.get_all_edges()) == 0
        
    def test_docWordIndex_get_all_edges(self):
        """Make sure nothing returned"""
        #since we have nothing in table yet relating to page rank, this should return nothing
        assert len(DocWordIndex.get_all_edges()) == 0
        
    def test_link_increment_and_get_freq(self):
        """Make sure we get valid frequency"""
        assert Link.increment_and_get_freq(1,2) >= 0 
        
    def test_docWordIndex_increment_and_get_freq(self):
        """Make sure we get valid frequency"""
        assert DocWordIndex.increment_and_get_freq(1,2) >= 0



if __name__ == '__main__':
    unittest.main()