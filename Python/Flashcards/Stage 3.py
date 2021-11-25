class Flashcards:
    def __init__(self, cards):
        assert isinstance(cards, dict)
        self.cards = cards
    
    def check(self, input_def):
        return input_def == next(iter(self.definitions))
    
    def check_all(self):
        for term, definition in self.cards.items():
            if definition == input(f'Print the definition of "{term}":\n'):
                print('Correct!')
            else:
                print(f'Wrong. The right answer is "{definition}".')
        

def main():
    n, cards = int(input('Input the number of cards:\n')), {}
    for i in range(1, n + 1):
        term = input(f'The term for card #{i}:\n')
        definition = input(f'The definition for card #{i}:\n')
        cards[term] = definition
    
    flashcards = Flashcards(cards)
    flashcards.check_all()

if __name__ == '__main__':
    main()
