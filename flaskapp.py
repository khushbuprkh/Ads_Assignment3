
# coding: utf-8

# In[96]:

from flask import Flask
from flask import render_template,request,jsonify
import json
import urllib2
import re
import time
from jinja2.utils import Markup


# In[97]:

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# In[98]:

@app.route('/predictionAlgorithms', methods=['POST','GET'])
def predictionAlgorithms():
    if request.method == 'POST':
        print ("POST")  
        data = {
                "Inputs": {
                        "input1":
                        [
                            {
                                    'OriginalInterestRate': request.form['OriginalInterestRate'],   
                                    'FirstTimeHomeBuyerFlag': request.form['FirstTimeHomeBuyerFlag'],      
                                    'Channel': request.form['Channel'],   
                                    'ServicerName': request.form['ServicerName'],   
                                    'CreditScore': request.form['CreditScore'] ,    
                                    'LoanPurpose': request.form['LoanPurpose'], 
                            }
                        ],
                },
            "GlobalParameters":  {
            }
        }
        if request.form['submit'] == 'linearRegression':
            result= predictionLR(data)
            return render_template('prediction.html', Status=json.loads(result))
        elif request.form['submit'] == 'randomForest':
            result= predictionRF(data)
            return render_template('prediction.html', Status=json.loads(result))
        else:
            result= predictionNN(data)
            return render_template('prediction.html', Status=json.loads(result))
        return render_template('prediction.html', Status=json.loads(result))
    return render_template('prediction.html')


# In[99]:

@app.route('/classificationAlgorithms', methods=['POST','GET'])
def classificationAlgorithms():
    if request.method == 'POST':
        print ("POST")  
        data = {
                "Inputs": {
                        "input1":
                        [
                            {
                                    'DelinquencyStatus': request.form['DelinquencyStatus'],   
                                    'LoanAge': request.form['LoanAge'],      
                                    'CurrentInterestRate': request.form['CurrentInterestRate'],   
                                    'ActualLossCalculation': request.form['ActualLossCalculation'],   
                                    'Modification Cost': request.form['ModificationCost'] ,    
                                    'RepurchaseFlag': request.form['RepurchaseFlag'], 
                            }
                        ],
                },
            "GlobalParameters":  {
            }
        }
        if request.form['submit'] == 'logisticRegression':
            result= classificationLR(data)
            return render_template('classification.html', Status=json.loads(result))
        elif request.form['submit'] == 'randomForest':
            result= classificationRF(data)
            return render_template('classification.html', Status=json.loads(result))
        else:
            result= classificationNN(data)
            return render_template('classification.html', Status=json.loads(result))
        return render_template('classification.html', Status=json.loads(result))
    return render_template('classification.html')


# In[100]:

def predictionLR(results) :
    body = str.encode(json.dumps(results))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/ddf618dd46804764a0e1c19666c50a65/execute?api-version=2.0&format=swagger'
    api_key = 'TKUC/dXxMUALGGQoeCyktYjJOZ8oVwJW/2BqfHhbLN+9wMf2HkbJhH/Ciy4wZ4aYse6BZMqM9yE8/I6MnTyzZw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)
    try:
        response = urllib2.urlopen(req)
        print(response)
        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[101]:

def predictionRF(results) :
    body = str.encode(json.dumps(results))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/2dd24743850a4fc680c7b2424e154380/execute?api-version=2.0&format=swagger'
    api_key = 'gSQeXBbXZxKVJ+uKxb5s7UeF/rTGg5+wka6xHXuzIHfWnKgYWLjw36fUdJr93hRYN5YeyF6u2irv1NK5dYtnhQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[102]:

def predictionNN(results) :

    body = str.encode(json.dumps(results))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/125f9ed9f6444b058980c99eafdaaa42/execute?api-version=2.0&format=swagger'
    api_key = '6/O5vdxIlI0uW+XgPw5Nn4KacZik68r87F+IpMSogcoKSvGj2htkYKrvrIahqcTDLeBSlabH0CLnBcOudrHJoQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)
    try:
        response = urllib2.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[103]:

def classificationLR(data):
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/6507018587a244779c1405171702ea99/execute?api-version=2.0&format=swagger'
    api_key = 'ck1Wz+0IozPGwvVb9oq7swzejnMvkP7BT1tXbH+/WDCKoi+KVjXqf6UyTncNGFSbdrdsQLF9XcFaCBcdeHpi1w==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[104]:

def classificationRF(data):
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/4b250ed8a7d34097aaf4d9d673cae8ac/execute?api-version=2.0&format=swagger'
    api_key = 'kb1Ke0u1AX/h39/FqjIoVq/80LxDf0ROxZr3iOTGnIEvl3CLsEwYy2O5W0qZWQvdF1CEgyNRUMxUl2QQMBjEsw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[105]:

def classificationNN(data):
    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/0d0c6a4913c64986bf10cff66d7ca35c/services/5fb37a40912540a9869035ba4585835c/execute?api-version=2.0&format=swagger'
    api_key = 'lQmdSQngkrZSq7hPlOpBeXNbdBgB1vgsGfEH2nPxwZbsuN37NsR9p8d3cZn1UeP9dCMiwQS9UvwWUUcUhVWbNA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = response.read()
        print(result)
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read())) 
    return result


# In[ ]:

if __name__=="__main__":
    app.run()


# In[ ]:




# In[ ]:




