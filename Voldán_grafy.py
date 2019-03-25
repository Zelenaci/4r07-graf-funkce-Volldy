import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry, Label, Button, filedialog
import pylab as lab

start = tk.Tk()
start.title("Graf funkce")

###GUI###
hlavniFrame = LabelFrame(start, text = "Vygeneruj graf funkce", padx=5, pady=5)
hlavniFrame.grid(row=0, column=0)

zesouboruFrame=LabelFrame(start, text = "Vygeneruj si graf ze souboru", padx=5, pady=5)
zesouboruFrame.grid(row=1, column=0)

osypopisFrame=LabelFrame(start, text = "Popiš si své osy", padx=5, pady=5)
osypopisFrame.grid(row=2, column=0)

graf=LabelFrame(start, text = "Vygeneruj")
graf.grid(row=0, column=1)

graf2=LabelFrame(start, text = "Vygeneruj")
graf2.grid(row=1, column=1)

###PROMĚNNÉ###
funkceMin=tk.StringVar()
funkceMax=tk.StringVar()

osaxVar=tk.StringVar()
osayVar=tk.StringVar()

funkceVar=tk.StringVar()

zesouboruVar=tk.StringVar()

def zesouboruVyber():
    cesta= filedialog.askopenfilename(title="Vyber si mě")
    if cesta != '':
        zesouboruVar.set(cesta)

def funkceGraf():
    try:
        od = float(funkceMin.get())
        do = float(funkceMax.get())
        x=lab.linspace(od, do, 500)
        if funkceVar.get() == "sin":
            y=lab.sin(x)
        elif funkceVar.get() == "log":
            y=lab.log10(x)
        elif funkceVar.get() == "exp":
            y=lab.exp(x)
        lab.figure()
        lab.plot(x,y)
        lab.xlabel(osaxVar.get())
        lab.ylabel(osayVar.get())
        lab.grid(True)
        lab.show()
    except:
        pass

def zeSouboru():
    try:
        cesta=zesouboruVar.get()
        f=open(cesta,"r")
        od=[]
        do=[]
        while 1:
            radek=f.readline()
            if radek == "":
                break
            cisla=radek.split()
            od.append(float(cisla[0]))
            do.append(float(cisla[1]))
            x=lab.linspace(od, do, 500)
        if funkceVar.get() == "sin":
            y=lab.sin(x)
        elif funkceVar.get() == "log":
            y=lab.log10(x)
        elif funkceVar.get() == "exp":
            y=lab.exp(x)
        f.close()
        lab.figure()
        lab.plot(x,y)
        lab.xlabel(osaxVar.get())
        lab.ylabel(osayVar.get())
        lab.grid(True)
        lab.show()
    except:
        pass

###Graf funkce menu###
Radiobutton(hlavniFrame, variable=funkceVar, text="Sin", value="sin").grid(row=0, column=0)
Radiobutton(hlavniFrame, variable=funkceVar, text="Log", value="log").grid(row=0, column=1)
Radiobutton(hlavniFrame, variable=funkceVar, text="Exp", value="exp").grid(row=0, column=2)

Entry(hlavniFrame, textvariable=funkceMin, width=5).grid(row=1, column=1, columnspan=2)
Entry(hlavniFrame, textvariable=funkceMax, width=5).grid(row=2, column=1, columnspan=2)

Label(hlavniFrame, text="Od").grid(row=1, column=0) 
Label(hlavniFrame, text="Do").grid(row=2, column=0)

Button(graf, height=2, width=3, background="#00FFFF", activebackground="#800080", command=funkceGraf).grid(column=2)

###Popisky OS menu###
Label(osypopisFrame, text="osa X").grid(row=0, column=0)
Label(osypopisFrame, text="osa Y").grid(row=1, column=0)

osaXEntry=Entry(osypopisFrame, textvariable=osaxVar, width=5).grid(row=0, column=1, columnspan=2)
osaYEntry=Entry(osypopisFrame, textvariable=osayVar, width=5).grid(row=1, column=1, columnspan=2)

###Graf ze souboru###
Button(zesouboruFrame, text="Vyber souborek", command=zesouboruVyber).grid(row=1, column=0)
Entry(zesouboruFrame, textvariable=zesouboruVar).grid(row=0, column=0)
Button(graf2, height=2, width=3, background="#00FFFF", activebackground="#800080", command=zeSouboru).grid(column=2)

start.mainloop()
