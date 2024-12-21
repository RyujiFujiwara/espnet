# For TWER
# 後に使うscliteはスペース区切りで動作する。
from espnet2.text.whisper_tokenizer import OpenAIWhisperTokenizer
import os

## SETTING
_scoredir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_5best_asr_model_valid.acc.ave/test_clean/score_wer"
##


input_ref = os.path.join(_scoredir,"ref.trn")
input_hyp = os.path.join(_scoredir,"hyp.trn")
output_ref = os.path.join(_scoredir,"ref_token.trn")
output_hyp = os.path.join(_scoredir,"hyp_token.trn")

tokenizer =  OpenAIWhisperTokenizer(
    model_type= 'whisper_multilingual',
    language= "en",
    task= "transcribe",
    added_tokens_txt=None,
    sot=False,
)

# ファイルを開いて処理
with open(input_ref, "r", encoding="utf-8") as ref_file, \
     open(input_hyp, "r", encoding="utf-8") as hyp_file, \
     open(output_ref, "w", encoding="utf-8") as ref_out, \
     open(output_hyp, "w", encoding="utf-8") as hyp_out:
    
    # 両方のファイルを同時に1行ずつ読み込む
    for ref_line, hyp_line in zip(ref_file, hyp_file):
        # ref.txtの処理
        ref_word_devide = ref_line.split()
        ref_word_ID = ref_word_devide[-1] # ex.) (908-31957-908-31957-0024)
        ref_line = " ".join(ref_word_devide[:-1]) # 話者IDを除き、再びスペース区切りで結合して戻す
        ref_token_devide = tokenizer.text2tokens(ref_line)
        ref_out.write(" ".join(ref_token_devide))
        ref_out.write(f' {ref_word_ID}') # 最後に話者IDを付与する
        ref_out.write("\n")

        # hyp.txtの処理
        hyp_word_devide = hyp_line.split()
        hyp_word_ID = hyp_word_devide[-1] # ex.) (908-31957-908-31957-0024)
        hyp_line = " ".join(hyp_word_devide[:-1]) # 話者IDを除き、再びスペース区切りで結合して戻す
        hyp_token_devide = tokenizer.text2tokens(hyp_line) 
        hyp_out.write(" ".join(hyp_token_devide))
        hyp_out.write(f' {hyp_word_ID}') # 最後に話者IDを付与する
        hyp_out.write("\n")

print(f"Processing complete. Results saved in '{output_ref}' and '{output_hyp}'.")