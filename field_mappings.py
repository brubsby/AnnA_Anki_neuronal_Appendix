# This variable contains as key a notetype model name and as value the
# name of the fields to keep, in order
# * for example : "occlusion": ["Header", "Image"] will match all templates that
#     contain "occlusion" in their name
# * note that matching for note type or field name is case insensitive
# * if you use tfidf as vectorizer, you can add a field multiple times to
#   give it more importance relative to other fields.

field_dic = {
             "clozolkor": ["Header", "Header", "Body", "Body", "Body", "Hint", "More"],
             # shameless plug: clozolkor is my own template,
             # more info: https://github.com/thiswillbeyourgithub/Clozolkor
             "occlusion": ["Header", "Header", "Header", "Header", "Header",
                           "Header", "Header", "Header", "Header", "Header",
                           "Image"],
             "basic": ["Front", "Back", "Hint"],
             "spanish cards": ["Spanish", "English"],
             "morse": ["Front", "mnemonic"],
             "fallacy_bias": ["Name & Picture", "Summary", "Description"],
             "basic (and reverse cards) (wo": ["Font", "Back"],
             }

