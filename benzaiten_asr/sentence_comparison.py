"""
The idea for this is to manage comparison of sentences between different models and provide tools for it

"""

from typing import List, Tuple

import pandas

from benzaiten_asr.phoneme_analysis import WERDetails, AlternativeCMUDict
from benzaiten_asr.utils import HParam
import pandas as pd
import pkg_resources
import os


# class Record():
#
#     def __init__(self, id: str, val: List[str]):
#
#         self.id = id
#         self._val = val
#
#     def add_new_val(self, val: str):
#         self._val.append(val)
#
#     def record_merge(self, record_list_1: List['Record'], record_list_2: List['Record']):
#
#         for record_1 in record_list_1
#
#
#         new_record = Record(id,val)



class SentenceComparer():

    def __init__(self, per_utts: list, model_types: list, suffixes: list, romanise: bool):

        assert len(per_utts) == len(model_types), "Each female_dc_read_kaldi_per_utt needs to be given its corresponding model_type (either kaldi or espnet)"

        total_df = None

        stream = pkg_resources.resource_filename(__name__, 'configs/mandarin.yaml')
        config = HParam(stream)
        package_dependent_dict = pkg_resources.resource_filename(__name__, os.path.join(config.phoneme.dictionary))

        self.alternative_cmudict = AlternativeCMUDict(location=package_dependent_dict, conf=config)

        for per_utt, model_type, suffix in zip(per_utts,model_types,suffixes):

            sentence_df = self.load_sentences(per_utt,model_type,suffix,romanise)

            if total_df is None:
                total_df = sentence_df
            else:
                total_df = pd.concat((total_df,sentence_df), axis=1)


        equal_idx = total_df.eq(total_df.iloc[:, 0], axis=0).all(axis=1)
        non_equal_rows = total_df[equal_idx == False]
        self.non_equal_rows = non_equal_rows[non_equal_rows.columns.drop(list(non_equal_rows.filter(regex='ref_words_*'))[1:])]
        print("")
    def export(self, filename: str):

        self.non_equal_rows.to_csv(filename)

    def clean_non_words(self, sentence: list) -> list:

        #regex = regex.
        return WERDetails.clean_non_words(sentence)

    def clear(self, sentence: list) -> str:
        clear_words = self.clean_non_words(sentence)
        clear_words_lower = [self.alternative_cmudict.get_arpabet(clear_word.lower()).replace("{","").replace("}","") \
                             for clear_word in clear_words]
        return " ".join(clear_words_lower)

    def load_sentences(self, per_utt: str, asr: str, suffix: str, romanize: bool) -> pandas.DataFrame:
        """
        Loads the references and hypothesis sentences from the WER details file
        :return: two list of sentences
        """
        assert (asr == "kaldi") | (asr == "espnet")


        with open(per_utt, 'r') as f:
            all_lines = f.readlines()

            if asr == "kaldi":

                id_sentencewise = [line.split()[0] for line in all_lines if ("ref" in line)]
                ref_words_sentencewise = [self.clear(line.split()[2:]) for line in all_lines if ("ref" in line)]
                hyp_words_sentencewise = [self.clear(line.split()[2:]) for line in all_lines if ("hyp" in line)]

            else:  # ESPNET (due to assert)

                id_sentencewise = [line.split()[1].rstrip(")").lstrip("(") for line in all_lines if "id:" in line]
                ref_words_sentencewise = [self.clear(line.split()[1:]) \
                                          for line in all_lines if ("REF:" in line)]

                hyp_words_sentencewise = [self.clear(line.split()[1:]) \
                                          for line in all_lines if ("HYP:" in line)]


            df_dict = {
                "id": id_sentencewise,
                "ref_words_" + suffix: ref_words_sentencewise,
                "hyp_words_" + suffix: hyp_words_sentencewise
            }

            df = pd.DataFrame.from_dict(df_dict)
            df = df.set_index("id")
            return df




if __name__ == '__main__':
    print()
    path_1 = "/home/boomkin/PycharmProjects/benzaiten_asr/tests/examples/espnet_mandarin_per_utt"
    path_2 = "/home/boomkin/PycharmProjects/benzaiten_asr/tests/examples/kaldi_mandarin_per_utt"

    SentenceComparer([path_1,path_2],["espnet","kaldi"],["espnet","kaldi"],romanise=True)