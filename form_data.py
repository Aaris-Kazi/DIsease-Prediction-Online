from numpy import array
from joblib import load

def ValuePredictor(to_predict_list, size):
    result = []
    print(size)
    to_predict = array(to_predict_list).reshape(1, size)
    if(size == 7): # heart
        loaded_model = load(r'models/heart_model.pkl')
        result = loaded_model.predict(to_predict)
        return result[0]
    elif(size==8):#Diabetes
        loaded_model = load(r'models/diabetes.pkl')
        result = loaded_model.predict(to_predict)
        return result[0]
    # elif(size==12):#Kidney
    #     loaded_model = load(r'models/kidney')
    #     result = loaded_model.predict(to_predict)
    #     return result[0]
    
def ValuePredictor1(to_predict_list, size):
    result = []
    print(size)
    to_predict = array(to_predict_list).reshape(1, size)
    loaded_model = load(r'models/liver_log.pkl')
    result = loaded_model.predict(to_predict)
    return result[0]