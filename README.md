# Quiz Generator with Streamlit

This Streamlit application allows users to generate dynamic multiple-choice quizzes from custom text content. By leveraging LLMs (Large Language Models), it automates the creation of educational assessments, complete with difficulty levels and instant feedback.

---

### Key Features
* **Dynamic Generation:** Instantly turns long articles or notes into multiple-choice questions.
* **Difficulty Settings:** Adjustable levels (Easy, Medium, Hard) to match the learner's proficiency.
* **Instant Feedback:** Real-time scoring and display of correct answers upon submission.
* **Intuitive UI:** A clean, sidebar-driven interface for seamless navigation and configuration.

---

### Getting Started

#### 1. Installation
Clone the repository and install the necessary Python packages:
```bash 
git clone [https://github.com/farzanapomy/quiz_generator_with_streamlit.git](https://github.com/farzanapomy/quiz_generator_with_streamlit.git)
cd quiz_generator_with_streamlit
pip install -r requirements.txt
```

#### 2. Configuration
Ensure you have an OpenAI API key. Create a .env file in the root directory and add your key:
```bash 
OPENAI_API_KEY=your_api_key_here
```

#### 3. Launching the App
Run the application using Streamlit:
```bash 
streamlit run app.py
```


### How to Use
Input Text: Paste the text content you want to be quizzed on into the main text area.

Set Difficulty: Use the sidebar to select the desired complexity level.

Generate: Click the Generate Quiz button.

Answer & Review: Select your answers for the generated questions and click Submit to view your score and explanations


### HAPPY CODING ###
