from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
import shutil



class Move:
    def __init__(self,root):
        self.root=root
        self.root.title("Move Copy")
        self.root.geometry("500x450")
        self.root.iconbitmap("logo3.ico")
        self.root.resizable(0,0)

        folder_path=StringVar()
        file_path=StringVar()



        def on_enter1(e):
            but_copy['background']="black"
            but_copy['foreground']="cyan"
  
        def on_leave1(e):
            but_copy['background']="SystemButtonFace"
            but_copy['foreground']="SystemButtonText"

        def on_enter2(e):
            but_move['background']="black"
            but_move['foreground']="cyan"
  
        def on_leave2(e):
            but_move['background']="SystemButtonFace"
            but_move['foreground']="SystemButtonText"


        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def on_enter4(e):
            but_open_folder['background']="black"
            but_open_folder['foreground']="cyan"
  
        def on_leave4(e):
            but_open_folder['background']="SystemButtonFace"
            but_open_folder['foreground']="SystemButtonText"


        def on_enter5(e):
            but_open_file['background']="black"
            but_open_file['foreground']="cyan"
  
        def on_leave5(e):
            but_open_file['background']="SystemButtonFace"
            but_open_file['foreground']="SystemButtonText"



        def open_dir():
            folder_path.set("")
            fold=tkinter.filedialog.askdirectory(title="choose folder")
            folder_path.set(fold)
            self.root.update()
            #Lab.config(text="file is selected")

        def open_file():
            file_path.set("")
            file= tkinter.filedialog.askopenfilename(title = "Select file",filetypes =(("All files","*.*"),("All files","."))) 
            file_path.set(file)
            self.root.update()


        def clear():
            folder_path.set("")
            file_path.set("")


        
        def move():
            if len(folder_path.get())!=0:
                if len(file_path.get())!=0:
                    shutil.move(file_path.get(),folder_path.get())
                else:
                    tkinter.messagebox.showerror("Error","Please Select file")
            else:
                tkinter.messagebox.showerror("Error","Please Select the folder to move or copy file")



        def copy():
            if len(folder_path.get())!=0:
                if len(file_path.get())!=0:
                    shutil.copy(file_path.get(),folder_path.get())
                else:
                    tkinter.messagebox.showerror("Error","Please Select file")
            else:
                tkinter.messagebox.showerror("Error","Please Select the folder to move or copy file")









#============================================================================#



        mainframe=Frame(self.root,width=500,height=450,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=390,relief="ridge",bd=3,bg="steelblue")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=54,relief="ridge",bd=3,bg="cyan")
        secondframe.place(x=0,y=390)

#=======================firstframe=============================================#



        but_open_folder=Button(firstframe,text="Open Folder",command=open_dir,width=15,font=("times new roman",12,"bold"),bd=3,cursor="hand2")
        but_open_folder.place(x=160,y=10)
        but_open_folder.bind("<Enter>",on_enter4)
        but_open_folder.bind("<Leave>",on_leave4)

        ent_folder_path=Entry(firstframe,width=50,relief="ridge",bd=3,font=('times new roman',13),textvariable=folder_path)
        ent_folder_path.place(x=14,y=80)


        but_open_file=Button(firstframe,text="Open File",command=open_file,width=15,font=("times new roman",12,"bold"),bd=3,cursor="hand2")
        but_open_file.place(x=160,y=210)
        but_open_file.bind("<Enter>",on_enter5)
        but_open_file.bind("<Leave>",on_leave5)


        ent_file_path=Entry(firstframe,width=50,relief="ridge",bd=3,font=('times new roman',13),textvariable=file_path)
        ent_file_path.place(x=14,y=280)




#===========================secondframe======================================================#

        but_copy=Button(secondframe,text="Copy",font=('times new roman',13),width=16,cursor="hand2",command=copy)
        but_copy.place(x=5,y=7)
        but_copy.bind("<Enter>",on_enter1)
        but_copy.bind("<Leave>",on_leave1)

        but_move=Button(secondframe,text="Move",font=('times new roman',13),width=16,cursor="hand2",command=move)
        but_move.place(x=165,y=7)
        but_move.bind("<Enter>",on_enter2)
        but_move.bind("<Leave>",on_leave2)



        but_clear=Button(secondframe,text="Clear",font=('times new roman',13),width=16,cursor="hand2",command=clear)
        but_clear.place(x=325,y=7)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)





if __name__ == "__main__":
    root=Tk()
    Move(root)
    root.mainloop()