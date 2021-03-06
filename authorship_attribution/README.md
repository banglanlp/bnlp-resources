# Authorship Attribution Dataset

The authorship attribution dataset curated from the work of [Bangla Text Classification using Transformers](https://arxiv.org/abs/2011.04446). The dataset is originally hosted on Mendeley: [https://data.mendeley.com/datasets/6d9jrkgtvv/2](https://data.mendeley.com/datasets/6d9jrkgtvv/2).

## Dataset
The dataset contains writings of 14 different authors from an online Bangla e-library (e.g., novels, story, series, etc.).

### Directory Structure:
In the `authorship.tar.gz` file is a zip version of train, dev, and test set of combined dataset.

To unzip the file, use the following command:
```unzip
tar -xvzf authorship.tar.gz

```
- **train.tsv**
- **dev.tsv**
- **test.tsv**

## Licensing
The original dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The *data split version* is licensed under *MIT license*.

## Citation

Please cite the following papers if you are using the data:

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
