# For TWER
from espnet2.text.whisper_tokenizer import OpenAIWhisperTokenizer
import os

_scoredir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/LibriFullText/test_clean"

input_ref = os.path.join(_scoredir,"fulltext.txt")
output_ref = os.path.join(_scoredir,"fulltext_token.trn")

tokenizer =  OpenAIWhisperTokenizer(
    model_type= 'whisper_multilingual',
    language= "en",
    task= "transcribe",
    added_tokens_txt=None,
    sot=False,
)

# ファイルを開いて処理
with open(input_ref, "r", encoding="utf-8") as ref_file, \
     open(output_ref, "w", encoding="utf-8") as ref_out:
    # 両方のファイルを同時に1行ずつ読み込む
    for ref_line in ref_file:
        # ref.txtの処理
        ref_word_devide = ref_line.split()
        ref_word_ID = ref_word_devide[0] # ex.) (908-31957-908-31957-0024)
        ref_line = " ".join(ref_word_devide[1:]).lower() # 話者IDを除き、再びスペース区切りで結合して戻す
        ref_token_devide = tokenizer.text2tokens(ref_line) 
        ref_out.write(" ".join(ref_token_devide))
        ref_out.write(f' ({ref_word_ID})') # 最後に話者IDを付与する
        ref_out.write("\n")

print(f"Processing complete. Results saved in '{output_ref}'.")