import os
import re

## SETTING
_scoredir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.0_5best/test_clean/score_wer"
N_mask = 1 # マスクする単語数の設定(FWER算出対象)
fulltext = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/LibriFullText/test_clean/fulltext_token.trn" # フルのトークン化されたテキストを準備する必要がある
##


input_ref = os.path.join(_scoredir,"ref_token.trn")
input_hyp = os.path.join(_scoredir,"hyp_token.trn")
output_ref = os.path.join(_scoredir,"ref_eoscont.txt")
output_hyp = os.path.join(_scoredir,"hyp_eoscont.txt")

N = N_mask + 1 # 話者IDを含める
mask_Length = 0 # マスクする単語列の長さの初期化

# ファイルを開いて処理
with open(fulltext, "r", encoding="utf-8") as full_file, \
     open(input_ref, "r", encoding="utf-8") as ref_file, \
     open(input_hyp, "r", encoding="utf-8") as hyp_file, \
     open(output_ref, "w", encoding="utf-8") as ref_out, \
     open(output_hyp, "w", encoding="utf-8") as hyp_out:
    
    # 3つのファイルを同時に1行ずつ読み込む
    for text_line, ref_line, hyp_line in zip(full_file, ref_file, hyp_file):
        # 単語に分割
        full_words = re.split(r"[ ']", text_line)
        ref_words = ref_line.strip().split()
        hyp_words = hyp_line.strip().split()

        if len(full_words) == len(ref_words):
            ref_out.write("<eos>" + "\n")
        else:
            ref_out.write("<cont>" + "\n")

        if len(ref_words) >= len(hyp_words):
            hyp_out.write("<eos>" + "\n")
        else:
            hyp_out.write("<cont>" + "\n")

print(f"Processing complete. Results saved in '{output_ref}' and '{output_hyp}'.")
