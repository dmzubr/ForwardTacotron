# Preprocess
python preprocess.py --path /synthesis/datasets/russian/from_yandex --hp_file hparams_yandex_fix.py

# Train
python train_tacotron.py --hp_file hparams_yandex_fix.py
python train_tacotron.py --hp_file hparams_yandex_fix.py --force_align
python train_forward.py --hp_file hparams_yandex_fix.py
