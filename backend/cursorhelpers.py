import sqlite3

#global cursors which all classes in this module use
connection = None


"""In general, Inserts return true or false. Searches return a value or None"""


class DocLexBaseDB(object):
    """The document and lexicon databases are very similar
    This class fulfills the functionalities of both. Variable names 
    and comments are named and described corresponding to the lexicon 
    table for clarity. Generalizing all the naming proved to be too confusing.
    """

    #static methods
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

class Link(object):
    @classmethod
    def increment_and_get_freq(cls, from_doc_id, to_doc_id):
        """Returns the new frequency"""
        cursor = connection.cursor()
        try:
            cursor.execute('select freq from link where from_doc_id=? and to_doc_id=?',(from_doc_id,to_doc_id))
        finally:
            cursor_list = list(cursor)

        if len(cursor_list)<1:
            #key doesn't exist - insert it
            new_cursor = connection.cursor()
            cursor.execute('insert into link values (?,?,?)',(from_doc_id, to_doc_id, 1))
            connection.commit()
            return 1
        else: 
            print list(cursor)
            #key did exist
            return list(cursor)[0][0]
         
