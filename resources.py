import wikipedia

def fetch_wikipedia(query, sentences=2):
    try:
        return wikipedia.summary(query, sentences=sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e}"
    except wikipedia.exceptions.PageError:
        return "Wikipedia page not found."
    except Exception as e:
        return f"Error: {e}"

def fetch_ncert(topic):
    ncert_data = {
        "Newton's laws": "Newton's laws describe motion: 1) inertia, 2) F=ma, 3) action-reaction.",
        "Periodic table": "Elements are arranged by atomic number in the periodic table."
    }
    return ncert_data.get(topic, "")