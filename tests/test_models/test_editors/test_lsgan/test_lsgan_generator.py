# Copyright (c) OpenMMLab. All rights reserved.
import pytest
import torch

from mmedit.models.editors.lsgan import LSGANGenerator
from mmedit.registry import MODULES


class TestLSGANGenerator(object):

    @classmethod
    def setup_class(cls):
        cls.noise = torch.randn((3, 128))
        cls.default_config = dict(
            type='LSGANGenerator', noise_size=128, output_scale=128)

    def test_lsgan_generator(self):

        # test default setting with builder
        g = MODULES.build(self.default_config)
        assert isinstance(g, LSGANGenerator)
        x = g(None, num_batches=3)
        assert x.shape == (3, 3, 128, 128)
        x = g(None, num_batches=3, return_noise=True)
        assert x['noise_batch'].shape == (3, 128)
        x = g(self.noise, return_noise=True)
        assert x['noise_batch'].shape == (3, 128)
        x = g(torch.randn, num_batches=3, return_noise=True)
        assert x['noise_batch'].shape == (3, 128)

        # test different output_scale
        config = dict(type='LSGANGenerator', noise_size=128, output_scale=64)
        g = MODULES.build(config)
        assert isinstance(g, LSGANGenerator)
        x = g(None, num_batches=3)
        assert x.shape == (3, 3, 64, 64)

    @pytest.mark.skipif(not torch.cuda.is_available(), reason='requires cuda')
    def test_lsgan_generator_cuda(self):

        # test default setting with builder
        g = MODULES.build(self.default_config).cuda()
        assert isinstance(g, LSGANGenerator)
        x = g(None, num_batches=3)
        assert x.shape == (3, 3, 128, 128)
        x = g(None, num_batches=3, return_noise=True)
        assert x['noise_batch'].shape == (3, 128)
        x = g(self.noise.cuda(), return_noise=True)
        assert x['noise_batch'].shape == (3, 128)
        x = g(torch.randn, num_batches=3, return_noise=True)
        assert x['noise_batch'].shape == (3, 128)

        # test different output_scale
        config = dict(type='LSGANGenerator', noise_size=128, output_scale=64)
        g = MODULES.build(config).cuda()
        assert isinstance(g, LSGANGenerator)
        x = g(None, num_batches=3)
        assert x.shape == (3, 3, 64, 64)
