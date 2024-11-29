import  tkinter as tk

window = tk.Tk()
window.title("Finestra di prova")
window.geometry("800x800")
window.resizable(True, True)
window.configure(background="black")

etichetta=tk.Label(window, text= "Etichetta di prova", fg="white", font=("Times New Roman", 16), background="black")
etichetta.grid(row=0, column=0, sticky="W", padx=10, pady=10)

def stampa_etichetta():
    text= "Etichetta di prova da funzione"
    text_output = tk.Label(window, text=text, fg= "white", font=("Times New Roman", 16), background="black")

    text_output.grid(row=1, column=1, sticky="W")

first_button=tk.Button(text="Clicca!", command=stampa_etichetta)
first_button.grid(row=1, column=0, sticky="E")


#funzione per stampare un'etichetta con input 
def stampa_etichetta_input():
    testo = input_text.get()
    text_output1 = tk.Label(window, text=testo, fg="white", font=("Times New Roman", 16))
    text_output1.grid(row=15, column=0, sticky="S")

#creazione del campo di input
input_text = tk.Entry(window)
input_text.grid(row=20, column=10, sticky="W")

#creazione del secondo bottone
second_button = tk.Button(window, text="Clicca!", command=stampa_etichetta_input)
second_button.grid(row=3, column=0, sticky= "W")

if __name__ == "__main__":
    window.mainloop()


