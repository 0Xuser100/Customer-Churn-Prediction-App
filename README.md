# Customer Churn Prediction App  

This **Streamlit-based application** predicts the likelihood of customer churn using a pre-trained machine learning model. The app allows users to input customer data and provides a churn probability score with an interpretation of the result.  

---

## 🌟 Features  

- **Intuitive Input Interface**:  
  - Users can select customer attributes such as geography, gender, age, balance, credit score, and more.  

- **Real-Time Prediction**:  
  - Calculates and displays the probability of customer churn instantly.  

- **User-Friendly Design**:  
  - Built with **Streamlit** to provide an interactive and responsive experience.  

---

## 🛠️ Technologies Used  

- **[Streamlit](https://streamlit.io/)**: Web application framework.  
- **[TensorFlow](https://www.tensorflow.org/)**: For loading and running the pre-trained model.  
- **[scikit-learn](https://scikit-learn.org/)**: Used for encoding categorical features and scaling input data.  
- **[Pandas](https://pandas.pydata.org/)**: For data manipulation.  

---

## ⚙️ Installation  

### 📋 Prerequisites  
- Python 3.7 or higher  
- pip  

### 📂 Clone the Repository  
```bash  
git clone https://github.com/yourusername/customer-churn-prediction.git  
cd customer-churn-prediction  
```  

### 🧹 Create a Virtual Environment  
```bash  
python -m venv venv  
```  

### 🔑 Activate the Virtual Environment  
#### On Windows:  
```bash  
venv\Scripts\activate  
```  
#### On macOS/Linux:  
```bash  
source venv/bin/activate  
```  

### 📦 Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

---

## 🚀 Usage  

1. **Run the Streamlit App**:  
   ```bash  
   streamlit run app.py  
   ```  

2. **Open the Web Interface**:  
   - Open your browser and navigate to: [http://localhost:8501](http://localhost:8501)  

3. **Input Customer Data**:  
   - Select the customer details such as geography, gender, age, credit score, etc.  

4. **View Prediction**:  
   - The app will display:  
     - **Churn Probability**: Likelihood of the customer leaving.  
     - **Interpretation**: Whether the customer is likely to churn or stay.  

---

## 📂 File Structure  

- `app.py`: Main Streamlit application script.  
- `model.h5`: Trained machine learning model (TensorFlow format).  
- `label_encoder_gender.pkl`: Label encoder for the `Gender` feature.  
- `onehot_encoder_geo.pkl`: One-hot encoder for the `Geography` feature.  
- `scaler.pkl`: Scaler for standardizing numerical features.  
- `requirements.txt`: List of required Python libraries.  

---

## ✨ Example Inputs and Outputs  

### Example Input:
- **Geography**: France  
- **Gender**: Female  
- **Age**: 35  
- **Credit Score**: 600  
- **Balance**: 50000  
- **Estimated Salary**: 80000  
- **Tenure**: 3  
- **Number of Products**: 2  
- **Has Credit Card**: Yes  
- **Is Active Member**: No  

### Example Output:
- **Churn Probability**: `0.75`  
- **Interpretation**: `The customer is likely to churn.`  

---

## 🔮 Future Enhancements  

- **Visualizations**:  
  - Add graphical insights like feature importance and churn probability distribution.  

- **Data Upload**:  
  - Allow bulk predictions through CSV upload.  

- **Model Customization**:  
  - Provide options to adjust prediction thresholds or retrain the model.  

---

## 📞 Contact  

For questions or contributions:  
- **Name**: Mahmoud Abdelhamid  
- **Email**: [mahmoudabdulhamid22@gmail.com](mailto:mahmoudabdulhamid22@gmail.com)  
- **GitHub**: [https://github.com/0Xuser100](https://github.com/0Xuser100)  

---

## 📝 License  

This project is licensed under the MIT License.  

---  

Empower your business with actionable insights on customer churn prediction! 🚀  
