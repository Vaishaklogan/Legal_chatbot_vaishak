🧠 Step-by-Step Process Explanation of the Legal Advice Chatbot (Using Python)
1️⃣ Importing Necessary Tools
The project starts by importing the necessary Python libraries — mainly pandas, which is used for reading and handling data from a CSV file.

2️⃣ Loading the Dataset
A dataset (CSV file) that contains frequently asked legal questions and their corresponding answers is loaded into the program. This data is structured in two main columns: "Question" and "Answer".

3️⃣ Cleaning and Preprocessing the Data
Before comparing the data with user input, all the questions in the dataset are converted to lowercase. This step ensures that the comparison is not affected by uppercase or lowercase differences.

4️⃣ Accepting User Input
The chatbot then prompts the user to enter a legal question. This input is also converted to lowercase and broken down into individual words for easier comparison.

5️⃣ Keyword Matching Logic
The chatbot uses a basic keyword-based search logic. It goes through each question in the dataset and checks if any of the words from the user's input are present in the dataset’s questions.

6️⃣ Providing a Relevant Answer
If a match is found between the user’s question and any of the questions in the dataset, the chatbot displays the matched question along with the appropriate legal answer.

7️⃣ Handling Unmatched Questions
If no relevant match is found, the chatbot informs the user and suggests rephrasing the question for better results.

8️⃣ Continuous Interaction
The program runs in a loop, allowing users to ask multiple questions until they choose to exit the chatbot.

🧩 Skill Applications (From Basic to Advanced):

1.Understanding and processing structured data (CSV).

2.Text preprocessing and normalization.

3.Building interactive command-line tools.

4.Implementing search logic using string operations.

5.Creating a user-friendly and efficient flow.