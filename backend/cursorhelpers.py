import sqlite3

#global cursors which all classes in this module use
cursor = None

def count_rows(cursor):
    return len(list(cursor))

class Lexicon(object):
    MAXWORDLEN = 100

    #static methods
    @classmethod
    def insert(cls,word):
        """Return True if success and False if failure"""
        if len(word)>100:
            return False

        c = cursor.execute('insert into lexicon (word) values (?)',("testword",))
        if count_rows(c)==1:
            return True
        else:
            return False

    @classmethod
    def get_word_id(cls,word):
        """Returns None if the word doesn't exist in the database, otherwise return
        the word_id of the word specified"""
        result = cursor.execute('select word_id from lexicon where word=?',(word,))

        if count_rows(result) == 0:
            return None
        else:
            #the word_id we are looking for is the first(and only)
            #element of the first row
            return result[0][0]
