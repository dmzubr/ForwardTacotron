""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from . import cmudict
from .sova_tts_tps_zdy.tps.ssymbols.russian import RU_TRANS_SET

_pad = '_'
_punctuation = '!\'(),.:;? '
_special = '-'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Phonemes
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_non_pulmonic_consonants = 'ʘɓǀɗǃʄǂɠǁʛ'
_pulmonic_consonants = 'pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ'
_suprasegmentals = 'ˈˌːˑ'
_other_symbols = 'ʍwɥʜʢʡɕʑɺɧ'
_diacrilics = 'ɚ˞ɫ'


en_phonemes = sorted(list(
   _pad + _punctuation + _special + _vowels + _non_pulmonic_consonants
   + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics)
)


phonemes = sorted(
   list(_pad + _punctuation + _special) +
   RU_TRANS_SET
)
print(f'Resulting Taco phonemes list is')
print(phonemes)

phonemes_set = set(phonemes)
