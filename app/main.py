from pipeline import generate_answer

if __name__ == "__main__":
    while True:
        query = input("Ask leadership question: ")
        answer = generate_answer(query)
        print("\n=== AI Insight ===\n")
        print(answer)
