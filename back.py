import json
import http.client
import random
import csv


# Get the Calorie with provided body facts

def get_fitness_api(url):
    """
    Given a properly formatted URL, return a string containing the response to that request.
    """
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
    """
    Given a string, convert the string into dictionary.
    """
    diction = json.loads(str)
    return diction


def get_goal_cal(goal, diction):
    """
    Given a weight control goal and the dictionary, return the corresponding daily calories requirement to that goal.
    """
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
    """
    Given the body facts including age, gender, height, weight, activitylevel, return a properly formatted url.
    Then with the given weight control goal, return the daily calories requirement of this person with the input body facts and goal.
    """
    age = abs(int(age))
    gender = gender.lower()
    height = abs(int(height))
    weight = abs(int(weight))
    activitylevel = activitylevel.lower()

    url = f"/dailycalorie?age={age}&gender={gender}&height={height}&weight={weight}&activitylevel={activitylevel}"
    text = get_fitness_api(url)
    diction = str_dict(text)
    cal = get_goal_cal(goal, diction)
    return cal


# print(get_daily_cal(21,"female",164,52,"level_1","Mild weight loss"))

# Generate dietary suggestion according to the calories goal


def csv_read(category):
    """
    Given a category of the food, read its csv and convert it into dictionary with two fieldnames of 'food' and 'calories', 
    each pair with a number index.
    """
    with open(f'data/{category}.csv', mode='r', encoding='utf-8-sig') as csvfile:
        foodlistread = csv.DictReader(csvfile, fieldnames=['food', 'calories'])
        foodlist = {}
        idx = 0
        for row in foodlistread:
            foodlist[str(idx)] = row
            idx = idx + 1
        return foodlist

# chck = csv_read("fruit")
# res = type(chck)
# print(res)

def random_food(category):
    """
    Given a category of the food, randomly return an item in that category.
    """
    d = dict()
    d = csv_read(category)
    choice = random.choice(list(d.items()))
    return choice

# chck2 = random_food("fruit")
# res = type(chck2)
# print(res)

def unpack(tuple):
    """
    Given a tuple (randomly returned item in previous function),
    convert the tuple into dictionary that only contain the food pair that has its name and calories.
    """
    (num, pair) = tuple
    return pair

# chck3 = unpack(chck2)
# res = type(chck3)
# print(res)

def all_category(cal):
    """
    Given a daily calories requirement, return a randomly chose diet plan containing one food from each food category.
    The generated diet plan will have a total calories that is no more or less than 50 calories of the calories requirement.
    """
    totalcal = 0
    while abs(totalcal-cal) > 50:
        fruit = unpack(random_food("fruit"))
        vegetables = unpack(random_food("vegetables"))
        dairy_eggs = unpack(random_food("dairy_eggs"))
        drinks = unpack(random_food("drinks"))
        fish = unpack(random_food("fish"))
        grains_pulses = unpack(random_food("grains_pulses"))
        meat = unpack(random_food("meat"))

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

    return f"Your diet plan is:\nVegetables: {vegename} * 100g\nMeat: {meatname} * 100g\nFish: {fishname} * 100g\nDairy and eggs: {dairyname} * 100g\nGrain and pulses: {grainname} * 100g\nFruit: {fruitname} * 100g\nDrink: {drinkname} * 100ml\nYour calories goal is {cal}, this plan's total calories is {totalcal}.\nIf you want to generate another plan, please refresh this page."


def main():
    """
    Test all the functions here.
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
