import coremltools

output_labels = ['Banana', 'Battery', 'Computer', 'Glass bottle', 'Light bulb', 'Paper', 'Phone', 'Plastic']

coreml_mnist = coremltools.converters.keras.convert(
    './models/model_v7_0_final.h5', input_names=['image'], output_names=['output'], 
    class_labels=output_labels, image_input_names='image')
coreml_mnist.save('./models/model_v7_1_final.mlmodel')


