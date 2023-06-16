import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("Delphi supports rapid application development (RAD). Prominent features are a visual designer and two application frameworks, VCL for Windows and FireMonkey (FMX) for cross-platform development. Delphi uses the Pascal-based programming language Object Pascal created by Anders Hejlsberg for Borland (now IDERA) as the successor to Turbo Pascal. It supports native cross-compilation to many platforms including Windows, Linux, iOS and Android. To better support development for Microsoft Windows and interoperate with code developed with other software development tools, Delphi supports independent interfaces of Component Object Model (COM) with reference counted class implementations, and support for many third-party components. Interface implementations can be delegated to fields or properties of classes. Message handlers are implemented by tagging a method of a class with the integer constant of the message to handle. Database connectivity is extensively supported through VCL database-aware and database access components. Later versions have included upgraded and enhanced runtime library routines, some provided by the community group FastCode.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)