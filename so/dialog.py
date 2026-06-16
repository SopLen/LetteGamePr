import csv


class Dialog:
    
    
    
    def __init__(self):
        self.question = []

    def getQuestion(self, lehrer):
        with open("test_fragenkatalog.csv", "r", encoding="utf8") as file:
            csv_reader_object = csv.reader(file, delimiter=";")
            for row in csv_reader_object:
                if not row[0] == "Lehrer":
                    if row[0] == lehrer:
                        self.question = row
                        return
    
    def testAnswer(self, answer):
        # if answer == 1 and self.question[6] == 1:
        #     return True
        # elif answer == 2 and self.question[6] == 2:
        #     return True
        # elif answer == 3 and self.question[6] == 3:
        #     return True
        # else:
        #     return False 
        return answer == int(self.question[5])
            


dialog = Dialog()

dialog.getQuestion("Test")
print(dialog.testAnswer(1))
