import pandas as pd
file_path=(r"C:\Users\91936\Desktop\Vaishak_miniproject\legal2.csv")
df = pd.read_csv(file_path, encoding="utf-8")
df["Question"] = df["Question"].astype(str).str.lower()
def legal_advice(query):
    query = query.lower()  
    query_words = query.split()  
    
    for index, row in df.iterrows():
        question_words = row["Question"].split() 
        if any(word in question_words for word in query_words): 
            print("\nQ:", row["Question"])
            print("\nA:", row["Answer"])
            return
    print("\nNo relevant legal information found. Try rephrasing your question.")
while True:
    user_input = input("\nAsk your legal question (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    legal_advice(user_input)
    