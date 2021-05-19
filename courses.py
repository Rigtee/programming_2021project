import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("programmeshec.db")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"Error: ' {e}'")

create_courses_table = """
CREATE TABLE courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(40) NOT NULL,
course_professor VARCHAR(30) NOT NULL,
course_credits INT NOT NULL,
course_quantitative VARCHAR(2));
"""

execute_query(conn, create_courses_table)

add_records = """
INSERT INTO courses VALUES
(1, "Droit des marchés financiers", "A. Richa", 3, "NQ"),
(2, "Programming", "S. Scheidegger", 6, "HQ"),
(3, "Financial Analysis", "J. Froidevaux", 6, "HQ");
"""

execute_query(conn, add_records)

add_more_records = """
INSERT INTO courses VALUES
(4, "Fixed Income and Credit Risk", "M. Rockinger", 6, "HQ"),
(5, "Empirical Methods in Finance", "F. Ielpo", 6, "HQ"),
(6, "Advanced Data Analytics", "S. Scheidegger", 6, "HQ"),
(7, "Asset Pricing", "L. Bretscher", 6, "HQ"),
(8, "International Strategy", "U. Khan", 6, "NQ"),
(9, "Droit bancaire", "C. Lombardini", 6, "NQ"),
(10, "Valuation", "P. Valta", 6, "HQ"),
(11, "Derivatives", "L. Bretscher", 6, "HQ"),
(12, "CFA Advanced Research Challenge", "N.Schuerhoff", 3, "HQ"),
(13, "Quantitative Asset and Risk Management", "F. Ielpo", 6, "HQ"),
(14, "Corporate Sustainability Reporting", "G. Melloni", 3, "SQ"),
(15, "Gestion du risque", "E. Fragniere", 3, "NQ"),
(16, "Cours avancé en gouvernance et finance d'entreprise", "A. Schatt", 6, "SQ"),
(17, "Audit des systèmes d'information de gestion", "E. Campos", 3, "NQ"),
(18, "Advanced Management Accounting", "G. Derchi", 3, "SQ"),
(19, "Advanced Financial Analysis", "P. André", 3, "HQ"),
(20, "Banking Accounting and Reporting", "M. Dong", 3, "NQ"),
(21, "Fiscalité directe II & Fiscalité indirecte (TVA)", "P. Glauser", 6, "NQ"),
(22, "Life Contingencies I", "F. Dufresne", 6, "HQ"),
(23, "Loss Models", "E. Hashorva", 6, "HQ"),
(24, "Time Series", "E. Hashorva", 6, "HQ"),
(25, "Simulation Methods in Finance and Insurance", "M. Tamraz", 3, "HQ"),
(26, "Social Insurance", "S. Arnold", 3, "SQ"),
(27, "Risk Theory", "H. Albrecher", 6, "SQ"),
(28, "Ratemaking and Claims Reserving", "J. Trufin", 3, "HQ"),
(29, "Business and IS Architecture Design", "C. Legner", 6, "SQ"),
(30, "Big-Scale Analytics", "M. Vlachos", 6, "SQ"),
(31, "Digital Innovation", "B. Mueller", 6, "NQ"),
(32, "Audit & Gouvernance II", "Y. Borboen", 6, "NQ"),
(33, "Research Introduction Seminar: Computer Science Research Methodology", "B. Garbinato", 3, "SQ"),
(34, "Séminaire d’introduction à la recherche : Qualitative research and Design Science research", "S. Missonier", 3, "NQ"),
(35, "Cybersécurité et intelligence économique", "S. Ghernaouti", 6, "NQ"),
(36, "Project Management & Outsourcing in a Digital Era", "P. Bienz", 6, "NQ"),
(37, "International Macroeconomics", "P. Bacchetta", 6, "HQ"),
(38, "Biological Invasions", "C. Bertelsmeier", 1.5, "NQ"),
(39, "Current Problems in Conversation Biology", "C. Wedekind", 3, "NQ" ),
(40, "Macroeconometrics", "J. Renne", 3, "HQ"),
(41, "Game Theory", "L. Santos Pinto", 6, "HQ"),
(42, "Neuroéconomie", "A. Villa", 6, "SQ"),
(43, "Public Economics", "C. Terrier", 6, "SQ"),
(44, "Introduction to primate behaviour, cognition and culture", "E. Van de Waal", 1.5, "NQ"),
(45, "Business Cycles", "F. Bilbiie", 6, "HQ"),
(46, "Political and Institutional Economics", "D. Rohner", 6, "HQ"),
(47, "Co-evolution, mutualism, parasitism", "I. Sanders", 1.5, "NQ"),
(48, "Spatial Modelling of Species and Biodiversity", "A. Guisan", 3, "NQ"),
(49, "Advanced Topics in Industrial Organization", "O. Striumbu", 6, "NQ"),
(50, "Behavior, economics, and evolution lecture series", "L. Lehmann", 6, "NQ"),
(51, "Economic Growth", "J. Buggle", 6, "SQ"),
(52, "Microeconometrics", "J. Maurer", 6, "HQ"),
(53, "Environmental Economics", "S. Di Falco", 3, "HQ"),
(54, "The Evolution of Cooperation: from Genes to Culture", "L. Lehmann", 3, "NQ"),
(55, "Competitive Advantage & Strategic Interactions", "A. Conti", 6, "SQ"),
(56, "Distribution Management", "T. Eckardt", 6, "SQ"),
(57, "Machine Learning in Business Analytics", "M. Boldi", 6, "HQ"),
(58, "Sustainable Logistics", "O. Gallay", 6, "SQ"),
(59, "Customer Relationship Management", "M. Christen", 6, "NQ"),
(60, "Power and leadership", "B. Tur", 6, "NQ"),
(61, "Strategy Consulting Project", "R. Iunius", 6, "NQ"),
(62, "Current Problems in Conservation Biology", "C. Wedekind", 3, "NQ"),
(63, "Brand Development Strategic Project", "R. Queiros", 6, "NQ"),
(64, "Managing People: Organizational Design, Change and Performance", "J. Dietz", 6, "NQ"),
(65, "Strategy of Innovation", "A. Conti", 6, "NQ"),
(66, "Innovation Law", "V. Junod", 3, "NQ"),
(67, "Strategic Modelling", "A. van Ackere", 6, "NQ"),
(68, "Innovation Strategy Project", "R. Queiros", 6, "NQ"),
(69, "New Trends in Product Innovation", "F. Leclerc", 3, "NQ"),
(70, "Evidence-Based Management", "J. Dietz", 6, "NQ"),
(71, "Grand Challenges Strategy Project", "P. Haack", 6, "NQ"),
(72, "Group Processes", "F. Krings", 6, "NQ"),
(73, "Supply-chain Analytics", "S. De Treville", 6, "HQ"),
(74, "Forecasting I", "M. Baumgartner", 3, "HQ"),
(75, "Forecasting II", "V. Chavez", 3, "HQ"),
(76, "Sustainable Innovation Challenge", "J. Petty", 3, "NQ"),
(77, "Negociations", "C. Efferson", 6, "NQ"),
(78, "Simple Rules for Leadership and Strategy: a practical approach", "J. Marewski", 6, "NQ"),
(79, "The Management of Risk, Reputation and Legitimacy", "P. Haack", 6, "NQ"),
(80, "Environmental crisis and societal change", "G. Palazzo", 3, "NQ"),
(81, "Deep learning", "I. Rudnytskyi", 3, "NQ"),
(82, "Social Well Being", "F. Petersen", 6, "NQ"),
(83, "Consumer Behavior", "K. Rege", 3, "NQ"),
(84, "Sustainability Strategy Project", "C. Fischer", 6, "NQ"),
(85, "Company Project in Business Analytics", "M. Boldi", 6, "NQ"),
(86, "Project Management & Outsourcing in a Digital Era", "P. Bienz", 6, "NQ"),
(87, "Brand Management", "A. Dabrowska-Leszcynska", 3, "NQ"),
(88, "Social Media", "D. Gillet", 3, "NQ"),
(89, "Company Project in Marketing", "A. Dabrowska-Leszcynska", 6, "NQ");
"""

execute_query(conn, add_more_records)

def search_courses(params):
    query = "SELECT * FROM courses"
    if len(params) > 0:
        filters = ['{}=?'.format(k) for k in params]
        query += ' WHERE ' + ' AND '.join(filters)
    else:
        print('Please specify parameters to search in the database.')
    t = tuple(params.values())
    c = conn.cursor()
    c.execute(query, t)
    search_result = []
    for row in c:
        search_result.append(row[1])
    return search_result

def search_information(params):
    if len(params) > 0:
        t = tuple(params.values())
        keyword = str('%' + str(t) + '%')
        bad_characters = ["'", "(", ")", ","]
        newkeyword = ''.join(i for i in keyword if not i in bad_characters)
        query = "SELECT * FROM courses WHERE course_name LIKE (?)"
    else:
        print('Please specify parameters to search in the database.')
    c = conn.cursor()
    c.execute(query, [newkeyword])
    search_result = []
    for row in c:
        search_result.append(row[1])
        search_result.append(row[2])
        search_result.append(row[3])
        search_result.append(row[4])
    return search_result



def display_courses(result):
    if result:
        print('Courses found: ' + str(result))
    else:
        print('No course was found based on your search criteria.')

def display_information(result):
    if result:
        print('Information about the keyword found: ')
        course = [result[i:i+4] for i in range(0, len(result), 4)]
        for el in course:
            if el[3] == "HQ":
                el[3] = "highly quantitative"
            elif el[3] == "SQ":
                el[3] = "semi quantitative"
            elif el[3] == "NQ":
                el[3] = "non quantitative"

            print("{course_name} given by {course_professor}, {course_credits} credits "
                  "and having a {course_quantitative} scale.".format(course_name = el[0], course_professor = el[1],
                                                                                 course_credits = el[2], course_quantitative = el[3]))

params = {'course_professor':'S. Scheidegger', 'course_credits': 6, 'course_quantitative' : "HQ"}
params2 = {'course_credits': 3, 'course_quantitative': 'SQ'}
result1 = search_courses(params)
result2 = search_courses(params2)

display_courses(result1)
display_courses(result2)

params3 = {'course_name': 'adv'}
result3 = search_information(params3)
display_information(result3)