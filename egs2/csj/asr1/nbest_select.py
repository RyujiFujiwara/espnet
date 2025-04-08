import os
from jiwer import wer

# It is only of FCER

# future_ref_lineにて文字化けのエラーあり。ひとまず、この時は1-bestを使って対処している

## (whisper_tokendevide_forfulltext.py) → nbest_select.py

## SETTING (example)
# Nbest = 5
# data_type = "text" (only)
# experiment_path = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/csj/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_ja_whisper_multilingual_sp/decode_asr_whisper_noctc_primtoken_asr_model_valid.acc.ave/eval1"
# for_fwer_fter = 1 # DEFAULT: 0 (calculate only future words or tokens. Indicate number of this.)
# limit = True # False: calculate FCER , Ture: limit only N words/tokens (Indicate number in "for_fwer_fter")
##

## SETTING
Nbest = 1
data_type = "text" # "text" (only)
experiment_path = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/csj/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_ja_whisper_multilingual_sp/decode_asr_whisper_noctc_primtoken2_asr_model_valid.acc.ave/eval1"
for_fwer_fter = 0 # DEFAULT: 0 (If calculate only future words or tokens, indicate number of this.)
limit = False # False: calculate FCER , Ture: limit only "for_fwer_fter" words/tokens
##

reference_file = os.path.join(experiment_path,"score_cer/ref.trn")
candidate_files = [os.path.join(experiment_path,f"logdir/output.1/{i}best_recog/{data_type}") for i in range(1,Nbest+1)]
input_text_file = os.path.join(experiment_path,f"logdir/output.1/1best_recog/input_text")
output_file = os.path.join(experiment_path,f"score_cer/hyp_{Nbest}best.trn")

if not os.path.isfile(reference_file):
    raise FileNotFoundError(f"Input file not found: {reference_file}")
for file in candidate_files:
    if not os.path.isfile(file):
        raise FileNotFoundError(f"Input file not found: {file}")

def process_files(reference_file, candidate_files, input_text_file, output_file):
    # 正解ファイルの読み込み
    with open(reference_file, 'r', encoding='utf-8') as ref:
        reference_lines = ref.readlines()

    # 各候補ファイルの読み込み
    candidate_lines_list = []
    for candidate_file in candidate_files:
        with open(candidate_file, 'r', encoding='utf-8') as cand:
            candidate_lines_list.append(cand.readlines())

    # 各サンプルにおける入力文字列を示したファイルの読み込み
    with open(input_text_file, 'r', encoding='utf-8') as input_text:
        input_lines = input_text.readlines()

    # 出力ファイルの準備
    with open(output_file, 'w', encoding='utf-8') as out:
        # 正解ファイルの各行に対して処理
        for i, (ref_line, input_line) in enumerate(zip(reference_lines, input_lines)):

            # 話者IDの格納および改行マークの除去
            ref_line = ref_line.strip()
            ID = ref_line.split()[-1]
            ref_line = ref_line.split()[:-1]
            input_line = input_line.strip()
            input_ID = input_line.split()[0]

            # 入力テキストが無い場合「input_line」は話者IDのみになってしまうため、配列外参照を起こす
            if len(list(input_line.split(" "))) == 1:
                input_length = 0
            else:
                input_length = len(list(input_line.split(" ", 1)[1]))

            future_ref_line = ref_line[input_length:]

            best_wer = float('inf')
            best_sentence = " "

            # 各候補ファイルの同じ行を比較
            for candidate_lines in candidate_lines_list:
                if i < len(candidate_lines):  # 範囲チェック 
                    candidate_line = candidate_lines[i].strip()
                    candidate_line = candidate_line.split(" ", 1)[1]
                    candidate_line = ["<space>" if s == " " else s for s in candidate_line]
                    future_candidate_line = list(candidate_line[input_length:])

                    if len(future_candidate_line) == 0:
                        current_wer = float(len(future_ref_line))
                    elif len(future_ref_line) == 0:
                        current_wer = 0
                    else:
                        current_wer = wer(' '.join(future_ref_line), ' '.join(future_candidate_line))

                    if current_wer < best_wer:
                        best_wer = current_wer
                        best_sentence = " ".join(candidate_line)

            # 最良の文を出力ファイルに書き込む
            out.write(best_sentence + " " + ID +'\n')

if __name__ == "__main__":
    process_files(reference_file, candidate_files, input_text_file, output_file)
