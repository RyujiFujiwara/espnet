# FWER,FTER算出の準備に使う。
from espnet.utils.cli_utils import get_commandline_args
import argparse
import parser
import os
import sys

def get_parser() -> argparse.ArgumentParser:
    # スクリプトの説明 (python sclite_fcer_prepare.py --help で引数等が出力に明示される。)
    parser = argparse.ArgumentParser(
        description="prepare for FCER",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--numb_of_nbest",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--exp_testsets_dir",
        type=str,
        required=True,
    )

    return parser

def forward(
    numb_of_nbest: int,
    exp_testsets_dir: str,
):
    ## SETTING
    _exp_testsets_dir = exp_testsets_dir
    input_ref = os.path.join(_exp_testsets_dir,"score_cer/ref.trn")
    input_hyp = os.path.join(_exp_testsets_dir,f"score_cer/hyp_{numb_of_nbest}best.trn") # hyp.trn or hyp_nbest.trn
    input_text = os.path.join(_exp_testsets_dir,"logdir/output.1/1best_recog/input_text")
    output_ref = os.path.join(_exp_testsets_dir,f"score_cer/ref_fcer_{numb_of_nbest}best.trn")
    output_hyp = os.path.join(_exp_testsets_dir,f"score_cer/hyp_fcer_{numb_of_nbest}best.trn")
    ##

    with open(input_ref, "r", encoding="utf-8") as ref_file, \
        open(input_hyp, "r", encoding="utf-8") as hyp_file, \
        open(input_text, "r", encoding="utf-8") as input_file, \
        open(output_ref, "w", encoding="utf-8") as ref_out, \
        open(output_hyp, "w", encoding="utf-8") as hyp_out:
        
        # 正解データ、推論データ、入力テキストのファイルを同時に1行ずつ読み込む
        for ref_line, hyp_line, input_line in zip(ref_file, hyp_file, input_file):
            
            try:
                input_line = list(input_line.strip().split(" ", 1)[1])
            except IndexError as e:
                continue # 入力テキストが無かったらとばす
            mask_Length = len(input_line)

            ref_words = ref_line.strip().split()[mask_Length:]  # 単語に分割
            hyp_words = hyp_line.strip().split()[mask_Length:]  # 単語に分割

            ref_result = " ".join(ref_words)
            hyp_result = " ".join(hyp_words)

            ref_out.write(ref_result + "\n")
            hyp_out.write(hyp_result + "\n")

    print(f"Processing complete. Results saved in '{output_ref}' and '{output_hyp}'.")

def main(cmd=None):
    print(get_commandline_args(), file=sys.stderr) # pythonプロセスのコマンドラインを文字列で標準エラー出力
    parser = get_parser() # 引数の受け取り方を指定 ArgumentParser(prog='sclite_fwer_prepare.py', usage=None, description='prepare for FWER', formatter_class=<class 'argparse.ArgumentDefaultsHelpFormatter'>, conflict_handler='error', add_help=True)
    args = parser.parse_args(cmd) # cmd=Noneの時、"--score_dir its" → "Namespace(score_dir='its')"
    kwargs = vars(args)
    forward(**kwargs)

if __name__ == "__main__":
    main()
