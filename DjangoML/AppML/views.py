from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        married = request.POST['married']
        dependents = request.POST['dependents']
        education = request.POST['education']
        self_employed = request.POST['self_employed']
        applicant_income = request.POST['applicant_income']
        coapplicant_income = request.POST['coapplicant_income']
        loan_amount = request.POST['loan_amount']
        loan_amount_term = request.POST['loan_amount_term']
        credit_history = request.POST['credit_history']
        property_area = request.POST['property_area']

        # Print the field values in the terminal
        print("Gender:", gender)
        print("Married:", married)
        print("Dependents:", dependents)
        print("Education:", education)
        print("Self Employed:", self_employed)
        print("Applicant Income:", applicant_income)
        print("Coapplicant Income:", coapplicant_income)
        print("Loan Amount:", loan_amount)
        print("Loan Amount Term:", loan_amount_term)
        print("Credit History:", credit_history)
        print("Property Area:", property_area)


        pred = predict(gender, married, dependents, education, self_employed, applicant_income,coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area)

        print(pred)
        
        """"
        context = {
            'gender': gender,
            'married': married,
            'dependents': dependents,
            'education': education,
            'self_employed': self_employed,
            'applicant_income': applicant_income,
            'coapplicant_income': coapplicant_income,
            'loan_amount': loan_amount,
            'loan_amount_term': loan_amount_term,
            'credit_history': credit_history,
            'property_area': property_area,
            'pred' : pred,
        }
        """

        return render(request, 'main2.html', {'pred' : pred})
    return render(request, 'main2.html')



def predict(gender, married, dependent, education, self_employed, applicant_income,
           coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea):
    # processing user input
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
    edu = 0 if education == 'Graduate' else 1
    sem = 0 if self_employed == 'Yes' else 1
    pro = 0 if propertyArea == 'Semiurban' else 1 if propertyArea == 'Urban' else 2
    Lam = int(loanAmount) / 1000
    Lam = float(Lam)
    cap = int(coApplicantIncome) / 1000
    cap = float(cap)
    applicant_income = float(applicant_income)
    loan_amount_term = float(loan_amount_term)
    creditHistory = float(creditHistory)
    # making predictions
    prediction = model.predict([[gen, mar, dep, edu, sem, applicant_income, cap,
                                      Lam, loan_amount_term, creditHistory, pro]])
    verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
    return verdict