import tkinter as tk

import util
from util import FaceRecognition
from App import App
import db
from db import DBConn



if __name__ == '__main__':
    # dbConnect = DBConn('localhost',user='itcs498',password='itcs498',database='itcs498')
    # classSchedule = dbConnect.get_class_schedule(studentID=6388143)
    # print(str(classSchedule))

    app = App('IT324')
    app.fr.load_images_from_path('./faces')
    app.start()
