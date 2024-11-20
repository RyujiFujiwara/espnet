import os

# パスの設定
_scoredir="./exp/asr_train_asr_whisper_medium_decselfatten_finetune_part_predict_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_asr_model_valid.acc.ave/test_clean/score_wer"
N_mask = 2 # マスクする単語数の設定(FWER算出対象)

input_ref = os.path.join(_scoredir,"ref.trn")
input_hyp = os.path.join(_scoredir,"hyp.trn")
output_ref = os.path.join(_scoredir,"ref_fwer.trn")
output_hyp = os.path.join(_scoredir,"hyp_fwer.trn")

N = N_mask + 1 # 話者IDを含める
mask_Length = 0 # マスクする単語列の長さの初期化

# ファイルを開いて処理
with open(input_ref, "r", encoding="utf-8") as ref_file, \
     open(input_hyp, "r", encoding="utf-8") as hyp_file, \
     open(output_ref, "w", encoding="utf-8") as ref_out, \
     open(output_hyp, "w", encoding="utf-8") as hyp_out:
    
    # 両方のファイルを同時に1行ずつ読み込む
    for ref_line, hyp_line in zip(ref_file, hyp_file):
        # ref.txtの処理
        ref_words = ref_line.strip().split()  # 単語に分割
        mask_Length = len(ref_words) - N
        if mask_Length > 0:
            ref_result = " ".join(ref_words[mask_Length:])  # 最初のmask_Length単語を除外
        else:
            ref_result = " ".join(ref_words) if ref_words else ""  # 最後の単語または空文字列
        ref_out.write(ref_result + "\n")

        # hyp.txtの処理
        hyp_words = hyp_line.strip().split()  # 単語に分割
        if mask_Length > 0:
            hyp_result = " ".join(hyp_words[mask_Length:])  # 最初のmask_Length単語を除外
        else:
            hyp_result = " ".join(hyp_words[:]) if hyp_words else ""  # 最後の単語または空文字列
        hyp_out.write(hyp_result + "\n")

print(f"Processing complete. Results saved in '{output_ref}' and '{output_hyp}'.")
