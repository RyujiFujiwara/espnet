# 途中及び終端をランダムにマスクさせたときに、以後のN単語の予測を行わせるための正解データを生成する
# N単語マスクを行うので、かならずN単語は残すようにする。

import os
import random

# パスの設定
_textdir="./LibriFullText/test_clean"
N = 1 # 限定する単語数の設定

input_hyp = os.path.join(_textdir,"fulltext.txt")
output_hyp = os.path.join(_textdir,"text_masked.txt")

mask_Length = 0 # マスクする単語列の長さの初期化

# ファイルを開いて処理
with open(input_hyp, "r", encoding="utf-8") as hyp_file, \
     open(output_hyp, "w", encoding="utf-8") as hyp_out:
    
    # ファイルを1行ずつ読み込む
    for hyp_line in hyp_file:
        hyp_words = hyp_line.strip().split()  # 単語に分割
        if len(hyp_words) > N+1: # 話者ID含む
            mask_Length = random.randint(0,len(hyp_words)-(N+1))
            if mask_Length != 0:
                hyp_result = " ".join(hyp_words[:(-1)*mask_Length])  # 最初からmask_Length単語を外す
            else:
                hyp_result = " ".join(hyp_words)
        else:
            hyp_result = " ".join(hyp_words)
        hyp_out.write(hyp_result + "\n")

print(f"Processing complete. Results saved in '{output_hyp}'.")
