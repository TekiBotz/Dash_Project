from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, database, collection):
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,passwd,host,port))
        self.database = self.client['%s' % (database)]
        self.collection = self.database['%s' % (collection)]

# Create method
    def create(self, data):
        if data is not None:    # Ensures data is valid
            self.database.animals.insert_one(data)  # Inserts document into database
            return True   # Retruns true if document is inserted successfully
        else:
            raise Exception("Nothing to save, because data parameter is empty")   # Error handler if document isn't inserted

# Read method
    def read(self, query):
        if query is not None:   # Ensures query is valid
            validQuery = self.database.animals.find(query) # Creates variable named validQuery and executes query
            return list(validQuery)    # Converts return cursor to list
        else:
            return []   # Returns empty list
        


# Update method
    def update(self, query, updated_entry):
        if query is not None and updated_entry is not None:
            new_entry = self.database.animals.update_one(query, {'$set': updated_entry})    # Update one document matching the query with the new data
            return new_entry.modified_count
        else:
            raise Exception("No entry to update")

# Delete method
    def delete(self, query):
        if query is not None:
            deleted_data = self.database.animals.delete_one(query)  # Delete the first document found matching the query
            return deleted_data.deleted_count   # Return the number of deleted documents
        else:
            raise Exception("Nothing deleted")

def main():
    # Parameters for initializing connection
    USER = 'aacuser'
    PASS = 'SNHU1234'
    HOST = '127.0.0.1'
    PORT = 27017
    DB = 'AAC'
    COL = 'animals'
    
    # Create an instance of the AnimalShelter class
    shelter = AnimalShelter(USER, PASS, HOST, PORT, DB, COL)

    # Test the create method
    new_animal = {"name": "Thomas McGruffG", "species": "cat", "age": 15}
    result = shelter.create(new_animal)
    if result:
        print("Animal created successfully!")
    else:
        print("Failed to create animal.")

    # Test the read method
    query = {"species": "cat"}
    cats = shelter.read(query)
    print("Found cats:", cats)

    # Test the update method
    update_query = {"name": "Thomas McGruffG"}
    update_data = {"age": 10}   # Change age
    num_modified = shelter.update(update_query, update_data)
    print("Number of animals updated:", num_modified)

    # Test the delete method
    delete_query = {"name": "Thomas McGruffG"}
    num_deleted = shelter.delete(delete_query)
    print("Number of animals deleted:", num_deleted)

# Call the main function if the script is run directly
if __name__ == "__main__":
    main()