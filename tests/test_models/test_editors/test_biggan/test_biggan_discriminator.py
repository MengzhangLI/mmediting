# Copyright (c) OpenMMLab. All rights reserved.
from copy import deepcopy

import pytest
import torch

from mmedit.models.editors.biggan import BigGANDiscriminator
from mmedit.registry import MODULES


class TestBigGANDiscriminator(object):

    @classmethod
    def setup_class(cls):
        num_classes = 1000
        cls.default_config = dict(
            type='BigGANDiscriminator',
            input_scale=128,
            num_classes=num_classes,
            base_channels=8)
        cls.x = torch.randn((2, 3, 128, 128))
        cls.label = torch.randint(0, num_classes, (2, ))

    def test_biggan_discriminator(self):
        # test default settings
        d = MODULES.build(self.default_config)
        assert isinstance(d, BigGANDiscriminator)
        y = d(self.x, self.label)
        assert y.shape == (2, 1)

        # test different init types
        cfg = deepcopy(self.default_config)
        cfg.update(dict(init_type='N02'))
        d = MODULES.build(cfg)
        y = d(self.x, self.label)
        assert y.shape == (2, 1)

        cfg = deepcopy(self.default_config)
        cfg.update(dict(init_type='xavier'))
        d = MODULES.build(cfg)
        y = d(self.x, self.label)
        assert y.shape == (2, 1)

        # test different num_classes
        cfg = deepcopy(self.default_config)
        cfg.update(dict(num_classes=0))
        d = MODULES.build(cfg)
        y = d(self.x, None)
        assert y.shape == (2, 1)

        # test with `with_spectral_norm=False`
        cfg = deepcopy(self.default_config)
        cfg.update(dict(with_spectral_norm=False))
        d = MODULES.build(cfg)
        y = d(self.x, self.label)
        assert y.shape == (2, 1)

        # test torch-sn
        cfg = deepcopy(self.default_config)
        cfg.update(dict(sn_style='torch'))
        d = MODULES.build(cfg)
        y = d(self.x, self.label)
        assert y.shape == (2, 1)

    @pytest.mark.skipif(not torch.cuda.is_available(), reason='requires cuda')
    def test_biggan_discriminator_cuda(self):
        # test default settings
        d = MODULES.build(self.default_config).cuda()
        y = d(self.x.cuda(), self.label.cuda())
        assert y.shape == (2, 1)

        # test different init types
        cfg = deepcopy(self.default_config)
        cfg.update(dict(init_type='N02'))
        d = MODULES.build(cfg).cuda()
        y = d(self.x.cuda(), self.label.cuda())
        assert y.shape == (2, 1)

        cfg = deepcopy(self.default_config)
        cfg.update(dict(init_type='xavier'))
        d = MODULES.build(cfg).cuda()
        y = d(self.x.cuda(), self.label.cuda())
        assert y.shape == (2, 1)

        # test different num_classes
        cfg = deepcopy(self.default_config)
        cfg.update(dict(num_classes=0))
        d = MODULES.build(cfg).cuda()
        y = d(self.x.cuda(), None)
        assert y.shape == (2, 1)

        # test with `with_spectral_norm=False`
        cfg = deepcopy(self.default_config)
        cfg.update(dict(with_spectral_norm=False))
        d = MODULES.build(cfg).cuda()
        y = d(self.x.cuda(), self.label.cuda())
        assert y.shape == (2, 1)

        # test torch-sn
        cfg = deepcopy(self.default_config)
        cfg.update(dict(sn_style='torch'))
        d = MODULES.build(cfg).cuda()
        y = d(self.x.cuda(), self.label.cuda())
        assert y.shape == (2, 1)
