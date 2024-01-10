import re
import sys

class RegexGenerator:

    def generate_pattern(self, example):
        pattern = self.analyze_example(example)
        return pattern

    def analyze_example(self, example):
        pattern = ''
        sequence_count = 0

        for char in example:
            if char.isalnum():  # Check if character is alphanumeric (letter or digit)
                sequence_count += 1
            else:
                if sequence_count > 0:
                    pattern += f'\\w{{{sequence_count}}}'  # Add regex for alphanumeric sequence
                    sequence_count = 0
                pattern += re.escape(char)  # Escape and add non-alphanumeric characters

        if sequence_count > 0:  # Add any remaining sequence at the end
            pattern += f'\\w{{{sequence_count}}}'

        return pattern

def main():
    if len(sys.argv) != 2:
        print("Usage: python test.py '<example>'")
        sys.exit(1)

    example = sys.argv[1]
    generator = RegexGenerator()
    regex_pattern = generator.generate_pattern(example)
    print(f"Generated Regex: {regex_pattern}")

if __name__ == "__main__":
    main()
