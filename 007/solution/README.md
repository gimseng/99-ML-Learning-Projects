# Deep-Dream:
It is a computer vision program which uses a convolutional neural network to find and enhance patterns in images, thus creating a dream-like hallucinogenic appearance in the deliberately over-processed images. 
<p> It adapts the input images to match the network weights with gradient ascent which results in visualizing network filters on the input images giving them psychodelic look. </p>
<p> This notebook recreates a style transfer method that is outlined in the paper
  <a href="https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf"> Image Style Transfer Using Convolutional Neural Networks, by Gatys </a> in PyTorch.
  <p> <h2> Style Transfer: </h2> </p>
  <p> Style transfer relies on separating the content and style of an image. Given one content image and one style image, we aim to create a new, target image which should contain our desired content and style components:
<ul>
<li> objects and their arrangement are similar to that of the content image </li>
<li> style, colors, and textures are similar to that of the style image </li> </ul>

<p> <h4> Example: </h4> </p>
<img src="https://raw.githubusercontent.com/geekquad/deep-learning-v2-pytorch/master/style-transfer/notebook_ims/style_tx_cat.png">
<p> An example is shown, where the content image is of a cat, and the style image is of Hokusai's Great Wave. The generated target image still contains the cat but is stylized with the waves, blue and beige colors, and block print textures of the style image. </p>
<h2> VGG-19: </h2>
</p>
<p> Using VGG-19 as a feature extractor and 
using backpropogation to minimize a defined loss function between our target and content images.
Not training it to produce a specific output. </p>
<img src="https://raw.githubusercontent.com/geekquad/deep-learning-v2-pytorch/master/style-transfer/notebook_ims/vgg19_convlayers.png">
<p> The above image shows the various layers of the model VGG-19. </p>
