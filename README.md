# Nonspeech7k dataset: Classification and analysis of human non-speech sound

### [Paper link](https://doi.org/10.1049/sil2.12233) 

### [Nonspeech7k dataset link ](https://zenodo.org/record/6967442)

## Prerequisites
- Ubuntu
- Python 3
- NVIDIA GPU (11G memory or larger) 
## Getting Started
### Installation
- Clone this repo:
```bash
git clone https://github.com/mamunctg/nonspeech-sound-classification.git
cd nonspeech-sound-classification
```

## Create environment
- see requirements.txt
### Training and Testing
- Download the dataset from [Nonspeech7k ](https://zenodo.org/record/6967442) and convert it into '.pkl' from the '.wav' format file
- set the local PATH of the dataset to the constants.py file
- run
```
python model_run.py
```

## Citation

If you find this useful for your research, please use the following.


```
@article{rashid2023nonspeech7k,
  title={Nonspeech7k dataset: Classification and analysis of human non-speech sound},
  author={Rashid, Muhammad Mamunur and Li, Guiqing and Du, Chengrui},
  journal={IET Signal Processing},
  volume={17},
  number={6},
  pages={e12233},
  year={2023},
  publisher={Wiley Online Library}
}
```


## Acknowledgments
This code borrows heavily from [Very Deep Convolutional Networks For Raw Waveforms](https://github.com/philipperemy/very-deep-convnets-raw-waveforms).



