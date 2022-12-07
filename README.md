# 🥑 EatMo吃啥 [Healthy Daily Random Diet Plan Generator]()
## ⭐️ Author [Ziqi Zhou](https://github.com/LydiaQ1) and [Tina Zhang](https://github.com/YuchengZhang104)

<p align="center" >
  <samp>
    Trying to keep on a healthy diet ? 
  <br/> Trying to get to a certain weight ? 
    <br/>BUT DON'T KNOW WHAT TO EAT ???
    <br/>EatMo Got This!
  <br/>A randomized recommendation of daily diet plan customized for all goal above.
  </samp>
  <br/>
  <br/>
  <br/>
</p>

## <img src="https://raw.githubusercontent.com/alexnaiman/alexnaiman/master/resources/PusheenCompute.gif" width="70px" /> Our Goal
This program aims to provide users with randomized healthy daily meal plan recommendations that satisfy their dietary goals. These recommendations will not only make sure users can reach their eventual diet goals scientifically, but also the users can have sufficient nutrition for healthy human needs. 

## <img src="https://raw.githubusercontent.com/alexnaiman/alexnaiman/master/resources/Confused_Dog.gif" height="50px" /> Program Overview
The program is presented in a website, users can simply inputing their age, gender, height, weight, activity level, and weight goal. As a result, the users can conveniently return a recommended list of food that covers  all 7 categories: fruits, vegetables, dairy eggs, drinks, fish, grains pluses, meat (all in a 100 grams or 100 milliliters unit). Since the  recommendation is generated randomly, if the users are not satisfied with the recommended items in the list, all they need to do is to just refresh the web page and a new list will be generated. 

We utilize API to get the information about the matched calories based on user provided age, gender, height, weight, and activity level. And we also use the data provided by MYPROTEIN's Food Calories Chart to create a set of csv files that contain the calories information (Kcal per 100g) about each food item across all 7 categories. 

## <img src="https://raw.githubusercontent.com/alexnaiman/alexnaiman/master/resources/pug_dance.gif" width="60px" /> User Handbook
### Step 1
Open VisualStudio Code, install [Flask](https://flask.palletsprojects.com/en/2.2.x/).
### Step 2
Download all files in this repository (entire data folder, back.py, front.py, index.html, results.html), open and save the files in VS Code.
### Step 3
Run front.py in VS Code, you should see this terminal:
![This is an image](https://ibb.co/557nwKz)
Once you see this, control(command) + right click on http://127.0.0.1:5000 to access the app website.
### Step 4
Opening up the website, you will see on the page that there are 6 parameters that await your INPUTS: Age (integer only), Gender ("female" or "male" in lowercase only), Height (integer only), Weight (integer only), Activity Level (select from drop-down list only), and Diet Goal (select from drop-down list only).
![This is an image](https://ibb.co/LdXtLz3)
### Step 5
After you've inputed all information required on the page, please CLICK the dark pink button below "Generate your daily diet plan!".  You will then be directed to a new web page that shows the newly generated daily meal plan, a recommendation that is created based on your physical metrics and dietary goals.
![This is an image](https://ibb.co/4J15DMb)
### Step 6
After you clicked the dark pink button "Generate your daily diet plan!",  you know will see this web page, and there you go with your daily meal plan that is customized using your physical metrics and dietary goals. If you do not like the food items in this meal plan, simply refresh the page, EatMo will automatically generate a new meal plan that is also randomized, and created based on your physical metrics and dietary goals.
![This is an image](https://ibb.co/GvDxMXK)

## <img src="https://raw.githubusercontent.com/alexnaiman/alexnaiman/master/resources/cool_duck.gif" width="60px" /> Parameters
<img src="https://raw.githubusercontent.com/alexnaiman/alexnaiman/master/resources/party_parrot.gif" height="35px" /> Here below are a detailed explanation about the parameters EatMo has used in its program code:

### Input:
Age: 
It should use to input the user’s age. It must be an integer. It cannot be negative or bigger than 80. If the inputed number is negative, the program will run automatically its absolute value; if the inputed number is not an integer, the input column will show as "Please Input Valid Value"; if the inputed number is over 80, it will show as "Error".
Gender:
It should use to input the user’s gender. It can only be male or female in lowercase.
Height:
It should use to input the user’s height. It must be integer. It cannot be smaller than 130 or bigger than 230. The unit of weight is in cm.  If the inputed number is negative, the program will run automatically its absolute value; if the inputed number is not an integer, the input column will show as "Please Input Valid Value"; if the inputed number is smaller than 130 or bigger than 230, it will show as "Error"
Weight:
It should use to input the user’s mass. It must be an integer. It cannot be smaller than 40 or bigger than 160. The unit of weight is in kg. If the inputed number is negative, the program will run automatically its absolute value; if the inputed number is not an integer, the input column will show as "Please Input Valid Value"; if the inputed number is smaller than 40 or bigger than 160, it will show as "Error".
Activity Level:
There are 7 options:
Sedentary: little or no exercise
Exercise 1-3 times/week
Exercise 4-5 times/week
Daily exercise or intense exercise 3-4 times/week
Intense exercise 6-7 times/week
Very intense exercise daily, or physical job
Goals:
maintain weight
Mild weight loss
Weight loss
Extreme weight loss
Mild weight gain
Weight gain
Extreme weight gain

### Output:
Vegetables: [item name] * 100g
Meat: [item name] * 100g
Fish: [item name] * 100g
Dairy and eggs: [item name] * 100g
Grain and pulses: [item name] * 100g
Fruit: [item name] * 100g
Drink: [item name] * 100ml
Your calories goal is [number], this plan's total calories is [number].

---
⭐️ From [Ziqi Zhou](https://github.com/LydiaQ1) and [Tina Zhang](https://github.com/YuchengZhang104)