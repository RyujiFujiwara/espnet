from espnet2.text.whisper_tokenizer import OpenAIWhisperTokenizer
import os
import random

textdir = "./LibriFullText/test_clean"
N = 1 # 推論対象のトークン数

input_text = os.path.join(textdir,"fulltext.txt")
output_text = os.path.join(textdir,"fulltext_tokenmask.txt")

tokenizer =  OpenAIWhisperTokenizer(
    model_type= 'whisper_multilingual',
    language= "en",
    task= "transcribe",
    added_tokens_txt=None,
    sot=False,
)

if not os.path.isfile(input_text):
    raise FileNotFoundError(f"Input file not found: {input_text}")

# ファイルを開いて処理
with open(input_text, "r", encoding="utf-8") as ref_file, \
     open(output_text, "w", encoding="utf-8") as ref_out:
    
    # ファイルを同時に1行ずつ読み込む
    for ref_line in ref_file:
        ref_word_devide = ref_line.split()
        ref_word_ID = ref_word_devide[0] # ex.) (908-31957-908-31957-0024)
        ref_line = " ".join(ref_word_devide[1:]).lower() # 話者IDを除き、テキスト列を小文字化したものを用意する
        ref_token_devide = tokenizer.text2tokens(ref_line) 
        ref_token_list = []
        token = len(ref_token_devide)
        if token > N:
            mask_Length = random.randint(1,token-N)
            ref_token_list = ref_token_devide[:(-1)*mask_Length]
            ref_token_list = tokenizer.tokens2text(ref_token_list).upper()
                # 最後からj個のトークンorスペースを外す
        else:
            ref_token_list = tokenizer.tokens2text(ref_token_devide).upper()
        ref_out.write(f'{ref_word_ID} ') # 最初に話者IDを付与する
        ref_out.write(ref_token_list)
        ref_out.write("\n")

print(f"Processing complete. Results saved in '{output_text}'.")