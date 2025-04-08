# scliteの準備
. ./path.sh
. ./cmd.sh

# スコアディレクトリを指定（～/score_cer）
_scoredir="/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/csj/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_ja_whisper_multilingual_sp/decode_asr_whisper_noctc_primtoken_asr_model_valid.acc.ave/eval1/score_cer"

# scliteの実行
sclite \
    -r "${_scoredir}/ref_fcer_5best.trn" trn \
    -h "${_scoredir}/hyp_fcer_5best.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fcer_5best.trn"