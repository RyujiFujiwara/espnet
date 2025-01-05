# from espnet2.text.whisper_tokenizer import OpenAIWhisperTokenizer
# from espnet2.text.whisper_token_id_converter import OpenAIWhisperTokenIDConverter

# tokenizer =  OpenAIWhisperTokenizer(
#                 model_type= 'whisper_multilingual',
#                 language= "en",
#                 task= "transcribe",
#                 added_tokens_txt= None,
#                 sot= False,
#             )

# converter = OpenAIWhisperTokenIDConverter(
#                 model_type= 'whisper_multilingual',
#                 added_tokens_txt= None,
#                 language= "en",
#                 task= "transcribe",
#                 sot= False,
#             )

# token_list = tokenizer.text2tokens("he hoped there would be stew for dinner turnips and carrots and bruised potatoes and fat mutton pieces to be ladled out in thick peppered flour fattened sauce")
# token_ID_list = converter.tokens2ids(token_list)

# token_text = converter.ids2tokens([675, 19737, 220, 15456, 576, 312, 22654, 337, 6148, 220, 33886, 2600, 293, 21005, 293, 25267, 2640, 11811, 293, 4046, 5839, 1756, 3755, 220, 1353, 312, 6632, 1493, 484, 294, 220, 392, 618, 8532])

# print(token_text)
# print(token_ID_list)

import re

CHAR = "YO'"
CHAR2 = "DON'T"

print(re.split(r"[ '\n]", CHAR))
print(re.split(r"[ '\n]", CHAR2))