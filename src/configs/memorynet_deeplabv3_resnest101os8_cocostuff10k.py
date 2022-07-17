'''memorynet_deeplabv3_resnest101os8_cocostuff10k'''
import os
from .base_cfg import *


# modify dataset config
DATASET_CFG = DATASET_CFG.copy()
DATASET_CFG.update({
    'type': 'cocostuff10k',
    'rootdir': os.path.join(os.getcwd(), 'COCOStuff10k'),
})
DATASET_CFG['test']['set'] = 'test'
# modify dataloader config
DATALOADER_CFG = DATALOADER_CFG.copy()
DATALOADER_CFG['train'].update({
    'batch_size': 32,
})
# modify optimizer config
OPTIMIZER_CFG = OPTIMIZER_CFG.copy()
OPTIMIZER_CFG.update({
    'type': 'sgd',
    'sgd': {
        'learning_rate': 0.001,
        'min_lr': 1e-4,
        'momentum': 0.9,
        'weight_decay': 5e-4,
    },
    'max_epochs': 150
})
# modify losses config
LOSSES_CFG = LOSSES_CFG.copy()
# modify segmentor config
SEGMENTOR_CFG = SEGMENTOR_CFG.copy()
SEGMENTOR_CFG.update({
    'num_classes': 182,
    'backbone': {
        'type': 'resnest101',
        'series': 'resnest',
        'pretrained': True,
        'outstride': 8,
        'selected_indices': (0, 1, 2, 3),
    },
})
SEGMENTOR_CFG['memory']['use_loss'] = False
SEGMENTOR_CFG['memory']['update_cfg']['momentum_cfg']['base_lr'] = 0.001 * 0.9
# modify inference config
INFERENCE_CFG = INFERENCE_CFG.copy()
# modify common config
COMMON_CFG = COMMON_CFG.copy()
COMMON_CFG['work_dir'] = 'memorynet_deeplabv3_resnest101os8_cocostuff10k'
COMMON_CFG['logfilepath'] = 'memorynet_deeplabv3_resnest101os8_cocostuff10k/memorynet_deeplabv3_resnest101os8_cocostuff10k.log'
COMMON_CFG['resultsavepath'] = 'memorynet_deeplabv3_resnest101os8_cocostuff10k/memorynet_deeplabv3_resnest101os8_cocostuff10k_results.pkl'