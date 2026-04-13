# Smart Customer Segmentation using RFM and K-Means

## Project Overview
This project focuses on segmenting customers based on their purchasing behavior using machine learning techniques. It uses RFM analysis (Recency, Frequency, Monetary) along with K-Means clustering to group customers into meaningful segments.

The project is deployed as a Streamlit web application where users can input customer details and receive:
- Customer segment
- Behavioral explanation
- Business recommendations

---

## Objective
To analyze customer behavior and classify customers into distinct segments that help businesses make data-driven marketing decisions.

---

## Methodology

1. Data Cleaning
   - Removed missing values
   - Removed duplicate records
   - Filtered invalid transactions (negative quantity or price)

2. Feature Engineering (RFM)
   - Recency: Days since last purchase
   - Frequency: Number of transactions
   - Monetary: Total amount spent

3. Data Transformation
   - Applied log transformation to reduce skewness
   - Applied MinMax scaling for normalization

4. Clustering
   - Applied K-Means clustering algorithm
   - Determined optimal clusters using:
     - Elbow Method
     - Silhouette Score

5. Cluster Labeling
   - Interpreted clusters into meaningful segments:
     - Luxury Seekers
     - Budget Buyers
     - Impulse Shoppers

6. Deployment
   - Built an interactive web application using Streamlit

---

## Model Details

- Algorithm: K-Means Clustering
- Features: Recency, Frequency, Monetary
- Preprocessing:
  - Log Transformation
  - MinMax Scaling

---

## Visualizations

- Histograms for RFM distribution
- Boxplots for outlier detection
- Elbow curve for optimal number of clusters
- Scatter plots for cluster visualization

---

## Customer Segments

| Segment           | Characteristics                                   |
|------------------|--------------------------------------------------|
| Luxury Seekers   | High spending, frequent and recent purchases     |
| Budget Buyers    | Low spending and inactive customers              |
| Impulse Shoppers | Occasional but unpredictable purchasing behavior |

---

## Streamlit Application

The application allows users to:
- Enter Recency, Frequency, and Monetary values
- Predict customer segment
- View explanation and recommendations

---

## Project Structure
customer-segmentation-ml/
│
├── app.py
├── notebook.ipynb
├── kmeans_model.pkl
├── scaler.pkl
├── README.md


---

## How to Run
pip install -r requirements.txt
streamlit run app.py


---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn

---

## Key Insights

- RFM analysis effectively captures customer behavior
- K-Means clustering helps group similar customers
- Segmentation supports targeted marketing and better customer retention

---

## References

- Research papers on RFM and K-Means clustering
- Online Retail Dataset (Kaggle)

