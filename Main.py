import tkinter as tk
import tkinter.font as tkFont

def Eval_button_command():
    ques = Question.get()
    ans = eval(ques)
    Answer.delete(0, "end")
    Answer.insert(0, str(ans))

root = tk.Tk()
root.title("Simple Python Calculator")
width=511
height=190
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

Name=tk.Label(root)
ft = tkFont.Font(family='Times',size=20)
Name["font"] = ft
Name["fg"] = "#333333"
Name["justify"] = "center"
Name["text"] = "Simple Calculator"
Name.place(x=110,y=20,width=278,height=30)

Question=tk.Entry(root)
Question["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Question["font"] = ft
Question["fg"] = "#333333"
Question["justify"] = "center"
Question["text"] = ""
Question.place(x=110,y=60,width=371,height=30)

Question_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=20)
Question_label["font"] = ft
Question_label["fg"] = "#333333"
Question_label["justify"] = "center"
Question_label["text"] = "Question"
Question_label.place(x=0,y=60,width=115,height=30)

Answer=tk.Entry(root)
Answer["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Answer["font"] = ft
Answer["fg"] = "#333333"
Answer["justify"] = "center"
Answer["text"] = ""
Answer.place(x=110,y=130,width=371,height=30)

Answer_label=tk.Label(root)
ft = tkFont.Font(family='Times',size=20)
Answer_label["font"] = ft
Answer_label["fg"] = "#333333"
Answer_label["justify"] = "center"
Answer_label["text"] = "Answer"
Answer_label.place(x=0,y=130,width=104,height=30)

Eval_button=tk.Button(root)
Eval_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
Eval_button["font"] = ft
Eval_button["fg"] = "#000000"
Eval_button["justify"] = "center"
Eval_button["text"] = "Evaluate"
Eval_button.place(x=260,y=100,width=70,height=25)
Eval_button["command"] = Eval_button_command



if __name__ == "__main__":
    root.mainloop()