import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer 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"}

def classify_sentences(source,sentences):
    payload = {
        "inputs": {
            "source_sentence": source,
            "sentences": sentences
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Classify each category against the provided data
def tagClassify(source):
    data = {
    "Personal": ["Invitation to my birthday party!",
                 "Let's plan a weekend getaway.",
                 "Updates about family reunion.",
                 "Movie night at my place this Friday!",
                 "Let's go hiking this weekend.",
                 "Dinner at the new restaurant downtown.",
                 "Picnic in the park next Saturday!",
                 "Game night at my place next weekend.",
                 "Barbecue party at the beach!",
                 "Road trip to the mountains.",
                 "Karaoke night this Saturday!",
                 "Visit to the art museum on Sunday.",
                 "Potluck dinner at my house.",
                 "Beach bonfire party!",
                 "Wine tasting event next Friday.",
                 "Book club meeting this Thursday.",
                 "Exploring the local farmer's market.",
                 "Biking adventure in the countryside.",
                 "Outdoor yoga session in the park.",
                 "Crafting workshop this weekend."],
    "Professional": ["Meeting agenda for next week.",
                      "Proposal for new project.",
                      "Follow-up on client meeting.",
                      "Request for feedback on recent presentation.",
                      "Schedule for team training session.",
                      "Agenda for quarterly review meeting.",
                      "Budget proposal for upcoming fiscal year.",
                      "Status update on ongoing projects.",
                      "Request for collaboration on research paper.",
                      "Planning for upcoming trade show.",
                      "Agenda for monthly department meeting.",
                      "Proposal for process improvement.",
                      "Request for input on strategic planning.",
                      "Training schedule for new software rollout.",
                      "Request for partnership opportunity.",
                      "Project brainstorming session.",
                      "Updates on industry trends.",
                      "Request for participation in survey.",
                      "Planning for company retreat.",
                      "Proposal for client workshop series."]
}

    max_category = {}
    for category, sentences in data.items():
        classified_sentences = classify_sentences(source,sentences)
        max_category[category] = max(classified_sentences)

    # Find the category with the highest parameter value
    result_category = max(max_category, key=max_category.get)

    return result_category

