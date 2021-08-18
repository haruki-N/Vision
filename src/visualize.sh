#!/bin/bash -ev

USAGE="bash visualize.sh -i [IN_DIR] -o [OUT_DIR] -m [MODEL] -g [GPU]"

while getopts i:o:m:g: OPT
do
    case ${OPT} in
        "i" ) FLG_I="TRUE"; IN_DIR=${OPTARG};;
        "o" ) FLG_O="TRUE"; OUT_DIR=${OPTARG};;
        "m" ) FLG_M="TRUE"; MODEL=${OPTARG};;
        "g" ) FLG_G="TRUE"; GPU=${OPTARG};;
        *) echo ${USAGE}
	   exit 1 ;;
    esac
done

if test "${FLG_M}" != "TRUE"; then
    MODEL="COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"
fi

if test "${FLG_G}" != "TRUE"; then
    GPU=0
fi

CUDA_VISIBLE_DEVICES=$GPU python src/visualize.py \
    --dir_in $IN_DIR \
    --dir_out $OUT_DIR \
    --model $MODEL
