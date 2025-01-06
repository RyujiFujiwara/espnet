import codecs
import os

Nbest = 1
prob_file = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_asr_model_valid.acc.ave/test_clean/logdir/prob_end.trn"
ref_hyp_dir = "/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_5best_asr_model_valid.acc.ave/test_clean/score_wer"
border = 1e-10

ref_file = os.path.join(ref_hyp_dir,"ref_token.trn")
hyp_file = os.path.join(ref_hyp_dir,"hyp_1best.trn")
output_reffile = os.path.join(ref_hyp_dir,"refprob_token.trn")
output_hypfile = os.path.join(ref_hyp_dir,f"{Nbest}best_hypprob_token.trn")

if not(os.path.isfile(prob_file) and os.path.isfile(ref_file) and os.path.isfile(hyp_file)):
    raise FileNotFoundError(f"Input file not found.")

with codecs.open(prob_file,"r","utf-8") as prob, \
     codecs.open(ref_file,"r","utf-8") as ref, \
     codecs.open(hyp_file,"r","utf-8") as hyp, \
     codecs.open(output_reffile,"w","utf-8") as o_ref, \
     codecs.open(output_hypfile,"w","utf-8") as o_hyp:
     for p, r, h in zip(prob, ref, hyp):
        if float(p) > border:
            o_ref.write(r)
            o_hyp.write(h)