<img src = "https://github.com/Aaris-Kazi/DIsease-Prediction-Online/blob/main/preview_doc/logo.gif" height =190px width=190px>
 
 # DIsease-Prediction-Online
 ### What is Disease Preiction? This app will help you to analyze your disease symptoms and give you correct prediction by using Machine Learning on web 
 
<img src = "https://github.com/Aaris-Kazi/DIsease-Prediction-Online/blob/main/preview_doc/cancer.gif">

To build from the repository, execute the following commands first:

    git clone https://github.com/Aaris-Kazi/DIsease-Prediction-Online.git
    cd DIsease-Prediction-Online
    
Import the necessary modules:

    pip install -r requirements.txt
    

Run the repository by this command:

    flask run
    
| Disease   | Accuracy | Models |
|-----------|----------|--------|
| Cancer    | 78% | multispec_rfc15.pkl |
| Pneumonia | 92% | xray_model_final.h5 |
| Heart     | 95% | heart_model.pkl |
| Malaria   | 85% | malaria_cnn.h5 |
| Liver     | 95% | liver_log.pkl |
| Diabetes  | 95% | diabetes.pkl |
