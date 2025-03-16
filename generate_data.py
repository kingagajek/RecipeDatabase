import random
import pandas as pd
from faker import Faker

fake = Faker()

# Liczba rekordów
NUM_USERS = 5000
NUM_RECIPES = 4000
NUM_INGREDIENTS = 3000
NUM_INSTRUCTIONS = 10000
NUM_RECIPES_INGREDIENTS = 15000
NUM_CUISINE = 10
NUM_MEAL_TYPE = 4
NUM_DIET = 5
NUM_DIFFICULTY = 3

# Prawdziwe wartości dla kuchni, diet, posiłków, składników, poziomów trudności
CUISINES = ["Italian", "Mexican", "French", "Chinese", "Japanese", "Indian", "Thai", "Spanish", "Greek", "Turkish"]
MEAL_TYPES = ["Breakfast", "Lunch", "Dinner", "Snack"]
DIETS = ["Vegetarian", "Vegan", "Gluten-Free", "Keto", "Paleo"]
DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
INGREDIENTS = ["Tomato", "Chicken", "Rice", "Onion", "Garlic", "Beef", "Cheese", "Salt", "Pepper", "Olive Oil",
               "Basil", "Pasta", "Mushroom", "Carrot", "Cucumber", "Yogurt", "Potato", "Milk", "Butter", "Fish"]
RECIPE_NAMES = ["Spaghetti Carbonara", "Chicken Tikka Masala", "Sushi Rolls", "Pad Thai", "Greek Salad", 
                "Tacos al Pastor", "French Onion Soup", "Lasagna", "Pancakes", "Miso Soup"]

# Generowanie użytkowników
users = []
for i in range(1, NUM_USERS + 1):
    users.append({
        "id": i,
        "email": fake.unique.email(),
        "login": fake.unique.user_name(),
        "password": fake.password()
    })

# Tworzenie DataFrame i usunięcie duplikatów
df_users = pd.DataFrame(users)

# Generowanie kuchni
cuisine = [{"id": i + 1, "name": CUISINES[i % len(CUISINES)]} for i in range(NUM_CUISINE)]

# Generowanie rodzajów posiłków
meal_type = [{"id": i + 1, "name": MEAL_TYPES[i % len(MEAL_TYPES)]} for i in range(NUM_MEAL_TYPE)]

# Generowanie typów diet
diet = [{"id": i + 1, "type": DIETS[i % len(DIETS)]} for i in range(NUM_DIET)]

# Generowanie poziomów trudności
difficulty = [{"id": i + 1, "level": DIFFICULTY_LEVELS[i % len(DIFFICULTY_LEVELS)]} for i in range(NUM_DIFFICULTY)]

# Generowanie składników
ingredients = [{"id": i + 1, "name": INGREDIENTS[i % len(INGREDIENTS)]} for i in range(NUM_INGREDIENTS)]

# Generowanie przepisów
recipes = []
for i in range(1, NUM_RECIPES + 1):
    recipes.append({
        "id": i,
        "title": random.choice(RECIPE_NAMES),
        "description": fake.text(),
        "cook_time": random.randint(5, 120),
        "serving_size": random.randint(1, 6),
        "views": random.randint(0, 5000),
        "rating": round(random.uniform(1, 5), 1),
        "id_cuisine": random.randint(1, NUM_CUISINE),
        "id_diet": random.randint(1, NUM_DIET),
        "id_difficulty": random.randint(1, NUM_DIFFICULTY),
        "id_meal_type": random.randint(1, NUM_MEAL_TYPE)
    })

# Generowanie relacji przepisy - składniki
recipes_ingredients = []
for i in range(1, NUM_RECIPES_INGREDIENTS + 1):
    recipes_ingredients.append({
        "id": i,
        "id_recipe": random.randint(1, NUM_RECIPES),
        "id_ingredient": random.randint(1, NUM_INGREDIENTS),
        "quantity": round(random.uniform(0.1, 5), 2),
        "measurement": random.choice(["g", "ml", "tsp", "tbsp", "cup", "piece"])
    })

# Generowanie instrukcji
instructions = []
for i in range(1, NUM_INSTRUCTIONS + 1):
    instructions.append({
        "id": i,
        "recipe_id": random.randint(1, NUM_RECIPES),
        "step_number": random.randint(1, 10),
        "description": fake.sentence(nb_words=8)
    })

# Eksport do CSV
df_users.to_csv("users_cleaned.csv", index=False)
pd.DataFrame(cuisine).to_csv("cuisine.csv", index=False)
pd.DataFrame(meal_type).to_csv("meal_type.csv", index=False)
pd.DataFrame(diet).to_csv("diet.csv", index=False)
pd.DataFrame(difficulty).to_csv("difficulty.csv", index=False)
pd.DataFrame(ingredients).to_csv("ingredients.csv", index=False)
pd.DataFrame(recipes).to_csv("recipes.csv", index=False)
pd.DataFrame(recipes_ingredients).to_csv("recipes_ingredients.csv", index=False)
pd.DataFrame(instructions).to_csv("instructions.csv", index=False)

# Eksport do JSON
df_users.to_json("users_cleaned.json", orient="records")
pd.DataFrame(cuisine).to_json("cuisine.json", orient="records")
pd.DataFrame(meal_type).to_json("meal_type.json", orient="records")
pd.DataFrame(diet).to_json("diet.json", orient="records")
pd.DataFrame(difficulty).to_json("difficulty.json", orient="records")
pd.DataFrame(ingredients).to_json("ingredients.json", orient="records")
pd.DataFrame(recipes).to_json("recipes.json", orient="records")
pd.DataFrame(recipes_ingredients).to_json("recipes_ingredients.json", orient="records")
pd.DataFrame(instructions).to_json("instructions.json", orient="records")

print("✅ Dane wygenerowane, sensowne i zapisane w formatach CSV i JSON!")