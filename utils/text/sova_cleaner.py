import os

from .sova_tts_tps_zdy.tps.handler import Handler
from .sova_tts_tps_zdy.tps.types import Delimiter

# Now - initialise handler in context of this scope
# TO DO - refactor this - wrap initialisation logic somewhere
sova_config_path = os.environ["SOVA_TEXT_HANDLER_CONFIG"]
sova_handler = Handler.from_config(sova_config_path)


def sova_cleaner(text):
  text = to_sova_phonemes(text)
  return text


def to_sova_phonemes(text: str):
    res = sova_handler.generate(
        text=text,
        # cleaner=cleaners.,
        # user_dict=self.user_dict,
        keep_delimiters=True,
        mask_stress=False,
        mask_phonemes=False
    )

    # Remove delimiter tokens from output
    resp = list(res)
    resp = [x for x in resp if x != Delimiter.eos]
    res = ' '.join(resp).replace('_', ' ')
    return res
