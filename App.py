import os.path
import datetime
import pickle

import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition

import util
from util import FaceRecognition
from db import DBConn


class App:

    RoomNum = ''

    def __init__(self,roomNum):
        self.RoomNum = roomNum
        self.dbConnect = DBConn('localhost',user='itcs498',password='itcs498',database='itcs498')
        
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x820+350+100")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)


        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

        # self.Text1 = util.get_text_widget(self.main_window, text= 'You are: ')
        self.Text1 = util.get_text_label(self.main_window, 'You are: ')
        self.Text1.place(x = 50, y=500)

        self.text_show_id = util.get_text_label(self.main_window, '')
        self.text_show_id.place(x=200,y=500)

        self.canvas_authorized = tk.Canvas(self.main_window, bg='white', height = 250, width=450)
        self.canvas_authorized.place(x=700,y=520)

        # self.canvas_authorized.create_text(225,125,text="Authorized",font=('Helvetica bold',18))

        self.text_room_number = util.get_text_label(self.main_window, self.RoomNum)
        self.text_room_number.place(x=825,y=600)
        self.text_authorized = util.get_text_label(self.main_window, '')
        self.text_authorized.place(x=825,y=650)
        
        self.text_show_room_holder = util.get_text_label(self.main_window,'Your class Schedule: ')
        self.text_show_room_holder.place(x=50, y=550)

        self.text_show_room = util.get_text_label(self.main_window, '')
        self.text_show_room.place(x=50,y=600)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        
        self.log_path = './log.txt'

        self.fr = FaceRecognition(self.db_dir)
    
    def update_text(self,label,text):
        label.configure(text = text)

    
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()
    
    def process_webcam(self):
        ret, frame = self.cap.read()

        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)
    
    def login(self):

        # small_frame = cv2.resize(self.most_recent_capture_arr, (0, 0), fx=0.25, fy=0.25)
        small_frame = self.most_recent_capture_arr
        name = self.fr.run_recognition(small_frame)
        self.update_text(self.text_show_id, name)
        if (name == 'no_persons_found'):
            self.update_text(self.text_authorized, 'Unauthorized')
            return
        if (name == 'More than one person fouded'):
            return
        if (name not in (['unknown person'])):
            classSchedule = self.dbConnect.get_class_schedule(studentID=name)
            print(classSchedule)
            if classSchedule is None:
                self.update_text(self.text_authorized,'Unauthorized')
                self.update_text(self.text_show_room,'Free')
                return
            if(classSchedule[1] ==self.RoomNum):
                print('Enter Authorized')
                self.update_text(self.text_authorized, 'Authorized')
                self.update_text(self.text_show_room, '{}\n{} at \n\n{}'.format(classSchedule[0],classSchedule[2],classSchedule[1]))
                return
            else:
                print('Enter Unauthorized')
                self.update_text(self.text_authorized, 'Unauthorized')
                self.update_text(self.text_show_room, '{}\n{} at \n\n{}'.format(classSchedule[0],classSchedule[2],classSchedule[1]))
        else:
            self.update_text(self.text_authorized, 'Unauthorized')
            self.update_text(self.text_show_room, 'You are not allowed to enter')


        
        print(name)
        pass


    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \ninput username:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")

        face_location = face_recognition.face_locations(self.register_new_user_capture)
        
        # embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]
        embeddings = face_recognition.face_encodings(self.register_new_user_capture,face_location,num_jitters=15)[0]

        file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')
        pickle.dump(embeddings, file)

        file.close()

        self.fr.reload_images()
        
        # img = cv2.cvtColor(self.register_new_user_capture,cv2.COLOR_BGR2RGB)

        # img_path =os.path.join(self.db_dir,name+'.png')
        # print(img_path)
        # cv2.imwrite(img_path,img)

        # self.fr.load_images()

        # util.msg_box('Success!', 'User was registered successfully !')

        self.register_new_user_window.destroy()

