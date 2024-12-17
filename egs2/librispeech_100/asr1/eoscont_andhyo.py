#!/usr/bin/env python3
# encoding: utf-8

import codecs
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

## SETTING
hyp_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer/hypo.trn"
eoscont_reffile = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer/ref_eoscont.txt"
output_scoredir = "./exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer"
##

output_file = os.path.join(output_scoredir,"result_hypo.trn")

def main():

    cont_sum = 0
    eos_sum = 0
    cont_count = 0
    eos_count = 0
    cont_list = []
    eos_list = []

    with codecs.open(hyp_file, "r", "utf-8") as hyp_f, \
         codecs.open(eoscont_reffile, "r", "utf-8") as ref_f:
        for hyp_line,ref_line in zip(hyp_f,ref_f):
            hyp_line = hyp_line.strip()
            hyp_line = int(hyp_line.split()[1])
            ref_line = ref_line.strip()
            if ref_line == "<cont>":
                cont_sum += hyp_line
                cont_list += [hyp_line]
                cont_count += 1
            elif ref_line == "<eos>":
                eos_sum += hyp_line
                eos_list += [hyp_line]
                eos_count += 1
    
    with codecs.open(output_file,"w","utf-8") as out_f:
        out_f.write(f"cont_hypo_average = {cont_sum / cont_count}\n")
        out_f.write(f"eos_hypo_average = {eos_sum / eos_count}")

    x1 = cont_list
    x2 = eos_list

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # ax.hist(x1, bins=20, color='red', alpha=0.5)
    ax.hist(x2, bins=20, color='blue',alpha=0.5)
    ax.set_title('Number of hypothesis in 1 token (<eos>)')
    ax.set_xlabel('number of hypo')
    ax.set_ylabel('freq')
    plt.xticks(np.arange(0, 21, step=1))
    fig.savefig("result.png")


    print(f"cont_count = {cont_count}")
    print(f"eos_count = {eos_count}")


if __name__ == "__main__":
    main()