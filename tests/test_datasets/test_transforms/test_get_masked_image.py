# Copyright (c) OpenMMLab. All rights reserved.
import numpy as np

from mmedit.datasets.transforms import GetMaskedImage


def test_masked_img():
    img = np.random.rand(4, 4, 3).astype(np.float32)
    mask = np.zeros((4, 4, 1), dtype=np.float32)
    mask[1, 1] = 1

    results = dict(gt=img, mask=mask)
    get_masked_img = GetMaskedImage(zero_value=0)
    results = get_masked_img(results)
    masked_img = img * (1. - mask)
    assert np.array_equal(results['img'], masked_img)

    name_ = repr(get_masked_img)
    class_name = get_masked_img.__class__.__name__
    assert name_ == class_name + ("(img_key='gt', mask_key='mask'"
                                  ", out_key='img', zero_value=0)")
