import pkg_resources

def espnet_english_path():
    return pkg_resources.resource_filename(__name__, 'examples/kaldi_dutch_per_utt')
