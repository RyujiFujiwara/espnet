import os
from jiwer import wer

## (whisper_tokendevide_forfulltext.py) → nbest_select.py

## SETTING (example)
# Nbest = 5
# data_type = "token" # "text" or "token"
# reference_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/LibriFullText/test_clean/fulltext_tokenmask1_devided.trn"
# candidate_path = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/logdir/output.1"
# output_path = '/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer'

# for_fwer_fter = 1 # DEFAULT: 0 (calculate only future words or tokens. Indicate number of this.)
# limit = True # False: calculate FWER/FTER , Ture: limit only "for_fwer_fter" words/tokens
##

## SETTING
Nbest = 5
data_type = "token" # "text" or "token"
experiment_path = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean"
for_fwer_fter = 1 # DEFAULT: 0 (calculate only future words or tokens. Indicate number of this.)
limit = True # False: calculate FWER/FTER , Ture: limit only "for_fwer_fter" words/tokens
##

reference_file = os.path.join(experiment_path,"score_wer/ref_token.trn")
candidate_files = [os.path.join(experiment_path,f"logdir/output.1/{i}best_recog/{data_type}") for i in range(1,Nbest+1)]
output_file = os.path.join(experiment_path,"score_wer/hyp_nbest.trn")

if not os.path.isfile(reference_file):
    raise FileNotFoundError(f"Input file not found: {reference_file}")
for file in candidate_files:
    if not os.path.isfile(file):
        raise FileNotFoundError(f"Input file not found: {file}")

def process_files(reference_file, candidate_files, output_file):
    # 正解ファイルの読み込み
    with open(reference_file, 'r', encoding='utf-8') as ref:
        reference_lines = ref.readlines()

    # 各候補ファイルの読み込み
    candidate_lines_list = []
    for candidate_file in candidate_files:
        with open(candidate_file, 'r', encoding='utf-8') as cand:
            candidate_lines_list.append(cand.readlines())

    # 出力ファイルの準備
    with open(output_file, 'w', encoding='utf-8') as out:
        # 正解ファイルの各行に対して処理
        for i, ref_line in enumerate(reference_lines):
            ref_line = ref_line.strip()
            ID = ref_line.split()[-1]
            ref_line = " ".join(ref_line.split()[:-1]) # 話者IDを除く
            best_wer = float('inf')
            best_sentence = None

            # 各候補ファイルの同じ行を比較
            for candidate_lines in candidate_lines_list:
                if i < len(candidate_lines):  # 範囲チェック 
                    candidate_line = candidate_lines[i].strip()
                    candidate_line = " ".join(candidate_line.split()[1:])

                    if for_fwer_fter:
                        ref_line_f = " ".join(ref_line.split()[-1*(for_fwer_fter):])
                        ref_length = len(ref_line.split()[:-1*(for_fwer_fter)])
                        candidate_line_f = " ".join(candidate_line.split()[ref_length:])
                        if limit == True:
                            if for_fwer_fter < len(candidate_line_f):
                                candidate_line_f = " ".join(candidate_line_f.split()[:for_fwer_fter])
                        current_wer = wer(ref_line_f, candidate_line_f)
                    else:
                        current_wer = wer(ref_line, candidate_line)

                    if current_wer < best_wer:
                        best_wer = current_wer
                        best_sentence = candidate_line

            # 最良の文を出力ファイルに書き込む
            if best_sentence is not None:
                out.write(best_sentence + " " + ID +'\n')

process_files(reference_file, candidate_files, output_file)
