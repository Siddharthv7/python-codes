class SimpleSearchEngine:
    def __init__(self):
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def search(self, query):
        results = []
        for i, document in enumerate(self.documents):
            if query.lower() in document.lower():
                results.append(i)
        return results

# Example usage
search_engine = SimpleSearchEngine()

search_engine.add_document("Python is a versatile programming language.")
search_engine.add_document("Searching with Python can be powerful.")
search_engine.add_document("https://www.google.com/search?q=")

query = "python"
search_results = search_engine.search(query)

print(f"Search results for '{query}':")
for result in search_results:
    print(f"Document {result + 1}: {search_engine.documents[result]}")
