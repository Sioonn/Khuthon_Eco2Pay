from create_embedding import create_embedding_vector
import pandas as pd
# from oil import calculate_co2_emission
# from carbon_footprint_regression import co2_per_clothes
from ingredient_prediction_model import MultiClassModel
import torch
# import re

payment_institution = '부타센세'
embeded_vec = create_embedding_vector(payment_institution)
ingred_tensor_input = torch.FloatTensor(embeded_vec)
ingred_model = MultiClassModel(300, 50)
ingred_checkpoint = torch.load('model/ingredient_prediction_model.pth')
ingred_model.load_state_dict(ingred_checkpoint['model_state_dict'])

ingred_model.eval()
with torch.no_grad():
    output = ingred_model(ingred_tensor_input)
print(output)

