from controle.controlador_sistema import ControladorSistema

if __name__ == "__main__":
  ct1 = ControladorSistema()
  ct1.inicializa_sistema()

  #teste Singleton. Ao tentar inicializar um segundo objeto, ele retorna o já existente.
  #ct2 = ControladorSistema()
  #print("é a mesma instância? ", ct1 is ct2)


