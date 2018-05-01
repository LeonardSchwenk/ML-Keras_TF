import coremltools

output_labels = ['0', '1', '2', '3', '4', '5', '6', '7']

coreml_mnist = coremltools.converters.keras.convert(
    './models/modelv4.8_12_channels_last.categories.h5', input_names=['image'], output_names=['output'], 
    class_labels=output_labels, image_input_names='image')
coreml_mnist.save('modelv4v8_12.categories.mlmodel')


