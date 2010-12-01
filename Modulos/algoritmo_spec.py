import unittest
from should_dsl import should
from algoritmo import Age, Number, Measure, PersonalData, Fish, Ink, Year, Letter, Average, Price, Date_time, Salary


class TestAlgoritmo(unittest.TestCase):
        # Question 1
    def test_it_checks_if_self_is_adult(self):
        Age(0).adult() |should| equal_to ('Minor')
        Age(22).adult() |should| equal_to ('Adult')
        Age(19).adult() |should| equal_to ('Minor')
        Age(21).adult() |should| equal_to ('Adult')

        # Question 2
    def test_it_checks_greater_number(self):
        Number(1).greaterNumber(2,7) |should| equal_to (7)
        Number(9).greaterNumber(2,3) |should| equal_to (9)
        Number(1).greaterNumber(8,3) |should| equal_to (8)

        # Question 3
    def test_it_convert_meters_to_centimeters(self):
        Measure(1).metersToCent() |should| equal_to (100)
        Measure(10).metersToCent() |should| equal_to (1000)
        Measure(1.5).metersToCent() |should| equal_to (150.0)

        # Question 4
    def test_it_calculates_area_of_a_water_tank(self):
        Measure().cube_area(1, 1, 1) |should| equal_to (1)
        Measure().cube_area(2, 2, 2) |should| equal_to (8)
        Measure().cube_area(1.5, 3.1, 10) |should| equal_to (46.5)

        # Question 5
    def test_it_calculates_the_ideal_weight(self):
        PersonalData().ideal_weight('F',1.5,70) |should| equal_to ("acima do peso ideal")
        PersonalData().ideal_weight('M',1.5,70) |should| equal_to ("acima do peso ideal")

        # Question 6
    def test_it_calculates_the_penalty_of_excess_weight_of_fish(self):
        Fish(51).penalty() |should| equal_to ((1, 4.00))
        Fish(50).penalty() |should| equal_to ((0, 0))

        # Question 7
    def test_it_calculates_the_amount_of_ink(self):
        Ink(60).amount() |should| equal_to (10)
        Ink(160.2).amount() |should| equal_to (26.7)

    def test_it_calculates_only_buy_cans(self):
        Ink(108).buying_cans(18)  |should| equal_to ((1, 80.00))
        Ink(110).buying_cans(18.333333333333332)  |should| equal_to ((2, 160.00))

    def test_it_calculates_only_buy_gallons(self):
        Ink(21.6).buying_gallons(3.6)  |should| equal_to ((1, 25.00))
        Ink(110).buying_gallons(18.333333333333332)  |should| equal_to ((6, 150.00))

        # Question 8
    def test_it_checks_whether_the_number_is_positive(self):
        Number(1).positive() |should| equal_to ('Positive')
        Number(0).positive() |should| equal_to ('Positive')
        Number(-1).positive() |should| equal_to ('Negative')

        # Question 9
    def test_it_checks_the_sex_of_a_person(self):
        PersonalData('F').sex_person() |should| equal_to ('Female')
        PersonalData('f').sex_person() |should| equal_to ('Female')
        PersonalData('M').sex_person() |should| equal_to ('Male')
        PersonalData('m').sex_person() |should| equal_to ('Male')
        PersonalData('n').sex_person() |should| equal_to ('Invalid sex')

        # Question 10
    def test_it_checks_the_leap_year(self):
        Year(2000).leap_year() |should| equal_to ('Leap Year')
        Year(2001).leap_year() |should| equal_to ('Non-Leap Year')

        # Question 11
    def test_it_checks_whether_the_letter_is_a_vowel(self):
        Letter('a').vowel()  |should| equal_to ('Vowel')
        Letter('b').vowel()  |should| equal_to ('Consonant')

        # Question 12
    def test_it_calculates_the_average_of_a_studant(self):
        Average(6).concept(6)|should| equal_to ('Disapproved')
        Average(7).concept(7)|should| equal_to ('Approved')
        Average(10).concept(10)|should| equal_to ('Pass with Distinction')

        # Question 13
    def test_it_decides_cheaper_price(self):
        Price(1.00).cheaper(2.00,3.00) |should| equal_to (1.00)
        Price(10.00).cheaper(8.00,30.00) |should| equal_to (8.00)
        Price(10.50).cheaper(25.00,3.20) |should| equal_to (3.20)

        # Question 14
    def test_it_tells_the_time_of_day(self):
        Date_time('M').day_shift() |should| equal_to ("Good Morning!")
        Date_time('V').day_shift() |should| equal_to ("Good Afternoon!")
        Date_time('N').day_shift() |should| equal_to ("Good Night!")
        Date_time('K').day_shift() |should| equal_to ("Invalid!")

        # Question 16
    def test_it_calculates_the_percentage_increase_applied(self):
        Salary(280.00).percentage() |should| equal_to ('20%')
        Salary(700.00).percentage() |should| equal_to ('15%')
        Salary(1500.00).percentage() |should| equal_to ('10%')
        Salary(2000.00).percentage() |should| equal_to ('5%')

    def test_it_calculates_the_value_of_the_increase(self):
        Salary(280.00).increase() |should| equal_to (56.00)
        Salary(700.00).increase() |should| equal_to (105.00)
        Salary(1500.00).increase() |should| equal_to (150.00)
        Salary(2000.00).increase() |should| equal_to (100.00)

    def test_it_calculates_the_new_salary_after_the_increase(self):
        Salary(280.00).new_salary() |should| equal_to (336.00)
        Salary(700.00).new_salary() |should| equal_to (805.00)
        Salary(1500.00).new_salary() |should| equal_to (1650.00)
        Salary(2000.00).new_salary() |should| equal_to (2100.00)

        # Question 17
    def test_it_calculates_the_gross_wage(self):
        Salary().gross_wage(5,220)  |should| equal_to (1100.00)

    def test_it_calculates_the_IR_Discount(self):
        Salary(900.00).IR_Discount()  |should| equal_to ('Free')
        Salary(1500.00).IR_Discount() |should| equal_to (75)
        Salary(2500.00).IR_Discount() |should| equal_to (250)
        Salary(3000.00).IR_Discount() |should| equal_to (600)

    def test_it_calculates_the_INSS_Discount(self):
        Salary(900.00).INSS_Discount()  |should| equal_to (90.00)
        Salary(1200.00).INSS_Discount()  |should| equal_to (120.00)

    def test_it_calculates_the_FGTS_Discount(self):
        Salary(900.00).FGTS_Discount()  |should| equal_to (99.00)

    def test_it_calculates_the_Total_Discounts(self):
        Salary(2500.00).total_Discounts()  |should| equal_to (575.00)

    def test_it_calculates_the_final_salary(self):
        Salary(2500.00).final_salary() |should| equal_to (1925.00)

        # Question 18
    def test_it_tells_the_day_of_the_week(self):
        Date_time(1).day_week() |should| equal_to ('Sunday')
        Date_time(9).day_week() |should| equal_to ('Invalid')

        # Question 19
    def test_it_informs_price_and_provenance(self):
        Price(80.00).provenance(1)  |should| equal_to ('80.00   -   South')
        Price(80.00).provenance(10)  |should| equal_to ('80.00   -   Imported')

        # Question 20
    def test_it_calculates_the_average_of_a_studant_in_letters(self):
        Average(4.00).letter_concept(4.00) |should| equal_to ((4.0, "E", "Disapproved"))
        Average(6.00).letter_concept(6.00) |should| equal_to ((6.0, "D", "Disapproved"))
        Average(7.50).letter_concept(7.50) |should| equal_to ((7.5, "C", "Approved"))
        Average(9.00).letter_concept(9.00) |should| equal_to ((9.0, "B", "Approved"))
        Average(10.00).letter_concept(10.00) |should| equal_to ((10.0, "A", "Approved"))

        # Question 22
    def test_it_determines_the_type_of_triangle(self):
        Measure().type_triangle(1, 1, 1) |should| equal_to (("Triangle Exists", 'Equilateral'))
        Measure().type_triangle(2, 3, 1) |should| equal_to ("Triangle doesn't Exists")
        Measure().type_triangle(2, 3, 2) |should| equal_to (("Triangle Exists", 'Isosceles'))

        #Question 23
    def test_it_prints_in_the_screen_the_full_name_number(self):
        Number(111).full_name() |should| equal_to ('1 hundred, 1 ten e 1 unit')
        Number(211).full_name() |should| equal_to ('2 hundreds, 1 ten e 1 unit')
        Number(12).full_name() |should| equal_to ('1 ten e 2 units')
        Number(201).full_name() |should| equal_to ('2 hundreds e 1 unit')

       #Question 24
    def test_it_informs_the_mid_age(self):
        Age(24).mid_class(24,24) |should| equal_to ((24, "Youth Class"))
        Age(39).mid_class(39,39) |should| equal_to ((39, "Adult Class"))
        Age(49).mid_class(49,49) |should| equal_to ((49, "Senior Class"))



if __name__ == "__main__":
    unittest.main()

