from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from textblob import TextBlob

def summarizer_feedback(file_path, num_sentences=3):
    with open(file_path, 'r') as file:
        text = file.read()

    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, num_sentences)
    summarized_text = ' '.join(str(sentence) for sentence in summary)
    return summarized_text

def analyze_sentiment(file_path):
    #reads the content
    with open(file_path,'r') as file:
        text = file.readlines()

    positive_count= 0
    negative_count= 0
    netural_count= 0

    for line in text:
        feedback = line.strip()
        if feedback:
            analysis = TextBlob(feedback)
            polarity = analysis.sentiment.polarity

            if polarity > 0:
                positive_count+=1
            elif polarity < 0:
                negative_count +=1
            else:
                netural_count += 1
    return positive_count, negative_count, netural_count
            


file_path = "C:/Users/User/Desktop/majorpp/sample_feedback_25.txt"


summary = summarizer_feedback(file_path, num_sentences=4)
print("\n")
print("Summary of sample_feedback.txt: ")
print(summary)

positive , negative , netural = analyze_sentiment(file_path)
print("\n Sentiment Analysis Results : ")
print(f"Postive Feedback : {positive}")
print(f"Negative Feedback : {negative}")
print(f"Netural Feedback : {netural}")