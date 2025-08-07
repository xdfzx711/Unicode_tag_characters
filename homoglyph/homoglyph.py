#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HomoglyphGenerator:
    def __init__(self):
        # Common homoglyph mapping table
        self.homoglyphs = {
            # Latin letters
            'a': ['а', 'ɑ', 'α', 'ａ'],  # Cyrillic а, Latin small ɑ, Greek α, Fullwidth a
            'A': ['А', 'Α', 'Ａ'],  # Cyrillic А, Greek Α, Fullwidth A
            'o': ['о', 'ο', 'ｏ', '0'],  # Cyrillic о, Greek ο, Fullwidth o, Digit 0
            'O': ['О', 'Ο', 'Ｏ', '０'],  # Cyrillic О, Greek Ο, Fullwidth O, Fullwidth 0
            'e': ['е', 'ｅ'],  # Cyrillic е, Fullwidth e
            'E': ['Е', 'Ｅ'],  # Cyrillic Е, Fullwidth E
            'p': ['р', 'ρ', 'ｐ'],  # Cyrillic р, Greek ρ, Fullwidth p
            'P': ['Р', 'Ρ', 'Ｐ'],  # Cyrillic Р, Greek Ρ, Fullwidth P
            'c': ['с', 'ｃ'],  # Cyrillic с, Fullwidth c
            'C': ['С', 'Ｃ'],  # Cyrillic С, Fullwidth C
            'x': ['х', 'χ', 'ｘ'],  # Cyrillic х, Greek χ, Fullwidth x
            'X': ['Х', 'Χ', 'Ｘ'],  # Cyrillic Х, Greek Χ, Fullwidth X
            'y': ['у', 'γ', 'ｙ'],  # Cyrillic у, Greek γ, Fullwidth y
            'Y': ['Υ', 'Ｙ'],  # Greek Υ, Fullwidth Y
            'B': ['В', 'Β', 'Ｂ'],  # Cyrillic В, Greek Β, Fullwidth B
            'H': ['Н', 'Η', 'Ｈ'],  # Cyrillic Н, Greek Η, Fullwidth H
            'K': ['К', 'Κ', 'Ｋ'],  # Cyrillic К, Greek Κ, Fullwidth K
            'M': ['М', 'Μ', 'Ｍ'],  # Cyrillic М, Greek Μ, Fullwidth M
            'T': ['Т', 'Τ', 'Ｔ'],  # Cyrillic Т, Greek Τ, Fullwidth T

            # Digits
            '0': ['О', 'Ο', 'ο', 'о', '０'],  # Various letter O and fullwidth 0
            '1': ['１', 'l', 'I', '|'],  # Fullwidth 1, lowercase l, uppercase I, vertical bar
            '2': ['２'],  # Fullwidth 2
            '3': ['３'],  # Fullwidth 3
            '4': ['４'],  # Fullwidth 4
            '5': ['５'],  # Fullwidth 5
            '6': ['６'],  # Fullwidth 6
            '7': ['７'],  # Fullwidth 7
            '8': ['８'],  # Fullwidth 8
            '9': ['９'],  # Fullwidth 9

            # Special characters
            '-': ['‐', '‑', '‒', '–', '—', '－'],  # Various hyphens and dashes
            '.': ['․', '‧', '。', '．'],  # Various dots
            ',': ['‚', '，'],  # Various commas
            ';': ['；'],  # Fullwidth semicolon
            ':': ['：'],  # Fullwidth colon
            '!': ['！'],  # Fullwidth exclamation mark
            '?': ['？'],  # Fullwidth question mark
            '"': ['"', '"', '＂'],  # Various quotation marks
            "'": ["'", "'", '＇'],  # Various apostrophes
            '(': ['（'],  # Fullwidth left parenthesis
            ')': ['）'],  # Fullwidth right parenthesis
            ' ': ['\u2000', '\u2001', '\u2002', '\u2003', '\u2004', '\u2005',
                  '\u2006', '\u2007', '\u2008', '\u2009', '\u200A', '\u3000'],  # Various spaces
        }

    def generate_variants(self, text, max_variants=5):
        """
        Generate homoglyph variants for the given text

        Args:
            text (str): Input text
            max_variants (int): Maximum number of variants

        Returns:
            list: List containing the original text and variants
        """
        variants = [text]  # Include original text

        import itertools
        import random

        # Find positions in the text that can be replaced
        replaceable_positions = []
        for i, char in enumerate(text):
            if char in self.homoglyphs and len(self.homoglyphs[char]) > 0:
                replaceable_positions.append((i, char))

        if not replaceable_positions:
            return variants

        # Generate variants
        generated_count = 0
        attempts = 0
        max_attempts = max_variants * 10  # Avoid infinite loop

        while generated_count < max_variants and attempts < max_attempts:
            attempts += 1
            new_text = list(text)

            # Randomly choose characters to replace
            num_replacements = random.randint(1, min(3, len(replaceable_positions)))
            positions_to_replace = random.sample(replaceable_positions, num_replacements)

            for pos, original_char in positions_to_replace:
                # Randomly select a homoglyph replacement
                replacement = random.choice(self.homoglyphs[original_char])
                new_text[pos] = replacement

            new_variant = ''.join(new_text)
            if new_variant not in variants:
                variants.append(new_variant)
                generated_count += 1

        return variants

    def show_unicode_info(self, text):
        """Display Unicode information for each character in the text"""
        print(f"Text: {text}")
        print("Character details:")
        for i, char in enumerate(text):
            print(f"  Position {i}: '{char}' (U+{ord(char):04X}) - {self.get_char_name(char)}")
        print()

    def get_char_name(self, char):
        """Get descriptive name of a character"""
        import unicodedata
        try:
            return unicodedata.name(char)
        except ValueError:
            return "Unknown character"

    def compare_texts(self, text1, text2):
        """Compare differences between two texts"""
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Visually identical: {'Yes' if text1 == text2 else 'No'}")
        print(f"Encoding identical: {'Yes' if text1.encode() == text2.encode() else 'No'}")

        if len(text1) == len(text2):
            print("Character differences:")
            for i, (c1, c2) in enumerate(zip(text1, text2)):
                if c1 != c2:
                    print(f"  Position {i}: '{c1}' (U+{ord(c1):04X}) vs '{c2}' (U+{ord(c2):04X})")
        else:
            print("Texts have different lengths")
        print()


def main():
    generator = HomoglyphGenerator()

    print("Homoglyph Generator")
    print("=" * 50)

    while True:
        print("\nChoose an operation:")
        print("1. Generate text variants")
        print("2. Show Unicode info of text")
        print("3. Compare two texts")
        print("4. Display available homoglyph mappings")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == '1':
            text = input("Enter text to generate variants: ")
            max_variants = int(input("Enter max variants (default 5): ") or "5")

            variants = generator.generate_variants(text, max_variants)

            print(f"\nGenerated {len(variants)} variants:")
            for i, variant in enumerate(variants):
                print(f"{i + 1}. {variant}")
                if i > 0:  # Do not show Unicode info for original text
                    print(f"   Unicode: {' '.join(f'U+{ord(c):04X}' for c in variant)}")

        elif choice == '2':
            text = input("Enter text to analyze: ")
            generator.show_unicode_info(text)

        elif choice == '3':
            text1 = input("Enter first text: ")
            text2 = input("Enter second text: ")
            generator.compare_texts(text1, text2)

        elif choice == '4':
            print("\nAvailable homoglyph mappings:")
            for original, alternatives in generator.homoglyphs.items():
                print(f"'{original}' -> {alternatives[:3]}{'...' if len(alternatives) > 3 else ''}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
