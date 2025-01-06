#!/usr/bin/env python3
# encoding: utf-8

import codecs
import glob
import os

## SETTING
log_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_tmp_asr_model_valid.acc.ave/test_clean/logdir/asr_inference.1.log"
output_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_tmp_asr_model_valid.acc.ave/test_clean/logdir"
# output_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_asr_model_valid.acc.ave/test_clean/score_wer"
##

output_file = os.path.join(output_dir,"prob.trn")

def main():

    prob_sum = 0.0
    count = 0

    prob_marker = "and probability :"

    with codecs.open(log_file, "r", "utf-8") as f:
        with codecs.open(output_file, "w", "utf-8") as o_f:
            for line in f:
                x = line.strip() # remove the blank
                if prob_marker in x: #ex.) If it contains "and probability :"
                    prob = float(x.split(prob_marker + " ")[1])
                    prob_sum += prob
                    count += 1
                    o_f.write(str(prob) + "\n")

    print(f"average_prob = {prob_sum / count}")
    print(count)


if __name__ == "__main__":
    main()