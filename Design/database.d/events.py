""" clanlist manage a list of members in a clan """
import sqlite3

DATABASE = "./database"


class XmasListException(Exception):
    pass


class XmasNoClan(XmasListException):
    pass


class clanlist:

    def __init__(self, clanname=None, clanid=None):
        self.cursor = None

        if (clanname and clanid) or not(clanname or clanid):
            raise ValueError

        self.connect_database()
        if clanname:
            clanid = self.from_database(
                "select id from clan where clanname = ?",
                clanname)
        else:
            clanname = self.from_database(
                "select clanname from clan where id = ?",
                clanid)
        self.clanname = clanname
        self.clanid = clanid
        self.members = self.get_members()

    def connect_database(self):
        conn = sqlite3.connect(DATABASE)
        self.cursor = conn.cursor()

    def from_database(self, sql, parm):
        self.connect_database()
        return self.cursor.execute(sql, (parm,)).fetchone()[0]

    def get_members(self):
        sql = """select fullname from person join clanmember
            on (person.id = clanmember.userid)
            where clanid = ?"""
        answer = self.cursor.execute(sql, (self.clanid,))
        answer = [x[0] for x in answer]
        return answer

if __name__ == "__main__":
    for y in [1, 2]:
        x = clanlist()
        x.clanid = y
        print(x.clanname)
