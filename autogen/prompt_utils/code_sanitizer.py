class CodeSanitizer:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer
        self.original_order_map = {}

    def process_code_block(self, code_block):
        """
        Public function to process a code block with sanitization and deconstruction.
        """
        # Separate lines and shuffle them randomly
        lines = code_block.split("\n")
        random.shuffle(lines)

        # Apply RegexSanitizer and record original order
        for i in range(len(lines)):
            sanitized_line = self.sanitizer.sanitize(lines[i])
            self.original_order_map[sanitized_line] = lines[i]
            lines[i] = sanitized_line

        # Join the shuffled and sanitized lines and return
        return "\n".join(lines)

    def revert_code_order(self, sanitized_block):
        """
        Reverts the order of code lines to the original, using the original_order_map.
        """
        lines = sanitized_block.split("\n")
        reverted_lines = [self.original_order_map.get(line, line) for line in lines]
        return "\n".join(reverted_lines)

    # Additional methods for handling different input types (files, lists, etc.)
    # ...
class PandorasBox:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer
        self.original_order_map = {}

    def process_code_block(self, code_block):
        """
        Public function to process a code block with sanitization and deconstruction.
        """
        # Separate lines and shuffle them randomly
        lines = code_block.split("\n")
        random.shuffle(lines)

        # Apply PandorasLock and record original order
        for i in range(len(lines)):
            sanitized_line = self.sanitizer.sanitize(lines[i])
            self.original_order_map[sanitized_line] = lines[i]
            lines[i] = sanitized_line

        # Join the shuffled and sanitized lines and return
        return "\n".join(lines)

    def revert_code_order(self, sanitized_block):
        """
        Reverts the order of code lines to the original, using the original_order_map.
        """
        lines = sanitized_block.split("\n")
        reverted_lines = [self.original_order_map.get(line, line) for line in lines]
        return "\n".join(reverted_lines)