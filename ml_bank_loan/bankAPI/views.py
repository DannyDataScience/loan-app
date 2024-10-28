from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib import messages
from .forms import ApprovalForm
from .models import approvals
from .serializers import approvalsSerializers
import joblib
import numpy as np
import pandas as pd


def about_view(request):
    return render(request, 'myform/about.html')

# Approvals API View for Django Rest Framework
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers

# Helper function: One Hot Encoding
def ohevalue(df):
    """
    Applies One Hot Encoding to the categorical features of the input DataFrame.
    Ensures that the resulting DataFrame has the same columns as the ones used during model training.
    
    Parameters:
    df (DataFrame): Input data from the form.

    Returns:
    DataFrame: DataFrame with One Hot Encoded columns matching the training set.
    """
    ohe_col = joblib.load("bankAPI/allcol.pkl")
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    
    # Apply One Hot Encoding to categorical columns
    df_processed = pd.get_dummies(df, columns=cat_columns)
    
    # Ensure the encoded DataFrame has the same columns as the model expects
    newdf = pd.DataFrame({col: df_processed[col] if col in df_processed.columns else 0 for col in ohe_col})
    
    return newdf

# Helper function: Loan approval or rejection prediction
def approvereject(processed_data):
    """
    Predicts whether a loan application will be approved or rejected based on the model's threshold.

    Parameters:
    processed_data (DataFrame): DataFrame containing scaled input features.

    Returns:
    tuple: (approval status, scaled input data) or (error message, None)
    """
    try:
        # Load model and scaler
        model = joblib.load("bankAPI/loan_model.pkl")
        scaler = joblib.load("bankAPI/scaler.pkl")
        
        # Scale the input data
        scaled_data = scaler.transform(processed_data)
        
        # Make the prediction with the model
        prediction = model.predict(scaled_data)
        approval_status = 'Approved' if prediction > 0.58 else 'Rejected'
        
        return (approval_status, scaled_data[0])
    except ValueError as e:
        return (str(e), None)

# View to handle form interaction and loan application processing
def cxcontact(request):
    """
    Handles the loan application form submission, processes the data, and displays the approval/rejection status.
    
    Renders a form for the loan application and, upon submission, validates and processes the input data.
    If the loan amount is less than 25,000, it makes a prediction using a pre-trained model.

    Parameters:
    request (HttpRequest): The request object used to submit the form.

    Returns:
    HttpResponse: Renders the form template with the result or error message.
    """
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        
        if form.is_valid():
            # Extract cleaned form data
            form_data = form.cleaned_data
            loan_amount = form_data['LoanAmount']
            
            # Create DataFrame from form data
            df = pd.DataFrame([form_data])
            
            # Validate loan amount before prediction
            if loan_amount < 25000:
                # Apply One Hot Encoding and make prediction
                encoded_data = ohevalue(df)
                approval_status, _ = approvereject(encoded_data)
                
                # Display success message with approval status
                messages.success(request, f'Application Status: {approval_status}')
            else:
                # Display error message for excessive loan amount
                messages.error(request, 'Invalid: Your Loan Request Exceeds $25,000 Limit')
    else:
        form = ApprovalForm()  # Show empty form for GET request

    # Render the form template
    return render(request, 'myform/cxform.html', {'form': form})
