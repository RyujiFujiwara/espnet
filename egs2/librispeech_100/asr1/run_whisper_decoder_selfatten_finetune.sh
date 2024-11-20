#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

train_set="train_clean_100"
valid_set="dev"
test_sets="test_clean"

asr_config=conf/tuning/train_asr_whisper_medium_decselfatten_finetune.yaml
inference_config=conf/tuning/decode_asr_whisper_noctc_primtext.yaml

lm_config=conf/train_lm_transformer.yaml
use_lm=false
use_wordlm=false

# speed perturbation related
# (train_set will be "${train_set}_sp" if speed_perturb_factors is specified)
speed_perturb_factors="0.9 1.0 1.1"

./asr.sh \
    --nj 8 \
    --gpu_inference true \
    --inference_nj 2 \
    --lang en \
    --token_type whisper_multilingual \
    --feats_normalize "" \
    --audio_format "flac.ark" \
    --feats_type raw \
    --use_lm ${use_lm}                                 \
    --use_word_lm ${use_wordlm}                        \
    --lm_config "${lm_config}"                         \
    --cleaner whisper_basic                            \
    --asr_config "${asr_config}"                       \
    --inference_config "${inference_config}"           \
    --train_set "${train_set}"                         \
    --valid_set "${valid_set}"                         \
    --test_sets "${test_sets}"                         \
    --speed_perturb_factors "${speed_perturb_factors}" \
    --asr_speech_fold_length 512 \
    --asr_text_fold_length 150 \
    --lm_fold_length 150 \
    --lm_train_text "data/${train_set}/text" "$@"

# ./asr.sh \
#     --nj 8 \                                                  The number of parallel jobs. 〇
#     --gpu_inference true \                                    Whether to perform gpu decoding.
#     --inference_nj 2 \                                        The number of parallel jobs in decoding.
#     --lang en \                                               Language　〇
#     --token_type whisper_multilingual \                       Tokenization type (char or bpe).
#     --feats_normalize "" \                                    Normalizaton layer type.
#     --audio_format "flac.ark" \                               Audio format: wav, flac, wav.ark, flac.ark　〇
#     --feats_type raw \                                        Feature type (raw, raw_copy, fbank_pitch or extracted)　〇
#     --use_lm ${use_lm}                                 \      Use language model for ASR decoding.
#     --use_word_lm ${use_wordlm}                        \      Whether to use word language model.
#     --lm_config "${lm_config}"                         \      Config for language model training
#     --cleaner whisper_basic                            \      Text cleaner.
#     --asr_config "${asr_config}"                       \      Config for asr model training.〇
#     --inference_config "${inference_config}"           \      Config for decoding.〇
#     --train_set "${train_set}"                         \      Name of training set
#     --valid_set "${valid_set}"                         \      Name of validation set used for monitoring/tuning network training.
#     --test_sets "${test_sets}"                         \      Names of test sets. Multiple items
#     --speed_perturb_factors "${speed_perturb_factors}" \      perturbation factors, e.g. "0.9 1.0 1.1" (separated by space).
#     --asr_speech_fold_length 512 \                            fold_length for speech data during ASR training. トレーニングデータを一定の長さに区切る時の長さ
#     --asr_text_fold_length 150 \                              fold_length for text data during ASR training.
#     --lm_fold_length 150 \                                    fold_length for LM training.
#     --lm_train_text "data/${train_set}/text" "$@"             Text file path of language model training set.