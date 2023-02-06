

import pymysql.cursors


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

    def save(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='QWDrt@12345',
                                     database='web_scrapping',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT IGNORE INTO `chemical` (`chemical_name`, `cas_number`) VALUES (%s, %s)"
                cursor.execute(sql, (f'{self.name}', f'{self.cas_number}'))

            connection.commit()

        print(
            f"chemical name : {self.name} and cas_number = {self.cas_number} saved")
