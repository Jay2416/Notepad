#Importing important moduled for making Notepad:-
from tkinter import *
import tkinter.ttk as tk
import tkinter.messagebox as tmsg
import tkinter.font as font
import tkinter.colorchooser as cc
import tkinter.filedialog as box
import os

save_file=False

#Making command for file menu:-
#Making command for new:-
def new():
    global file
    root.title("Untitled - Notepad")
    file=None
    typing_area.delete(1.0, END)

#Making command for new window:-
def new_window():
    window=Toplevel()
    window.geometry("1280x720")

file=None

#Making command for open:-
def _open():
    global file
    file = box.askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        typing_area.delete(1.0, END)
        f = open(file, "r")
        typing_area.insert(1.0, f.read())
        f.close()

    global save_file
    save_file=file

#Making command for save:-
def save_as():
    global file
    if file==None:
        file=box.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt"),
                                      ("HTML files", "*.txt"),
                                      ("WORD FILES", "*.docx")])
        if file=="":
            file=None

        else:
            #Saving it as a new file:-
            f=open(file, "w")
            f.write(typing_area.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
        #Save the file:-
        f=open(file, "w")
        f.write(typing_area.get(1.0, END))
        f.close()

#Making command for save as:-
def save():
    global file
    f=open(save_file, "w")
    content = str(typing_area.get(1.0, END))
    f.write(content)

#Making command for edit menu:-
#Making command for exit:-
def exit():
    root.destroy()

#Making command for edit menu:-
#Making command for copy:-
def copy():
    typing_area.event_generate("<<Copy>>")
    pass

def quiting():
    global file
    f1=open(os.path.basename(save_file), "r")
    f2=open(file, "w")
    content = str(typing_area.insert(1.0, END))

    if f1!=f2:
        root.protocol("WM_DELETE_WINDOW", quiting)
        print("Success!!")

    f2.close()
    f1.close()
    

#Making command for paste:-
def paste():
    typing_area.event_generate("<<Paste>>")
    pass
#Making command for cut:-
def cut():
    typing_area.event_generate("<<Cut>>")
    pass

def send(event):
    tmsg.showinfo("Send FeedBack", "Thanks for your FeedBack/Suggestion/Complain!!")

#Making command for changing the font and its size:-
font_now="Arial"
size_now=16
def font_change(event):
    global font_now, size_now
    font_now=font_value.get()
    size_now=size_box.get()
    typing_area.configure(font=(font_now, size_now))

#Making command for bold:-
def bold_font(event):
    text_font=font.Font(font=typing_area["font"])
    if text_font.actual()["weight"]=="normal":
        typing_area.configure(font=(font_now, size_now, "bold"))
    if text_font.actual()["weight"]=="bold":
        typing_area.configure(font=(font_now, size_now, "normal"))

#Making command for italic:-
def italic_font(event):
    text_font=font.Font(font=typing_area["font"])
    if text_font.actual()["slant"]=="roman":
        typing_area.configure(font=(font_now, size_now, "italic"))
    if text_font.actual()["slant"]=="italic":
        typing_area.configure(font=(font_now, size_now, "roman"))

#Making command for underline:-
def underline_font(event):
    text_font=font.Font(font=typing_area["font"])
    if text_font.actual()["underline"]==0:
        typing_area.configure(font=(font_now, size_now, "underline"))
    if text_font.actual()["underline"]==1:
        typing_area.configure(font=(font_now, size_now, "normal"))

#Making command for choosing colour:-
def colour_chooser(event):
    colour=cc.askcolor()
    typing_area.configure(fg=colour[1])

#Making command for help menu:-
#Making command for about:-
def about():
    tmsg.showinfo("About", "Made by:-\n          Jay Patel\n          Priyanshi Desai")

#Making command for send feedback:-
def feedback():
    fd=Toplevel()
    fd.title("Send Feedback")
    fd.geometry("550x200")
    label=Label(fd, text="Write your FeedBack/Suggestion/Complain here", font="cooper 14")
    label.pack(pady=10)
    fd_value=StringVar()
    def send(event):
        tmsg.showinfo("Send FeedBack", "Thanks for your FeedBack/Suggestion/Complain!!")
        

        fd.destroy()
    fd_entry=Entry(fd, textvariable=fd_value, width=32, font="arial 16", borderwidth=2, relief=SUNKEN)
    fd_entry.bind("<Return>", send)
    fd_entry.pack(pady=10)

#Making command for changing the text styl:-
change_text=False
def change_value(root):
    global change_text
    if typing_area.edit_modified():
        change_text=True
        word=len(typing_area.get(1.0, "end-1c").split())
        character=len(typing_area.get(1.0, "end-1c").replace(" ",""))
        statusbar.config(text=f"CHARACTER:{character}; WORD{word}", font="arial 12")
    typing_area.edit_modified(False)

#Showing and hiding TOLLBAR and STATUSBAR:-
show_statusbar=1
show_toolbar=1

def hide_toolbar():
    global show_toolbar
    if show_toolbar==1:
        toolbar_ribbon.pack_forget()
        show_toolbar=0
    else:
        typing_area.pack_forget()
        statusbar.pack_forget()
        toolbar_ribbon.pack(side=TOP, fill=X)
        typing_area.pack(fill=BOTH, expand=True)
        statusbar.pack(side=BOTTOM, fill=Y)
        show_toolbar=1

def hide_statusbar():
    global show_statusbar
    if show_statusbar==1:
        statusbar.pack_forget()
        show_statusbar=0
    else:
        statusbar.pack(side=BOTTOM, fill=Y)
        show_statusbar=1

#Making a "main" for making a GUI:-
#height=720              (HEIGHT OF GUI)
#width=1280              (WIDTH OF GUI)
if __name__ == '__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.geometry("1280x720")
    root.wm_iconbitmap("1.ico")


    #Creating Toolbar ribbon:-
    toolbar_ribbon=Label(root)
    toolbar_ribbon.pack(side=TOP, fill=X)

    #Creating FONT and SIZE:-
    #Adding Font:-
    all_font=font.families()
    font_value=StringVar()
    #Adding Font Box:-
    font_box=tk.Combobox(toolbar_ribbon, width=24, height=20, textvariable=font_value, state="readonly")
    font_box["values"]=all_font
    font_box.current(all_font.index("Arial"))
    font_box.bind("<<ComboboxSelected>>", font_change)
    font_box.grid(row=0, column=0, padx=5)

    size_value=IntVar()
    #Adding Size Box:-
    size_box=tk.Combobox(toolbar_ribbon, width=8, height=20, textvariable=size_value, state="readonly")
    size_box["values"]=tuple(range(8, 164, 2))
    size_box.bind("<<ComboboxSelected>>", font_change)
    size_box.current(4)
    size_box.grid(row=0, column=1, padx=5)

    #Creating icon for decorating font:-
    bold_icon=PhotoImage(file="icons for notepad\\bold2_icon.png")
    italic_icon=PhotoImage(file="icons for notepad\\italic_icon.png")
    underline_icon=PhotoImage(file="icons for notepad\\underline_icon.png")
    colourpicker_icon=PhotoImage(file="icons for notepad\\colourpicker_icon.png")

    #Making button for decorating font:-
    #Making bold button:-
    bold=Button(toolbar_ribbon, image=bold_icon, borderwidth=4, relief=GROOVE)
    bold.bind("<Button-1>", bold_font)
    bold.grid(row=0, column=2, padx=5)
    #Making italic button:-
    italic=Button(toolbar_ribbon, image=italic_icon, borderwidth=4, relief=GROOVE)
    italic.bind("<Button-1>", italic_font)
    italic.grid(row=0, column=3, padx=5)
    #Making underline button:-
    underline=Button(toolbar_ribbon, image=underline_icon, borderwidth=4, relief=GROOVE)
    underline.bind("<Button-1>", underline_font)
    underline.grid(row=0, column=4, padx=5)
    #Making colourpicker button:-
    colourpicker=Button(toolbar_ribbon, image=colourpicker_icon, borderwidth=4, relief=GROOVE)
    colourpicker.bind("<Button-1>", colour_chooser)
    colourpicker.grid(row=0, column=5, padx=15)

    #Creating TextArea:-
    typing_area=Text(root, font="arial 16", relief=FLAT, undo=True)
    typing_area.bind("<<Modified>>", change_value)
    typing_area.config(wrap=WORD, relief=FLAT)
    typing_area.focus_set()
    typing_area.pack(expand=True, fill=BOTH)

    #Creating ScrollBar:-
    Scroll = Scrollbar(typing_area)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=typing_area.yview)
    typing_area.config(yscrollcommand=Scroll.set)

    #Creating Statusbar:-
    statusbar=Label(root, text="STATUSBAR", font="arial 12")
    statusbar.bind("<<Modified>>", change_value)
    statusbar.pack(side=BOTTOM, fill=Y)

    #Making icons for File Menubar:-
    new_icon=PhotoImage(file="icons for notepad\\new_icon.png")
    open_icon=PhotoImage(file="icons for notepad\\open_icon.png")
    save_icon=PhotoImage(file="icons for notepad\\save_icon.png")
    saveas_icon=PhotoImage(file="icons for notepad\\saveas_icon.png")
    exit_icon=PhotoImage(file="icons for notepad\\exit_icon.png")

    #Making icons for Edit Menubar:-
    undo_icon=PhotoImage(file="icons for notepad\\undo_icon.png")
    redo_icon=PhotoImage(file="icons for notepad\\redo_icon.png")
    copy_icon=PhotoImage(file="icons for notepad\\copy_icon.png")
    paste_icon=PhotoImage(file="icons for notepad\\paste_icon.png")
    cut_icon=PhotoImage(file="icons for notepad\\cut_icon.png")

    #Making icons for View Menubar:-
    toolbar_icon=PhotoImage(file="icons for notepad\\toolbar_icon.png")
    status_icon=PhotoImage(file="icons for notepad\\status_icon.png")

    #Making icons for About Menubar:-
    feedback_icon=PhotoImage(file="icons for notepad\\feedback_icon.png")
    about_icon=PhotoImage(file="icons for notepad\\about_icon.png")

    #Creating a menubar:-
    menubar=Menu(root)
    #Creating file menu for menubar:-
    file_menu=Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", image=new_icon, compound=LEFT, accelerator="(Ctrl + N)", command=new)
    file_menu.add_command(label="Open", image=open_icon, compound=LEFT, accelerator="(Ctrl + O)", command=_open)
    file_menu.add_separator()
    file_menu.add_command(label="Save", image=save_icon, compound=LEFT, accelerator="(Ctrl+S)", command=save)
    file_menu.add_command(label="Save As", image=saveas_icon, compound=LEFT, command=save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", image=exit_icon, compound=LEFT, accelerator="(Alt + F4)", command=exit)
    #Adding all the buttons in 'File menu':-
    menubar.add_cascade(label="File", menu=file_menu)

    #Creating edit menu for menubar:-
    edit_menu=Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Undo", image=undo_icon, accelerator="(Ctrl + Z)", compound=LEFT, command=typing_area.edit_undo)
    edit_menu.add_command(label="Redo", image=redo_icon, compound=LEFT, accelerator="(Ctrl + Y)", command=typing_area.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_command(label="Copy", image=copy_icon, compound=LEFT, accelerator="(Ctrl + C)", command=copy) #typing_area.event_generate("<Control c>")
    edit_menu.add_command(label="Paste", image=paste_icon, compound=LEFT, accelerator="(Ctrl + V)", command=paste) #typing_area.event_generate("<Control v>")
    edit_menu.add_command(label="Cut", image=cut_icon, compound=LEFT, accelerator="(Ctrl + X)", command=cut) #typing_area.event_generate("<Control x>")
    #Adding all buttons in 'Edit menu':-
    menubar.add_cascade(label="Edit", menu=edit_menu)

    #Creating View menu for menubar:-
    view_menu=Menu(menubar, tearoff=False)
    view_menu.add_checkbutton(label="Hide Toolbar", onvalue=True, offvalue=False, image=toolbar_icon, compound=LEFT, command=hide_toolbar)
    view_menu.add_checkbutton(label="Hide Statusbar", onvalue=True, offvalue=False, image=status_icon, compound=LEFT, command=hide_statusbar)
    #Adding all buttons in 'Edit menu':-
    menubar.add_cascade(label="View", menu=view_menu)

    #Creating help menu for menubar:-
    help_menu=Menu(menubar, tearoff=0)
    help_menu.add_command(label="Send Feedback", image=feedback_icon, compound=LEFT, command=feedback)
    help_menu.add_separator()
    help_menu.add_command(label="About", image=about_icon, compound=LEFT, accelerator="(F1)", command=about)
    #Adding all buttons in 'Help menu':-
    menubar.add_cascade(label="Help", menu=help_menu)

    #Packing it in the root:-
    root.config(menu=menubar)

    root.mainloop()