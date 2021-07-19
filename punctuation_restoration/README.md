# Punctuation Restoration Dataset

We used the dataset reported in in the work of [Punctuation Restoration using Transformer Models for High-and Low-Resource Languages](http://noisy-text.github.io/2020/pdf/2020.d200-1.18.pdf). Please also check the git repo for the experimental scripts: [https://github.com/xashru/punctuation-restoration](https://github.com/xashru/punctuation-restoration).

## Dataset
The dataset consists of train, development, and test splits prepared from a publicly available corpus of Bangla newspaper articles. Additionally, the authors prepared two test datasets from manual and ASR transcribed texts. These were collected from 65 minutes of speech excerpts extracted from four Bangla short stories. There are four labels including three punctuation marks: (i) Comma: includes commas, colons and dashes, (ii) Period: includes full stops, exclamation marks and semicolons, (iii) Question: only question mark, and (iv) O: for any other token.

### Directory Structure:

* **train:** *training* newspapers articles
* **dev:** *development* newspapers articles
* **test_news:** newspapers articles
* **test_ref:** manual transcription
* **test_asr:** ASR transcription
* **test_bn.txt:**



## Licensing

The dataset is released under *MIT License*.


## Citation

```
@article{alam2021review,
  title={A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models},
  author={Alam, Firoj and Hasan, Md Arid and Alam, Tanvir and Khan, Akib and Tajrin, Janntatul and Khan, Naira and Chowdhury, Shammur Absar},
  journal={arXiv preprint arXiv:2107.03844},
  year={2021}
}

@inproceedings{alam-etal-2020-punctuation,
    title = "Punctuation Restoration using Transformer Models for High-and Low-Resource Languages",
    author = "Alam, Tanvirul  and Khan, Akib  and Alam, Firoj",
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
