class Age(int):

        # Question 1
    def adult(self):
        if self >= 21:
            return 'Adult'
        return 'Minor'

        # Question 24
    def mid_class(self, age2, age3):
        average = (self + age2 + age3) / 3.
        if average < 25: return average, "Youth Class"
        elif average < 40: return average, "Adult Class"
        return average, "Senior Class"

class Number(int):

        # Question 2
    def greaterNumber(self, number2, number3):
            self.number2 = number2
            self.number3 = number3
            if self.number2 > self and self.number2 > self.number3:
                return self.number2
            elif self.number3 > self and self.number3 > self.number2:
                return self.number3
            return self

         # Question 8
    def positive(self):
        if self >= 0:
            return 'Positive'
        return 'Negative'

        #Question 23
    def full_name(self):
        hundred = self / 100
        self = self % 100
        ten = self / 10
        unit = self % 10
        sentence = ''
        if hundred != 0:
            sentence += str(hundred) + ' hundred' + str(hundred > 1 and 's' or '')
            if ten !=0:
                if unit !=0: sentence += ', '
            elif unit !=0 : sentence += ' e '
        if ten != 0 :
            sentence += str(ten) + ' ten' + str(ten > 1 and 's' or '')
            if unit != 0: sentence += ' e '
        if unit != 0 :
            sentence += str(unit) + ' unit' + str(unit > 1 and 's' or '')
        return sentence

class Measure(float):

        # Question 3
    def metersToCent(self):
        return self*100

        # Question 4
    def cube_area(self,length, width, height):
        self.length = length
        self.width = width
        self.height = height
        return self.length * self.width * self.height

        # Question 22
    def type_triangle(self, side1, side2, side3):
        if (side1 < sum([side2, side3])) and (side2 < sum([side1, side3])) and \
           (side3 < sum([side1, side2])): exists = True
        else: exists = False

        if exists == True:
            if side1 == side2 == side3: return "Triangle Exists", "Equilateral"
            elif side1 != side2 != side3 != side1:
                return "Triangle Exists", "Scalene"
            return "Triangle Exists", "Isosceles"
        return "Triangle doesn't Exists"

class PersonalData(str):

        # Question 5
    def ideal_weight(self,sex, height, weight):
        self.height = height
        self.weight = weight
        self.sex = sex
        if self.sex == 'F':
            right_weight = (62.1 * self.height) - 44.7
        elif self.sex == 'M':
            right_weight = (72.7 * self.height) - 58

        if self.weight > right_weight:
            return "acima do peso ideal"
        elif self.weight < right_weight:
            return "abaixo do peso ideal"
        return "no peso ideal"

        # Question 9
    def sex_person(self):
        if self.lower() == 'f':
            return 'Female'
        elif self.lower() == 'm':
            return 'Male'
        return 'Invalid sex'

class Fish(float):

        # Question 6
    def penalty(self):
        if self <= 50.00:
            return 0, 0
        return self - 50, ((self-50.00)*4.00)

class Ink(float):

        # Question 7
    def amount(self):
        litros = self / 6.
        return litros

    def buying_cans(self, litros):
        cans = int(litros / 18.)
        if litros % 18.0 != 0:
            cans += 1
        return cans, cans * 80

    def buying_gallons(self, litros):
        gallons = int(litros / 3.6)
        if litros % 3.6 != 0:
            gallons += 1
        return gallons, gallons * 25

class Year(int):

        # Question 10
    def leap_year(self):
        if (((self % 4 == 0) and (self % 100 != 0)) or (self % 400 == 0)):
            return 'Leap Year'
        return 'Non-Leap Year'

class Letter(str):

        # Question 11
    def vowel(self):
        if self.lower() == ('a' or 'e' or 'i' or 'o' or 'u'):
            return 'Vowel'
        return 'Consonant'

class Average(float):

        # Question 12
    def concept(self, other):
        if (self + other) / 2 < 7:
            return 'Disapproved'
        elif (self + other) / 2 < 10:
            return 'Approved'
        return 'Pass with Distinction'

        # Question 20
    def letter_concept(self, other):
        media = (self + other) / 2
        if media  <= 4.00:  return media, "E", "Disapproved"
        elif media <= 6.00: return media, "D", "Disapproved"
        elif media <= 7.50: return media, "C", "Approved"
        elif media <= 9.00: return media, "B", "Approved"
        return media, "A", "Approved"


class Price(float):

        # Question 13
    def cheaper(self, price2, price3):
            return min(self, price2, price3)


        # Question 19
    def provenance(self, provenance):
        if provenance <= 8:
            provenance_= {1:'South', 2:'North', 3:'East', 4:'West', 5 or 6:'Northeast', 7 or 8:'Midwest'}
            return '%2.2f   -   %s'%(self, provenance_[provenance])
        return '%2.2f   -   Imported'%(self)

class Date_time(str):

        # Question 14
    def day_shift(self):
        if self.upper() == 'M':
            return "Good Morning!"
        elif self.upper() == 'V':
            return "Good Afternoon!"
        elif self.upper() == 'N':
            return "Good Night!"
        return "Invalid!"

        # Question 18
    def day_week(self):
        self = int(self)
        if self <=7:
            week = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
            return week[self]
        return 'Invalid'

class Salary(float):

        # Question 16
    def percentage(self):
        if self <= 280.00:
            return '20%'
        elif self <= 700.00:
            return '15%'
        elif self <= 1500.00:
            return '10%'
        return '5%'

    def increase(self):
        if self <= 280.00:
            return self * 0.2
        elif self <= 700.00:
            return self * 0.15
        elif self <= 1500.00:
            return self * 0.1
        return self * 0.05

    def new_salary(self):
        if self <= 280.00:
            return self * 1.2
        elif self <= 700.00:
            return self * 0.15 + self
        elif self <= 1500.00:
            return self * 0.1 + self
        return self * 0.05 + self

        # Question 17

    def gross_wage(self,value_time, hour_months):
        self = value_time * hour_months
        return self

    def IR_Discount(self):
        if self <= 900.00:
            return 'Free'
        elif self <= 1500.00:
            return self * 0.05
        elif self <= 2500.00:
            return self * 0.1
        return self * 0.2

    def INSS_Discount(self):
        return self * 0.1

    def FGTS_Discount(self):
        return self * 0.11

    def total_Discounts(self):
        return (self * 0.03 + self.IR_Discount() + self.INSS_Discount())

    def final_salary(self):
        return self - self.total_Discounts()

