import os, json, cv2

from utility import get_args, setup_model


def inference():
    """
        Object detection on input images.
        Save the json files which store the result of inference.
    :return: None
    """
    args = get_args()
    dir_img = args.dir_in
    dir_out = args.dir_out

    # set up model of detectron2
    predictor, _ = setup_model(args)

    # inference
    img_files = os.listdir(dir_img)
    out_dict = dict()
    for img_file in img_files:
        im = cv2.imread(img_file)   # 画像の読み込み. 高さ(H)×幅(W)×色(RGBなら3)次元のnp.ndarray
        outputs = predictor(im)
        out_dict[img_file] = {
            'image_size': outputs.instance.image_size,   # the size of input image
            'num_instance': len(outputs.instance),   # the number of detected object
            'pred_classes': outputs.instance.pred_classes.cpu().tolist(),   #
            'scores': outputs.instance.scores.cpu().tolist(),  # confidence scores for each objects
            'pred_boxes': outputs.instance.pred_boxes,   # detected boxes of objects
        }

    to_write = open(dir_out, 'w')
    json.dump(out_dict, to_write, indent=2)


def main():
    inference()


if __name__ == '__main__':
    main()
