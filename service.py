import psycopg2
import utils

conn = psycopg2.connect(dbname='n35',
                        user='postgres',
                        password='102030',
                        port=5432,
                        host='localhost')
cur = conn.cursor()

username = 'admin1'
new_password = '123'

select_user_query = '''SELECT * FROM users WHERE username = %s;'''
cur.execute(select_user_query, (username,))

# Natijalarni olish va chiqarish
user = cur.fetchone()
hashpassword = user[2]
if user:

    print('Foydalanuvchi mavjud')
    # utils.check_password(new_password, user[2])
    check = utils.check_password(new_password, hashpassword)
    if check:
        print("Password is correct.")
    else:
        print("Password is incorrect.")
else:
    print("Foydalanuvchi topilmadi.")

# Bog'lanishni yopish
cur.close()
conn.close()
