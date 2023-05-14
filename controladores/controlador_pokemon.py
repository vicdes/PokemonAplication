
from exceptions.pokemon_inexistente_exception import PokemonInexistenteException
from telas.tela_pokemon import TelaPokemon
from entidades.pokemon import Pokemon
from entidades.tipo_pokemon import TipoPokemon

class ControladorPokemon():
    lista_pokemons = [] 
    lista_pokemons_iniciais = [Pokemon("Bulbasaur", 1, 45, 49, [TipoPokemon("Grama")]), Pokemon("Charmander", 4, 39, 52,[TipoPokemon("Fogo")]), Pokemon("Squirtle", 7, 44, 48,[TipoPokemon("Água")])]
    
    def __init__(self, controlador_sistema):
        self.__tela_pokemon = TelaPokemon()
        self.__controlador_sistema = controlador_sistema
        # * adicionar controlador_sistema: ControladorSistema no init depois
    
    
    def add_pokemon(self, pokemon): # adiciona um pokémon novo a lista de pokémons
        self.lista_pokemons.append(pokemon)

    def add_lista(pokemon):
        ControladorPokemon.lista_pokemons.append(pokemon)

    def del_pokemon(self):
        try:
            pokemon = self.selecionar_pokemon()
            ControladorPokemon.lista_pokemons.remove(pokemon)
            self.__tela_pokemon.mostra_mensagem(f"\n[!] O pokemon {pokemon.nome} foi removido do jogo com sucesso.")
        
        except PokemonInexistenteException as e:
            self.__tela_pokemon.mostra_mensagem(e)
            #print deu ruim
        
    def selecionar_pokemon(self):
        num_pokemon = self.__tela_pokemon.seleciona_pokemon_numero()
        for pokemon in self.lista_pokemons:
            if pokemon.num == num_pokemon:
                return pokemon
        
        raise PokemonInexistenteException(num_pokemon)

    def altera_status(self):
        try:
            pokemon = self.selecionar_pokemon()
            self.__tela_pokemon.mostra_mensagem(f'\nPokemon selecionado:\n     {pokemon.nome} #{pokemon.num}, {pokemon.hp}HP, {pokemon.ataque} Ataque')
            
            novo_hp = self.__tela_pokemon.le_num_inteiro("\nDigite o novo valor de HP: ")
            novo_ataque = self.__tela_pokemon.le_num_inteiro("Digite o novo valor de ataque: ")
            pokemon.hp = novo_hp
            pokemon.ataque = novo_ataque

            self.__tela_pokemon.mostra_mensagem(f'\nPokemon selecionado com seus atributos alterados:\n     {pokemon.nome} #{pokemon.num}, {pokemon.hp}HP, {pokemon.ataque} Ataque')
        
        except PokemonInexistenteException as e:
            self.__tela_pokemon.mostra_mensagem(e)
            
    def mostra_pokemons(self):
        pokemons = ControladorPokemon.lista_pokemons
        nomes_e_nums = []
        for pokemon in pokemons:
            nomes_e_nums.append((pokemon.nome, pokemon.num))
        self.__tela_pokemon.mostrar_pokemons(nomes_e_nums)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.del_pokemon, 2: self.mostra_pokemons, 3:self.altera_status, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pokemon.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()