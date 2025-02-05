from sqlite3 import connect

def dBconnection():
    '''Connects and returns a cursor and connection object'''
    conn = connect("quizdb.db")
    cur = conn.cursor()
    return conn, cur

def readDbdata():
    ''' connect and read records'''
    conn, cur = dBconnection()
    cur.execute("SELECT * FROM tblstudents")
    records = cur.fetchall()
    print(records)
    
def searchPerson(Nm):
    ''' connect and read records'''
    conn, cur = dBconnection()
    query = f'''SELECT * FROM tblstudents WHERE name ="{Nm}" '''
    cur.execute(query,)
    records = cur.fetchall()
    return records
    
def personChecker(Nm):
    conn, cur = dBconnection()
    query = f'''SELECT * FROM tblstudents WHERE name ="{Nm}" '''
    cur.execute(query,)
    results = cur.fetchall()
    return results
    
def getScores(Nm):
    conn, cur = dBconnection()
    query = f'''SELECT score2, score3 FROM tblstudents WHERE name ="{Nm}" '''
    cur.execute(query,)
    records = cur.fetchall()
    return records

def updateRecord(Nm, S1, S2, S3):
    ''' Updates a record '''
    conn, cur = dBconnection()
    query = f'''UPDATE tblstudents SET score1={S1}, score2={S2}, score3={S3} WHERE name="{Nm}"'''
    cur.execute(query)
    conn.commit()
    conn.close()


def nextId():
    conn, cur = dBconnection()
    cur.execute("SELECT ID FROM tblstudents")
    records = cur.fetchall()
    NewId= records[-1][0]+1
    return NewId

def addrecord(Nm,S3):
    '''adds new record'''
    conn,cur =dBconnection()
    query = "INSERT INTO tblstudents VALUES(?,?,0, 0, ?)"
    cur.execute(query,(nextId(), Nm, S3))
    conn.commit()
    conn.close()

def updateOrAdd(Nm, S3):
    ''' Either update an existing record or add a new one '''
    results = personChecker(Nm)
    if results:  
        scores = getScores(Nm)
        S2 = scores[0][1]
        S1 = scores[0][0]  
        updateRecord(Nm, S1, S2, S3)
    else:  
        addrecord(Nm, S3)
    
    
scores = [0, 1,2]
newScore =7



