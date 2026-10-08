import tkinter as tk


class Tamagoxi:
	def __init__(self, root):
		self.root = root
		self.root.title("Tamagoxi")
		self.root.geometry("420x500")
		self.root.resizable(False, False)
		self.vivo = False
		self.dormindo = False
		self.tela_criacao()

	def limpar_tela(self):
		for widget in self.root.winfo_children():
			widget.destroy()

	def tela_criacao(self):
		self.limpar_tela()
		tk.Label(self.root, text="Crie seu Tamagoxi", font=("Arial", 22, "bold")).pack(pady=35)
		tk.Label(self.root, text="Nome do animal:").pack()
		self.nome_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
		self.nome_entry.pack(pady=8)
		self.nome_entry.focus_set()
		self.aviso = tk.Label(self.root, text="", fg="red")
		self.aviso.pack()
		tk.Button(self.root, text="NASCER", command=self.nascer,
				  font=("Arial", 14, "bold"), bg="#91e6a1", width=16).pack(pady=15)
		tk.Label(self.root, text="A energia diminui com o tempo. Cuide bem dele!").pack(pady=8)

	def nascer(self):
		nome = self.nome_entry.get().strip()
		if not nome:
			self.aviso.config(text="Digite um nome para o seu animal.")
			return
		self.nome = nome
		self.energia = 100
		self.vivo = True
		self.dormindo = False
		self.tela_jogo()
		self.root.after(4000, self.diminuir_energia)

	def tela_jogo(self):
		self.limpar_tela()
		tk.Label(self.root, text=self.nome, font=("Arial", 22, "bold")).pack(pady=(20, 5))
		self.indicador_energia = tk.Label(self.root, font=("Arial", 14, "bold"))
		self.indicador_energia.pack(pady=5)

		self.canvas = tk.Canvas(self.root, width=220, height=190, bg="white", highlightthickness=1)
		self.canvas.pack(pady=15)
		# Cabeça branca, orelhas caídas e manchas pretas de dálmata.
		self.canvas.create_oval(28, 55, 72, 130, fill="black", outline="#333333", width=2)
		self.canvas.create_oval(148, 55, 192, 130, fill="black", outline="#333333", width=2)
		self.canvas.create_oval(35, 20, 185, 175, fill="white", outline="#333333", width=3)
		for x, y, tamanho in [(51, 45, 10), (155, 42, 12), (47, 115, 9),
							 (165, 112, 10), (70, 145, 8), (143, 148, 7)]:
			self.canvas.create_oval(x, y, x + tamanho, y + tamanho,
								 fill="black", outline="black")
		self.canvas.create_oval(75, 75, 87, 87, fill="black")
		self.canvas.create_oval(133, 75, 145, 87, fill="black")
		self.canvas.create_oval(99, 94, 121, 109, fill="black", outline="black")
		self.boca = self.canvas.create_arc(85, 90, 135, 130, start=200, extent=140, style="arc", width=3)

		botoes = tk.Frame(self.root)
		botoes.pack(pady=10)
		tk.Button(botoes, text="Comer (+20)", command=self.comer,
				  font=("Arial", 12), bg="#ffe08a").grid(row=0, column=0, padx=6)
		tk.Button(botoes, text="Tomar banho (-5)", command=self.tomar_banho,
				  font=("Arial", 12), bg="#9de4f2").grid(row=0, column=1, padx=6)
		self.botao_dormir = tk.Button(self.root, text="Dormir (5 min)", command=self.dormir,
								  font=("Arial", 12), bg="#c7b8f5")
		self.botao_dormir.pack(pady=5)
		self.mensagem = tk.Label(self.root, text="Seu animal nasceu!", font=("Arial", 11))
		self.mensagem.pack(pady=10)
		self.atualizar_energia()

	def atualizar_energia(self):
		if self.energia >= 80:
			humor, extent = "feliz", 140
		elif self.energia >= 60:
			humor, extent = "tranquilo", 110
		elif self.energia >= 40:
			humor, extent = "preocupado", 70
		elif self.energia >= 20:
			humor, extent = "triste", 35
		else:
			humor, extent = "muito triste", 0
		self.indicador_energia.config(text=f"Energia: {self.energia}% — {humor}")
		self.canvas.itemconfigure(self.boca, extent=extent)

	def comer(self):
		if self.energia + 20 > 100:
			self.mensagem.config(text=f"{self.nome} comeu demais e vomitou!")
			self.morrer("Ele comeu demais, vomitou e morreu.")
			return
		self.alterar_energia(20, f"{self.nome} comeu e recuperou energia!")

	def dormir(self):
		if not self.vivo or self.dormindo:
			return
		self.dormindo = True
		self.botao_dormir.config(state="disabled")
		self.mensagem.config(text="Está dormindo... acorda em 5:00.")
		self.atualizar_contagem_sono(300)

	def atualizar_contagem_sono(self, segundos):
		if not self.vivo or not self.dormindo:
			return
		if segundos <= 0:
			self.dormindo = False
			self.energia = min(100, self.energia + 40)
			self.atualizar_energia()
			self.botao_dormir.config(state="normal")
			self.mensagem.config(text=f"{self.nome} acordou descansado e recuperou energia!")
			self.root.after(4000, self.diminuir_energia)
			return
		self.mensagem.config(text=f"Está dormindo... acorda em {segundos // 60}:{segundos % 60:02d}.")
		self.root.after(1000, self.atualizar_contagem_sono, segundos - 1)

	def tomar_banho(self):
		self.alterar_energia(-5, f"{self.nome} tomou banho. Que limpinho!")

	def alterar_energia(self, quantidade, mensagem):
		if not self.vivo:
			return
		self.energia = max(0, min(100, self.energia + quantidade))
		self.atualizar_energia()
		self.mensagem.config(text=mensagem)
		if self.energia == 0:
			self.morrer()

	def diminuir_energia(self):
		if not self.vivo:
			return
		if self.dormindo:
			return
		self.energia = max(0, self.energia - 5)
		self.atualizar_energia()
		if self.energia == 0:
			self.morrer()
		else:
			self.root.after(4000, self.diminuir_energia)

	def morrer(self, motivo="A energia chegou a zero."):
		self.vivo = False
		self.dormindo = False
		self.limpar_tela()
		tk.Label(self.root, text="☠", font=("Arial", 70), fg="#555555").pack(pady=(55, 5))
		tk.Label(self.root, text=f"{self.nome} morreu...", font=("Arial", 22, "bold"),
				 fg="#aa3333").pack(pady=8)
		tk.Label(self.root, text=motivo).pack(pady=5)
		tk.Label(self.root, text="RETRY", font=("Arial", 24, "bold"), fg="#4444aa").pack(pady=18)
		tk.Button(self.root, text="Tentar novamente", command=self.tela_criacao,
				  font=("Arial", 14), bg="#91e6a1", width=18).pack(pady=10)


if __name__ == "__main__":
	janela = tk.Tk()
	Tamagoxi(janela)
	janela.mainloop()
