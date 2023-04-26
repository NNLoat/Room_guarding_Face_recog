import os
import pickle


import tkinter as tk
from tkinter import messagebox
import face_recognition
import numpy as np
import cv2
# from pathlib import Path

def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )

    return button

def get_text_widget(window,text):
    text_wid = tk.Text(window, height=5,width=50,font=('Helvetica bold',18))
    label = tk.Label(window,text=text_wid)


def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label


def get_entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15, font=("Arial", 32))
    return inputtxt


def msg_box(title, description):
    messagebox.showinfo(title, description)


# def load_image(db_path):
#         known_faces_encoding = []
        
#         db_dir = sorted(os.listdir(db_path))
#         for i in range (len(db_dir)):
#             path_ = os.path.join(db_path,db_dir[i])

#             file = open(path_,'rb')
#             embeddings = pickle.load(file)

#             known_faces_encoding.append(embeddings)
#         return known_faces_encoding

def recognize(img, db_path):
    # it is assumed there will be at most 1 match in the db


    # known_faces_encoding = load_image(db_path)

    face_locations = face_recognition.face_locations(img) 
    embeddings_unknown = face_recognition.face_encodings(img,face_locations)

    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    else:
        embeddings_unknown = embeddings_unknown[0]


    db_dir = sorted(os.listdir(db_path))

    match = False
    j = 0
    

    while not match and j < len(db_dir):
        path_ = os.path.join(db_path, db_dir[j])


        file = open(path_, 'rb')
        embeddings = pickle.load(file)

        match = face_recognition.compare_faces([embeddings], embeddings_unknown)
        j += 1

    if match:
        return db_dir[j - 1][:-7]
    else:
        return 'unknown_person'

    # for face_encoding in embeddings_unknown:
    #     matches = face_recognition.compare_faces(known_faces_encoding, face_encoding)



class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True
    db_path = ''


    def __init__(self,db_path):
        self.db_path = db_path
        self.load_images()

    def load_images(self):
        db_dir = sorted(os.listdir(self.db_path))
        
        for i in range(len(db_dir)):
            path_ = os.path.join(self.db_path,db_dir[i])
            file = open(path_,'rb')
            known_face_encoding = pickle.load(file)
            self.known_face_encodings.append(known_face_encoding)
            self.known_face_names.append(db_dir[i][:-7])
        print(self.known_face_names)
    
    def reload_images(self):

        db_dir = sorted(os.listdir(self.db_path))
        for i in range(len(db_dir)):

            if db_dir[i][:-7] not in self.known_face_names:
                path_ = os.path.join(self.db_path,db_dir[i])
                file = open(path_,'rb')
                known_face_encoding = pickle.load(file)
                self.known_face_encodings.append(known_face_encoding)
                self.known_face_names.append(db_dir[i][:-7])
        print(self.known_face_names)
    
    def load_images_from_path(self,img_path):
        img_ls = sorted(os.listdir(img_path))
        mypath =os.path.abspath(os.path.dirname(__file__))
        for i in range(len(img_ls)):
            name = img_ls[i][:-4]
            if name not in self.known_face_names:
                
                face_image = face_recognition.load_image_file(os.path.join(mypath,img_path,img_ls[i]))
                face_location = face_recognition.face_locations(face_image)
                print(face_location)
                if (len(face_location) == 0):
                    print('No person Founded')
                    break
                face_encoding = face_recognition.face_encodings(face_image,num_jitters=15,known_face_locations=face_location)[0]

                file = open(os.path.join(self.db_path,'{}.pickle'.format(name)), 'wb')
                pickle.dump(face_encoding,file)
                file.close()

        self.reload_images()


    def run_recognition(self,img):

        self.face_locations = face_recognition.face_locations(img,number_of_times_to_upsample=3)
        self.face_encodings = face_recognition.face_encodings(img,self.face_locations,num_jitters=13)
        
        if(len(self.face_encodings) == 0):
            return 'no_persons_found'
        
        if (len(self.face_locations) > 1):
            return 'More than one person fouded'

        self.face_names = []

        for face_encoding in self.face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings,face_encoding,tolerance=0.45)
            
            face_distances = face_recognition.face_distance(self.known_face_encodings,face_encoding)

            best_match_index = np.argmin(face_distances)

            print(matches)
            print(face_distances)

            if(face_distances[best_match_index]>0.45):
                return 'unknown person'
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            
        return name


