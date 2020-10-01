# 👋🛳️ Hello, Welcome the seventh ML Project

This is one of the best newbie challenge/problem that you should be doing to enter into the world of ML.

We will use machine learning/deep learning to create a model that predicts the character of EMNIST (Extened MNIST) dataset.

# Description

# Introduction / The Dataset
The MNIST dataset has become a standard benchmark for learning, classification and computer vision systems. The MNIST database was derived from a larger dataset known as the NIST Special Database 19 which contains digits, uppercase and lowercase handwritten letters. Extended MNIST (EMNIST) follows the same conversion paradigm used to create the MNIST dataset.

EMNIST is categorized into 5 datasets:

<table>
    <!-- Image -->
    <tr><img src="https://i.imgur.com/pIoVt4u.png" /></tr>
    <!-- Content -->
    <tr><p>
    <b>Balanced</b><br>
    The only balanced set of all. Has 47 class containing 10 digits and 37 letters, a cut-down from 52 since some characters (e.g. small i and capital I) have similar form regardless of cases and thus are grouped together.
    </p></tr>
</table>

<table>
    <!-- Image -->
    <tr><img src="https://i.imgur.com/ez89Xyr.png)" /></tr>
    <!-- Content -->
    <tr><p>
    <b>By_Merge</b><br>
    Similar to the above, but has significantly more samples (and also more unbalanced.)
    </p></tr>
</table>

<table>
    <!-- Image -->
    <tr><img src="https://i.imgur.com/Sh2Z2Wn.png" /></tr>
    <!-- Content -->
    <tr><p>
    <b>By_Classes</b><br>
    Similar to the <b>By_Merge</b> set but has more classes due to it being case-sensitive for all 26 letters (raising the total number of letter-related classes to 52.)
    </p></tr>
</table>

<table>
    <!-- Image -->
    <tr><img src="https://i.imgur.com/hQiSXoY.png" /></tr>
    <!-- Content -->
    <tr><p>
    <b>Letters</b><br>
    Contains 26 classes corresponding to 26 letters, case-insensitive.
    </p></tr>
</table>

<table>
    <!-- Image -->
    <tr><img src="https://i.imgur.com/gWzm2OO.png" /></tr>
    <!-- Content -->
    <tr><p>
    <b>Digits</b><br>
    The simplest set of all, similar to the original MNIST.
    </p></tr>
</table>

We only use the **Balanced** dataset in this project for beginner.


<div style="page-break-after: always"></div>

# Practice Skills
1. Using Colab/Kaggle API to handle problem.
2. Computer vision fundamentals including simple deep neural networks.
3. Classification methods such as SVM, Softmax and K-nearest neighbors,...

# Acknowledgements
- EMNIST: Paper ([`arXiv:1702.05373`](https://arxiv.org/abs/1702.05373)) and Kaggle dataset ([`crawford/emnist`](https://www.kaggle.com/crawford/emnist))