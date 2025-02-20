# Copyright (c) OpenMMLab. All rights reserved.

from mmedit.registry import BACKBONES, COMPONENTS
from ..global_local import GLEncoderDecoder


@BACKBONES.register_module()
class AOTEncoderDecoder(GLEncoderDecoder):
    """Encoder-Decoder used in AOT-GAN model.

    This implementation follows:
    Aggregated Contextual Transformations for High-Resolution Image Inpainting
    The architecture of the encoder-decoder is:
    (conv2d x 3) --> (dilated conv2d x 8) --> (conv2d or deconv2d x 3).

    Args:
        encoder (dict): Config dict to encoder.
        decoder (dict): Config dict to build decoder.
        dilation_neck (dict): Config dict to build dilation neck.
    """

    def __init__(self,
                 encoder=dict(type='AOTEncoder'),
                 decoder=dict(type='AOTDecoder'),
                 dilation_neck=dict(type='AOTBlockNeck')):
        super().__init__()
        self.encoder = COMPONENTS.build(encoder)
        self.decoder = COMPONENTS.build(decoder)
        self.dilation_neck = COMPONENTS.build(dilation_neck)
