import mysql.connector

class QueryEngine:
  
  def __init__(self, host="", user="", password="", database=""):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.connected = False
    if(len(self.host + self.user + self.password + self.database) == 0):
      self.setup_default()
  
  
  def setup_default(self):
    self.host = ""
    self.user = ""
    self.password = ""
    self.database = ""

  
  def connect(self):
    if(self.connected):
      return
    self.con = mysql.connector.connect(host = self.host, user = self.user, password = self.password, database = self.database)
    self.connected = True
    
  def disconnect(self):
    if(not self.connected):
      return
    self.con.close()
    self.connected = False
  
  def commit(self):
    if(self.connected):
      self.con.commit()
  
  def do_query(self, query_string):
    if(not self.connected):
        return
    cursor = self.con.cursor()
    
    cursor.execute(query_string)
    
    # List to return all results
    results = []
    
    for n in cursor:
      results.append(n)
    
    return results
  
  
