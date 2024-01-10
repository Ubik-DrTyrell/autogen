class RegexSanitizer:
    def __init__(self, config_path=None, encryption_key=None):
        self.config_path = config_path or os.getenv('REGEXSANITIZER_CONFIG', 'default_config.json')
        self.encryption_key = encryption_key or os.getenv('REGEXSANITIZER_KEY')
        self.regex_generator = RegexGenerator()
        self.literal_matcher = LiteralMatcher(self.encryption_key)
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as file:
                config = json.load(file)
            for key, value in config.get("literals", {}).items():
                self.literal_matcher.add_literal(key, value, encrypted=True)
            # Load regex patterns as needed
            # ...
        except Exception as e:
            logging.error(f"Error loading config: {e}")

    def add_regex_pattern(self, example):
        pattern = self.regex_generator.generate_pattern(example)
        # Add this pattern to your regex patterns list or file

    def add_literal(self, key, value):
        self.literal_matcher.add_literal(key, value)

    def sanitize(self, text):
        text = self.literal_matcher.sanitize(text)
        # Apply regex sanitization as well
        # ...
        
class PandorasLock:
    """
    A class to sanitize sensitive information in text using regular expressions
    and to reverse the sanitization in AI responses.
    """
    def __init__(self, config_path=None):
        # Set a default path and allow override by an environment variable or direct argument
        default_path = '/home/todd6585/git/r3d91lls_repo/python-tools/PandorasLock/pandorasconfig.json'
        self.config_path = config_path or os.getenv('PANDORACONFIG_PATH', default_path)
        self.patterns = self.load_regex_patterns()
        self.sanitization_map = {}  # To keep track of original and sanitized data

    def load_regex_patterns(self):
        """
        Load regular expression patterns from a JSON configuration file.
        """
        try:
            with open(self.config_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Config file {self.config_path} not found.")
            return {}

    def sanitize(self, text):
        """
        Sanitize sensitive information in the given text based on loaded regex patterns.
        """
        for pattern, replacement in self.patterns.items():
            matches = re.findall(pattern, text)
            for match in matches:
                match_str = ''.join(match) if isinstance(match, tuple) else match
                sanitized = replacement  # Consistent placeholder for the same match
                self.sanitization_map[sanitized] = match_str
                text = text.replace(match_str, sanitized)
        return text

    def reverse_sanitization(self, text):
        """
        Reverse the sanitization process using the sanitization map.
        """
        for sanitized, original in self.sanitization_map.items():
            text = text.replace(sanitized, original)
        return text
