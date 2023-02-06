class chemical:
    def __init__(self, cname, cas_number):
        self.name = cname
        self.cas_number = cas_number

        if cname and cas_number:
            print(
                f"chemical with name : {self.name} and CAS number : {self.cas_number} created")
        else:
            print("expected field missing ... try agian later .")

    def show(self):
        print(
            f"chemical name : {self.name} and cas_number = {self.cas_number}")


object1 = chemical("sghdvghewgfh", 67346)
object1.show()
