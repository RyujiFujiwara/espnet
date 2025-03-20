#!/usr/bin/env python3
# encoding: utf-8

import codecs
import glob
import os

## SETTING
log_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_text_input_onebyone_asr_model_valid.acc.ave/test_clean/logdir/asr_inference.1.log"
output_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_text_input_onebyone_asr_model_valid.acc.ave/test_clean/score_wer"
##

output_file = os.path.join(output_dir,"count_cont_eos.trn")

def main():

    contcount = 0
    endcount = 0
    contcorrect = 0
    endcorrect = 0

    continue_marker = "continue : "
    end_marker = "end : "

    with codecs.open(log_file, "r", "utf-8") as f:
        for line in f:
            if continue_marker in line:
                line = line.strip()
                check = line.split(continue_marker)[1]
                contcount += 1
                if check == "Correct":
                    contcorrect += 1
            elif end_marker in line:
                line = line.strip()
                check = line.split(end_marker)[1]
                endcount += 1
                if check == "Correct":
                    endcorrect += 1

    # with codecs.open(output_file, "w", "utf-8") as o_f:


    print(f"contcount = {contcount}")
    print(f"contcorrect = {contcorrect}")
    print(f"endcount = {endcount}")
    print(f"endcorrect = {endcorrect}")


if __name__ == "__main__":
    main()