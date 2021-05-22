import distutils.util

from courses import *

state = 3

if state == 0:
    print("I'm here to assist you to discover our interesting courses at the HEC faculty!")

else:
    print("\n\n#########################################################################")
    print("\n Would you like to search for other courses?")

# Model identifies user wants to look for courses by parameters (search_information)

if state == 1:
    print("Here you can filter courses based on parameters, mainly the number of credits \nor "
          "the quantitative scale (HQ, SQ or NQ for high, semi or no quantitative respectively).")
    # You can also look for courses by their names or professor but be sure to exactly match the case.
    # We therefore recommend searching by keyword for that.

    credits = int(input("Enter the number of credits you look for: "))
    quant = str(input("Enter HQ, SQ or NQ to filter the quantitative scale: "))

    information = {"course_credits": credits, "course_quantitative": quant}
    search_information(information)

elif state == 2:
    print("Here you can find courses based on keywords. "
          "\nThe search is made to match names in any position.")
    course = str(input("Enter a keyword to find courses: "))
    keyword_course = {"course_name": course}

    search_course_name(keyword_course)

elif state == 3:
    print("Here you can find professors based on keywords. "
          "\nThe search is made to match last names in any position of the word.")
    professor = str(input("Enter a keyword to find professors: "))
    keyword_professor = {"course_professor": professor}

    output = search_professor_name(keyword_professor)
    if output:
        display_professor_name(output)
    else:
        print("No professors were found based on your keyword.")
        new_search = str(input("Would like to search with another keyword? "))
        new_search = bool(distutils.util.strtobool(new_search))
        while new_search:
            professor = str(input("Enter a keyword to find professors: "))
            keyword_professor = {"course_professor": professor}
            output = search_professor_name(keyword_professor)
            if output:
                display_professor_name(output)
                new_search = False
            else:
                print("No professors were found based on your keyword.")
                new_search = str(input("Would like to search with another keyword? "))
                new_search = bool(distutils.util.strtobool(new_search))



