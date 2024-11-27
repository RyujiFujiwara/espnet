# 出力単語列においてWERの適用範囲を最初のN単語のみに限定させる
# 「sclite_fwer_prepare.py」の実行後に行う

import os

# パスの設定
_scoredir="./exp/asr_train_asr_whisper_medium_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_asr_model_valid.acc.ave/test_clean/score_wer"
N = 2 # 限定する単語数の設定(FWER算出対象)

input_hyp = os.path.join(_scoredir,"hyp_fwer.trn")
output_hyp = os.path.join(_scoredir,"hyp_fwer_limit.trn")

mask_Length = 0 # マスクする単語列の長さの初期化

# ファイルを開いて処理
with open(input_hyp, "r", encoding="utf-8") as hyp_file, \
     open(output_hyp, "w", encoding="utf-8") as hyp_out:
    
    # ファイルを1行ずつ読み込む
    for hyp_line in hyp_file:
        hyp_words = hyp_line.strip().split()  # 単語に分割
        if len(hyp_words) > N+1: # 話者ID含む
            hyp_result = " ".join(hyp_words[:N])  # 最初のN単語と最後の単語を残す
            hyp_result = hyp_result + " " + hyp_words[-1]
        else:
            hyp_result = " ".join(hyp_words[:]) if hyp_words else ""
        hyp_out.write(hyp_result + "\n")

print(f"Processing complete. Results saved in '{output_hyp}'.")
