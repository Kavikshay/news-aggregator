import requests 
import json 
from pathlib import Path 

def del_fav():
	try:
		with open("favourites.json","r")as file:
			data=json.load(file)
		for i,j in enumerate(data,start=1):
			print(i,".",j["title"])
		choice=int(input("enter number to delete:"))
		if choice >=1 and choice<=len(data):
			num=choice-1
			del data[num]
			print("data is deleted")
		else:
			print("enter right number ")
		with open("favourites.json","w")as file:
			json.dump(data,file,indent=4)
			
		
	except FileNotFoundError:
		print("file not found ")								
						
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")

def display_fav():
	try:
		with open("favourites.json","r")as file:
			data=json.load(file)
		for i in data:			
			print("title:",i["title"])
			print("description:",i["description"])
			print("published_at:",i["published_at"])
			print("sitename:",i["sitename"])
			print("url:",i["url"])
			print("host:",i["host"])
			print("----------------------------")
			
	except FileNotFoundError:
		print("file not found ")								
						
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")
			
		

def save_fav(data):
	try:
		file_path=Path("favourites.json")
		new=data
		if file_path.exists():
			if file_path.stat().st_size==0:
				with open("favourites.json","w")as file:
					json.dump(new,file,indent=4)
				print("\n data saved successfully \n")
			else:
				old=[]
				with open(file_path,"r")as file:
					old=json.load(file)
				exists={
				i["title"] for i in old
				}
				if new["title"]not in exists:
					old.append(new)
					exists.add(new["title"])
				else:
					print("data is already saved")
				with open("favourites.json","w")as file:
					json.dump(old,file,indent=4)
				print("\n saved successfully \n")
	except FileNotFoundError:
		print("file not found ")								
						
	except json.JSONDecodeError:
        	print("The JSON file is corrupted or improperly formatted.")
			
				

def search(name):
	try:
		url=f"https://freenewsapi.ai/v1/search?q={name}&size=5"
		response=requests.get(url, timeout=10)
		print("status code:",response.status_code)
		data=response.json()
		count=1
		news_save=[]
		spacific=input("do you want the result form spacific website (yes/no):")
		if spacific.lower()=="no":
			for i in data["results"]:			
				title=i["title"]
				description=i["description"]
				published=i["published_at"]
				site="site name not found "
				if i["sitename"]:
					site=i["sitename"]
				siteurl=i["url"]
				host=i["host"]
				print(count)		
				print("title:",title)
				print("description:",description)
				print("published_at:",published)
				print("sitename:",site)
				print("url:",siteurl)
				print("host:",host)
				print()
				count+=1
				news_search={
				"title":title,
				"description":description,
				"published_at":published,
				"sitename":site,
				"url":siteurl,
				"host":host}
				news_save.append(news_search)
		elif spacific.lower()=="yes":
			sname=input("enter site to search:")
			for i in data["results"]:			
				if i["sitename"]==sname:
					title=i["title"]
					description=i["description"]
					published=i["published_at"]
					site="site name not found "
					if i["sitename"]:
						site=i["sitename"]
					siteurl=i["url"]
					host=i["host"]
					print(count)		
					print("title:",title)
					print("description:",description)
					print("published_at:",published)
					print("sitename:",site)
					print("url:",siteurl)
					print("host:",host)
					print()
					count+=1
					news_search={
					"title":title,
					"description":description,
					"published_at":published,
					"sitename":site,
					"url":siteurl,
					"host":host}
					news_save.append(news_search)
			
		
		if count==0 and len(news_search)==0:
			print("data not found ")
		choice=input("do you want to save data to favorites (yes/no):")
		if choice.lower()=="yes":
			saved=0
			for i,j in enumerate(news_save, start=1):
				print(i,".",j["title"])
			select=int(input("enter number to save in favourite:"))
			for i,j in enumerate(news_save, start=1 ):
				if i==select:
					save_fav(j)
					saved+=1
			if saved==0:
				print("enter valid number please try again ")
		elif choice.lower()=="no":
			return 
		else:
			print("enter valid choice (yes/no)")
	
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")
			

def fetch():
	try:
		url="https://freenewsapi.ai/v1/search?q=movies&size=5"			
		response=requests.get(url, timeout=10)	
		print("status code",response.status_code)
		data=response.json()
		news_data=[]
		count=1
		for i in data["results"]:			
			title=i["title"]
			description=i["description"]
			published=i["published_at"]
			site="site name is not found "
			if i["sitename"]:
				site=i["sitename"]
			siteurl=i["url"]
			host=i["host"]
			print(count)		
			print("title:",title)
			print("description:",description)
			print("published_at:",published)
			print("sitename:",site)
			print("url:",siteurl)
			print("host:",host)
			print("------------------------------------------------")
			count+=1
			news_list={
			"title":title,
			"description":description,
			"published_at":published,
			"sitename":site,
			"url":siteurl,
			"host":host}
			news_data.append(news_list)
		choice=input("do you want to save data to favorites (yes/no):")
		if choice.lower()=="yes":
			saved=0
			for i,j in enumerate(news_data, start=1):
				print(i,".",j["title"])
			select=int(input("enter number to save in favourite:"))
			for i,j in enumerate(news_data, start=1 ):
				if i==select:
					save_fav(j)
					saved+=0
			if saved==0 and len(news_data)==0:
				print("enter valid number")
		elif choice.lower()=="no":
			return news_data
		else:
			print("enter valid number")
							
		return news_data
	except requests.exceptions.Timeout:
	   	print("Request timed out. Please try again.")
	except requests.exceptions.ConnectionError:
	   	print("No internet connection.")
	except requests.exceptions.RequestException:
	   	print("There was a problem with the API request.")
	except (KeyError, TypeError):
	  	 print("Unexpected data received from the API.")
		

def mane():
	try:
		news=[]
		while True:		
			print("----------NEWS MENU----------")
			print("1. Fetch Latest News\n2. Search News by Topic\n3. Display Saved Favorites\n4. Remove a Favorite\n5. Exit")
			a=int(input("enter your choice:"))
			if a==5:
				print("\n menu is ended vesit again ")
				print("-----------------------------")
				break
			elif a==1:
				result=fetch()
				if result is not None:
					news=result
				
			elif a==2:
				name=input("enter topic to search:")
				if not name.strip():
					print ("name can't me empty ")
				else:
					search(name)
			elif a==3:
				display_fav()
			elif a==4:
				del_fav()
				
			
	except ValueError:
			print("enter number not text")
mane()	