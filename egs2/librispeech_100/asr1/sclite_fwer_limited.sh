. ./path.sh
. ./cmd.sh

_scoredir="./exp/asr_train_asr_whisper_medium_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primtext1_asr_model_valid.acc.ave/test_clean/score_wer"

sclite \
    -r "${_scoredir}/ref_fwer.trn" trn \
    -h "${_scoredir}/hyp_fwer_limit.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fwer_limit.trn"