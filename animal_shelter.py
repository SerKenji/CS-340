# Kenneth Askew
# SNHU CS-340

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self):
        """
        Constructor to set up the connection to the MongoDB database
        """        
        USER = 'aacuser'
        PASS = 'greatPASSword1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30923
        DB = 'AAC'
        COL = 'animals'
        
        # Create the MongoDB client connection string and connect
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/')
        # Select database
        self.database = self.client[DB]
        # Select the collection table
        self.collection = self.database[COL]
        
        # Track stats for last update/delete operations
        self.records_update = 0
        self.records_match = 0
        self.records_deleted = 0
        
        
    # Create record method. C in CRUD
    def createRecord(self, data):
        """
        Insert a single record into the collection
        Returns True if insert was successful, else False
        """
        if not data:
            raise Exception("Nothing to save, because data parameter is empty")
        try:
            res = self.collection.insert_one(data)
            return bool(res.acknowledged)
        except Exception:
            return false
            
            
    # Read a record method. R in CRUD
    def readRecord(self, query=None):
        """
        Read all documents that match the query using find()
        Returns a a list of documents (empty list if none)
        """
        if query is None:
            query = {}
        return list(self.collection.find(query))
        
        
    # Update a record method. U in CRUD
    def updateRecord(self, query, newValue):
        """
        Update all documents that match query with new values
        Returns number if any documents were modified.
        """
        if not query:
            raise Exception("No search criteria is present.")
        if not newValue:
            raise Exception("No update value is present.")
        
        _updateValid = self.collection.update_many(query, {"$set": newValue})
        self.records_update = _updateValid.modified_count
        self.records_match = _updateValid.matched_count            
        return int(_updateValid.modified_count)
        
    # Delete a record. D in CRUD
    def deleteRecord(self, query):
        """
        Delete all documents that match query.
        Returns the number of documents deleted.
        """
        if not query:
            raise Exception("No search criteria is present.")
        _deleteValid = self.collection.delete_many(query)
        
        # Track how many documents werre deleted
        self.records_deleted = _deleteValid.deleted_count
        
        # Return number of deleted documents
        return int(_deleteValid.deleted_count)
    
    
    
    
    
    
    
    