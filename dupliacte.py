import pandas as pd
import random
from faker import Faker

fake = Faker()

# Liczba rekordów
NUM_INGREDIENTS = 3000

# Lista unikalnych składników
INGREDIENTS = [
    "Tomato", "Chicken", "Rice", "Onion", "Garlic", "Beef", "Cheese", "Salt", "Pepper", "Olive Oil",
    "Basil", "Pasta", "Mushroom", "Carrot", "Cucumber", "Yogurt", "Potato", "Milk", "Butter", "Fish",
    "Egg", "Lemon", "Lettuce", "Honey", "Cinnamon", "Paprika", "Chili", "Coconut", "Tofu", "Shrimp"
]

# Generowanie unikalnych składników
unique_ingredients = set()
while len(unique_ingredients) < NUM_INGREDIENTS:
    unique_ingredients.add(random.choice(INGREDIENTS) + " " + fake.word())

ingredients = [{"id": i + 1, "name": name} for i, name in enumerate(unique_ingredients)]

# Tworzenie DataFrame i zapisanie do CSV oraz JSON
df_ingredients = pd.DataFrame(ingredients)
df_ingredients.to_csv("ingredients.csv", index=False)
df_ingredients.to_json("ingredients.json", orient="records", indent=4)

print("✅ Wygenerowano ponad 3000 unikalnych składników bez duplikatów!")