# Contact Page with Streamlit and AWS Lambda 📧☁️

This project demonstrates how to create a contact page using Streamlit and send emails using AWS Lambda and SES. 

## Structure 📂
project-root-directory/
│
├── .env # Contains environment variables like API_GATEWAY_ENDPOINT
├── .gitignore # Contains patterns of files or directories that git should ignore
│
├── streamlit_app/
│ ├── app.py # Streamlit frontend code
│ └── requirements.txt # Python libraries for Streamlit app
│
└── lambda_function/
├── lambda_function.py # AWS Lambda code for sending emails
└── requirements.txt # Python libraries for Lambda function


## Setup & Installation ⚙️

1. **Environment Variables**: Set up the `.env` file with the necessary environment variables, e.g., `API_GATEWAY_ENDPOINT`.
2. **Python Libraries**: Navigate to both `streamlit_app` and `lambda_function` and run:
   
pip install -r requirements.txt

3. **Deploy Lambda**: Deploy the `lambda_function.py` to AWS Lambda.
4. **Run Streamlit App**: In the root directory, execute:

streamlit run streamlit_app/app.py

## Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License 📜

[MIT](https://choosealicense.com/licenses/mit/)