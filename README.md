# PokemonGAN
This is an attempt to create a GAN using a dataset of pokemon images.
This is primarily planned to be a WGAN, but I plan to experiment with other types of GANs as well.

Website link: https://abhishek-choudharys.github.io/PokemonGAN/

To clone the repository on your desktop or google colab, type in:
```
!git clone https://github.com/abhishek-choudharys/PokemonGAN

cd ../content/PokemonGAN
```


If on desktop, navigate to the PokemonGAN directory.
Once your current directory is set to PokemonGAN directory, you may follow the following instructions to run the code.

<h2> Running instructions: </h2>
First, we need to perform certain operations on the default images to make them usable.
This includes resizing them to 256x256 using resize.py and the latter file converts them to RGB from RGBA, by effectively removing the aplha channel and saves them as .jpg images, which can be used much more efficiently in our approach to build a GAN. 

To use the smaller dataset:

```
run resize.py --dataset 1
run convertRGBAtoRGB.py --type WGAN
```

Inorder to use the much larger dataset (default), on which the results have been obtained, download and extract https://www.kaggle.com/kvpratama/pokemon-images-dataset to pokemon/ in the main directory.
Update: Images have already been included.

Run:

```
run resize.py --dataset 2
run convertRGBAtoRGB.py --type WGAN
```

or, if you want to use the GAN, run:
```
run convertRGBAtoRGB.py --type GAN
```

Now, to run a certain file for training, type in:

```
run name/of/the/file.py
```

For example, to train the WGAN, run:

```
run WGAN/pokemonWGAN_3_final.py
```

I'll be adding the saved model checkpoints and results soon...

<hr>

<h2> GAN </h2>
GAN stands for Generative Adversarial network. It's a class of machine learning frameworks where two neural nets interact with each other, often in a zero sum game. It aims to generate new data, by learning from a training set.

<h2> WGAN </h2>
WGAN is an improvement over traditional GANs. The 'W' stands for Wasserstein, a reference to the fact that it uses a new loss function called the Wasserstein loss. Thus, the discriminator functions more like a critic that assess image quality.

<hr>

Website link: https://abhishek-choudharys.github.io/PokemonGAN/

