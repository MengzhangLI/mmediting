# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from mmedit.apis.inferencers.translation_inferencer import \
    TranslationInferencer
from mmedit.utils import register_all_modules

register_all_modules()


def test_translation_inferencer():
    cfg = osp.join(
        osp.dirname(__file__), '..', '..', '..', 'configs', 'pix2pix',
        'pix2pix_vanilla-unet-bn_1xb1-80kiters_facades.py')
    data_path = osp.join(
        osp.dirname(__file__), '..', '..', 'data', 'unpaired', 'trainA',
        '1.jpg')
    result_out_dir = osp.join(
        osp.dirname(__file__), '..', '..', 'data', 'translation_result.png')

    inferencer_instance = \
        TranslationInferencer(cfg, None)
    inferencer_instance(img=data_path)
    inference_result = inferencer_instance(
        img=data_path, result_out_dir=result_out_dir)
    result_img = inference_result[1]
    assert result_img[0].numpy().shape == (3, 256, 256)


if __name__ == '__main__':
    test_translation_inferencer()
