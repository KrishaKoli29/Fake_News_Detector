user_input = input("Enter a news headline or article text to test: ")
custom_news_text = [user_input]

processed_news = preprocess_text(custom_news_text)

vectorized_news = vectorization.transform(processed_news)

prediction = model.predict(vectorized_news)

print("-" * 30)
print(f"You entered: '{user_input}'")

if prediction[0] == 0:
    print("Prediction: This is FAKE NEWS 🚨")
else:
    print("Prediction: This is REAL NEWS ✅")
print("-" * 30)