
from benzaiten_asr.phoneme_analysis import WERDetails
from tests.examples import *
import pkg_resources

def test_kaldi_dutch_analysis():

    #sajt = WERDetails(filename, config="dutch_kaldi")

    return 1

def test_kaldi_english_analysis():
    filename = pkg_resources.resource_filename(__name__, 'examples/kaldi_english_per_utt')
    #filename = espnet_english_path()
    sajt = WERDetails(filename, config="eng_kaldi")

    return 1

def test_espnet_english_analysis():
    filename = pkg_resources.resource_filename(__name__, 'examples/espnet_english_per_utt')
    sajt = WERDetails(filename, config="eng_espnet")

    return 1
