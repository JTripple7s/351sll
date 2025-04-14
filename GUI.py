import tkinter as tk
from lexer import cutOneLineTokens
from parse import *

current_line = 1

window = tk.Tk()
window.title("Lexical Analyzer for TinyPie")

window.rowconfigure(1, minsize=0, weight=1)
window.columnconfigure(1, minsize=0, weight=1)

#Frame 1: Source Input
#Note that indexing starts at 0
#Row 1, Col 1 of Window
frm_Source = tk.Frame(window, bd=2)
frm_Source.grid(row=0, column=0, sticky="w")

#Row 1 of Frame 1
lbl_SCI = tk.Label(master=frm_Source, text="Source Code Input:") #Source Code Input
lbl_SCI.grid(row=0, column=0, sticky="w", pady=5)

#Row 2 of Frame 1
txt_input = tk.Text(master=frm_Source, relief=tk.SOLID, width=45, height=20)
txt_input.grid(row=1, column=0, padx=20)

#Row 3 of Frame 1
#We want a line number here and a label for it, create another frame
frm_CPL = tk.Frame(master=frm_Source)
frm_CPL.grid(row=2, column=0, sticky="ew")
#Row 1, Col 1 of frm_CPL
lbl_CPL = tk.Label(master=frm_CPL, text=f"Current Processing Line: {current_line}") #Current Processing Line
lbl_CPL.grid(row=0, column=0, sticky="w")

#Row 4 of Frame 1
btn_NextLine = tk.Button(master=frm_Source, text="Next Line")
btn_NextLine.grid(row=3, column=0, sticky="e")

#Frame 2: Result Output
#Row 1, Col 2 of Window
frm_Result = tk.Frame(window, bd=2)
frm_Result.grid(row=0, column=1, sticky="e")

#Row 1 of Frame 2
lbl_LAR = tk.Label(master= frm_Result, text="Lexical Analyzed Result:") #Lexical Analyzed Result
lbl_LAR.grid(row=0, column=0, sticky="w", pady=3)

#Row 2 of Frame 2
txt_result = tk.Text(master=frm_Result, relief=tk.SOLID, width=45, height=20)
txt_result.grid(row=1, column=0, padx=20)

#Row 3 of Frame 2
#Nothing is here
lbl_dummy = tk.Label(master=frm_Result)
lbl_dummy.grid(row=2, column=0)

#Row 4 of Frame 2
#Nothing is here
lbl_dummy2 = tk.Label(master=frm_Result)
lbl_dummy2.grid(row=3, column=0)

#Frame 3: Parse Tree
#Row 1, Col 3 of Window
frm_Parse = tk.Frame(window, bd=2)
frm_Parse.grid(row=0, column=2, sticky="e")

#Row 1 of Frame 3
lbl_PTR = tk.Label(master= frm_Parse, text="Parse Tree Result:") #Lexical Analyzed Result
lbl_PTR.grid(row=0, column=0, sticky="w", pady=5)

#Row 2 of Frame 3
txt_prsResult = tk.Text(master=frm_Parse, relief=tk.SOLID, width=45, height=20)
txt_prsResult.grid(row=1, column=0, padx=20)

#Row 3 of Frame 3
#Nothing is here
lbl_dummy = tk.Label(master=frm_Parse)
lbl_dummy.grid(row=2, column=0)

#Row 4 of Frame 3
btn_Quit = tk.Button(master=frm_Parse, text="Quit", command=window.quit)
btn_Quit.grid(row=3, column=0, sticky="e")

def btn_NextLine_click():
    global current_line
    start_index = f"{current_line}.0"
    end_index = f"{current_line}.end"

    source_line = txt_input.get(start_index, end_index).strip()
    if source_line:
        tokens = cutOneLineTokens(source_line)
        txt_result.delete("1.0", tk.END)
        for i in tokens:
            txt_result.insert(tk.END, str(i)+"\n")
        parser = Parser(tokens)
        tree = parser.parse_one_line()
        txt_prsResult.delete("1.0", tk.END)
        txt_prsResult.insert(tk.END, str(tree))

    else:
        txt_result.delete("1.0", tk.END)
        txt_result.insert(tk.END, "No Input")

    current_line += 1
    lbl_CPL.config(text=f"Current Processing Line: {current_line}")

btn_NextLine.config(command=btn_NextLine_click)
window.mainloop()
