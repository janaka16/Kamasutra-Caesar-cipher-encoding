import matplotlib.pyplot as plt
import string

class Kcipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        a = self.key[:len(self.key) // 2] #key1
        b = self.key[len(self.key) // 2:] #key2

        encrypted = ""
        for c in text:
            if c.isalpha():
                cl = c.lower()
                i1 = a.find(cl)
                i2 = b.find(cl)

                if i1 != -1:
                    if c.islower():
                        encrypted += b[i1]
                    else:
                        encrypted += b[i1].upper()
                elif i2 != -1:
                    if c.islower():
                        encrypted += a[i2]
                    else:
                        encrypted += a[i2].upper()
                else:
                    encrypted += c
            else:
                encrypted += c

        return encrypted


class Cipher:
    @staticmethod
    def caesar_cipher(text, shift, alphs):
        def shift_alph(alphabet):
            return alphabet[shift:] + alphabet[:shift]

        shifted_alphs = tuple(map(shift_alph, alphs))
        final_alph = ''.join(alphs)
        final_shift = ''.join(shifted_alphs)
        table = str.maketrans(final_alph, final_shift)
        return text.translate(table)

    @staticmethod
    def frequency_analysis(text):
        freq = {char: 0 for char in string.ascii_lowercase}

        for char in text:
            if char.isalpha():
                freq[char.lower()] += 1

        for char in freq:
            freq[char] = round(freq[char] / len(text.replace(" ", "")) * 100, 2)

        return freq

    @staticmethod
    def plot_histogram(frequencies):
        letters = list(frequencies.keys())  
        percentages = list(frequencies.values())  
        plt.bar(letters, percentages, edgecolor='black', color='red') 
        plt.xlabel('Letters')
        plt.ylabel('Percentage (%)')
        plt.title('Frequency of Letters in Cipher Text')
        plt.ylim(0, 100)  #
        plt.yticks(range(0, 101, 5))
        plt.show()


plain_text = "Janaka Herath"

#kamasutra
kamasutra_key = "wirlzubjqycvfaxdmtesnpgokh"
cipher = Kcipher(kamasutra_key)
encrypted_text = cipher.encrypt(plain_text)
print("Encrypted (Cipher):", encrypted_text)


#Caesar cipher with shift 11
caesar_cipher_text = Cipher.caesar_cipher(plain_text, 11, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation])
print(f"Caesar Cipher Text (Shift 11): {caesar_cipher_text}")

# Frequency analysis
caesar_freq = Cipher.frequency_analysis(caesar_cipher_text)
print("Frequency Analysis of Caesar Cipher Text:")
print(caesar_freq)

#histogram
Cipher.plot_histogram(caesar_freq)