import cv2, os

from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer

from utility import get_args, setup_model


def visualize():
    """
        Object detection on input images.
        Save the infered images to dir_out
    :return: None
    """
    args = get_args()
    print(args)
    dir_img = args.dir_in
    dir_out = args.dir_out

    # set up model of detectron2
    predictor, cfg = setup_model(args)
    print(f'DIR_img: {dir_img}')
    img_files = os.listdir(dir_img)
    img_files = [file for file in img_files if file.endswith('.jpeg') or file.endswith('.png')]
    for img_file in img_files:
        img_file = os.path.join(dir_img, img_file)
        im = cv2.imread(img_file)
        outputs = predictor(im)
        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        out = v.draw_instance_predictions(outputs['instances'].to('cpu'))
        path = os.path.join(dir_out, os.path.basename(img_file))
        cv2.imwrite(path, out.get_image()[:, :, ::-1])   # imreadの結果がBGRの順なので::-1でRGBに変換しているっぽい


def main():
    visualize()


if __name__ == '__main__':
    main()
