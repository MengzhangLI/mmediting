# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from mmedit.datasets import SinGANDataset
from mmedit.utils import register_all_modules

register_all_modules()


class TestSinGANDataset(object):

    @classmethod
    def setup_class(cls):
        cls.imgs_root = osp.join(
            osp.dirname(osp.dirname(__file__)), 'data/image/gt/baboon.png')
        cls.min_size = 25
        cls.max_size = 250
        cls.scale_factor_init = 0.75
        cls.pipeline = [dict(type='PackEditInputs', pack_all=True)]

    def test_singan_dataset(self):
        dataset = SinGANDataset(
            self.imgs_root,
            min_size=self.min_size,
            max_size=self.max_size,
            scale_factor_init=self.scale_factor_init,
            pipeline=self.pipeline)
        assert len(dataset) == 1000000

        data_dict = dataset[0]['inputs']
        assert all([f'real_scale{i}' in data_dict for i in range(10)])
