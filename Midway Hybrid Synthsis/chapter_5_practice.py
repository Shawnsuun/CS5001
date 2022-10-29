import random

#list candidates to store all the candidites joined the lottery
candidates = []

#function for adding a lottery candidate, string candidate is candidate's name
def add_candidate(candidate):
    #change the string candidate into lower case
    candidate = candidate.lower()
    #candidate are able to add to list if it is not in the list candidates
    if candidate not in candidates and len(candidate) > 0:
        #the size of list candidates is limited to 20
        if len(candidates) < 20:
            #add candidate name into the list candidates in lowercase
            candidates.append(candidate)
        else:
            #enough people to start lottery, print a message
            print("Ready to start lottery.\n")
    else:
        #the name has already been in the list, or name is empty, print a message
        print("Unable to add candidate.\n")

#function for deleting a lottery candidate, string candidate is candidate's name
def cancel_candidate(candidate):
    #change the string candidate into lower case
    candidate = candidate.lower()
    #only available when there are at least 1 person in the list candidates, and candidate to remove is in the list candidates
    if len(candidates) > 0 and candidate in candidates:
        #remove the candidate from the list
        candidates.remove(candidate)
    else:
        #unable to remove from the list, print a message
        print("Unable to cancel.\n")

#function to get a lucky candidate who won the lottery
def get_lucky_candidate():
    #set at least 15 persons to start the lottery
    if len(candidates) < 15:
        print("No enough candidates to start!\n")
    else:
        #get a random number as index of list candidates
        index = random.randint(0, len(candidates) - 1)
        #print the award message to the lucky candidate, name set to uppercase in title
        print(f"{candidates.pop(index).title()}, you won the award!\n")

#function to show all candidates who joined the lottery
def show_all_candidates():
    print('Here are all candidates:\n')
    #sort the list
    candidates.sort()
    #loop the list candidates
    for candidate in candidates:
        #name set to uppercase in title
        print(candidate.title())

#function to show candidates amount
def show_candidates_number():
    print(f'{len(candidates)} candidates joined the lottery.\n')

#function to load 20 example candidates for testing
def load_example_candidates():
    #string including 20 names, separated by ","
    candidates_str = 'Olivia,Emma,Charlotte,Amelia,Ava,Sophia,Isabella,Mia,Evelyn,Harper,Luna,Camila,Gianna,Elizabeth,Eleanor,Ella,Abigail,Sofia,Avery,Scarlett'
    #transfer the string into list with 20 strings
    candidates_examples = candidates_str.split(',')
    #add 20 names to the list candidates
    for candidates_example in candidates_examples:
        add_candidate(candidates_example)

def main():
    #the menu message
    menu =  "1. Join the lottery\n"
    menu += "2. Cancel joining lottery\n"
    menu += "3. Get lucky candidate\n"
    menu += "4. Show all candidates names\n"
    menu += "5. Show candidate numbers\n"
    menu += "6. Quit\n"
    menu += "7. Load example 20 candidates\n"
    #boolean to decide whether program is running
    running = True

    while running:
        #get user selection, run different functions based on the selection
        selection = input(menu) 
        if selection == "1":
            candidate = input("Please enter your full name")
            add_candidate(candidate)
        elif selection == "2":
            candidate = input("Please enter your full name")
            cancel_candidate(candidate)
        elif selection == "3":
            get_lucky_candidate()
        elif selection == "4":
            show_all_candidates()
        elif selection == "5":
            show_candidates_number()
        elif selection == "6":
            #terminate the loop
            running = False
        elif selection == "7":
            load_example_candidates()
        else:
            #handle wrong input
            print ("Please select an option from 1 ~ 7!")

main()