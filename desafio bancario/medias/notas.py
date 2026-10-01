import tkinter as tk


def receber_nota():
    while True:
     nota = float(input("digite as notas:"))
     if nota <= 0 or nota <= 10:
        print("nota invalida! a nota deve ser de 0 a 10!")
     else:
        return receber_nota
     return nota


def calcular_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3
    return media
import tkinter as tk

def calcular_media():
    try:
        media = (float(nota1.get()) + float(nota2.get()) + float(nota3.get())) / 3
        resultado.config(text=f"Média: {media:.2f}")
    except ValueError:
        resultado.config(text="Preencha as três notas com números.")

janela = tk.Tk()
janela.title("Média das notas")

tk.Label(janela, text="Nota 1").pack()
nota1 = tk.Entry(janela)
nota1.pack()

tk.Label(janela, text="Nota 2").pack()
nota2 = tk.Entry(janela)
nota2.pack()

tk.Label(janela, text="Nota 3").pack()
nota3 = tk.Entry(janela)
nota3.pack()

tk.Button(janela, text="Calcular", command=calcular_media).pack()
resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()


nota1 = receber_nota()
nota2 = receber_nota()
nota3 = receber_nota()
media = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {media}")




