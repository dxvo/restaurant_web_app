from QueryEngine import QueryEngine
from flask import flash

qe = QueryEngine()
qe.setup_default()

def login_check(username, password):
  qe.connect()
  query_string = f"SELECT COUNT(*) FROM log_in WHERE UserName = '{username}' AND Password_Hash = '{password}';"
  check_acc = qe.do_query(query_string)
  count = check_acc[0][0]
  qe.disconnect()
  if count == 1:
    #print("I am in")
    return True
  else:
    #print("wrong account")
    return False

def transaction_check(transaction):
  transaction_hist = []
  qe.connect()
  query_string = f"SELECT DISTINCT transanction_id FROM Transaction;"
  response = qe.do_query(query_string)
  qe.disconnect()
  for i in response:
    transaction_hist.append(i[0])

  if(transaction in transaction_hist):
    return True
  else:
    return False

