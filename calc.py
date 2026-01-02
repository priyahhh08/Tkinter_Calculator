import tkinter as tk 
# imports Tkinter module,tk is an alias for easy access

# button click handler
def press(v):
    entry.insert(tk.END, v)  #entry is the text field
'''Called when a number or operator button is clicked,
inserts the pressed val (v) at end of entry widget'''

# Clear function
def clear():
    entry.delete(0, tk.END)
'''clears the calculator screen
delets all characters from index 0 - END'''

# calculation function
def calc():
    try:
        result = eval(entry.get())
        '''enrty.get()retrives the expressions (e.g. 5+3)
        eval() evaluates the string as a python expression'''

        entry.delete(0, tk.END) #clears the old expression
        entry.insert(0, result) #displays the result of expression

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid expression")
        '''Handles invalid expressions (e.g. 5++)
        Displays "error" instead of crashing'''


# Main window creation
root=tk.Tk()
'''Creates the main application window'''
root.title("Calculator")
'''sets window title'''
root.configure(bg="#1e1e1e")
'''sets the background color (dark theme)'''
root.resizable(False, False)

#Enrty widgets (Display screen)
entry=tk.Entry(
    root,
    font=("Times new Roman",20),  #font type, size
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
    )
'''acts as calculator display
right-aligned for better calculator look'''
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
'''place entry at top
columnspan=4 makes it streach across 4 columns'''

#button labels
buttons=[
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]
# Represent calculator buttons stored in list to reduce repetitive code

# dynamic button creation
r=1
c=0
'''Row and column counters for grid layout'''

for b in buttons: #iterates through each button label
    cmd = calc if b == "=" else lambda x=b: press(x)
    '''if button is "=", cal calc()
    otherwise call press() with the button value
    lambda x=b prevents late binding issue'''

    tk.Button(
        root,
        text=b,
        command=cmd, #these threelines creates button widgets
        font=("Calibri", 14),
        width=5,
        height=2,
        bg="#ff9550" if b in "+-*/" else "#3a3a3a",
        #operator buttons are orange, number buttons are gray
        fg="white",
        bd=0,
    ).grid(row=r, column=c, padx=6, pady=6)

    c+=1
    #after 4 columns, move to next row
    if c==4:
        r+=1
        c=0
    #moves to next row after 4 buttons


# clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri", 14),
    bg="#f3bf3b",
    fg="white",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4, pady=8)
'''clear the calculator
Spans across all columns'''


# Event loop
root.mainloop()
'''Keeps the window running
Listens for the user intercations'''