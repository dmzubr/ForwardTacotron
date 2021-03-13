sudo docker run --gpus=all --ipc=host -itd --restart=unless-stopped --name=taco -v /home/dmzubr/slutbot/synthesis:/synthesis -v /home/dmzubr/nltk_data:/root/nltk_data cr.yandex/crpmg9qeitngo9ui36lc/taco2-train
sudo docker exec -it taco bash

# Additional apt dependencies in this container
# apt install build-essential

# Additional pip dependencies in this container
# pip install nltk pyyaml unidecode pyworld webrtcvad
