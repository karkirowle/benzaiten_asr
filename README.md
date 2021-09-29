## Phoneme and articulatory analysis framework for Kaldi/ESPNet ASR

This works is a phoneme and articulatory analysis framework based on lexicon-based grapheme to phoneme mappings. 
Phoneme recognition is known to be difficult, as the task is highly contextual, nevertheless, phoneme analysis should be
a first step in order to analyse where understanding of ASR models are lacking. This approach can use decoded sentences from
word-level ASRs to quantify their performing on phonemes and articulatory features. 

The code in this repository can be used to calculate PER and AFER based on a Kaldi wer details file.

## What does it do
* Implements a new variant of PER on word-level ASR
* Implements a new error rate, the AFER (Articulatory Feature Error Rate) on word-level ASR


### Requirements

```
pip install git+https://github.com/karkirowle/benzaiten_asr.git
```

### Example for PER extraction

See example.py

## Languages supported
:us: :netherlands:
### Future plans
* Support for multiple languages, and g2p models in PER
* Fully support MoA-PoA for Dutch/Mandarin phonemes
