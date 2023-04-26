import mysql.connector
import datetime
from datetime import datetime as datet
from dateutil.relativedelta import relativedelta

class DBConn:
    host = ''
    user = ''
    password = ''
    database = ''
    special_day = ['Tue','Thu','Fri']
    special_time = ['9:00:00','13:30:00', '9:00:00']
    
    def __init__(self, host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database = self.database)
        self.cursor = self.check_conn()
        self.special_time= [((datetime.datetime.strptime(x, '%H:%M:%S')).time()) for x in self.special_time]

    def check_conn(self):
        if self.db.is_connected:
            cursor =  self.db.cursor()
            cursor.execute('select database();')
            record = cursor.fetchone()
            print('Connected to: ', record)
            return cursor
        else:
            print('Database not Connected')
            return
        
    def close_conn(self):
        self.db.close()
        self.cursor.close()

    def check_cs(self,today,timeNow):
        if(today in self.special_day):
            delta = datetime.timedelta(hours=3)
            # special_time_end = [(x + delta) for x in self.special_time]
            special_time_end = [time_plus(x,delta) for x in self.special_time]
            # print('special time end',special_time_end)
            tmp_ind = self.special_day.index(today)
            if (self.special_time[tmp_ind] <= timeNow and special_time_end[tmp_ind] >= timeNow):
                return True
            else:
                return False
    def get_class_schedule(self,studentID):
        sql1 = "select * from student where studentID = {};".format(studentID)
        self.cursor.execute(sql1)
        result = self.cursor.fetchone()
        sec, mj, lab, engSec = (result[2], result[3],result[4],result[5])
        dt = datetime.datetime.now()
        today = dt.strftime('%a')
        # today = 'Mon'
        timeNow = dt.time()
        # timeNow = datetime.datetime.strptime('09:00:00', '%H:%M:%S').time()
        if(mj == 'CS'):
            if(self.check_cs(today,timeNow)):
                sql2 = "select cs.courseID, RoomNum, c.courseName from CSEnrollment cs inner join course c on c.courseID = cs.courseID inner join classSchedule csc on csc.courseID = cs.courseID where (dayLearn like '{}') and ( start_at <= '{}' and end_at >= '{}') and studentID = {};".format(today,timeNow,timeNow,studentID)
                print("CS special")
                self.cursor.execute(sql2)
                result = self.cursor.fetchone()
                return result
        sql2 = "select cs.courseID, RoomNum, courseName from classSchedule cs inner join course c on cs.courseID = c.courseID where (secLearn like '{}' or secLearn like 'all') and  (major like '{}' or major like 'all') and (dayLearn like '{}') and ( start_at <= '{}' and end_at >= '{}') and (lab like 'NOT' or lab like '{}') and (engSec like '{}' or engSec like 'NOT');".format(sec,mj,today,timeNow,timeNow,lab,engSec)
        self.cursor.execute(sql2)
        result = self.cursor.fetchone()

        return result
        

def time_plus(time, timedelta):
    start = datetime.datetime(
        2000, 1, 1,
        hour=time.hour, minute=time.minute, second=time.second)
    end = start + timedelta
    return end.time()


def check_cs_str(today,timeNow):
    # today = 'Tue'
    # # today 
    # timeNow = '9:30:00'
    special_day = ['Tue','Thu','Fri']
    special_time = ['9:00:00','13:30:00', '9:00:00']

    if(today in special_day):
        delta = datetime.timedelta(hours=4)
        special_time_end = [((datetime.datetime.strptime(x, '%H:%M:%S') + delta).time()) for x in special_time]
        special_time= [((datetime.datetime.strptime(x, '%H:%M:%S')).time()) for x in special_time]
        # print(special_time)
        tmp_ind = special_day.index(today)
        # print(special_time[tmp_ind])

        if (special_time[tmp_ind] <= datetime.datetime.strptime(timeNow, '%H:%M:%S').time() and special_time_end[tmp_ind] >= datetime.datetime.strptime(timeNow, '%H:%M:%S').time()):
            #  print("True")
            return True
        else:
            #  print("False")
            return False
     

def get_class_schedule_from_str(studentID, today, timeNow, cursor):
    sql1 = "select * from student where studentID = {};".format(studentID)
    cursor.execute(sql1)
    result = cursor.fetchone()
    sec, mj, lab, engSec = (result[2], result[3],result[4],result[5])
    dt = datetime.datetime.now()
    # today = dt.strftime('%a')
    # today = 'Fri'
    # timeNow = dt.strftime('%H:%M:%S')
    # timeNow = '13:00:00'


    if(mj == 'CS'):
        if(check_cs_str(today,timeNow)):
            sql2 = "select cs.courseID, csc.RoomNum, c.courseName from CSEnrollment cs inner join course c on c.courseID = cs.courseID inner join classSchedule csc on csc.courseID = cs.courseID where (dayLearn like '{}') and ( start_at <= '{}' and end_at >= '{}') and studentID = {};".format(today,timeNow,timeNow,studentID)
            print("CS special")
            cursor.execute(sql2)
            result = cursor.fetchone()
            return result

    
    sql2 = "select cs.courseID, RoomNum, courseName from classSchedule cs inner join course c on cs.courseID = c.courseID where (secLearn like '{}' or secLearn like 'all') and  (major like '{}' or major like 'all') and (dayLearn like '{}') and ( start_at <= '{}' and end_at >= '{}') and (lab like 'NOT' or lab like '{}') and (engSec like '{}' or engSec like 'NOT');".format(sec,mj,today,timeNow,timeNow,lab,engSec)
    cursor.execute(sql2)
    result = cursor.fetchone()

    return result
    







# mydb.close()
# cursor.close()



# mydb = mysql.connector.connect(
#   host="localhost",
#   user="itcs498",
#   password="itcs498",
#   database = "itcs498"
# )


# if mydb.is_connected:
#     cursor =  mydb.cursor()
#     cursor.execute('select database();')
#     record = cursor.fetchone()
#     print('Connected to: ', record)

# studentID = '6388143'

# sql1 = 'select * from student where studentID = {};'.format(studentID)

# cursor.execute(sql1)

# result = cursor.fetchone()

# sec, mj, lab = (result[2], result[3],result[4])

# # dt = datetime.datetime.now()
# # today = dt.strftime('%a')
# # timeNow = dt.strftime('%H:%M:%S')

# today = 'Tue'

# timeNow = '13:00:00'

# print(today,timeNow)





# sql2 = "select cs.courseID, RoomNum, courseName from classSchedule cs inner join course c on cs.courseID = c.courseID where (secLearn like '{}' or secLearn like 'all') and  (major like '{}' or major like 'all') and (dayLearn like '{}') and ( start_at <= '{}' and end_at >= '{}') and (lab like 'NOT' or lab like '{}');".format(sec,mj,today,timeNow,timeNow,lab)


# # print(sql2)
# cursor.execute(sql2)

# result = cursor.fetchone()

# for x in result:
#     print(x)



