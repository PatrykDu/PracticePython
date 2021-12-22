import tkinter as tk


def clean_file():
    with open('user_data_commas.txt', 'w') as file:
        file.write('')


def clean_memory():
    global memory
    memory = []
    return memory


def add_line():
    global memory
    memory.append(e1.get())
    e1.delete(0, 'end')
    return memory


def close():
    for item in memory:
        with open('user_data_commas.txt', 'a') as file:
            file.write(str(item + '\n'))
    exit()


def save():
    for item in memory:
        with open('user_data_commas.txt', 'a') as file:
            file.write(str(item + '\n'))
    clean_memory()


master = tk.Tk()
clean_file()
memory = []

e1 = tk.Entry(master)
b1 = tk.Button(master, text='Add line', command=add_line)
b2 = tk.Button(master, text='Save changes', command=save)
b3 = tk.Button(master, text='Save and Close', command=close)

e1.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

master.mainloop()
