#!/usr/bin/env python3
# encoding: utf-8

import codecs
import glob
import os

## SETTING
log_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/logdir/asr_inference.1.log"
output_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer"
##

output_file = os.path.join(output_dir,"hypo.trn")

def main():

    endhyp = 0
    total_endhyp = 0

    endhyp_marker = "total number of ended hypotheses:"
    total_endhyp_marker = "total number of ended hypotheses less than"

    with codecs.open(log_file, "r", "utf-8") as f:
        with codecs.open(output_file, "w", "utf-8") as o_f:
            for line in f:
                x = line.strip() # remove the blank
                if endhyp_marker in x: #ex.) If it contains "total number of ended hypotheses:"
                    o_f.write(x.split(endhyp_marker + " ")[1]+" ")
                    total_endhyp += int(x.split(endhyp_marker + " ")[1])
                elif total_endhyp_marker in x: #ex.) If it contains is "total number of ended hypotheses less than"
                    o_f.write(x.split("token:")[1]+"\n")
                    endhyp += int(x.split("token:")[1])

    print(f"endhyp = {endhyp}")
    print(f"total_endhyp = {total_endhyp}")


if __name__ == "__main__":
    main()