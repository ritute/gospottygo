import sqlite3

#global cursors which all classes in this module use
connection = sqlite3.connect("../db/repo.db")


"""In general, Inserts return true or false. Searches return a value or None"""

class DataBase(object):
    @classmethod
    def drop_tables(cls):
        try:
            connection.cursor().execute("DROP TABLE lexicon")
            connection.cursor().execute("DROP TABLE document")
            connection.cursor().execute("DROP TABLE link")
            connection.cursor().execute("DROP TABLE doc_word_index")
            connection.cursor().execute("DROP TABLE page_rank")
            connection.commit()
        except:
            pass

    @classmethod
    def create_tables(cls):
        try:
            connection.cursor().execute('CREATE TABLE lexicon ( word_id INTEGER PRIMARY KEY ASC AUTOINCREMENT, word VARCHAR(100) UNIQUE NOT NULL)')
            connection.cursor().execute('CREATE TABLE document (url_id INTEGER PRIMARY KEY ASC AUTOINCREMENT, url VARCHAR(255) UNIQUE NOT NULL)')
            connection.cursor().execute('CREATE TABLE link ( from_doc_id INTEGER NOT NULL REFERENCES document(url_id), to_doc_id INTEGER NOT NULL REFERENCES document(url_id), freq UNSIGNED INTEGER, PRIMARY KEY(from_doc_id, to_doc_id))')
            connection.cursor().execute('CREATE TABLE doc_word_index ( doc_id INTEGER REFERENCES document(url_id), word_id INTEGER REFERENCES lexicon(word_id), freq UNSIGNED INTEGER, PRIMARY KEY(doc_id, word_id))')
            connection.cursor().execute('CREATE TABLE page_rank(doc_id INTEGER REFERENCES document(url_id), page_rank INTEGER, PRIMARY KEY(doc_id))')
            connection.commit()
        except:
            print "Error in trying to create tables!\n"
        

class DocLexBaseDB(object):
    """The document and lexicon databases are very similar
    This class fulfills the functionalities of both. Variable names 
    and comments are named and described corresponding to the lexicon 
    table for clarity. Generalizing all the naming proved to be too confusing.
    """

    #class methods
    @classmethod
    def get_all_words(cls):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM %s"%cls.DBNAME)
        return list(cursor)

    @classmethod
    def insert(cls,word):
        """Return True if success and False if failure"""
        if len(word)>cls.MAXWORDLEN:
            return False

        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO %s(%s) VALUES (?)"%(cls.DBNAME,cls.VALNAME),(word,))
            connection.commit()

        except sqlite3.IntegrityError:
            #if the word already exists: failure - return False
            return False

        return True

    @classmethod
    def get_word_id(cls,word):
        """Returns None if the word doesn't exist in the database, otherwise return
        the word_id of the word specified"""
        cursor = connection.cursor()
        cursor.execute('select %s from %s where %s=?'%(cls.IDNAME,cls.DBNAME,cls.VALNAME),(word,))
        cursor_list = list(cursor) 

        #if no rows are rturned, return None
        if len(cursor_list) == 0:
            return None
        else:
            #the id we are looking for is the first(and only)
            #element of the first row
            return cursor_list[0][0]

    @classmethod
    def get_word_id_add(cls,word):
        """Returns the word_id of a word. If the word is not in the database, it 
        first adds the word, then returns its word_id"""
        
        cls.insert(word)
        return cls.get_word_id(word)

class Lexicon(DocLexBaseDB):
    DBNAME = 'lexicon'
    IDNAME = 'word_id'
    VALNAME = 'word'
    MAXWORDLEN = 100

class Document(DocLexBaseDB):
    DBNAME = 'document'
    IDNAME = 'url_id'
    VALNAME = 'url'
    MAXWORDLEN = 255 





class LinkWordIndexBaseDB(object):
    """The doc_word_index and link databases are very similar
    This class fulfills the functionalities of both. Variable names 
    and comments are named and described corresponding to the link 
    table for clarity. Generalizing all the naming proved to be too confusing.
    """

    @classmethod
    def get_all_edges(cls):
        cursor = connection.cursor()
        cursor.execute('select * from %s'%cls.DBNAME)
        return list(cursor)

    @classmethod
    def increment_and_get_freq(cls, from_doc_id, to_doc_id):
        """Returns the new frequency"""
        cursor = connection.cursor()
        try:
            cursor.execute('select freq from %s where %s=? and %s=?'%(cls.DBNAME,cls.FIELD1,cls.FIELD2),(from_doc_id,to_doc_id))
        finally:
            cursor_list = list(cursor)

        if len(cursor_list)<1:
            #key doesn't exist - insert it
            new_cursor = connection.cursor()
            cursor.execute('insert into %s values (?,?,?)'%cls.DBNAME,(from_doc_id, to_doc_id, 1))
            connection.commit()
            return 1
        else: 
            #key did exist
            old_freq = cursor_list[0][0]
            new_freq = old_freq + 1

            cursor.execute('update %s set freq=? where %s=? and %s=?'%(cls.DBNAME,cls.FIELD1,cls.FIELD2),(new_freq,from_doc_id,to_doc_id))
            connection.commit()

            return new_freq
         
class Link(LinkWordIndexBaseDB):
    DBNAME = 'link'
    FIELD1 = 'from_doc_id'
    FIELD2 = 'to_doc_id'

class DocWordIndex(LinkWordIndexBaseDB):
    DBNAME = 'doc_word_index'
    FIELD1 = 'doc_id'
    FIELD2 = 'word_id'

class PageRank(object):
    
    @classmethod
    def insert_page_rank(cls,doc_id,page_rank):
        cursor = connection.cursor()
        cursor.execute('insert into page_rank values (?,?)',(doc_id,page_rank))
        connection.commit()

class Join(object):
    """A class that performs queries on joins of tables """
    @classmethod
    def get_page_rank_urls_by_word(cls,word_id):
        """Returns pages that contain the word corresponding to word_id by descending
        page_rank.
        Return:
        ((doc_id, page_rank, frequency of word, url),...)"""
        cursor = connection.cursor()
        cursor.execute('select document.url_id, page_rank.page_rank, doc_word_index.freq, document.url from document,page_rank,doc_word_index where document.url_id=page_rank.doc_id and page_rank.doc_id=doc_word_index.doc_id and doc_word_index.word_id=? order by page_rank desc',(word_id,))

        return list(cursor)
