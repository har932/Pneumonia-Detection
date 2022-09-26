# Pneumonia Detetion

Pneumonia is an inflammatory condition of the lung primarily affecting the small air sacs known as alveoli.
Symptoms typically include some combination of productive or dry cough, chest pain, fever, and difficulty breathing.
The severity of the condition is variable.
Pneumonia is usually caused by infection with viruses or bacteria, and less commonly by other 
microorganisms. 
Identifying the responsible pathogen can be difficult. Diagnosis is often based on symptoms and physical examination.
Chest X-rays, blood tests, and culture of the sputum may help confirm the diagnosis.The disease may be classified by where it was acquired, such as community- or hospital-acquired or healthcare-associated pneumonia.
Risk factors for pneumonia include cystic fibrosis, chronic obstructive pulmonary disease (COPD), sickle cell disease, asthma, diabetes, heart failure, a history of smoking, a poor ability to cough (such as following a stroke), and a weak immune system.

# Architecture 
```

```

# Tools and Technologies

CNN : It stands for Convolutional Neural Network. It is a Deep Learning algorithm which can take in an input    image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other.

VGG 16 : It has 16 convoltional layers. It is an easy and broadly used Convolutional Neural Network (CNN) Architecture used for ImageNet which is a huge visible database mission utilized in visual object recognition software research.

VGG 19 : It has 19 convoltional layers. It is an easy and broadly used Convolutional Neural Network (CNN) Architecture used for ImageNet which is a huge visible database mission utilized in visual object recognition software research. This means that VGG19 has three more convolutional layers than VGG16.

ResNet50 : It is a convolutional neural network that is 50 layers deep. You can load a pretrained version of the network trained on more than a million images from the ImageNet database [1]. The pretrained network can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals. As a result, the network has learned rich feature representations for a wide range of images. The network has an image input size of 224-by-224.

# Best Model

After training the images on these four models we got the accuracy as CNN - 91%, VGG 16 - 96.8%, VGG19 - 96.2%, ReNet50 - 89% . So we choose the best model as VGG16 as it is having the best accuracy.

# UI Screenshots
image.png

