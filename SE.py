class SimpleSearchEngine:
    def __init__(self):
        self.documents = {}

    def index_document(self, doc_id, content):
        self.documents[doc_id] = content.lower()

    def search(self, query):
        results = []
        query = query.lower()

        for doc_id, content in self.documents.items():
            if query in content:
                results.append(doc_id)

        return results

# Example usage
search_engine = SimpleSearchEngine()

# Indexing documents
search_engine.index_document(1, "Python is a programming language.")
search_engine.index_document(2, "Web scraping with Python is fun.")
search_engine.index_document(3, "Python developers build amazing applications.")

# Searching
query = "Python programming"
results = search_engine.search(query)

if results:
    print(f"Search results for '{query}': {results}")
else:
    print(f"No results found for '{query}'.")
