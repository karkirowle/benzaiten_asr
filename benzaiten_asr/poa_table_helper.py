

from benzaiten_asr.phoneme_analysis import AlternativeCMUDict
import pandas as pd
import numpy as np
from benzaiten_asr.utils import HParam


def generate_empty_csv():
    config = HParam("configs/mandarin.yaml")
    dict = AlternativeCMUDict("text/mandarin_lexicon.dict", conf=config)

    phonemes = dict.phonemes_in_dict()

    moa_list = config.phoneme.moa
    poa_list = config.phoneme.poa

    articulatory_features = set(moa_list).union(set(poa_list))

    zero_array = np.zeros((len(phonemes), len(articulatory_features)))

    df = pd.DataFrame(zero_array, phonemes, columns=articulatory_features)

    #df.to_csv("csvs/PhoneSet_mandarin_true_comments.csv")

    return df

if __name__ == '__main__':
    print(generate_empty_csv())