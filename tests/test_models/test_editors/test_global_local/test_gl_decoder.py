# Copyright (c) OpenMMLab. All rights reserved.
import pytest
import torch

from mmedit.registry import COMPONENTS
from mmedit.utils import register_all_modules


def test_gl_decoder():
    register_all_modules()
    input_x = torch.randn(1, 256, 64, 64)
    template_cfg = dict(type='GLDecoder')

    gl_decoder = COMPONENTS.build(template_cfg)
    output = gl_decoder(input_x)
    assert output.shape == (1, 3, 256, 256)

    cfg_copy = template_cfg.copy()
    cfg_copy['out_act'] = 'sigmoid'
    gl_decoder = COMPONENTS.build(cfg_copy)
    output = gl_decoder(input_x)
    assert output.shape == (1, 3, 256, 256)

    with pytest.raises(ValueError):
        # conv_cfg must be a dict or None
        cfg_copy = template_cfg.copy()
        cfg_copy['out_act'] = 'relu'
        gl_decoder = COMPONENTS.build(cfg_copy)
        output = gl_decoder(input_x)

    if torch.cuda.is_available():
        gl_decoder = COMPONENTS.build(template_cfg)
        gl_decoder = gl_decoder.cuda()
        output = gl_decoder(input_x.cuda())
        assert output.shape == (1, 3, 256, 256)
