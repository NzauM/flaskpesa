from flask import Flask, request
from flask_mpesa import MpesaAPI


app = Flask(__name__)

# mpesa.init_app(app)
app.config["API_ENVIRONMENT"] = "sandbox" #sandbox or production
app.config["APP_KEY"] = "RJTdTKoBISSdGovfVI61LlVqsh7jJr1A" # App_key from developers portal
app.config["APP_SECRET"] = '9txkkJcjGjQifvYt'


mpesa = MpesaAPI(app)
@app.route('/')
def home():
    return '<h1>Flask Mpesa! Welcome</h1>'

@app.route('/mytranzakshens', methods=['GET','POST'])
def mpesahome():
    if request.method == 'POST':
        regdata = {
            "shortcode": request.get_json('shortcode'),
            "response_type": "Completed",
            "confirmation_url": "http://127.0.0.1:5000/confirmation",
            "confirmation_url": "http://127.0.0.1:5000/validation"
                   }
        # resp = mpesa.C2B.register(**regdata)
        resp = "Hey"

        # print(resp)
        return resp

@app.route('/mpesacallback', methods = ['GET','POST'])
def callbackmpesa():
    print("At Callback xxxxxxxxxxxxxxxxxxxxxx")
    if request.method == 'POST':
        json_data = request.get_json()
        print (json_data)
        return json_data
        # sample response data {'Body': {'stkCallback': {'MerchantRequestID': '25071-1081856-2', 'CheckoutRequestID': 'ws_CO_19102023133301077711111446', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'RJJ3WU0GFZ'}, {'Name': 'TransactionDate', 'Value': 20231019133133}, {'Name': 'PhoneNumber', 'Value': 254711111446}]}}}}
        # We can now save this transaction to DB
        
    return "Callback reached" 

@app.route('/expresspay', methods = ['GET','POST'])
def stk_push():
    if request.method == "POST":
        mydata = request.get_json()
        data = {
            "business_shortcode": mydata.get('till_number'),
            "passcode": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
            # "passcode": "NkvPX/++D5lD0yMPT+czuiTUf0k0JdKutuEm5Qi/fpfGYQLdyeIL6iBGOn7SzPUm71GR0f2d7gY21QmJPuXEp3qHT2DXGbWrQmmSyBtjLAO7fq20IqLfRJ7hC3RY9/OXZRYtzZoXyKUxh8x07sQkYjVeb6+Rw0euhbTUZ/W0+uIfn44uP1FrmGw0NAAlxMO2zbrW4q1TQZympWJFX+92lAV9HmWvP5HknFMT+GfR4DSfeueDWzLkTbGMwoamzYMImTC4R/LEgDbIh2DBsWYmGxh6yL1gN38ewo7d/QqG43k1sXPUB0Fm5kY7EUNGQ3Hd+kdt3Jhw1gCXPpUKGaewGw==",
            "amount": mydata.get('amount'),
            "phone_number": mydata.get('phone_number'),
            "callback_url": 'https://secure-implicitly-crappie.ngrok-free.app/mpesacallback',
            "description": "Sample description for test",
            "reference_code": "Sample reference code for testing"
           }
        resp = mpesa.MpesaExpress.stk_push(**data)
        print(data)
        # resp = mpesa()
        print (resp)
        return resp
    else:
        return "It's a GET request"




if __name__ == '__main__':
    app.run()