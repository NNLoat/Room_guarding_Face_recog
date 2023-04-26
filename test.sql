drop database if exists itcs498;
create database if not exists itcs498;

use itcs498;

create table if not exists student (
	studentID int PRIMARY key,
    nickName varchar(50) not null,
    sec int not null,
    major varchar(10) not null,
    lab varchar(3),
    engSec varchar(1)
);

insert into student values
(6388143, 'Oat',2,"CS", 'DB','A'),
(6388144, 'Earth',2,"SE", 'MM', 'B'),
(6388151, 'Pun',2,"CS", 'DB', 'A'),
(6388029, 'Neo', 2, 'CS', 'MM', 'C'),
(6388027, 'Jem', 2, 'CS', 'CN', 'B'),
(6388085, 'James', 2, 'CS', 'CN', 'B'),
(6388093, 'Boom', 2, 'CS', 'CN', 'B');	


create table if not exists course (
	courseID varchar(10) primary key,
    CourseName varchar(50)
);

insert into Course values 
('ITCS337', 'Human Computer Interaction'),
('ITCS403', 'Introduction to Healthcare System'),
('ITCS422', 'Local Area Network'),
('ITCS498', 'Specials Topics in Computer Science'),
('ITCS413', 'Database Design'),
('ITCS439', 'E-Customer Relationship Management'),
('ITCS472', 'Software Metrics'),
('ITCS461', 'Computer and Communication Security'),
('ITLG302', 'Academic Writing'),
('ITCS393', 'Database System Lab'),
('ITCS391', 'Computer Network Lab'),
('ITCS392', 'Multimedia Systems Lab'),
('ITCS367', 'IT Infrastructure Management'),
('ITCS453', 'Data Warehousing and Data Mining'),
('ITCS481', 'Computer Graphic'),
('ITCS368', 'Information and Business Process Management'),
('ITCS493', 'Special Topics in Computer Networks'),
('ITCS486', 'Multimedia Data Technologies'),
('ITCS424', 'Wireless and Mobile Computing'),
('ITCS431', 'Software Design and Development');


create table if not exists classSchedule (
	scheduleID int PRIMARY KEY,
    roomNum VARCHAR(10),
    secLearn VARCHAR (10),
    major VARCHAR(10),
    start_at time,
    end_at time,
    dayLearn varchar(10),
    lab varchar(10),
    engSec varchar(3),
    courseID varchar(10),
    FOREIGN KEY (courseID) REFERENCES course(courseID)
);

insert into classSchedule values
(1,'IT325','1','all','09:00:00', '12:00:00', 'Mon', 'NOT', 'NOT', 'ITCS337'),
(2,'IT310','all','HT','13:00:00', '16:00:00', 'Mon', 'NOT', 'NOT', 'ITCS403'),
(3,'A3','all','CN','13:00:00', '16:00:00', 'Mon', 'NOT', 'NOT', 'ITCS422'),
(4,'IT324','all','CS','13:00:00','16:00:00', 'Mon', 'NOT', 'NOT', 'ITCS498'),
(5,'IT332','all','DB','09:00:00','12:00:00', 'Tue', 'NOT', 'NOT','ITCS413'),
(6,'IT332','all','CS','09:00:00','12:00:00', 'Tue', 'NOT', 'NOT','ITCS413'),
(7,'IT333', 'all', 'EB','09:00:00','12:00:00', 'Tue', 'NOT', 'NOT','ITCS439'),
(8,'IT305', 'all', 'SE','09:00:00','12:00:00', 'Tue', 'NOT', 'NOT','ITCS472'),
(9,'IT332', '1', 'all','13:00:00','16:00:00', 'Tue', 'NOT', 'NOT','ITCS461'),
(10,'IT333', 'all', 'EB','09:00:00','12:00:00', 'Tue', 'NOT', 'NOT','ITCS439'),
(11, 'IT322', '1','all','09:00:00','12:00:00', 'Wed', 'NOT', 'A', 'ITLG302'),
(12, 'IT333', '1','all','09:00:00','12:00:00', 'Wed', 'NOT', 'B', 'ITLG302'),
(13, 'IT305', '1','all','09:00:00','12:00:00', 'Wed', 'NOT', 'C', 'ITLG302'),
(14, 'Lab104', 'all','all','08:30:00','10:30:00', 'Thu', 'DB', 'NOT', 'ITCS393'),
(15, 'Lab104', 'all','all','10:30:00','12:30:00', 'Thu', 'DB', 'NOT', 'ITCS393'),
(16, 'Lab106', 'all','all','09:00:00','12:00:00', 'Thu', 'CN', 'NOT', 'ITCS391'),
(17, 'Lab103', 'all','all','09:00:00','12:00:00', 'Thu', 'MM', 'NOT', 'ITCS392'),
(18, 'IT310', 'all','MS','13:00:00','16:00:00', 'Thu', 'NOT', 'NOT', 'ITCS367'),
(19, 'IT324', 'all','DB','13:00:00','16:00:00', 'Thu', 'NOT', 'NOT', 'ITCS453'),
(20, 'IT324', 'all','HT','13:00:00','16:00:00', 'Thu', 'NOT', 'NOT', 'ITCS453'),
(21, 'Lab203', 'all','CS','13:00:00','16:00:00', 'Thu', 'NOT', 'NOT', 'ITCS481'),
(22, 'Lab203', 'all','MM','13:00:00','16:00:00', 'Thu', 'NOT', 'NOT', 'ITCS481'),
(23, 'IT305', 'all','CS','09:00:00','12:00:00', 'Fri', 'NOT', 'NOT', 'ITCS431'),
(24, 'IT305', 'all','EB','09:00:00','12:00:00', 'Fri', 'NOT', 'NOT', 'ITCS431'),
(25, 'IT305', 'all','SE','09:00:00','12:00:00', 'Fri', 'NOT', 'NOT', 'ITCS431'),
(26, 'A3', 'all','CN','09:00:00','12:00:00', 'Fri', 'NOT', 'NOT', 'ITCS493'),
(27, 'Lab203', 'all','MM','09:00:00','12:00:00', 'Fri', 'NOT', 'NOT', 'ITCS486'),
(28, 'IT324', '1','all','13:00:00','16:00:00', 'Fri', 'NOT', 'NOT', 'ITCS424'),
(29, 'IT324', '2','all','09:00:00','12:00:00', 'Mon', 'NOT', 'NOT', 'ITCS461'),
(30, 'IT324', '2','all','13:00:00','16:00:00', 'Tue', 'NOT', 'NOT', 'ITCS337'),
(31, 'IT324', '2','all','09:00:00','12:00:00', 'Wed', 'NOT', 'NOT', 'ITCS424'),
(32, 'IT333', '2','all','13:00:00','16:00:00', 'Fri', 'NOT', 'A', 'ITLG302'),
(33, 'IT310', '2','all','13:00:00','16:00:00', 'Fri', 'NOT', 'B', 'ITLG302'),
(34, 'IT311', '2','all','13:00:00','16:00:00', 'Fri', 'NOT', 'C', 'ITLG302'),
(35, 'IT334', '3','all','09:00:00','12:00:00', 'Mon', 'NOT', 'A', 'ITLG302'),
(36, 'IT321', '3','all','09:00:00','12:00:00', 'Mon', 'NOT', 'B', 'ITLG302'),
(37, 'IT322', '3','all','09:00:00','12:00:00', 'Mon', 'NOT', 'C', 'ITLG302'),
(38, 'IT325', '3','all','13:00:00','16:00:00', 'Tue', 'NOT', 'NOT', 'ITCS424'),
(39, 'IT325', '3','all','09:00:00','12:00:00', 'Wed', 'NOT', 'NOT', 'ITCS461'),
(40, 'IT325', '3','all','13:00:00','16:00:00', 'Fri', 'NOT', 'NOT', 'ITCS337')
;




create table if not exists CSEnrollment (
	studentID int,
    courseID varchar(10),
    FOREIGN KEY (studentID) REFERENCES student(studentID),
    FOREIGN KEY (courseID) REFERENCES course(courseID)
);

insert into CSEnrollment values 
(6388143,'ITCS413'),
(6388151,'ITCS431')
;

select * from classSchedule;


set @stuID = 6388143;

select * from student where studentID = @stuID;


set @sec_ = '2';
set @major_ = 'CS';
set @time_ = '13:30:00';
set @day_ = 'Mon';
set @lab_ = 'DB';
select cs.courseID, RoomNum, courseName from classSchedule cs
inner join course c on cs.courseID = c.courseID
where (secLearn like @sec_ or secLearn like 'all') and 
(major like @major_ or major like 'all')
and (dayLearn like @day_)
and ( start_at <= @time_ and end_at >= @time_)
and (lab like 'NOT' or lab like @lab_);


select cs.courseID, c.courseName from CSEnrollment cs inner join course c on c.courseID = cs.courseID inner join 
classSchedule csc on csc.courseID = cs.courseID where (dayLearn like @day_) 
and ( start_at <= @time_ and end_at >= @time_) and studentID = 6388143;

-- "select cs.courseID, c.courseName from CSEnrollment cs inner join course c on c.courseID = cs.courseID inner join 
-- classSchedule csc on csc.courseID = cs.courseID where (dayLearn like '{}') 
-- and ( start_at <= '{}' and end_at >= '{}') and studentID = {};".format(today,timeNow,timeNow,studentID)


