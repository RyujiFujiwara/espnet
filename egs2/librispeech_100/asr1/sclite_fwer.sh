. ./path.sh
. ./cmd.sh

_scoredir="/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_nofinetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primword_tmp_asr_model_valid.acc.ave/dev_other/score_wer"

sclite \
    -r "${_scoredir}/ref_fwer.trn" trn \
    -h "${_scoredir}/hyp_fwer.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fwer.trn"