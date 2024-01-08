import argparse
import csv
from pathlib import Path

def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_captions", type=str, default="", help="Location of input caption file / 入力captionファイルの場所")
    parser.add_argument("--output_folder", type=str, default="", help="Location of output caption files / 出力されるキャプションファイルの場所")
    parser.add_argument("--caption_extension", type=str, default=".caption", help="extension of caption file / 出力されるキャプションファイルの拡張子")
    parser.add_argument("--replacement_search", type=str, default="", required=False, help="Search string to replace / 置換する文字列")
    parser.add_argument("--replacement_value", type=str, default="", required=False, help="Replacement string / 置換後の文字列")

    return parser

def main(args):

    replacement_search = args.replacement_search;
    replacement_value = args.replacement_value;

    with open(args.input_captions, 'r') as csv_file:
        reader = csv.reader(csv_file)

        #skip header
        next(reader)

        for row in reader:
            if replacement_search:
                    row[1] = row[1].replace(replacement_search, replacement_value)
            print(row)
            file = open(Path(args.output_folder).joinpath(row[0] + args.caption_extension), 'w')
            file.write(row[1])
            file.close()    

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()

    main(args)