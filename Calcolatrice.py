import  tkinter as tk

window = tk.Tk()
window.title("Finestra di prova")
window.geometry("800x800")
window.resizable(True, True)
window.configure(background="black")

etichetta=tk.Label(window, text= "Calcolatrice", fg="blue", font=("Times New Roman", 16), background="lightblue")
etichetta.grid(row=0, column=0, sticky="W", padx=10, pady=10)


#menù e bottone operazione
def stampa_etichetta():
    text="Scegli tra le seguenti operazioni:\n 1) +\n 2) -\n 3) x\n 4) :\n "
    text_output = tk.Label(window, text=text, fg= "white", font=("Times New Roman", 16), background="black")

    text_output.grid(row=1, column=0, sticky="W")

first_button=tk.Button(text="Clicca!", command=stampa_etichetta)
first_button.grid(row=2, column=0, sticky="W")

#input operazione
def stampa_etichetta_input():
    testo = input_text.get()
    text_output1 = tk.Label(window, text=testo, fg="white", font=("Times New Roman", 16),  background="black")
    text_output1.grid(row=4, column=1, sticky="W")

input_text = tk.Entry(window)
input_text.grid(row=5, column=1, sticky="W")

second_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
second_button.grid(row=6, column=1, sticky= "W")

if input_text == 1:
    



#input 1° numero
def stampa_etichetta_input2():
    testo = input_text2.get()
    text_output2 = tk.Label(window, text=testo, fg="white", font=("Times New Roman", 16), background="black")
    text_output2.grid(row=7, column=1, sticky="W")

input_text2 = tk.Entry(window)
input_text2.grid(row=8, column=1, sticky="W")

third_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input2)
third_button.grid(row=9, column=1, sticky= "W")



#input 2° numero
def stampa_etichetta_input3():
    testo = input_text3.get()
    text_output3 = tk.Label(window, text=testo, fg="white", font=("Times New Roman", 16), background="black")
    text_output3.grid(row=10, column=1, sticky="W")

input_text3 = tk.Entry(window)
input_text3.grid(row=11, column=1, sticky="W")

third_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input3)
third_button.grid(row=12, column=1, sticky= "W")










if __name__ == "__main__":
    window.mainloop()
