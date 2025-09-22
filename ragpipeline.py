from resources import fetch_wikipedia, fetch_ncert
from vectorstore import search, add_document

def build_context(query):
    context_parts = []
    docs = search(query)
    if docs:
        context_parts.append("VectorStore: " + " ".join(docs))
    ncert_info = fetch_ncert(query)
    if ncert_info:
        context_parts.append("NCERT: " + ncert_info)
    wiki_info = fetch_wikipedia(query)
    if wiki_info:
        context_parts.append("Wikipedia: " + wiki_info)

    return "\n".join(context_parts)