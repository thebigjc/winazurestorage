from winazurestorage import *

def do_table_tests():
    print "Starting table tests"
    tables = TableStorage(CLOUD_TABLE_HOST, STORE_ACCOUNT, SECRET_KEY)
    for table in tables.list_tables():
        print table.name, 
        c = 0
        for e in tables.get_all(table.name):
            c += 1
            if (c % 1000) == 0:
                print ".",
            if c > 10000:
                break
        print c

    print "Done."

def run_tests():
    STORE_ACCOUNT = file('.storeaccount').read().strip()
    SECRET_KEY = file('.secretkey').read().strip()
    do_table_tests()

if __name__ == '__main__':
    run_tests()
