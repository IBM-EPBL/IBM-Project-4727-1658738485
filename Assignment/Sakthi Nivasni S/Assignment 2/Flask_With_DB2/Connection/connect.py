import ibm_db

def Connection():
    try:
        conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dkf92060;PWD=aUIIMe5Ip1OpH15a", "", "")
       
        print ("Database Connected Successfully !")
        return conn
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg())

def Create(email,name,phone,password,conn):

    columns = '"UNAME","UEMAIL","UPHONE","UPASSWORD"'
    val = "'"+name+"','"+email+"','"+phone+"','"+password+"'"
    sql = 'Insert into DKF92060.USER(' + columns + ') values('+val+')'
    try:
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.execute(stmt)
        print ("added :-)")
        return 1
    except:
        print("Error While Adding the User ! ")
        return 0

def Signin(email,password,conn):

    sql = "SELECT * FROM DKF92060.USER"
    try:
        result = ibm_db.exec_immediate(conn,sql)
        tuple = ibm_db.fetch_tuple(result)
        while tuple != False:
            if str(tuple[2]) == email and str(tuple[4]) == password:
                res = [str(tuple[1]),str(tuple[2]),str(tuple[3])]
                return res
            tuple = ibm_db.fetch_tuple(result)
        print("Fetch Success :-)")
        return 0
    except:
        print("fetch not found !")
        return 0