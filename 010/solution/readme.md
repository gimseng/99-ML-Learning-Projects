# Solution for EMNIST handwriting character recognition

## Software stack
- Language: Python3
- External libraries:
    - Data processing and storage: **NumPy**, **Pandas**
    - Plotting: **MatPlotLib**
    - Model building/training: **scikit-learn**, **Keras**
- IDE: Google Colab
- Dataset: EMNIST (Balanced variant, 47 classes)

## Abstract
This solution presents 3 models (Vanilla CNN, LeNet-5 modified and ResNet) to solve the problem of handwritten character classification with the EMNIST dataset. Some attempts, with the help from a combination of research papers and our personal experiences/insights, were made at improving the performance of said models, including modified preprocessing pipeline and additional layers in the network architecture. Basic methods such as confusion matrix and plot of accuracy through time was used to assess the performance of said models, with the accuracy of Vanilla CNN, LeNet-5 and ResNet being 88.25%, 89.61% and 82.60% respectively. While this might not (and cannot) be the state-of-the-art solution in its domain, it gave us the initial cursory knowledge with a prompt to research deeper in the future.

**Keywords**: `EMNIST`; `Neural Network`; `Classification`; `CNN (Convolutional Neural Network)`; `LeNet5`; `ResNet (Residual Neural Network)`

<div style="page-break-after: always"></div>

# Quick start

All of our stuff (Colab notebooks, images and raw videos) are located [**HERE**](https://drive.google.com/drive/folders/1G63_0KDMSYSMMl10mrKoBT6I-QgigKzx) (Google Drive).

Our quick demonstration video is available [**HERE**](https://youtu.be/-sTUVeDd3Lw) (YouTube, 4 mins)

1. **Prepare Kaggle token**
   Prepare your own Kaggle token (sign up for an account if needed). This is required for downloading the EMNIST dataset from Kaggle.
   
2. **Open a notebook and check the settings**
   Make sure the runtime type is GPU-accelerated (go to `Runtime` menu, then choose `Change runtime type`.)
   
3. **Upload the token and download dataset**
   After waiting for the runtime to completely spin up...
   - (Optional) Check if the current working directory is `/content`. This should be the default upon runtime initialization. If necessary, run `!pwd` to check.
   - Upload the token (whose file name should be `kaggle.json`) to `/content` 
   - Copy the code block from `Step 0a` into a new code block and run that
       - This is a workaround, since we have the tendency to restart the whole notebook for "clean" debugging (no leftovers from Python runtime) and downloading + unpacking the dataset from scratch is quite inconvenient.
   
   After all the above steps, the current directory should be populated with files from the dataset.
   
4. **Run the remaining of the notebook**
   Move to the next cell (right below the one created in step 4) then hit <kbd>Ctrl</kbd> + <kbd>F10</kbd>

<div style="page-break-after: always"></div>

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

We only use the **Balanced** dataset in this project.


<div style="page-break-after: always"></div>

# Structures
We approached this problem with 3 different solutions:



## Preprocessing

With the exception of LeNet, the following approaches have similar preprocessing steps as the following list lays out:
- Load dataset
- Apply basic transformations to correct image orientations and normalize them
- One-hot encoding: create label sets from mapping file
- Flip image:
    - Dataset has a format of nonsense:
    ![](https://i.imgur.com/BUC7Web.png)
    - After flip and rotate:
    ![](https://i.imgur.com/HFO3qkU.png)

- Reshaping images to their actual size + spliting train/test



## Vanilla CNN (Convolutional Neural Network)

CNN image classifications takes an input image ($28 \times 28$), process it and classify it under certain categories ($47$).
These step is pass by a architecture concept:

<figure>
    <img style="display: block; margin: 0 auto;" alt="acc_epoch_graph" src="https://i.imgur.com/b9O6Jov.png" />
    <figcaption style="text-align: center; font-style: italic;">Neural network with many convolutional layers</figcaption>
</figure>



There are many of popular CNN architectures such as LeNet, AlexNet, VGGNet, ResNet,... with a spirit of learning, we firstly using Vanilla CNN to solve the problem of EMNIST dataset classification.

In our approach, we add a Dropout layer in between 2 Fully Connected layers to reduce number of parammeters. By the way, these is a thread said that do not use dropout in CNN network[^3], but it is for the mordern CNN, when they don't use 2 Dense layer at the end for classification anymore. So, the Dropout will work in this situation. Here's our network structure:

- 2 layers of Conv2D w/ ReLU + MaxPool
- Flattener
- Dense network w/ ReLU
- Dropout (randomly drop nodes from the network above) -- to prevent overfitting
- Dense network w/ softmax


> [Features Engineering]: Two conolutional layers for features extraction, one for low features and one for higher features. The the image flattened, but it keep the infomation from each pixel nearby because after features extraction, these pixel is keep after Conv layers. MaxPooling block is used for 2 reasons: Reduces the dimension of data (H $\times$ W $\times$ F) (with $F$ is a number of filters) to smaller dimension and keep the rotation/shifting information of that image (If another image is a shifted version of that image, it can reconize by MaxPooling block because the MaxPool when rotating,shifting is the same).

> [Classification]: Using 2 Dense nets with first layer is a non-linear function for remove clearly noise after feature extraction, the second layer with softmax activation function for classification our classes. 

Here's the model summary:
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 28, 28, 128)       3328      
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 14, 14, 128)       0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 14, 14, 64)        73792     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 7, 7, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 3136)              0         
_________________________________________________________________
dense (Dense)                (None, 128)               401536    
_________________________________________________________________
dropout (Dropout)            (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 47)                6063      
=================================================================
Total params: 484,719
Trainable params: 484,719
Non-trainable params: 0
```



## LeNet-5

After a bunch of (wasted) time, our team had to come up with some different approaches to get better performance. LeNet was the first that we took a look at.

> The LeNet-5[^1] means the emergence of CNN and defines the basic components of CNN. But it was not popular at that time because of the lack of hardware equipment, especially GPU(Graphics Processing Unit, a specialized electronic circuit designed to rapidly manipulate and alter memory to accelerate the creation of images in a frame buffer intended for output to a display device) and other algorithm, such as SVM can achieve similar effects or even exceed the LeNet.

LeNet is a Convolutional Neural Network comprising of 7 layers:
<img style="align: center" alt="lenet_arch" src="https://i.imgur.com/hQ4bVlq.png" />

LeNet-5 get input of 32 $\times$ 32 image to shift it to center of the image by pading 2 pixel each side in preprocessing step.
From LeNet-5 implemented model from scratch[^2] with 99.05% accuracy in MNIST dataset. We soft reduce the preprocessing step (because with the preprocessing step - the accuracy in EMNIST is not better than our CNN model). Follow this model improvement with 99.62% accuracy in MNIST dataset, resize the input to 28 $\times$ 28 and change the last Dense (Fully Connected Layer) to 47 classes (fit for EMNIST's numclasses). There is the final architecture:

```
# Feature Engineering
ConvNet --> ConvNet --> BatchNorm --> Pool --> (Dropout) --> 
ConvNet --> ConvNet --> BatchNorm --> Pool --> (Dropout) --> 
#Classification
(Flatten) --> FullyConnected --> BatchNorm --> FullyConnected --> 
BatchNorm --> FullyConnected --> BatchNorm --> (Dropout) --> 
Softmax
```
Hence, adding BatchNorm with Dropout(0.25) to make model converge faster than normal. L2 regularization to reduce the parameters of model.

Here's the model summary for LeNet-5 version 2 (LeNet5v2):
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
convolution_1 (Conv2D)       (None, 24, 24, 32)        832       
_________________________________________________________________
convolution_2 (Conv2D)       (None, 20, 20, 32)        25600     
_________________________________________________________________
batchnorm_1 (BatchNormalizat (None, 20, 20, 32)        128       
_________________________________________________________________
activation (Activation)      (None, 20, 20, 32)        0         
_________________________________________________________________
max_pool_1 (MaxPooling2D)    (None, 10, 10, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 10, 10, 32)        0         
_________________________________________________________________
convolution_3 (Conv2D)       (None, 8, 8, 64)          18496     
_________________________________________________________________
convolution_4 (Conv2D)       (None, 6, 6, 64)          36864     
_________________________________________________________________
batchnorm_2 (BatchNormalizat (None, 6, 6, 64)          256       
_________________________________________________________________
activation_1 (Activation)    (None, 6, 6, 64)          0         
_________________________________________________________________
max_pool_2 (MaxPooling2D)    (None, 3, 3, 64)          0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 3, 3, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 576)               0         
_________________________________________________________________
fully_connected_1 (Dense)    (None, 256)               147456    
_________________________________________________________________
batchnorm_3 (BatchNormalizat (None, 256)               1024      
_________________________________________________________________
activation_2 (Activation)    (None, 256)               0         
_________________________________________________________________
fully_connected_2 (Dense)    (None, 128)               32768     
_________________________________________________________________
batchnorm_4 (BatchNormalizat (None, 128)               512       
_________________________________________________________________
activation_3 (Activation)    (None, 128)               0         
_________________________________________________________________
fully_connected_3 (Dense)    (None, 84)                10752     
_________________________________________________________________
batchnorm_5 (BatchNormalizat (None, 84)                336       
_________________________________________________________________
activation_4 (Activation)    (None, 84)                0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 84)                0         
_________________________________________________________________
output (Dense)               (None, 47)                3995      
=================================================================
Total params: 279,019
Trainable params: 277,891
Non-trainable params: 1,128
```

<figure>
    <img style="display: block; margin: 0 auto;" alt="acc_epoch_graph" src="https://i.imgur.com/OpcA8BO.png" />
    <figcaption style="text-align: center; font-style: italic;">Accuraccy and epoch graph through time</figcaption>
</figure>



## ResNet (Residual Neural Network)
- The last model we choose to implement is ResNet. For some experiment in practical result, we have a conclusion that ResNet have some advantages of classification image
|![](https://i.imgur.com/q2qqLcX.png)|
|------------------------------------|
|Practical result                    |

- ResNet has a defining characteristic of **Residual Block** structures:

<figure>
    <img style="display: block; margin: 0 auto;" alt="resnet34_block" src="https://i.imgur.com/z25xhuF.png" />
    <figcaption style="text-align: center; font-style: italic;">Residual Block shortcut</figcaption>
</figure>




- This special structure allow ResNet to learn more deeply without some problem which we usually encounter such as Vanishing Gradient,... This structure have a similar aspect to LSTM (Long-short term memory), which also use a shortcut to connect from node to node.
- ResNet's classes categorize base on figure of layer in network. A simple config structure of ResNet is described:

<figure>
    <img style="display: block; margin: 0 auto;" alt="resnet_config" src="https://i.imgur.com/F3wZmKh.png" />
    <figcaption style="text-align: center; font-style: italic;">ResNet variants</figcaption>
</figure>


- We implement version ResNet34, which will suitable for the solution. Model isn't too deep, and it's deep enough to solve the problem.
- From the above configuration, we can implement the flow of ResNet34
<figure>
    <img style="display: block; margin: 0 auto;" alt="resnet_34_vs_plain" src="https://i.imgur.com/OHHvsxW.png" />
    <figcaption style="text-align: center; font-style: italic;">ResNet-34 Layer</figcaption>
</figure>


- Here is ResNet34's Residual Block:
<figure>
    <img style="display: block; margin: 0 auto;" alt="resnet_config" src="https://i.imgur.com/qcFVH5v.png" />
    <figcaption style="text-align: center; font-style: italic;">ResNet-34 Residual Block</figcaption>
</figure>


- A shortcut block input and output is changeable according to block's input and output:
    - If input's size equal to output's size of block, shortcut will serve to constantly block's input to block's output.
    - Else, input must be downsampling, due to the feature extraction of block. 
    - We can modify downsampling's case base on **`stride`** hyperparameter.
- ResNet-34 summary : 
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_7 (InputLayer)         [(None, 28, 28, 1)]       0         
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 14, 14, 64)        3200      
_________________________________________________________________
batch_normalization_6 (Batch (None, 14, 14, 64)        256       
_________________________________________________________________
re_lu_6 (ReLU)               (None, 14, 14, 64)        0         
_________________________________________________________________
max_pooling2d_6 (MaxPooling2 (None, 6, 6, 64)          0         
_________________________________________________________________
residual_block_96 (ResidualB (None, 6, 6, 64)          74368     
_________________________________________________________________
residual_block_97 (ResidualB (None, 6, 6, 64)          74368     
_________________________________________________________________
residual_block_98 (ResidualB (None, 6, 6, 64)          74368     
_________________________________________________________________
residual_block_99 (ResidualB (None, 3, 3, 128)         231296    
_________________________________________________________________
residual_block_100 (Residual (None, 3, 3, 128)         296192    
_________________________________________________________________
residual_block_101 (Residual (None, 3, 3, 128)         296192    
_________________________________________________________________
residual_block_102 (Residual (None, 3, 3, 128)         296192    
_________________________________________________________________
residual_block_103 (Residual (None, 2, 2, 256)         921344    
_________________________________________________________________
residual_block_104 (Residual (None, 2, 2, 256)         1182208   
_________________________________________________________________
residual_block_105 (Residual (None, 2, 2, 256)         1182208   
_________________________________________________________________
residual_block_106 (Residual (None, 2, 2, 256)         1182208   
_________________________________________________________________
residual_block_107 (Residual (None, 2, 2, 256)         1182208   
_________________________________________________________________
residual_block_108 (Residual (None, 2, 2, 256)         1182208   
_________________________________________________________________
residual_block_109 (Residual (None, 1, 1, 512)         3677696   
_________________________________________________________________
residual_block_110 (Residual (None, 1, 1, 512)         4723712   
_________________________________________________________________
residual_block_111 (Residual (None, 1, 1, 512)         4723712   
_________________________________________________________________
global_average_pooling2d_6 ( (None, 512)               0         
_________________________________________________________________
dense_6 (Dense)              (None, 47)                24111     
=================================================================
Total params: 21,328,047
Trainable params: 21,311,023
Non-trainable params: 17,024
_________________________________________________________________
```
![](https://i.imgur.com/gCrljg5.png)
![](https://i.imgur.com/KbcNscy.png)



<div style="page-break-after: always"></div>



# Experiment Results



## CNN

We tested with two optimizers: Adam and its "improved" variant AdaMax (and also Adadelta, just because it's also one of the relevant optimizer we found at the time while browsing the documentations for `tf.keras.optimizers`), and here's the following loss/accuracy results on models built with a limited number of permutations on three hyperparameters: batch size, epoch and dropout rate.

| Optimizer | Batch size | Epoch | Dropout | Loss   | Accuracy |
| --------- | ---------- | ----- | ------- | ------ | -------- |
| adam      | 512        | 10    | 0.5     | 0.3617 | 0.8770   |
| adam      | 512        | 10    | 0.2     | 0.3569 | 0.8779   |
| adam      | 512        | 20    | 0.5     | 0.3474 | 0.8825   |
| adam      | 512        | 20    | 0.2     | 0.3885 | 0.8782   |
| adam      | 1024       | 10    | 0.5     | 0.3749 | 0.8700   |
| adam      | 1024       | 10    | 0.2     | 0.3620 | 0.8753   |
| adam      | 1024       | 20    | 0.5     | 0.3691 | 0.8724   |
| adam      | 1024       | 20    | 0.2     | 0.3636 | 0.8801   |
| adamax    | 512        | 20    | 0.5     | 0.3663 | 0.8735   |
| adamax    | 512        | 20    | 0.2     | 0.3649 | 0.8777   |
| adamax    | 1024       | 20    | 0.5     | 0.3861 | 0.8675   |
| adamax    | 1024       | 20    | 0.2     | 0.3783 | 0.8705   |
| adadelta  | 512        | 20    | 0.5     | 3.7389 | 0.1439   |

Apart from `adadelta`, which is obviously slow to converge, there's not enough difference between `adam` and `adamax` in terms of which one performs better over what condition. We achieved the highest accuracy of 88.25% with the hyperparameter combination (512, 20, 0.5).



## LeNet-5

| Version                  | Epoch | Accuracy |
| ------------------------ | ----- | -------- |
| LeNet-5                  | 100   | 0.8625   |
| LeNet-5 v2 (input 32x32) | 100   | 0.8646   |
| LeNet-5 v2 (input 28x28) | 100   | 0.8961   |

<figure>
    <img style="display: block; margin: 0 auto;" alt="confusion_matrix" src="https://i.imgur.com/5YQGTtJ.png" />
    <figcaption style="text-align: center; font-style: italic;">Confusion matrix after predict</figcaption>
</figure>


In this model, the highest error in prediction label are the letters `f` (small) and `F` (capital), with 169 (for `f`) and 106 (for `F`) incorrect predictions.





**A copy of all the images incorrectly predicted is available [here](https://drive.google.com/drive/folders/1L7lzbwIDfOySRlZFcIMsVlu7NAm7vRP2) (Google Drive).**



## ResNet34

| Version          |Batch size| Epoch | Accuracy |Val_Accuracy| Loss |
| -----------------|--------- | ----- | -------- | -----------|------|
| ResNet34         |    64    | 30    | 0.9861   |   0.8260   |0.0940|

We choose the best hyperparameter for this conclusion. Practically, the model missclassified some class which we also find it obstacle to discriminate:




Above is some of case that model is missunderstand due to some ambigous pattern

<figure>
    <img style="display: block; margin: 0 auto;" alt="confusion_matrix" src="https://i.imgur.com/YASCwPl.png" />
    <figcaption style="text-align: center; font-style: italic;">Confusion matrix after predict</figcaption>
</figure>

**A copy of all the images incorrectly predicted is available [here](https://drive.google.com/drive/folders/1zVuEFsuarj0ES7gXqnypjeUIjzQL4mVQ) (Google Drive).**

<div style="page-break-after: always"></div>

# Conclusion
For some practical result that we have mention above, it leads us to following conclusion:
- A model not always better than others for every datasets. As we mention above, ResNet have a particular structure that allow ResNet can learn data more deeply. 
- We has summarized the model's parameter. We can easily see that ResNet34 has the largest figure of parameter, we can expect ResNet has the more possitive result than the others. The practical experiment show that ResNet34 decribes the dataset more efficent, but the validation accuracy not better than LeNet5.
- At the end, deep model is not clearly good for simple problem. And sometimes simple model like Vanilla CNN can work with acecptable performace (~88%).
- The EMNIST dataset has some ambigous sample, which we, as human, still hardly classify. We think that, if all above models apply to another dataset, models will return an efficent predictation.
- We hope that we have more time to deeply research about this feild and further more in new AI problems.




***
# References
- Our friend:
    - ([@84436](https://github.com/84436)): Vanilla CNN, report
    - ([@kvmduc](https://github.com/kvmduc)): ResNet, report
- Kaggle notebook: [`ashwani07/emnist-using-keras-cnn`](https://www.kaggle.com/ashwani07/emnist-using-keras-cnn?)
- EMNIST: Paper ([`arXiv:1702.05373`](https://arxiv.org/abs/1702.05373)) and Kaggle dataset ([`crawford/emnist`](https://www.kaggle.com/crawford/emnist))
- [MIT 6.S191 "Introduction to Deep Learning", January 2020](introtodeeplearning.com/slides/6S191_MIT_DeepLearning_L3.pdf)
- [`arXiv:1412.6980` Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)
- [`arXiv:1512.03385` Deep Residual Learning for Image Recognition (ResNet)](https://arxiv.org/abs/1512.03385)
- [NN-SVG](http://alexlenail.me/NN-SVG/LeNet.html) for drawing network schematics
- [`arXiv:1508.02788` The Effects of Hyperparameters on SGDTraining of Neural Networks (Hyperparameters fine tuning)](https://arxiv.org/pdf/1508.02788.pdf)

[^1]: http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf
[^2]: https://towardsdatascience.com/going-beyond-99-mnist-handwritten-digits-recognition-cfff96337392
[^3]: https://www.kdnuggets.com/2018/09/dropout-convolutional-networks.html
