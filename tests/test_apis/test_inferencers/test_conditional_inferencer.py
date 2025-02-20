# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from mmedit.apis.inferencers.conditional_inferencer import \
    ConditionalInferencer
from mmedit.utils import register_all_modules

register_all_modules()


def test_conditional_inferencer():
    cfg = osp.join(
        osp.dirname(__file__), '..', '..', '..', 'configs', 'sngan_proj',
        'sngan-proj_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py')
    result_out_dir = osp.join(
        osp.dirname(__file__), '..', '..', 'data', 'conditional_result.png')
    inferencer_instance = \
        ConditionalInferencer(cfg,
                              None,
                              extra_parameters={'sample_model': 'orig'})
    inference_result = inferencer_instance(label=1)
    inference_result = inferencer_instance(
        label=1, result_out_dir=result_out_dir)
    result_img = inference_result[1]
    assert result_img.shape == (4, 3, 32, 32)


if __name__ == '__main__':
    test_conditional_inferencer()
