import json, argparse, os

def get_args():
    parser = argparse.ArgumentParser(description='replace "text" lines in json file with translated ones')
    parser.add_argument('--json_file', type=str, default='/Users/nagasawa_h/Desktop/TOHOKU_Univ./Lab/TaiwaClub/translation/image_chat/train.jsonl')
    parser.add_argument('--text_file', type=str, default='/Users/nagasawa_h/Desktop/TOHOKU_Univ./Lab/TaiwaClub/translation/tmp_enja/ja_train.txt')
    args = parser.parse_args()

    return args


def text_reader(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            yield line


def main():
    args = get_args()
    json_file = args.json_file
    txt_file = args.text_file
    txt_iter = text_reader(txt_file)
    out_json = 'ja_' + os.path.basename(json_file)
    if not os.path.exists(out_json):
        f = open(out_json, 'x')
        f.close()

    with open(json_file, 'r', encoding='utf-8') as f:
        with open(out_json, 'w') as fo:
            for jsonl in f:
                jsonl = json.loads(jsonl)
                for key in jsonl['dialog'].keys():
                    txt = next(txt_iter)
                    jsonl['dialog'][key]['text'] = txt.strip('\n')
                out = json.dumps(jsonl, ensure_ascii=False)
                print(out)
                fo.write(str(out))
                fo.write('\n')


if __name__ == '__main__':
    main()
