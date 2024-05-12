# ATS Tracker

The ATS Tracker is an Applicant Tracking System (ATS) designed to simplify and streamline the recruitment process for businesses. It utilizes the Google Gemini API for various functionalities and is built with Streamlit for the user interface. The application is deployed on the Hugging Face Spaces platform, making it accessible and easy to use.

## Features

- **Candidate Management**: Manage candidate profiles, including resumes, contact information, and notes.
- **Job Postings**: Create and publish job listings with customizable fields and requirements.
- **Application Tracking**: Track the status of each application from submission to hire.
- **Collaboration Tools**: Enable team collaboration with comments, ratings, and candidate sharing.
- **Search and Filter**: Efficiently search and filter candidates based on skills, experience, and other criteria.
- **Analytics and Reporting**: Gain insights into recruitment metrics with built-in analytics and reporting tools.
- **Customization**: Customize the system to fit your company's unique recruitment process and branding.

## Getting Started

To get started with the ATS Tracker, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone https://github.com/your_username/ats-tracker.git`.

2. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.

3. **Google API KEY**:Go to this site to generate api key [HERE](https://aistudio.google.com) You can see left side generate api thn click and copy. Once you have the api key, locate the .env file in your project directory. Open it and paste your aoi key like this:
  ```bash
  GOOGLE_API_KEY = "paste the api key here"
  ```
4. **Run the Application**: Run the application locally using Streamlit by executing `streamlit run app.py`.

5. **Access the Application**: Access the application in your web browser at `http://localhost:8501`.

## Deployment

The ATS Tracker is deployed on the Hugging Face Spaces platform. You can access the deployed application [here](https://huggingface.co/spaces/suriya7/ATS-Tracking-System).

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://developers.google.com/gemini)
- [Hugging Face Spaces](https://huggingface.co/spaces)

