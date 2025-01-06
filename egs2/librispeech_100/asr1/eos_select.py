import codecs
import os

## SETTING
ref_hyp_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_nofinetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primword_tmp_asr_model_valid.acc.ave/dev_clean/score_wer"
ref_file = os.path.join(ref_hyp_dir,"ref.trn")
hyp_file = os.path.join(ref_hyp_dir,"hyp.trn")
eos_cont_file = os.path.join(ref_hyp_dir,"hyp_eoscont.txt")
output_reffile = os.path.join(ref_hyp_dir,"end_ref.trn")
output_hypfile = os.path.join(ref_hyp_dir,"end_hyp.trn")


if not(os.path.isfile(eos_cont_file) and os.path.isfile(ref_file) and os.path.isfile(hyp_file)):
    raise FileNotFoundError(f"Input file not found.")

with codecs.open(eos_cont_file,"r","utf-8") as eoscont, \
     codecs.open(ref_file,"r","utf-8") as ref, \
     codecs.open(hyp_file,"r","utf-8") as hyp, \
     codecs.open(output_reffile,"w","utf-8") as o_ref, \
     codecs.open(output_hypfile,"w","utf-8") as o_hyp:
     for e_or_c, r, h in zip(eoscont, ref, hyp):
        e_or_c = e_or_c.strip("\n")
        if e_or_c == "<eos>":
            o_ref.write(r)
            o_hyp.write(h)