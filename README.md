# PokemonGAN
This is an attempt to create a GAN using a dataset of pokemon images.
This is primarily planned to be a WGAN, but I plan to experiment with other types of GANs as well.


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

```
run resize.py
run convertRGBAtoRGB.py
```

Now, to run a certain type of file for training, type in:
```
run [name of the file].py
```

I'll be adding the saved model checkpoints and results soon.
