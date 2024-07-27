import sqlite3

conn = sqlite3.connect('food.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS foods
               (id INTEGER PRIMARY KEY, name TEXT, calories INTEGER)''')


def create_food(name, calories):
    cur.execute("INSERT INTO foods (name, calories) VALUES (?, ?)", (name, calories))
    conn.commit()

def read_foods():
    cur.execute("SELECT * FROM foods")
    return cur.fetchall()

def update_food(food_id, name, calories):
    cur.execute("UPDATE foods SET name = ?, calories = ? WHERE id = ?", (name, calories, food_id))
    conn.commit()

def delete_food(food_id):
    cur.execute("DELETE FROM foods WHERE id = ?", (food_id,))
    conn.commit()

create_food('Apple', 95)
create_food('Banana', 105)
create_food('Carrot', 25)

print("All food items:")
foods = read_foods()
for food in foods:
    print(food)

update_food(1, 'Apple', 100)

print("All food items after update:")
foods = read_foods()
for food in foods:
    print(food)

delete_food(2)

print("All food items after deletion:")
foods = read_foods()
for food in foods:
    print(food)

conn.close()
