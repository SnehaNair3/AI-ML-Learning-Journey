
import contractions

txt="I can't believe it's already raining"

expanded_txt=contractions.fix(txt)
print(expanded_txt)


import re

def expand_contractions(text):
    contractions_pattern= {
      r"(?i)can't": "cannot",
      r"(?i)won't": "will not",
      r"(?i)it's": "it is",
      r"(?i)weren't": "were not",
      r"(?i)I'm": "I am",
      r"(?i)couldn't": "could not"
    }

    for contraction,expansion in contractions_pattern.items():
        text=re.sub(contraction,expansion,text)

    return text    


txt="I couldn't visit my aunt's place yesterday"
expanded_text=expand_contractions(txt)
print(expanded_text)


