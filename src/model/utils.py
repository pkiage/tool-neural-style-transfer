import os


def use_low_resource_settings(option):
    if option == 'Yes':
        os.environ['CUDA_VISIBLE_DEVICES'] = ''
        os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'


def suppress_warnings(option):
    if option == 'Yes':
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
