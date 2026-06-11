# Module 5 Lesson 5: After-Class Project
# Project Name: App Configuration KV Configuration INI File Parser Engine

class ConfigParserEngine:
    def parse_ini_string_blocks(self, raw_ini_text_corpus):
        configuration_map = {}
        active_section = "GLOBAL"
        
        for line in raw_ini_text_corpus.split("\n"):
            line = line.strip()
            if not line or line.startswith("#") or line.startswith(";"): continue
            
            if line.startswith("[") and line.endswith("]"):
                active_section = line[1:-1].strip()
                if active_section not in configuration_map:
                    configuration_map[active_section] = {}
            elif "=" in line:
                key, val = line.split("=", 1)
                configuration_map[active_section][key.strip()] = val.strip()
                
        return configuration_map

if __name__ == "__main__":
    sample_ini = """
    [DATABASE]
    host = 127.0.0.1
    port = 5432
    # Security Configuration Profile
    [SECURITY]
    encryption_enabled = true
    """
    engine = ConfigParserEngine()
    print(f"Parsed Config Map Tree Hierarchy: {engine.parse_ini_string_blocks(sample_ini)}")