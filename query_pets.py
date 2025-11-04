# Rafi Talukder Assignment_10
import sqlite3
"""---------------------------------------------------------------------------------"""
def main(): # This connects to pets.db
    conn = sqlite3.connect("pets.db")
    cur = conn.cursor()

    while True:
        user_input = input("Enter a person's ID (or -1 to exit): ")

        try:
            person_id = int(user_input)
        except ValueError:
            print("Oh oh, Please enter a valid number.")
            continue

        if person_id == -1:
            print("Okay me sleepy, time to exit program. Goodbye!=)")
            break

        # This retrieves a person's information
        cur.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cur.fetchone()

        if not person:
            print("Person is not found. oh oh")
            continue

        first_name, last_name, age = person
        print(f"{first_name} {last_name}, {age} years old")

        # Retrieve pets for that person
        cur.execute("""
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cur.fetchall()

        if pets:
            for (name, breed, pet_age, dead) in pets:
                status = "deceased" if dead == 1 else "alive"
                print(f"  - Owned {name}, a {breed}, {pet_age} years old ({status})")
        else:
            print("No pets found for this person. Womp womp")

    conn.close()
"""---------------------------------------------------------------------------------"""
if __name__ == "__main__":
    print("Running query_pets.py")
    main()

#What is the purpose of the person_pet table?
""" the person_pet table exists to represent the relationship between people and pets. This is a many to many relationship."""
"""each person can own multiple pets and I think each pet could also potentially belong to multiple people"""