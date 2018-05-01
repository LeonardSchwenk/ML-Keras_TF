import coremltools

output_labels = ['banana', 'battery', 'computer', 'glass_bottel', 'light_blub', 'paper', 'phone', 'plastic']
coreml_model = coremltools.converters.keras.convert('./models/modelv4.3_8.categories.h5',
                                                   input_names='image',
                                                   image_input_names='image',
                                                   output_names='output',
                                                   class_labels=output_labels)

coreml_model.author = 'GreenCycle'
coreml_model.short_description = 'Model to classify 8 different image categories'

coreml_model.save('modelv4.3_8.categories.mlmodel')