from time import sleep
import os
import time

vivo = 1

class Star_Adventure:
	gasolina = 100
	eletricidade = 100
	consumo = 0.5
	oxigenio = 100
	sistema_vital = True
	motor = False
	aceleracao = 0
	
	def status(self):
		for i in range(3):
			sleep(0.5)
			print("loading...")
		print(f"----------------------\n  Bem vindo capitão\n     \nGasolina: {self.gasolina}%\nEnergia: {self.eletricidade:,.2f}%\nOxigenio: {self.oxigenio:,.2f}%\nSistema vital: {self.sistema_vital}\nMotores: {self.motor}\nVelocidade: {self.aceleracao}\n----------------------")
		
		


g = Star_Adventure()						
while vivo == 1:
  if g.oxigenio <= 25:
  	print("Alerta... Oxigênio baixo ")
  elif g.motor == True:
  	g.gasolina -= 10
  	g.aceleracao += 10
  elif g.motor == False:
  	if g.aceleracao > 0:
  		g.aceleracao -= 5
  	
  if g.oxigenio < 0:
  	vivo = 0
  	
  c = str.lower(input("..."))									
  if c == "status":
  	g.eletricidade -= 1
  	g.oxigenio -= 0.5
  	g.status()
  elif c == "sv.off":
  	g.eletricidade -= 1
  	g.oxigenio -= 0.5
  	if g.sistema_vital == True:
  		g.sistema_vital = False
  		g.oxigenio -= 85
  	else:
  		print("impossivel executar")
  		time.sleep(5)
  		os.system('cls' if os.name == 'nt' else 'clear')
  elif c == "sv.on":
  	g.eletricidade -= 1
  	g.oxigenio -= 1
  	if g.sistema_vital == False:
  		g.sistema_vital = True
  		p = 50 - int(g.oxigenio)
  		for i in range(p):
  			g.oxigenio += 1
  	else:
  	    print("impossivel executar")
  elif c == "sv":
  	g.eletricidade -= 0.5
  	g.oxigenio -= 0.5
  	if g.sistema_vital == True:
  		print("---------------\nSitema vital operante e ativo")
  	else:
  		print("---------------\nSitema vital inoperante e/ou inativo")
  elif c == "motor.on":
    g.motor = True
  elif c == "motor.off":
    g.motor = False
  elif c == "motor.destroy":
    vivo = 0
  else:
    print("Comando invalido")
