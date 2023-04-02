# function untuk mengecek huruf vokal
def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels
# method untuk menghitung jumlah huruf vokal dan konsonan
class Counter:
    def _init_(self):
        self.vowels = 0
        self.consonants = 0
def count(self, text):
        for char in text:
            if char.isalpha():
                if is_vowel(char):
                    self.vowels += 1
                else:
                    self.consonants += 1
