model = dict(
    type='SAGAN',
    data_preprocessor=dict(type='GenDataPreprocessor'),
    num_classes=10,
    generator=dict(
        type='SAGANGenerator',
        num_classes=10,
        output_scale=32,
        base_channels=256,
        attention_cfg=dict(type='SelfAttentionBlock'),
        attention_after_nth_block=2,
        with_spectral_norm=True),
    discriminator=dict(
        type='ProjDiscriminator',
        num_classes=10,
        input_scale=32,
        base_channels=128,
        attention_cfg=dict(type='SelfAttentionBlock'),
        attention_after_nth_block=1,
        with_spectral_norm=True),
    generator_steps=1,
    discriminator_steps=5)
