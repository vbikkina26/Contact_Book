import sqlite3 as sl

#create or connect to DB
db=sl.connect('contacts.db')

def insert():
	name=input("Enter Contact Name:").lower()
	country=input("Enter country name:").upper()
	number=int(input("Enter Contact Number (Without Spaces and symbols):"))
	codeQ=f"select phonecode from country where name=='{country}';"
	# print(codeQ)

	selCode=db.execute(codeQ)
	conCode=[i[0] for i in selCode]
	insQ=f"insert into contacts values('{name}',{int(number)},'{country.capitalize()}',{int(conCode[0])});"
	# print(insQ)
	db.execute(insQ)
	db.commit()
    
	print(f'Contact {name.capitalize()} Saved successfully !!')
	data=db.execute("""select count(*) from contacts;""")
	db.commit()

	count=[i[0] for i in data]
	print(count)


def delete():
	contact=input("Enter Name or Number to delete a contact:")
	try:
		contact=int(contact)
		codeQ=f"delete from contacts where phNumber=='{contact}'"
		db.execute(codeQ)
		db.commit()

	except:
		codeQ=f"delete from contacts where name=='{contact}'"
		db.execute(codeQ)
		db.commit()
	print(f"Contact deleted sucessfully !!")

def search():
    opt=input("Search for a contact:")
    contDict={}
    codeQ="select name,phNumber from contacts;"
    data=db.execute(codeQ)
    db.commit()
    for i in data:
        contDict[i[0].lower()]=str(i[1])
#     print(contDict)
    if opt in contDict.keys():
        print(f"""Name: {opt.capitalize()}\nNumber: {contDict[opt]}""")
    elif opt in contDict.values():
        for key,value in contDict.items():
            if value==opt:
                print(f"""Name: {key.capitalize()}\nNumber: {opt}""")
    else:
        print("Sorry !!! Contact couldn't found")



opt=input("""Choose any option: save/search/delete:""").lower()
if opt=='save':
	insert()
elif opt=='delete':
	delete()
elif opt=='search':
	search()


#if error occured with code. replace contacts table with example table