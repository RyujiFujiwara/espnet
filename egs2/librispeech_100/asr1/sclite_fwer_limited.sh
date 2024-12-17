. ./path.sh
. ./cmd.sh

_scoredir="/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/primtoken1mask_randommask_penalty0.6_5best/test_clean/score_wer"

sclite \
    -r "${_scoredir}/ref_fter.trn" trn \
    -h "${_scoredir}/hyp_fter_limit.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fter_limit.trn"