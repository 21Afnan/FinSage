import re
import spacy
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer 
transformer_model = SentenceTransformer('all-mpnet-base-v2')
kw_model = KeyBERT(model=transformer_model)
class text_Extractor:
    def __init__(self, text):
        self.text = text
        # Call the function to extract the amounts (numbers with optional decimal)
        self.amounts = self.extract_amounts()
        self.location_extractor=self.location_extractor()
        self.keyword_extractor=self.keyword_extractor()
    def extract_amounts(self):
        # -------------------------------
        # STEP 1: Remove commas in numbers
        # e.g., "5,000" becomes "5000"
        clean_text = self.text.replace(",", "")
        # -------------------------------
        # STEP 2: Use regex to find numbers (whole or decimal)
        # r'\d+(?:\.\d+)?' explained:
        # r        --> Tells Python that this is a raw string (so backslashes \ are not treated specially)
        # \d+      --> Match one or more digits (e.g., 123, 5000, 42)
        # (?:      --> Start a special group that we won't "save" separately (non-capturing group)
        #   \.     --> A dot (decimal point), e.g., .
        #   \d+    --> Followed by one or more digits (decimal places), e.g., .25
        # )?       --> This whole decimal part is optional (so it also matches whole numbers)
        # --------------------------------
        numbers = re.findall(r'\d+(?:\.\d+)?', clean_text)
        # Print extracted number strings for debugging
        print("Extracted Numbers:", numbers)
        # -------------------------------
        # STEP 3: Convert string numbers into float type for math use
        return [float(num) for num in numbers]
        # OPTIONAL NEXT STEP: We can map location to currency symbol
        # Example:
        # location = "Lahore"
        # location_to_currency = {
        #     "Lahore": "₨", "Delhi": "₹", "New York": "$"
        # }
        # symbol = location_to_currency.get(location, "₨")
        # print(f"{symbol}{amounts[0]}")
    def location_extractor(self):
        Nlp=spacy.load("en_core_web_sm")
        doc=Nlp(self.text)
        self.locations = []
        for ent in doc.ents:
            if ent.label_ == "GPE":
              self.locations.append(ent.text)
        print(" All Locations:", self.locations)
    def keyword_extractor(self):
        self.keywords = kw_model.extract_keywords(
            self.text,
            keyphrase_ngram_range=(1, 1),
            stop_words='english',
            use_mmr=True,
            diversity=0.7,
            top_n=10
        )    
        print(self.keywords)
        self.filtered_keywords = [
            (word, score) for word, score in self.keywords
            if not word.isdigit() and len(word) > 2 and "000" not in word
        ]
        print(self.filtered_keywords)



       



