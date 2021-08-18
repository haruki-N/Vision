import argparse, os

from detectron2 import model_zoo
from detectron2.config import get_cfg, CfgNode
from detectron2.engine import default_argument_parser, default_setup, DefaultPredictor


def get_args():
    parser = argparse.ArgumentParser(description="ImageDetectionInference")
    parser.add_argument('--dir_in', type=os.path.abspath, help="推論対象の画像ディレクトリ")
    parser.add_argument('--dir_out', type=os.path.abspath, help="推論結果の保存ファイル名")
    parser.add_argument('--model', type=str, help="model type to use",
                        default="COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml")
    parser.add_argument('--thresh', type=float, default=0.7, help="thresh以上の確信度のobjectを検出")
    args = parser.parse_args()
    return args


def setup_model(args: argparse.ArgumentParser):
    """
        set up detectron2 configuration, model
    :param args:
        argparse for set up
    :return:
        model & cfg
    """
    # set up model of detectron2
    cfg: CfgNode = get_cfg()
    model_file_name = args.model
    print(model_file_name)
    fi_cfg = model_zoo.get_config_file(model_file_name)
    cfg.merge_from_file(fi_cfg)
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = args.thresh
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(model_file_name)
    predictor = DefaultPredictor(cfg)

    return predictor, cfg
