from benzaiten_asr.phoneme_analysis import WERDetails
import pandas as pd

wer_details_1 = WERDetails("tests/examples/kaldi_english_per_utt",
                       config="eng_kaldi")
dataframe = wer_details_1.all_pers_dataframe()

#print(dataframe)