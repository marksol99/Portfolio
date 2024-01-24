movieBudgets =[("birds of prey", 97.1), ("Dolittle", 175.0), ("the gentlemen", 7.0), ("falling", 22.0)]

#Bubble sorts a list of movies by largest budget
def sort_and_print(movieBudgets):

    list = len(movieBudgets)
    for i in range(0, list):

        for j in range(0, list - i - 1):
            if (movieBudgets[j][1] > movieBudgets[j + 1][1]):
                temp = movieBudgets[j]
                movieBudgets[j] = movieBudgets[j + 1]
                movieBudgets[j + 1] = temp
    movieBudgets.reverse()
    for name, budget in movieBudgets[:1]:
        return f"The movie with the highest budget is: {name}"


print(sort_and_print(movieBudgets))