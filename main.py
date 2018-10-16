from db import user_controller as uc

uc.add_user(user_id=1, user_name="test",first_name="alex", last_name="ivanov")
uc.add_user(user_id=2, user_name="Ivan221", first_name="Ivan", last_name="popov")
uc.add_user(user_id=3, user_name="Alexandr2145e2",first_name="Alexandr", last_name="Egorov" )
uc.add_user(user_id=4, user_name="Michael21312312", first_name="Michael", last_name="Phelps")
uc.add_user(user_id=5, user_name="Fedor232313de213", first_name="Fedor", last_name="Zaycev")



all_user = uc.get_all_users()
for users in all_user:
    print(users)