#!/bin/bash -ev

set -xe

USAGE="source log2txt.sh -i [LOG] -o [TXT]"

while getopts i:o: OPT
do
  case ${OPT} in
    "i" ) FLG_I="TURE"; LOG=${OPTARG};;
    "o" ) FLG_O="TRUE"; TXT=${OPTARG};;
    *) echo ${USAGE}
       exit 1 ;;
  esac
done
echo "PROCESSING"

# grepで'H'から始まる行のみを抽出. awkでタブ区切りし、3番目の値を取得. trで_を削除. sedで空白を除去. teeで出力
grep -E '^H.*' | awk -F\t '{print $3}' | tr -d ▁ | sed 's/ //g' | tee $TXT

echo "PROCESS DONE SUCESSFULLY"