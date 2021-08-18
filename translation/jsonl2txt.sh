#!/bin/bash -ev

set -xe

USAGE="source jsonl2txt.sh -i [JSONL] -o [TXT]"

while getopts i:o: OPT
do
  case ${OPT} in
    "i" ) FLG_I="TURE"; JSONL=${OPTARG};;
    "o" ) FLG_O="TRUE"; TXT=${OPTARG};;
    *) echo ${USAGE}
       exit 1 ;;
  esac
done
echo "PROCESSING"

# jqでtextキーのvalueを全て取得. trで"を削除. teeで出力
jq 'recurse | select(.text?).text' $JSONL | tr -d \" | tee $TXT

echo "PROCESS DONE SUCESSFULLY"
