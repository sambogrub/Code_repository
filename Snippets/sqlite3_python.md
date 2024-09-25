# sqlite3


# initialing and context management
 the point of doing it this way is to ensure proper opening and closing the connection. 

 - to connect using this, make sure you are using
  with class_name as instance:
    the thing you want to do

 - make sure when the instance is first created that you call the method to create the needed tables if they are not already

 - initialize the name and make sure that conn and cursor ar class attributes
  
 def __init__(self, db_name = 'database.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

 - this handles opening the database connection and returns the current instance of the class
 - opens a connection and cursor
 
 def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

 - this handles what happens when the connection is no longer needed
 - either rolls back or commits the changes, then closes the cursor and connection as needed
  
    def __exit__(self, exc_type, exc_val, exc_tb):
        #handle exceptions and clean up resources
        if exc_type is not None:
            #if there is an exception, roll back the transaction
            self.conn.rollback()
        else:
            self.conn.commit()

        #clean up cursor connection
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()