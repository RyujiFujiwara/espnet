# scliteの準備
. ./path.sh
. ./cmd.sh

# スコアディレクトリを指定（～/score_wer）
_scoredir="/mnt/kiso-qnap/fujiwara/B4/main/espnet/egs2/librispeech_100/asr1/exp/asr_train_asr_whisper_large_decselfatten_finetune_raw_en_whisper_multilingual_sp/decode_asr_whisper_noctc_primword_asr_model_valid.acc.ave/test_clean/score_wer"
number_of_maskwords=1

# fwer算出対象のファイルの作成
python3 sclite_fwer_prepare.py \
    --score_dir "${_scoredir}" \
    --N_mask "${number_of_maskwords}"

# scliteの実行
sclite \
    -r "${_scoredir}/ref_fwer.trn" trn \
    -h "${_scoredir}/hyp_fwer.trn" trn \
    -i rm -o all stdout > "${_scoredir}/result_fwer.trn"