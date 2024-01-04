import copy
class Memento:
    def __init__(self, turn, player1,pokemon1,player2,pokemon2):
        self.turn = turn
        self.player1 = copy.deepcopy(player1)
        self.pokemon1 = copy.deepcopy(pokemon1)
        self.player2 = copy.deepcopy(player2)
        self.pokemon2 = copy.deepcopy(pokemon2)

    def get_turn(self):
        return copy.deepcopy(self.turn)
    
    def get_player1(self):
        return copy.deepcopy(self.player1)
    
    def get_player2(self):
        return copy.deepcopy(self.player2)
    
    def get_pokemon1(self):
        return copy.deepcopy(self.pokemon1)
    
    def get_pokemon2(self):
        return copy.deepcopy(self.pokemon2)


# Wzorzec Strategii: ok
# Wykorzystaj wzorzec strategii do reprezentowania różnych ataków i umiejętności Pokemonów. Każdy atak może być osobnym obiektem implementującym wspólny interfejs.

# Wzorzec Stanu:
# Możesz użyć wzorca stanu do reprezentowania różnych stanów walki, takich jak "atak", "obrona", "czekanie". Każdy stan może mieć swoje własne zachowanie.

# Wzorzec Obserwatora: nie
# Wzorzec obserwatora może być użyteczny do śledzenia zdarzeń w grze, takich jak zmiana zdrowia Pokemonów, zakończenie walki itp.

# Wzorzec Kompozytu: raczej nie
# Możesz użyć wzorca kompozytu do zorganizowania struktury Pokemonów, gdzie każdy Pokemon może składać się z podstawowych komponentów, takich jak głowa, ciało, nogi, każdy z własnymi statystykami.

# Wzorzec Fabryki: podobne do strategii
# Wzorzec fabryki może być zastosowany do tworzenia różnych rodzajów Pokemonów. Każdy typ Pokemonów może być tworzony przez odpowiednią fabrykę.

# Wzorzec Komendy:
# Możesz użyć wzorca komendy do implementacji kolejki ruchów w walce. Każdy atak może być reprezentowany jako obiekt komendy.

# Wzorzec Dekoratora:
# Wzorzec dekoratora może być zastosowany do dodawania dodatkowych zdolności do Pokemonów w trakcie gry.

# Wzorzec Łańcucha Odpowiedzialności:
# Możesz użyć wzorca łańcucha odpowiedzialności do obsługi różnych zdarzeń w grze, takich jak otrzymywanie obrażeń.

# Wzorzec Singleton:
# Możesz zastosować wzorzec singleton do zarządzania globalnym stanem gry, na przykład licznikiem rund czy wynikiem.