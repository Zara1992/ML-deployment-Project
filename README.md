# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
Purpose of this study is to develop a model that will help the bank to automate the loan eligibility process for it’s customer.
The dataset contains random data of 614 individuals and 12 features. 1 column is the target data (Loan_Status: Yes/No)


## Hypothesis
Applicant having a credit history more likely to secure a loan


## EDA 
LoanAmount has 22 missing values (614 – 592) .
Loan_Amount_Term has 14 missing values (614 – 600) .
Credit_History has 50 missing values (614 – 564).
We can also look that about 84% applicants have a credit_history. 
The mean of Credit_History field is 0.84
OR 475/564
The ApplicantIncome distribution seems to be in line with expectation. Same with CoapplicantIncome

We can see that approximately 81% are Male and 19% are female.
Percentage of applicants with no dependents is higher.
There are a greater number of graduates than non graduates. 
Semi Urban people is slightly higher than Urban people among the applicants.
The percentage of people that the loan has been approved has been higher rather than the percentage of applicant for which the loan has been declined.

 Outliers for Applicant Income: Here we observe that there are few extreme values. Next, we look at box plots to understand the distributions. This confirms the presence of a lot of outliers/extreme values. This can be attributed to the income disparity in the society. Part of this can be driven by the fact that we are looking at people with different education levels.

Outliers for Loan Amount:  Here we observe that there are few extreme values. Next, we look at box plots to understand the distributions. This confirms the presence of a lot of outliers/extreme values. This means that some people have received a higher loan than usual. One of the reason might be that applicants that graduated were given a higher loan since they might have good jobs and means to return the loan. However, this still requires further analysis. 

PIVOT TABLE for categorical variable against numeric values
There is not much difference between the mean income of applicant income who got the loan and those who did not. 
Applicants that had there loan rejected had asked for a greater loan on average, which might be the reason for rejection.
On average, Male’s have a higher income and higher loan amount. 
More married people have applied for the loan and for a lot of them the loan amount is high. This might be due to house or car loans that couple take out.
Self-employed individuals have a higher income and higher loan amount. 
On average applicants that are graduate have a higher income. 


## Process
1. Feature engineering
  * treating null values
  * log transofrmation
  * Create new column for total income
  * changing 3+ value of dependents to 3
  * as.type to categorical and int
  * one hot encoding
  * drop columns
 
2. PCA and Elbow curve = Optimal features are 8 explaining 85% of the data 

3. Modeling: (Logistic Regression, Random Forest, Decision Tree, KNN Classifier)

4. Grid Search (Logistic Regression, Random Forest, Decision Tree, KNN Classifier)

5. Pipeline

6. Deployment 

## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)

## Challanges 
1. Time constraints 
2. Writing good code
3. Understanding data
4. Understanding logic of code

## Future Goals
1. Data provided is bias, would increase the data size to cover a broader range of applicants for better analysis. 
