import random

# Dictionary mapping tarot card names to interpretations
tarot_interpretations = {
    "The Fool": "New beginnings, innocence, spontaneity, a leap of faith",
    "The Magician": "Manifestation, resourcefulness, power, action, communication",
    "The High Priestess": "Intuition, subconscious mind, mystery, understanding, wisdom",
    "The Empress": "Fertility, nurturing, abundance, nature, femininity",
    "The Emperor": "Authority, stability, leadership, control, structure",
    "The Hierophant": "Tradition, conformity, education, spiritual guidance, belief system",
    "The Lovers": "Love, relationships, harmony, choices, union",
    "The Chariot": "Willpower, determination, victory, control, progress",
    "Strength": "Courage, inner strength, patience, compassion, self-control",
    "The Hermit": "Soul-searching, introspection, guidance, solitude, inner wisdom",
    "Wheel of Fortune": "Luck, destiny, cycles, fate, change",
    "Justice": "Fairness, balance, truth, accountability, legal matters",
    "The Hanged Man": "Surrender, release, suspension, perspective, sacrifice",
    "Death": "Endings, transformation, change, rebirth, letting go",
    "Temperance": "Balance, moderation, harmony, patience, blending opposites",
    "The Devil": "Materialism, bondage, addiction, limitation, temptation",
    "The Tower": "Chaos, upheaval, sudden change, revelation, destruction",
    "The Star": "Hope, inspiration, renewal, optimism, spirituality",
    "The Moon": "Illusion, fear, confusion, intuition, subconscious mind",
    "The Sun": "Success, joy, vitality, enlightenment, happiness",
    "Judgment": "Rebirth, redemption, awakening, forgiveness, evaluation",
    "The World": "Completion, fulfillment, achievement, integration, wholeness",
    "Ace of Wands": "Inspiration, new opportunities, potential, creativity",
    "Two of Wands": "Planning, preparation, choices, future possibilities",
    "Three of Wands": "Exploration, foresight, expansion, progress",
    "Four of Wands": "Celebration, harmony, homecoming, community",
    "Five of Wands": "Competition, conflict, challenges, disagreement",
    "Six of Wands": "Victory, recognition, success, achievement",
    "Seven of Wands": "Defensiveness, perseverance, standing your ground",
    "Eight of Wands": "Swiftness, progress, movement, communication",
    "Nine of Wands": "Resilience, determination, persistence, strength",
    "Ten of Wands": "Burden, responsibility, overwhelm, struggle",
    "Ace of Cups": "New feelings, emotional beginnings, intuition, love",
    "Two of Cups": "Partnership, connection, love, harmony, mutual attraction",
    "Three of Cups": "Celebration, friendship, community, joy, reunions",
    "Four of Cups": "Discontent, apathy, introspection, contemplation",
    "Five of Cups": "Loss, disappointment, regret, sorrow, focusing on the negative",
    "Six of Cups": "Nostalgia, childhood memories, innocence, reunion",
    "Seven of Cups": "Fantasy, choices, imagination, daydreaming, options",
    "Eight of Cups": "Withdrawal, abandonment, moving on, seeking inner fulfillment",
    "Nine of Cups": "Contentment, emotional satisfaction, wishes fulfilled, happiness",
    "Ten of Cups": "Harmony, family, emotional fulfillment, joy, happiness",
    "Ace of Swords": "Mental clarity, truth, breakthrough, new ideas, mental power",
    "Two of Swords": "Indecision, choices, stalemate, avoidance, compromise",
    "Three of Swords": "Heartbreak, sorrow, grief, emotional pain, separation",
    "Four of Swords": "Rest, relaxation, recuperation, healing, contemplation",
    "Five of Swords": "Conflict, defeat, loss, betrayal, humiliation",
    "Six of Swords": "Transition, moving on, recovery, leaving difficulties behind",
    "Seven of Swords": "Deception, dishonesty, sneakiness, evasion, strategy",
    "Eight of Swords": "Restriction, imprisonment, self-imposed limitations, feeling trapped",
    "Nine of Swords": "Anxiety, fear, nightmares, worry, guilt",
    "Ten of Swords": "Betrayal, rock bottom, failure, crisis, pain, endings",
    "Ace of Pentacles": "Manifestation, prosperity, new opportunity, wealth, abundance",
    "Two of Pentacles": "Balance, juggling priorities, adaptability, flexibility",
    "Three of Pentacles": "Collaboration, teamwork, skill, craftsmanship, recognition",
    "Four of Pentacles": "Greed, possessiveness, holding on, security, control",
    "Five of Pentacles": "Hardship, poverty, adversity, isolation, financial loss",
    "Six of Pentacles": "Generosity, charity, giving, receiving, sharing wealth",
    "Seven of Pentacles": "Patience, investment, waiting, assessment, long-term vision",
    "Eight of Pentacles": "Diligence, craftsmanship, skill development, detail-oriented work",
    "Nine of Pentacles": "Abundance, self-reliance, luxury, independence, financial security",
    "Ten of Pentacles": "Wealth, family, inheritance, legacy, long-term success",
    "The Fool (Reversed)": "Foolishness, recklessness, naivety, missed opportunities",
    "The Magician (Reversed)": "Manipulation, deceit, trickery, misuse of power",
    "The High Priestess (Reversed)": "Hidden agendas, secrets revealed, confusion, lack of intuition",
    "The Empress (Reversed)": "Neglect, dependency, creative block, lack of nurturing",
    "The Emperor (Reversed)": "Domination, tyranny, instability, lack of authority",
    "The Hierophant (Reversed)": "Rebellion, unconventional beliefs, challenging tradition",
    "The Lovers (Reversed)": "Disharmony, separation, imbalance, difficult choices",
    "The Chariot (Reversed)": "Lack of direction, obstacles, failure to move forward",
    "Strength (Reversed)": "Weakness, self-doubt, insecurity, lack of control",
    "The Hermit (Reversed)": "Isolation, loneliness, withdrawal, refusal of guidance",
    "Wheel of Fortune (Reversed)": "Bad luck, setbacks, delays, external forces at play",
    "Justice (Reversed)": "Injustice, unfairness, legal issues unresolved, imbalance",
    "The Hanged Man (Reversed)": "Resistance to change, delays in progress, missed opportunities",
    "Death (Reversed)": "Resistance to change, stagnation, fear of endings",
    "Temperance (Reversed)": "Imbalance, extremism, lack of moderation, impatience",
    "The Devil (Reversed)": "Release from bondage, freedom, breaking free from addiction",
    "The Tower (Reversed)": "Avoidance of disaster, gradual change, personal transformation",
    "The Star (Reversed)": "Hopelessness, lack of faith, despair, disappointment",
    "The Moon (Reversed)": "Confusion, fear, anxiety, illusion, deception",
    "The Sun (Reversed)": "Unhappiness, negativity, lack of clarity, blockage of joy",
    "Judgement (Reversed)": "Self-doubt, self-criticism, fear of judgment, avoidance",
    "The World (Reversed)": "Incompletion, lack of closure, feeling stuck, unfinished business",
    "Ace of Wands (Reversed)": "Lack of inspiration, delays in creative projects, missed opportunities",
    "Two of Wands (Reversed)": "Lack of planning, indecision, fear of change, inability to move forward",
    "Three of Wands (Reversed)": "Lack of foresight, delays in progress, missed opportunities",
    "Four of Wands (Reversed)": "Instability, disunity, home conflicts, lack of celebration",
    "Five of Wands (Reversed)": "Conflict resolution, compromise, coming to terms, cooperation",
    "Six of Wands (Reversed)": "Ego issues, lack of recognition, arrogance, failure to succeed",
    "Seven of Wands (Reversed)": "Giving up, surrender, overwhelmed by opposition, backing down",
    "Eight of Wands (Reversed)": "Delays, frustration, lack of progress, obstacles in communication",
    "Nine of Wands (Reversed)": "Exhaustion, burnout, feeling overwhelmed, giving up too easily",
    "Ten of Wands (Reversed)": "Burden released, delegation, letting go, sharing responsibilities",
    "Ace of Cups (Reversed)": "Blocked emotions, emotional emptiness, lack of connection",
    "Two of Cups (Reversed)": "Disharmony, imbalance in relationships, separation, disagreement",
    "Three of Cups (Reversed)": "Overindulgence, gossip, shallow friendships, celebration gone wrong",
    "Four of Cups (Reversed)": "Acceptance, moving on, new perspectives, coming out of a funk",
    "Five of Cups (Reversed)": "Acceptance, forgiveness, moving on, finding the silver lining",
    "Six of Cups (Reversed)": "Dwelling on the past, nostalgia holding you back, inability to move forward",
    "Seven of Cups (Reversed)": "Clarity, focus, making decisions, seeing through illusions",
    "Eight of Cups (Reversed)": "Return, reconciliation, choosing to stay, second chances",
    "Nine of Cups (Reversed)": "Superficial happiness, dissatisfaction, chasing empty pleasures",
    "Ten of Cups (Reversed)": "Dysfunctional family, shattered dreams, broken home, discontent",
    "Ace of Swords (Reversed)": "Confusion, chaos, lack of clarity, mental fog, miscommunication",
    "Two of Swords (Reversed)": "Indecision, stalemate, avoiding conflict, facing the truth",
    "Three of Swords (Reversed)": "Healing, recovery, forgiveness, moving on from heartbreak",
    "Four of Swords (Reversed)": "Restlessness, burnout, lack of recovery, inability to rest",
    "Five of Swords (Reversed)": "Reconciliation, making amends, forgiveness, releasing grudges",
    "Six of Swords (Reversed)": "Resistance to change, refusing to move on, emotional baggage",
    "Seven of Swords (Reversed)": "Honesty, coming clean, facing consequences, abandoning deceit",
    "Eight of Swords (Reversed)": "Freedom, release, breaking free from constraints, finding solutions",
    "Nine of Swords (Reversed)": "Overcoming anxiety, finding peace of mind, inner calmness",
    "Ten of Swords (Reversed)": "Recovery, healing, hitting rock bottom, learning from mistakes",
    "Ace of Pentacles (Reversed)": "Lost opportunity, lack of abundance, missed chance for prosperity",
    "Two of Pentacles (Reversed)": "Imbalance, disorganization, overwhelmed by responsibilities",
    "Three of Pentacles (Reversed)": "Lack of teamwork, criticism, not valuing skills or effort",
    "Four of Pentacles (Reversed)": "Letting go of greed, generosity, sharing resources, loosening control",
    "Five of Pentacles (Reversed)": "Recovery, finding help, turning things around, feeling supported",
    "Six of Pentacles (Reversed)": "Selfishness, charity with strings attached, unfair distribution",
    "Seven of Pentacles (Reversed)": "Impatience, lack of progress, wasted effort, impulsive decisions",
    "Eight of Pentacles (Reversed)": "Sloppiness, lack of attention to detail, low-quality work",
    "Nine of Pentacles (Reversed)": "Financial setbacks, dependence, lack of independence, extravagance",
    "Ten of Pentacles (Reversed": "Family conflict, instability, loss of inheritance, financial problems",
        }

# List of tarot card names
tarot_cards = list(tarot_interpretations.keys())

def perform_tarot_reading():
    # Shuffle the tarot cards
    random.shuffle(tarot_cards)
    
    # Select 10 cards for the reading
    reading = tarot_cards[:10]
    
    # Print the reading with interpretations
    print("Your 10-card tarot reading with interpretations:")
    for i, card in enumerate(reading, 1):
        interpretation = tarot_interpretations[card]
        if i==1:
            print(f"{i}. Significator or Present Situation:")
        if i==2:
            print(f"{i}. Crossing Card or Challenge:")
        if i==3:
            print(f"{i}. Foundation or Root Cause:")
        if i==4:
            print(f"{i}. Recent Past:")
        if i==5:
            print(f"{i}. Immediate Future:")
        if i==6:
            print(f"{i}. Distant Past or Subconscious Influences:")
        if i==7:
            print(f"{i}. Querent's Attitude or Self-Perception:")
        if i==8:
            print(f"{i}. External Influences:")
        if i==9:
            print(f"{i}. Hopes and Fears:")
        if i==10:
            print(f"{i}. Outcome or Final Advice:")
        print(f"{card}: {interpretation}")
if __name__ == "__main__":
    perform_tarot_reading()
