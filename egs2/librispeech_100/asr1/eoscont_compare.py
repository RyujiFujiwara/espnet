import os

_scoredir = "./exp/asr_train_asr_whisper_medium_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_asr_model_valid.acc.ave/test_clean/score_wer"

input_ref = os.path.join(_scoredir,"ref_eoscont.txt")
input_hyp = os.path.join(_scoredir,"hyp_eoscont.txt")

ref_cont_hyp_cont = 0
ref_cont_hyp_eos = 0
ref_eos_hyp_cont = 0
ref_eos_hyp_eos = 0

# ファイルを開いて処理
with open(input_ref, "r", encoding="utf-8") as ref_file, \
     open(input_hyp, "r", encoding="utf-8") as hyp_file:
    
    # 3つのファイルを同時に1行ずつ読み込む
    for ref, hyp in zip(ref_file, hyp_file):
        ref = ref.replace("\n", "")
        hyp = hyp.replace("\n", "")
        if ref == "<cont>" and hyp == "<cont>":
            ref_cont_hyp_cont += 1
        elif ref == "<cont>" and hyp == "<eos>":
            ref_cont_hyp_eos += 1
        elif ref == "<eos>" and hyp == "<cont>":
            ref_eos_hyp_cont += 1
        elif ref == "<eos>" and hyp == "<eos>":
            ref_eos_hyp_eos += 1

print(f"ref = cont , hyp = cont : {ref_cont_hyp_cont}")
print(f"ref = cont , hyp = eos : {ref_cont_hyp_eos}")
print(f"ref = eos , hyp = cont : {ref_eos_hyp_cont}")
print(f"ref = eos , hyp = eos : {ref_eos_hyp_eos}")

# ref = cont , hyp = cont : 1019
# ref = cont , hyp = eos : 1361
# ref = eos , hyp = cont : 90
# ref = eos , hyp = eos : 150