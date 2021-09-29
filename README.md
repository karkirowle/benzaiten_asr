## Phoneme and articulatory analysis framework for Kaldi/ESPNet ASR

This works is a phoneme and articulatory analysis framework based on lexicon-based grapheme to phoneme mappings. 
Phoneme recognition is known to be difficult, as the task is highly contextual, nevertheless, phoneme analysis should be
a first step in order to analyse where understanding of ASR models are lacking. This approach can use decoded sentences from
word-level ASRs to quantify their performing on phonemes and articulatory features. 

The code in this repository can be used to calculate PER and AFER based on a Kaldi wer details file.

## What does it do
* Implements a new variant of PER on word-level ASR
* Implements a new error rate, the AFER (Articulatory Feature Error Rate) on word-level ASR

The WER and the PER is calculated based on the Levensteihn distance.

### Requirements
- Use the conda environment.yml file provided

### Paper reproduction  :page_with_curl:
- Install the required packages for the framework
- Create your venv of your choice from the requirements.txt provided
  - We use a function which will be deprecated in sklearn version 0.25, so please be mindful of that
  
- Run analysis.py

### Adaptation for your own datasets
- Put your wer_details experiments in the same format as the other experiments, see example below
- Adapt the config files with your feature conversions and your lexicon, or use the already provided conversion
  tables or lexicons. (Provided for English and Dutch so far)
  
### Example for PER extraction

See example.py

## Languages supported
:us: :netherlands:
### Future plans
* Support for multiple languages, and g2p models in PER
* Fully support MoA-PoA for Dutch/Mandarin phonemes
