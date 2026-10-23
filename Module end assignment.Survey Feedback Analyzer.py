feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
print(feedback_data)

n = int(input("How many more feedbacks do you want to add? "))

for i in range(n):
    name = input("Enter name: ")
    text = input("Enter feedback: ")

    rating = int(input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

    feedback_data['S_No'].append(feedback_data['S_No'][-1] + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(text)
    feedback_data['Rating'].append(rating)
#Text cleaning
def clean_text(text):
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
    text = text.lower()
    return ' '.join(text.split())   # removes extra/leading/trailing spaces

feedback_data['Feedback'] = [clean_text(f) for f in feedback_data['Feedback']]
print(feedback_data)
#word count insights
# Step 4: Word Count Insights

def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0

    for feedback in feedback_data['Feedback']:
        words_in_feedback = feedback.split()   # break the feedback into a list of words
        if word in words_in_feedback:
            count = count + 1

    return count


print("\nWord Count Insights")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))
# final summary and insights
# Final cleaned dictionary
print("\nCleaned feedback data:")
print(feedback_data)

# Average rating
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("\nAverage rating:", round(average_rating, 2))

# Longest comment by word count
longest_index = 0
max_words = 0
for i, feedback in enumerate(feedback_data['Feedback']):
    if len(feedback.split()) > max_words:
        max_words = len(feedback.split())
        longest_index = i

print("\nLongest feedback:", feedback_data['Feedback'][longest_index])
print("By:", feedback_data['Name'][longest_index], "| Words:", max_words)

# Unique words
unique_words = []
for feedback in feedback_data['Feedback']:
    for word in feedback.split():
        if word not in unique_words:
            unique_words.append(word)

print("\nUnique words:", unique_words)
#sort by rating
combined = zip(feedback_data['S_No'], feedback_data['Name'],
               feedback_data['Feedback'], feedback_data['Rating'])

sorted_entries = sorted(combined, key=lambda entry: entry[3], reverse=True)

print("\nSorted by rating (high to low):")
for s_no, name, feedback, rating in sorted_entries:
    print(rating, "|", s_no, name, ":", feedback)