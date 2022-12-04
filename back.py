import json
import http.client
import random
import csv


# Get the Calorie with provided body facts

def get_fitness_api(url):
    conn = http.client.HTTPSConnection("fitness-calculator.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "e1b62cc7f9msh053d2e6f7ea766ap1e742djsnd1d93f380d2e",
        'X-RapidAPI-Host': "fitness-calculator.p.rapidapi.com"
    }
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def str_dict(str):
    diction = json.loads(str)
    return diction


def get_goal_cal(goal, diction):
    d = dict()
    d = diction

    if goal == "maintain weight":
        cal = d['data']["goals"]["maintain weight"]
    if goal == "Mild weight loss":
        cal = d["data"]["goals"]["Mild weight loss"]["calory"]
    if goal == "Weight loss":
        cal = d["data"]["goals"]["Weight loss"]["calory"]
    if goal == "Extreme weight loss":
        cal = d["data"]["goals"]["Extreme weight loss"]["calory"]
    if goal == "Mild weight gain":
        cal = d["data"]["goals"]["Mild weight gain"]["calory"]
    if goal == "Weight gain":
        cal = d["data"]["goals"]["Weight gain"]["calory"]
    if goal == "Extreme weight gain":
        cal = d["data"]["goals"]["Extreme weight gain"]["calory"]
    return cal


def get_daily_cal(age, gender, height, weight, activitylevel, goal):
    age = int(age)
    gender = gender.lower()
    height = int(height)
    weight = int(weight)
    activitylevel = activitylevel.lower()

    url = f"/dailycalorie?age={age}&gender={gender}&height={height}&weight={weight}&activitylevel={activitylevel}"
    text = get_fitness_api(url)
    diction = str_dict(text)
    cal = get_goal_cal(goal, diction)
    return cal

# print(get_daily_cal(21,"female",164,52,"level_1","Mild weight loss"))

# Generate dietary suggestion according to the calories goal


def csv_read(category):
    with open(f'data/{category}.csv', mode='r', encoding='utf-8-sig') as csvfile:
        foodlistread = csv.DictReader(csvfile, fieldnames=['food', 'calories'])
        foodlist = {}
        idx = 0
        for row in foodlistread:
            foodlist[str(idx)] = row
            idx = idx + 1
        return foodlist


def random_food(category):
    d = dict()
    d = csv_read(category)
    choice = random.choice(list(d.items()))
    return choice


def unpack(tuple):
    (num, pair) = tuple
    return pair


def all_category(cal):
    totalcal = 0
    while abs(totalcal-cal) > 50:
        fruit = dict(unpack(random_food("fruit")))
        vegetables = dict(unpack(random_food("vegetables")))
        dairy_eggs = dict(unpack(random_food("dairy_eggs")))
        drinks = dict(unpack(random_food("drinks")))
        fish = dict(unpack(random_food("fish")))
        grains_pulses = dict(unpack(random_food("grains_pulses")))
        meat = dict(unpack(random_food("meat")))

        d = dict()
        d = fruit
        fruitcal = float(d['calories'])
        fruitname = d['food']
        d = vegetables
        vegecal = float(d['calories'])
        vegename = d['food']
        d = dairy_eggs
        dairycal = float(d['calories'])
        dairyname = d['food']
        d = drinks
        drinkcal = float(d['calories'])
        drinkname = d['food']
        d = fish
        fishcal = float(d['calories'])
        fishname = d['food']
        d = grains_pulses
        graincal = float(d['calories'])
        grainname = d['food']
        d = meat
        meatcal = float(d['calories'])
        meatname = d['food']

        totalcal = fruitcal + vegecal + dairycal + drinkcal + fishcal + graincal + meatcal

    return f"Your diet plan is:\nVegetables:{vegename} * 100g\nMeat:{meatname} * 100g\nFish:{fishname} * 100g\nDairy and eggs:{dairyname} * 100g\nGrain and pulses:{grainname} * 100g\nFruit:{fruitname} * 100g\nDrink:{drinkname} * 100ml\nYour calories goal is {cal}, this plan's total calories is {totalcal}."


def main():
    """

    """
    age = 21
    gender = "Female"
    height = 164
    weight = 52
    activitylevel = "level_2"
    goal = "Weight loss"
    cal = float(get_daily_cal(age, gender, height, weight, activitylevel, goal))
    print(all_category(cal))


if __name__ == '__main__':
    main()
