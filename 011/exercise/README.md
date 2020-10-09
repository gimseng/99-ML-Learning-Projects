# Problem Statement  
To make an algorithm to dehaze images and get a clear image. Haze and fog interrupts various object detection tasks so it is neccessary to restore the clear image before using
it for further detection task. Using an architecture which follows encoder-decoder approach to restore clear image. Code is done on Tensorflow v2.3.

# Requirements  
- Tensorflow (version 2+)
- Python (3.6.9+)
- GPU Nvidia Tesla P100(provided by Kaggle)
- Get the data from [here](https://www.kaggle.com/wwwwwee/dehaze)

# Learnings
- Encoder-decoder architecture, how to implement.
- Getting into the domain of image dehazing and semi-supervised learning.
- Insights of Tensorflow, how to custom train a model, writing training loop from scratch(can't use fit, predict here).

# Sources 
- Star the [Original Repository](https://github.com/sanchitvj/Image-Dehazing-using-GMAN-net)
- [Research Paper](https://github.com/sanchitvj/Image-Dehazing-using-GMAN-net/blob/master/Dehazing%20-%20Generic%20Model-Agnostic%20Convolutional%20Neural.pdf)
- Detailed explanation and documentation [here](tinyurl.com/gman-dehaze-net).
