# Bangla Sentiment Classification Datasets

To obtain the compiled version of sentiment analysis dataset collected from several sources for benchmarking purpose. For this work, we curated the dataset from the work of [https://github.com/banglanlp/bangla-sentiment-classification](https://github.com/banglanlp/bangla-sentiment-classification).

## Dataset

### Directory structure:
In the following directories we have data splits (train/dev/test) for different datasets.

* ABSA_datasets -- This dataset has developed to per­form aspect ­based sentiment analysis task in Bangla.
  - License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* SAIL_data -- This dataset, consists of tweet posts, has developed in the Shared task on Sentiment Analysis in Indian Languages (SAIL) 2015. [2]
  - License: [Non-profit](http://amitavadas.com/SAIL/)
* multichannel_bsentiment -- This data was collected from several newspapers, TV news, books, blogs, and social me­dia.
  - License: [NA](https://github.com/rezacsedu/Classification_Benchmarks_Benglai_NLP)
  (N.B.: We have the permission to share this dataset.)
* youtube_sentiment -- This dataset was devel­oped by extracting comments from various YouTube videos.
  - License: [NA](https://www.kaggle.com/nit003/bangla-youtube-sentiment-and-emotion-datasets)
<!-- * consolidated -- all combined dataset from the above data splits -->
* **Note:** Due to the license limitation we are not able to release CogniSenti Dataset.


## Licensing

Our work is licensed under https://creativecommons.org/licenses/by-nc/4.0/. However, for each dataset, please see the license information associated with it. Any private dataset can be accessed by contacting with the respective authors.


## Citation

Please cite the following papers if you are using the data:

1. Alam, F., Hasan, M. A., Alam, T., Khan, A., Tajrin, J., Khan, N., & Chowdhury, S. A. (2021). A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models. arXiv preprint arXiv:2107.03844.
2. Md. Arid Hasan and Jannatul Tajrin and Shammur Absar Chowdhury and Firoj Alam, "Sentiment Classification in Bangla Textual Content: A Comparative Study", 23rd International Conference on Computer and Information Technology (ICCIT), 2020.
3. B. G. Patra, D. Das, A. Das, and R. Prasath, Shared task on sentiment analysis in Indian languages (sail) tweets­ an overview, in Proc. of MIKE. Springer, 2015, pp. 650–655.
4. M. Rahman, E. Kumar Dey et al., Datasets for aspect­based sentiment analysis in Bangla and its baseline evaluation, Data, vol. 3, no. 2, p. 15, 2018.
5. N. I. Tripto and M. E. Ali, Detecting multilabel sentiment and emotions from Bangla youtube comments, in Proc. of ICBSLP. IEEE, 2018, pp. 1–6.
6. M. Rezaul Karim, B. Raja Chakravarthi, M. Arcan, J. P. McCrae, and M. Cochez, Classification benchmarks for under­-resourced Bengali language based on multichannel convolutional­ LSTM network, arXiv, pp. arXiv–2004, 2020.

```
@article{alam2021review,
  title={A Review of Bangla Natural Language Processing Tasks and the Utility of Transformer Models},
  author={Alam, Firoj and Hasan, Md Arid and Alam, Tanvir and Khan, Akib and Tajrin, Janntatul and Khan, Naira and Chowdhury, Shammur Absar},
  journal={arXiv preprint arXiv:2107.03844},
  year={2021}
}
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
