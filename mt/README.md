# Machine Translation Dataset

This is a compiled version of machine translation dataset collected from several sources for benchmarking purpose. We provide data splits and benchmark results to compare with any future works.

## Dataset
In the `MT-dataset.tar.gz` file is a zip version of train, dev, and test set of combined dataset.

To unzip the file, use the following command:
```unzip
tar -xvzf MT-dataset.tar.gz
```
#### Combined Datasets Name
* Six Indian Parallel Corpora [7] (SIPC)
* Open Subtitles
* Indic Languages Multilingual Parallel Corpus [8] (ILMPC)
* SUPara Corpus [5, 6]
* AmaderCAT [4]
* Penn Treebank Bangla-English parallel corpus (PTB)
* Global Voices
* Tatoeba
* Tanzil

### Directory structure:
After extracting the zip file, the following directory we have data splits (train/dev/test) for combined dataset.

* MT-dataset/train.bn -- combined all Bangla training data of above mentioned dataset
* MT-dataset/train.en -- combined all English training data of above mentioned dataset
* MT-dataset/dev.bn -- Bangla development set from SUPara dataset
* MT-dataset/dev.en -- English development set from SUPara dataset
* MT-dataset/test.bn -- Bangla test set from SUPara dataset
* MT-dataset/test.en -- English test set from SUPara dataset


## Licensing
This is a compiled version from several datasets. We are releasing it as CC BY-NC-SA 2.0 (https://creativecommons.org/licenses/by-nc-sa/2.0/). However, for the respective data source please check the licence in the corresponding papers or source location.

## Citation
Please cite the following papers if you are using the data:

1. Alam, F., Hasan, M. A., Alam, T., Khan, A., Tajrin, J., Khan, N., & Chowdhury, S. A. (2021). A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models. arXiv preprint arXiv:2107.03844.
2. Hasan, M. A., Alam, F., Chowdhury, S. A., & Khan, N. (2019, December). Neural machine translation for the Bangla-English language pair. In 2019 22nd International Conference on Computer and Information Technology (ICCIT) (pp. 1-6). IEEE.
3. Hasan, M. A., Alam, F., Chowdhury, S. A., & Khan, N. (2019, September). Neural vs statistical machine translation: Revisiting the bangla-english language pair. In 2019 International Conference on Bangla Speech and Language Processing (ICBSLP) (pp. 1-5). IEEE.
4. Hasan, M. A., Alam, F., & Noori, S. R. H. (2020). A collaborative platform to collect data for developing machine translation systems. In Proceedings of International Joint Conference on Computational Intelligence (pp. 407-416). Springer, Singapore.
5. M. A. Al Mumin, M. H. Seddiqui, M. Z. Iqbal, and M. J.Islam, “Supara0.8m: A balanced english-bangla parallel corpus,” 2018.[Online]. Available: http://dx.doi.org/10.21227/gz0b-5p24
6. M. A. Al Mumin, S. M. H., M. Z. Iqbal, and M. J. Islam,“Supara-benchmark: A benchmark dataset for english-bangla machinetranslation,” 2018. [Online]. Available: http://dx.doi.org/10.21227/czes-gs42
7. M. Post, C. Callison-Burch, and M. Osborne, “Constructing parallelcorpora for six indian languages via crowdsourcing,” inProc. of the 7thWSMT. ACL, 2012, pp. 401–409
8. T. Nakazawa, S. Kurohashi, S. Higashiyama, C. Ding, R. Dabre,H. Mino, I. Goto, W. P. Pa, A. Kunchukuttanand, and S. Kurohashi,“Overview of the 5th Workshop on Asian Translation,” Tech. Rep.,2018. [Online]. Available: http://www2.nict.go.jp/astrec-att/


```bib
@article{alam2021review,
  title={A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models},
  author={Alam, Firoj and Hasan, Md Arid and Alam, Tanvir and Khan, Akib and Tajrin, Janntatul and Khan, Naira and Chowdhury, Shammur Absar},
  journal={arXiv preprint arXiv:2107.03844},
  year={2021}
}
@inproceedings{hasan2019neural,
  title={Neural machine translation for the Bangla-English language pair},
  author={Hasan, Md Arid and Alam, Firoj and Chowdhury, Shammur Absar and Khan, Naira},
  booktitle={2019 22nd International Conference on Computer and Information Technology (ICCIT)},
  pages={1--6},
  year={2019},
  organization={IEEE}
}
@inproceedings{hasan2019neural_b,
  title={Neural vs statistical machine translation: Revisiting the bangla-english language pair},
  author={Hasan, Md Arid and Alam, Firoj and Chowdhury, Shammur Absar and Khan, Naira},
  booktitle={2019 International Conference on Bangla Speech and Language Processing (ICBSLP)},
  pages={1--5},
  year={2019},
  organization={IEEE}
}
@inproceedings{hasan2020collaborative,
  title={A collaborative platform to collect data for developing machine translation systems},
  author={Hasan, Md Arid and Alam, Firoj and Noori, Sheak Rashed Haider},
  booktitle={Proceedings of International Joint Conference on Computational Intelligence},
  pages={407--416},
  year={2020},
  organization={Springer}
}
@data{al2018suparaBenchmark,
    doi = {10.21227/czes-gs42},
    url = {http://dx.doi.org/10.21227/czes-gs42},
    author = {Al Mumin, Md Abdullah and M. H., Seddiqui and Iqbal, M Zafar and M. J. Islam },
    publisher = {IEEE Dataport},
    title = {SUPara-Benchmark: A Benchmark Dataset for English-Bangla Machine Translation},
    year = {2018}
}
@data{al2018suparaLatest,
    doi = {10.21227/gz0b-5p24},
    url = {http://dx.doi.org/10.21227/gz0b-5p24},
    author = {Al Mumin, Md Abdullah and M. H. Seddiqui and Iqbal, M Zafar and M. J. Islam },
    publisher = {IEEE Dataport},
    title = {SUPara0.8M: A Balanced English-Bangla Parallel Corpus},
    year = {2018}
}

@inproceedings{post2012constructing,
  title={Constructing parallel corpora for six indian languages via crowdsourcing},
  author={Post, Matt and Callison-Burch, Chris and Osborne, Miles},
  booktitle={Proc. of the 7th WSMT},
  pages={401--409},
  year={2012},
  organization={ACL}
}

@techreport{Nakazawa2018,
    title = {{Overview of the 5th Workshop on Asian Translation}},
    author={Nakazawa, Toshiaki and Kurohashi, Sadao and Higashiyama, Shohei and Ding, Chenchen and Dabre, Raj and Mino, Hideya and Goto, Isao and Pa, Win Pa and Kunchukuttanand, Anoop and  Kurohashi, Sadao },
    url = {http://www2.nict.go.jp/astrec-att/},
    year={2018}
}

```
