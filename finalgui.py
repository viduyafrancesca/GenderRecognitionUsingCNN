import sys
import os
import cv2
import numpy as np 
# import updatedPreprocessing as pre
import loadModel as loadmodel

try:
    import Tkinter as tk
    from PIL import Image, ImageTk
    from tkFileDialog import askopenfilename
    from tkinter import filedialog #FOR UPLOAD FILE
except ImportError:
    import tkinter as tk
    from PIL import Image, ImageTk
    from PIL import ImageDraw2
    from tkinter.filedialog import askopenfilename
    from tkinter import filedialog #FOR UPLOAD FILE

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



from tkinter import *
from PIL import Image, ImageTk
from PyQt5 import QtGui
########################################################################
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Gender Face Recognition")
        self.frame = tk.Frame(parent)
        self.frame.pack()
        
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(self.root.winfo_screenwidth()/4 - windowWidth/4)
        positionLeft = int(self.root.winfo_screenheight()/4 - windowHeight/4)

        self.root.geometry("+{}+{}".format(positionRight, positionLeft))

        image = Image.open("homepageV2.png")
        img_copy= image.copy()
        background_image = ImageTk.PhotoImage(image)
        print('xxxx')

        # RESIZING
        new_width = 1300
        new_height = 683
        image = img_copy.resize((new_width, new_height))
        background_image = ImageTk.PhotoImage(image)
        # END OF RESIZING
        background = Label(self.frame, image=background_image)
        background.configure(image=background_image)
        background.image = background_image
        background.pack(fill=BOTH, expand=YES)
        # background.bind(/, self._resize_image)
 
        Button2 = Button(self.frame, command=self.openFrame)
        Button2.place(relx=0.130, rely=0.560, height=44, width=130)
        Button2.configure(activebackground="#ececec")
        Button2.configure(activeforeground="#297FB8")
        Button2.configure(background="#297FB8") #297FB8
        Button2.configure(foreground="#FFFFFF")
        Button2.configure(font=('Bebas Neue Thin', 13))
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="white")
        Button2.configure(highlightthickness="2")
        Button2.configure(pady="2")
        Button2.configure(relief='flat')

      #  helv36 = tkFont.Font(family = "Helvetica",size = 36,weight = "bold")

        Button2.configure(text="START NOW")
        Button2.configure(width=300)
        
        

 
    # def _resize_image(self, event):
 
    #     new_width = event.width
    #     new_height = event.height
 
    #     image = img_copy.resize((new_width, new_height))
 
    #     background_image = ImageTk.PhotoImage(image)
    #     background.configure(image=background_image)



        
 
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.geometry("1300x683")
        otherFrame.title("Gender Face Recognition")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
     

        image = Image.open("background.png")
        img_copy= image.copy()
        background_image = ImageTk.PhotoImage(image)
        
        windowWidth = otherFrame.winfo_reqwidth()
        windowHeight = otherFrame.winfo_reqheight()
        positionRight = int(otherFrame.winfo_screenwidth()/4 - windowWidth/4)
        positionLeft = int(otherFrame.winfo_screenheight()/4 - windowHeight/4)

        otherFrame.geometry("+{}+{}".format(positionRight, positionLeft))
        # RESIZING
        new_width = 1300
        new_height = 683
        image = img_copy.resize((new_width, new_height))
        background_image = ImageTk.PhotoImage(image)

        # END OF RESIZING
        background = Label(otherFrame, image=background_image)
        background.configure(image=background_image)
        background.image = background_image
        background.pack(fill=BOTH, expand=YES)
        # background.bind(/, self._resize_image)

        
        # self.preview = tk.Canvas()

####################### UPLOAD IMAGE BUTTON ##############################
        btnUpload = tk.Button(otherFrame, command=lambda: self.get_image(otherFrame, lblGResult, lblAResult))
        btnUpload.place(relx=0.750, rely=0.800, height=45, width=120)
        btnUpload.configure(background="#297FB8")
        btnUpload.configure(font=('Bebas Neue', 11))
        btnUpload.configure(foreground="#EDF2F4")
        btnUpload.configure(text='Upload Photo')
        btnUpload.configure(width=117)

###########################   FILE BUTTON  ################################

        btnFile = tk.Button(otherFrame,command=self.Help)
        btnFile.place(relx=0.850, rely=0.800, height=45, width=120)
        btnFile.configure(background="#297FB8")
        btnFile.configure(font=('Bebas Neue', 13))
        btnFile.configure(foreground="#EDF2F4")
        btnFile.configure(text='''Help''')
        btnFile.configure(width=117)

        btnExit = tk.Button(otherFrame, command=self.closeApplication)
        btnExit.place(relx=0.750, rely=0.900, height=45, width=240)
        btnExit.configure(background="#297FB8")
        btnExit.configure(font=('Bebas Neue', 13))
        btnExit.configure(foreground="#EDF2F4")
        btnExit.configure(text='''Exit Application''')
        btnExit.configure(width=117)

        #######################   ACCURACY & GENDER LABEL  ########################

        lblGender = tk.Label(otherFrame)
        lblGender.place(relx=0.740, rely=0.230, height=100, width=80)
        lblGender.configure(activeforeground="black")
        lblGender.configure(background="#0E1116")
        lblGender.configure(font=('Bebas Neue Book', 16))
        lblGender.configure(foreground="#FFFFFF")
        #self.lblGender.configure(highlightbackground="#d9d9d9")
        #self.lblGender.configure(highlightcolor="black")
        lblGender.configure(text='''Gender:''')

        lblGResult = tk.Label(otherFrame)
        lblGResult.place(relx=0.750, rely=0.350, height=50, width=250)
        lblGResult.configure(activeforeground="black")
        lblGResult.configure(background="#FFFFFF")
        #self.lblGender.configure(disabledforeground="#a3a3a3")
        lblGResult.configure(font=('Myriad Pro', 12))
        lblGResult.configure(foreground="#0E1116")
        #self.lblGender.configure(highlightbackground="#d9d9d9")
        #self.lblGender.configure(highlightcolor="black")
        lblGResult.configure(text="Gender Result")

        lblAccuracy = tk.Label(otherFrame)
        lblAccuracy.place(relx=0.745, rely=0.485, height=100, width=105)
        lblAccuracy.configure(activeforeground="black")
        lblAccuracy.configure(background="#05111E")
        #self.lblAccuracy.configure(disabledforeground="#a3a3a3")
        lblAccuracy.configure(font=('Bebas Neue Book', 15))
        lblAccuracy.configure(foreground="#FFFFFF")
        #self.lblAccuracy.configure(highlightbackground="#d9d9d9")
        #self.lblAccuracy.configure(highlightcolor="black")
        lblAccuracy.configure(text="Accuracy (%)")
       
        lblAResult = tk.Label(otherFrame)
        lblAResult.place(relx=0.750, rely=0.600, height=50, width=250)
        lblAResult.configure(activeforeground="black")
        lblAResult.configure(background="#FFFFFF")
        #self.lblAender.configure(disabledforeground="#a3a3a3")
        lblAResult.configure(font=('Myriad Pro', 12))
        lblAResult.configure(foreground="#0E1116")
        #self.lblAender.configure(highlightbackground="#d9d9d9")
        #self.lblAender.configure(highlightcolor="black")
        lblAResult.configure(text="Accuracy Result")
    
    def get_image(self, otherFrame, lblGResult, lblAResult):
        """"""
        image = Image.open(askopenfilename(filetypes=[("JPEG","*.jpg"), ("JPEG","*.JPG")]))
        output = loadmodel.predict(filename(image.filename))

        self.lblImage = tk.Label(otherFrame)
        self.lblImage.place(relx=0.048, rely=0.070, height=600, width=900)
        self.lblImage.configure(background="#d9d9d9")
        self.lblImage.configure(disabledforeground="#a3a3a3")
        self.lblImage.configure(foreground="#000000")

        lblGResult['text'] = output[0]
        lblAResult['text'] = output[1]

        maxWidth = 900
        maxHeight = 600
        SetWidth = 900
        SetHeight = 600

        # get the size of the original image
        width_org, height_org = image.size
        
        if width_org > maxWidth:
            SetWidth = float(maxWidth)
            SetHeight = float(maxWidth/width_org) * height_org

            if SetHeight > maxHeight:
                SetWidth = float(maxHeight/ height_org) * width_org
                SetHeight = float(maxHeight)
        
        if width_org <= maxWidth and height_org <=maxHeight:
            if width_org > height_org:
                SetWidth = float(maxWidth)
                SetHeight = float(maxWidth/width_org) * height_org
            
            else:
                SetWidth = float(maxHeight/height_org) * height_org
                SetHeight = float(maxHeight)
        self.img = image.resize((int(SetWidth), int(SetHeight)), Image.ANTIALIAS)
        self._img1 = ImageTk.PhotoImage(self.img)
        # resized = cv2.resize(gray, int(SetWidth), int(SetHeight))
        # preprocessedImage = Image.fromarray(pre.preprocess(image.filename))
        # self.img = preprocessedImage.resize((int(SetWidth), int(SetHeight)), Image.ANTIALIAS)
        # image.resize((int(SetWidth), int(SetHeight)), Image.ANTIALIAS) # resize the image
        # self._img1 = ImageTk.PhotoImage(self.img)
    #self.upload['image'] = self.image

        self.lblImage.configure(image= self._img1)
        self.lblImage.configure(text='''Label''')
        self.lblImage.configure(width=504)

    def Help(self,event=None):
        self.hide()
        helpFrame = tk.Toplevel()
        helpFrame.geometry("1300x683")
        helpFrame.title("Gender Face Recognition")
        handler = lambda: self.onCloseOtherFrame(helpFrame)

        windowWidth = helpFrame.winfo_reqwidth()
        windowHeight = helpFrame.winfo_reqheight()
        positionRight = int(helpFrame.winfo_screenwidth()/4 - windowWidth/4)
        positionLeft = int(helpFrame.winfo_screenheight()/4 - windowHeight/4)

        helpFrame.geometry("+{}+{}".format(positionRight, positionLeft))

        image = Image.open("help.png")
        img_copy= image.copy()
        background_image = ImageTk.PhotoImage(image)

        # RESIZING
        new_width = 1300
        new_height = 683
        image = img_copy.resize((new_width, new_height))
        background_image = ImageTk.PhotoImage(image)

        # END OF RESIZING
        background = Label(helpFrame, image=background_image)
        background.configure(image=background_image)
        background.image = background_image
        background.pack(fill=BOTH, expand=YES)




 
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()
 
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
    
    def closeApplication(self):
        self.root.destroy()

def filename(image):
    string = ""
    output = ""
    for x in reversed(image):
        if x != '/':
            string+=x
        else:
            break
    for x in reversed(string):
        output += x
    return output
        

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk()
    root.geometry("1300x683")
    app = MyApp(root)
    root.mainloop()