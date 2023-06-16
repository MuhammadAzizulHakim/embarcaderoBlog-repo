# Extract keywords
from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

## Keyword_processor.add_keyword(<unclean name>, <standardised name>)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
print(keywords_found)

# Replace keywords
keyword_processor.add_keyword('New Delhi', 'NCR region')
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
print(new_sentence)

# Case Sensitive example
from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor(case_sensitive=True)
keyword_processor.add_keyword('Big Apple', 'New York')
keyword_processor.add_keyword('Bay Area')
keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
print(keywords_found)