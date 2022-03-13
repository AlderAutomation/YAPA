# Notes

## RSS

we use http requests to get the feed information which is basically json. 

---

## Json 

the feed back from the RSS gives us a nested json object. To get to the nested items that we need to work with we need to do a for loop through the json for the 'Key' item that holds our data. And then we can loop through the actual episodic data and pull out the info that we are going to need / use. 

EG:


for element in pretty_json['items']:  
	for key, value in element.items():  
		if key == 'title':  
			print(key, ':', value)  
		if key == 'description':  
			print(key, ':', value)  
  
I'm betting there is a better way of doing this. prolly can put the first for loop to a variable and then loop from that.  

---

## QT Designer  
  
install via  
sudo apt install qttools5-dev-tools  
sudo apt install qttools5-dev  

start via  
designer  

---

## Audio Player  

Use pygame mixer. nice easy solution. doesnt help with video though. maybe we dont do video, id be ok with that  

---

## Json User Profile  

can use a json file to keep the user data.  
- User  
	- subscriptions  
		- IDs  
		- Titles  
		- Descriptions  
		- played boolean  
		- link  
		- enclosurelink  
		- episode  
		- feed ID

---

## Syncing data 

I want to sync data between devices withought using an account.  
Posibilities:  
	- was thinking QR code to transfer the json file. But the would require user maintenance. user wont want to do that.  
	- now am thinking using the QR code to setup the wifi? connection  
	- 