# Module 4 Lesson 2: After-Class Project
# Project Name: NLP Token Parsing Engine String Frequency Dictionary

class TokenFrequencyCompiler:
    def build_frequency_map(self, raw_document_corpus_text):
        sanitized_words = raw_document_corpus_text.lower().replace(",", "").replace(".", "").split()
        dictionary_frequency_counter = {}
        
        for token in sanitized_words:
            dictionary_frequency_counter[token] = dictionary_frequency_counter.get(token, 0) + 1
            
        return dictionary_frequency_counter

if __name__ == "__main__":
    compiler = TokenFrequencyCompiler()
    corpus = "Python is beautiful, python is clean, algorithms are efficient."
    print(f"Compiled Token Counter Dictionary Mappings: {compiler.build_frequency_map(corpus)}")