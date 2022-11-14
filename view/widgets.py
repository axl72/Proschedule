import tkinter as tk

class Ventana():
    
    pass



if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.geometry("800x500+300+200")


    height = 30
    width = 5
    cells = {}
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Entry(ventana, text="")
            b.grid(row=i, column=j)
            cells[(i,j)] = b

    ventana.mainloop()