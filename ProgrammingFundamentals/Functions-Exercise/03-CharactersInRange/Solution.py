def asci_code(character1,character2):
    return [chr(i) for i in range(ord(character1) + 1,ord(character2))]
print(" ".join(asci_code(input(),input())))