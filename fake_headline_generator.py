import random

subjects = [
    "Salman Khan", "Nirmala Sitharaman", "A group of monkeys", "An auto rickshaw driver from Delhi",
    "Virat Kohli", "Elon Musk", "Narendra Modi", "A lost tourist", "Shah Rukh Khan",
    "A goat wearing sunglasses", "The Indian cricket team", "A pizza delivery guy",
    "A talking parrot", "A hacker from Bangalore", "A Bollywood director"
]

actions = [
    "launches a new project", "cancels an event", "dances with fans", "orders street food", "celebrates a victory",
    "steals the spotlight", "paints a masterpiece", "announces a surprise", "eats a giant burger",
    "destroys a world record", "hugs strangers", "sings to the crowd", "argues with reporters",
    "challenges a rival", "photobombs a selfie"
]

places_or_things = [
    "at the Red Fort", "in Mumbai local trains", "while holding a plate of samosas", "inside Parliament", "at the Ganga Ghat",
    "during an IPL match", "on top of the Himalayas", "at a crowded market", "inside a spaceship",
    "in front of the Gateway of India", "inside a pani puri stall", "at a metro station",
    "while riding a camel", "at India Gate", "during a live TV interview"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (Yes/No): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have fun!")
