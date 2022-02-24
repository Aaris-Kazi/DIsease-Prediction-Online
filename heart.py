from numpy import array
from joblib import load

def ValuePredictor(to_predict_list, size):
    to_predict = array(to_predict_list).reshape(1, size)
    if(size == 7):
        loaded_model = load(r'models/heart_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]