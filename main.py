# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculate_BMI(weight, height):
    """
    Function which calculates BMI (body mass index)
    :param weight: weight
    :param height: height
    :return: BMI
    """
    return weight / (height ** 2)

def checkHealthStatus(BMI):
    """
    Returns Health status
    :param BMI: BMI
    :return: Health Status
    """
    if(BMI < 18.5):
        return "Underweight"
    elif (BMI <= 25):
        return "Normal"
    elif (BMI <= 30):
        return "Overweight"
    else:
        return "Obesity"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weight = float(input("Insert your weight: "))
    height = float(input("Insert your height: "))
    BMI = calculate_BMI(weight, height)
    print(BMI)
    print(checkHealthStatus(BMI))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
