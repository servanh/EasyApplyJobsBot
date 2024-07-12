from more_itertools import unique_everseen
import os




## Removes duplicates and returns boolean for if it succeeded or not
def main():
    try:

        os.rename('linkedin_questions.csv', 'linkedin_questions_cleaning.csv')
        with open('linkedin_questions_cleaning.csv', 'r') as file, open('linkedin_questions.csv','w') as outfile:
            outfile.writelines(unique_everseen(file))

        os.remove('linkedin_questions_cleaning.csv')
        return True
    except:
        return False
    
if __name__ == "__main__":
    print(main())