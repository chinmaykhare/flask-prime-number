import mysql.connector

def checkPrimeNumber(num):
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                print("Entered number {} is not a prime number".format(num))
                result = 'NOT_PRIME'
                break
            else:
                print("Entered number {} is a prime number".format(num))
                result = 'PRIME'
                break
    else:
        print("Entered number {} is not a prime number".format(num))
        result = 'NOT_PRIME'

    return result


def initializeDb(dbHostname):
    db = mysql.connector.connect(
        host=dbHostname,
    user="root",
    passwd="root",
    database="mysql",
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE PRIME_NUMBER_CHECK(SR_NO int NOT NULL AUTO_INCREMENT,INPUT_NUMBER varchar(255),RESULT varchar(255),PRIMARY KEY(SR_NO))")
    cursor.close()


def insertResult(dbHostname : str,num1 : str,result : str):
    db = mysql.connector.connect(
        host=dbHostname,
        user="root",
        passwd="root",
        database="mysql",
        auth_plugin='mysql_native_password'
    )

    cursor = db.cursor()
    sql = 'INSERT INTO PRIME_NUMBER_CHECK (INPUT_NUMBER,RESULT) VALUES(%s,%s)'
    val = (num1, result)
    cursor.execute(sql, val)
    cursor.close()
    db.commit()
