# Nonspeech7k dataset: Classification and analysis of human non-speech sound

### [Paper link](https://doi.org/10.1049/sil2.12233) 

### [Nonspeech7k dataset link ](https://zenodo.org/record/6967442)

## Image-to-image translation at 2k/1k resolution
- Our label-to-streetview results
<p align='center'>  
  <img src='imgs/feature.jpg' width='400'/>
  <img src='imgs/teaser_ours.jpg' width='400'/>
</p>

## Prerequisites
- Ubuntu
- Python 3
- NVIDIA GPU (11G memory or larger) 
## Getting Started
## Installation
- Clone this repo:
```bash
git clone https://github.com/mamunctg/nonspeech-sound-classification.git
cd nonspeech-sound-classification
```

## Create environment
- see requirements.txt
## Training and Testing
- Download the dataset from [Nonspeech7k ](https://zenodo.org/record/6967442)
- Convert the sound files into '.pkl' from the '.wav' format file using "process_data.py" for training and testing files separately
- Set the local PATH of the dataset to the "constants.py" file
- Run
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



