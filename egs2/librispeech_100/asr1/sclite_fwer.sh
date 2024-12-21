. ./path.sh
. ./cmd.sh

_scoredir="/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext_5best_asr_model_valid.acc.ave/test_clean/score_wer"

sclite \
    -r "${_scoredir}/ref_fter.trn" trn \
    -h "${_scoredir}/hyp_fter.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fter.trn"