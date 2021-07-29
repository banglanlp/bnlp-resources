# Resources for Bangla Natural Language Processing (BanglaNLP)

This repository contains available datasets for nine notable Bangla Natural Language Processing tasks: (i) POS tagging, (ii) lemmatization, (iii) NER, (iv) punctuation restoration, (v) MT, (vi) sentiment classification, (vii) emotion classification, (viii) authorship attribution, and (ix) news categorization.
For each task, we curated labeled datasets from different tasks, split them for training, development and evaluation. The purpose was to create benchmarks and facilitate reproducing the results. The compilation of the datasets is the results of the work of the paper [[A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models](https://arxiv.org/pdf/2107.03844.pdf)]. Please see below a brief summary of the work and major contributions.

__Table of contents:__
- [Datasets](dataset)
  - [Parts of Speech](pos)  
  - [Lemmatization](lemma)
  - [Named Entity Recognition](ner)
  - [Punctuation Restoration](punctuation_restoration)  
  - [Machine Translation](mt)
  - [Sentiment Classification](sentiment)
  - [Emotion Classification](emotion)
  - [Authorship Attribution](authorship_attribution)
  - [News Categorization](news_categorization)    
- [A brief summary of the work](#a-brief-summary-of-the-work)
- [Licensing](#licensing)
- [Citation](#citation)
  - [Parts of Speech](#parts-of-Speech)
  - [Lemmatization](#lemmatization)  
  - [Named Entity Recognition](#named-entity-recognition)
  - [Punctuation Restoration](#punctuation-restoration)
  - [Machine Translation](#machine-translation)
  - [Sentiment Classification](#sentiment-classification)
  - [Emotion Classification](#emotion-classification)
  - [Authorship Attribution](#authorship-attribution)
  - [News Categorization](#news-categorization)

## Datasets:
Below we provide a summary of the datasets. Note that for some datasets, we did not find license information, hence, it is reported as NA. <span style="color:red">We are in contact with the authors to see if we can get more clear information about license information</span>


## A brief summary of the work:

#### Brief summary
In our work [[A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models](https://arxiv.org/pdf/2107.03844.pdf)], we provide a review of Bangla NLP tasks, resources, and tools available to the research community; we benchmark datasets collected from various platforms for nine NLP tasks using current state-of-the-art algorithms (i.e., transformer-based models). We provide comparative results for the studied NLP tasks by comparing monolingual vs. multilingual models of varying sizes. We report our results using both individual and consolidated datasets and provide data splits for future research. We reviewed a total of 108 papers and conducted 175 sets of experiments. Our results show promising performance using transformer-based models while highlighting the trade-off with computational costs. We hope that such a comprehensive survey will motivate the community to build on and further advance the research on Bangla NLP.

#### Major contributions:

  - We provide a detailed survey on the most notable NLP tasks by reviewing 108 papers.
  - We benchmark different (nine) tasks with experimental results using nine different transformer models,(for MT we use one pre-trained transformer model) which resulted in 175 sets of experiments.
  - We provide comparative results for different transformer models comparing 
   - (1) models' size (large vs. small) and 
   - (2) style (mono vs. multilingual models).
  - We also report comparative results for individual vs. consolidated datasets, when multiple data source is available.
  - We analyze the trade-off between performance and computational complexity between the transformer-based and classical approaches like SVM.
  - We provide a concrete future direction for the community answering to questions like: (1) what resources are available? (2) the challenges? and (3) what can be done?
  - We provide data splits for reproducibility and future research. Note that we could only provide and share data splits, which were publicly accessible.

## Licensing

Our work is licensed under https://creativecommons.org/licenses/by-nc/4.0/. However, for each dataset, please see the license information associated with it. Any private dataset can be accessed by contacting with the respective authors.


## Citation
Please cite the following papers if you are using the data splits. If you use any task specific dataset, please make sure you cite the original paper.


```
@article{alam2021review,
  title={A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models},
  author={Alam, Firoj and Hasan, Md Arid and Alam, Tanvir and Khan, Akib and Tajrin, Janntatul and Khan, Naira and Chowdhury, Shammur Absar},
  journal={arXiv preprint arXiv:2107.03844},
  year={2021}
}
```

### [Parts of Speech](pos)

```
@inproceedings{alam2016bidirectional,
  title={Bidirectional LSTMs—CRFs networks for bangla POS tagging},
  author={Alam, Firoj and Chowdhury, Shammur Absar and Noori, Sheak Rashed Haider},
  booktitle={19th International Conference on Computer and Information Technology (ICCIT), 2016},
  pages={377--382},
  year={2016},
  organization={IEEE}
}
```

### [Lemmatization](lemma)

```
@inproceedings{chakrabarty-etal-2017-context,
 address = {Vancouver, Canada},
 author = {Chakrabarty, Abhisek  and Pandit, Onkar Arun  and Garain, Utpal},
 booktitle = {Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics},
 doi = {10.18653/v1/P17-1136},
 pages = {1481--1491},
 publisher = {Association for Computational Linguistics},
 title = {Context Sensitive Lemmatization Using Two Successive Bidirectional Gated Recurrent Networks},
 url = {https://www.aclweb.org/anthology/P17-1136},
 year = {2017}
}
```

### [Named Entity Recognition](ner)

```
@inproceedings{chowdhury2018towards,
 author = {Chowdhury, Shammur Absar and Alam, Firoj and Khan, Naira},
 booktitle = {2018 21st International Conference of Computer and Information Technology (ICCIT)},
 organization = {IEEE},
 pages = {1--7},
 title = {Towards Bangla named entity recognition},
 year = {2018}
}
```

### [Punctuation Restoration](punctuation_restoration)

```
@inproceedings{alam-etal-2020-punctuation,
    title = "Punctuation Restoration using Transformer Models for High-and Low-Resource Languages",
    author = "Alam, Tanvirul  and
      Khan, Akib  and
      Alam, Firoj",
    booktitle = "Proceedings of the Sixth Workshop on Noisy User-generated Text (W-NUT 2020)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.wnut-1.18",
    pages = "132--142",
}
@article{DBLP:journals/corr/abs-1911-07613,
 archiveprefix = {arXiv},
 author = {Aisha Khatun and
Anisur Rahman and
Hemayet Ahmed Chowdhury and
Md. Saiful Islam and
Ayesha Tasnim},
 bibsource = {dblp computer science bibliography, https://dblp.org},
 biburl = {https://dblp.org/rec/journals/corr/abs-1911-07613.bib},
 eprint = {1911.07613},
 journal = {CoRR},
 timestamp = {Mon, 02 Dec 2019 17:48:37 +0100},
 title = {A Subword Level Language Model for Bangla Language},
 url = {http://arxiv.org/abs/1911.07613},
 volume = {abs/1911.07613},
 year = {2019}
}
```

### [Machine Translation](mt)

```
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

### [Sentiment Classification](sentiment)

```
@inproceedings{iccit2020Arid,
	Author = {Md. Arid Hasan and Jannatul Tajrin and Shammur Absar Chowdhury and Firoj Alam},
	Booktitle = {23rd International Conference on Computer and Information Technology (ICCIT)},
	Month = {December},
	Title = {Sentiment Classification in Bangla Textual Content: A Comparative Study},
	Year = {2020}
}
@inproceedings{patra2015shared,
  title={Shared task on sentiment analysis in indian languages (sail) tweets-an overview},
  author={Patra, Braja Gopal and Das, Dipankar and Das, Amitava and Prasath, Rajendra},
  booktitle={Proc. of MIKE},
  pages={650--655},
  year={2015},
  organization={Springer}
}

@article{rahman2018datasets,
  title={Datasets for aspect-based sentiment analysis in bangla and its baseline evaluation},
  author={Rahman, Md and Kumar Dey, Emon and others},
  journal={Data},
  volume={3},
  number={2},
  pages={15},
  year={2018},
  publisher={Multidisciplinary Digital Publishing Institute}
}

@article{rezaul2020classification,
  title={Classification Benchmarks for Under-resourced {Bengali} Language based on Multichannel Convolutional-LSTM Network},
  author={Rezaul Karim, Md and Raja Chakravarthi, Bharathi and Arcan, Mihael and McCrae, John P and Cochez, Michael},
  journal={arXiv},
  pages={arXiv--2004},
  year={2020}
}
@inproceedings{tripto2018detecting,
  title={Detecting Multilabel Sentiment and Emotions from Bangla YouTube Comments},
  author={Tripto, Nafis Irtiza and Ali, Mohammed Eunus},
  booktitle={Proc. of ICBSLP},
  pages={1--6},
  year={2018},
  organization={IEEE}
}
```

### [Emotion Classification](emotion)

```
@article{alam2020bangla,
 author = {Alam, Tanvirul and Khan, Akib and Alam, Firoj},
 journal = {arXiv preprint arXiv:2011.04446},
 title = {Bangla Text Classification using Transformers},
 year = {2020}
}
@inproceedings{tripto2018detecting,
 author = {Tripto, Nafis Irtiza and Ali, Mohammed Eunus},
 booktitle = {2018 International Conference on Bangla Speech and Language Processing (ICBSLP)},
 organization = {IEEE},
 pages = {1--6},
 title = {Detecting multilabel sentiment and emotions from {B}angla youtube comments},
 year = {2018}
}
```

### [Authorship Attribution](authorship_attribution)

```
@article{alam2020bangla,
  title={Bangla Text Classification using Transformers},
  author={Alam, Tanvirul and Khan, Akib and Alam, Firoj},
  journal={arXiv preprint arXiv:2011.04446},
  year={2020}
}
@inproceedings{khatun2019authorship,
 author = {Khatun, Aisha and Rahman, Anisur and Islam, Md Saiful and others},
 booktitle = {2019 22nd International Conference on Computer and Information Technology (ICCIT)},
 organization = {IEEE},
 pages = {1--5},
 title = {Authorship Attribution in Bangla literature using Character-level {CNN}},
 year = {2019}
}
```

### [News Categorization](news_categorization)

```
@article{alam2020bangla,
  title={Bangla Text Classification using Transformers},
  author={Alam, Tanvirul and Khan, Akib and Alam, Firoj},
  journal={arXiv preprint arXiv:2011.04446},
  year={2020}
}
@article{kunchukuttan2020ai4bharat,
 author = {Anoop Kunchukuttan and Divyanshu Kakwani and Satish Golla and Gokul N.C. and Avik Bhattacharyya and Mitesh M. Khapra and Pratyush Kumar},
 journal = {arXiv preprint arXiv:2005.00085},
 title = {AI4Bharat-IndicNLP Corpus: Monolingual Corpora and Word Embeddings for Indic Languages},
 year = {2020}
}
```
