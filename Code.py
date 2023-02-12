import requests

# Make the GET request to the URL
Link = "https://groups.csail.mit.edu/sls/downloads/restaurant/restauranttrain.bio"
response = requests.get(Link)

# Check if the request was successful
if response.status_code == 200:
    # Extract the text content from the response
    Text = response.text
    print(Text)
else:
    # Raise an error if the request was unsuccessful
    response.raise_for_status()


import spacy

# Load the English NER model
NLP = spacy.load("en_core_web_sm")

def extract_entities(text):
    # Process the text using the NER model
    doc = NLP(Text)

    # Extract the entities and their labels
    Entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Return the entities as a dictionary
    return dict(Entities)

Entities = extract_entities(Text)
print(Entities)

