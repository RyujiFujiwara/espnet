# FWER,FTER算出の準備に使う。
from espnet.utils.cli_utils import get_commandline_args
import argparse
import parser
import os
import sys

def get_parser() -> argparse.ArgumentParser:
    # スクリプトの説明 (python sclite_fwer_prepare.py --help で引数等が出力に明示される。)
    parser = argparse.ArgumentParser(
        description="prepare for FWER",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--score_dir",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--N_mask",
        type=int,
        required=True,
    )

    return parser

def forward(
    score_dir: str,
    N_mask: int,
):
    ## SETTING
    _scoredir = score_dir
    N_mask = N_mask # マスクする単語数の設定(FWER,FTER算出対象)
    input_ref = os.path.join(_scoredir,"end_ref.trn")
    input_hyp = os.path.join(_scoredir,"end_hyp.trn") # hyp_token.trn or hyp_nbest.trn
    output_ref = os.path.join(_scoredir,"ref_fwer.trn")
    output_hyp = os.path.join(_scoredir,"hyp_fwer.trn")
    ##


    N = N_mask + 1 # 話者IDを含める
    mask_Length = 0 # マスクする単語列の長さの初期化

    # ファイルを開いて処理
    with open(input_ref, "r", encoding="utf-8") as ref_file, \
        open(input_hyp, "r", encoding="utf-8") as hyp_file, \
        open(output_ref, "w", encoding="utf-8") as ref_out, \
        open(output_hyp, "w", encoding="utf-8") as hyp_out:
        
        # 両方のファイルを同時に1行ずつ読み込む
        for ref_line, hyp_line in zip(ref_file, hyp_file):
            # ref.txtの処理
            ref_words = ref_line.strip().split()  # 単語に分割
            hyp_words = hyp_line.strip().split()  # 単語に分割
            mask_Length = len(ref_words) - N
            if mask_Length > 0:
                ref_result = " ".join(ref_words[mask_Length:])  # 最初のmask_Length単語を除外
                hyp_result = " ".join(hyp_words[mask_Length:])
            else:
                ref_result = " ".join(ref_words) if ref_words else ""  # 最後の単語または空文字列
                hyp_result = " ".join(hyp_words) if hyp_words else ""

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
