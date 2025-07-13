def caesar_cipher(text: str, shift: int) -> str:
    """
    Apply a Caesar shift to the given text.
    Positive shift → encryption; negative shift → decryption.
    Non-alphabetic characters are unchanged.
    """
    result = []

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            
            offset = (ord(ch) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(ch)

    return ''.join(result)


def main():
    print("Caesar Cipher")
    print("-------------")


    while True:
        mode = input("Type 'e' to encrypt, 'd' to decrypt: ").strip().lower()
        if mode in ('e', 'd'):
            break
        print("Please enter 'e' or 'd'.")

    msg = input("Enter your message: ")

    while True:
        try:
            shift_val = int(input("Enter shift value (e.g. 3): "))
            break
        except ValueError:
            print("That's not a valid integer. Try again.")

    
    if mode == 'd':
        shift_val = -shift_val

    transformed = caesar_cipher(msg, shift_val)
    action = "Encrypted" if mode == 'e' else "Decrypted"
    print(f"\n{action} message:")
    print(transformed)


if __name__ == "__main__":
    main()
