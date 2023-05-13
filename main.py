import robloxpy
import time
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("rgorbat.json", scope)
client = gspread.authorize(credentials)
print("Initialization in progress, standby...")
agrsheet = client.open('1. RG Armoured Division ORBAT').get_worksheet(1)
armsheet = client.open('1. RG Armoured Division ORBAT').get_worksheet(2)
thrsheet = client.open('1. RG Armoured Division ORBAT').get_worksheet(3)

firstagr = robloxpy.Group.External.GetMembersinRoleList(15987254,89665278)
secondagr = robloxpy.Group.External.GetMembersinRoleList(15987254,89664509)
firstarm = robloxpy.Group.External.GetMembersinRoleList(15987257,89665001)
secondarm = robloxpy.Group.External.GetMembersinRoleList(15987257,89664526)
firstthr = robloxpy.Group.External.GetMembersinRoleList(15987248,89665513)
secondthr = robloxpy.Group.External.GetMembersinRoleList(15987248,89664482)
thirdthr = robloxpy.Group.External.GetMembersinRoleList(15987248,92537373)

agr1 = list(firstagr[1])
agr2=  list(secondagr[1])
arm1 = list(firstarm[1])
arm2 = list(secondarm[1])
thr1 = list(firstthr[1])
thr2 = list(secondthr[1])
thr3 = list(thirdthr[1])

API_ENDPOINT = "https://users.roblox.com/v1/users"

def getUsername(userId):

    requestPayload = {
        "userIds": [
            userId
        ],

        "excludeBannedUsers": True # Whether to include banned users within the request, change this as you wish
    }

    responseData = requests.post(API_ENDPOINT, json=requestPayload)

    # Make sure the request succeeded
    assert responseData.status_code == 200

    username = responseData.json()["data"][0]["name"]

    #print(f"getUserId :: Fetched user ID of username {userId} -> {username}")
    return username

def GetFirstCompanyAGR():
    cellnum=26
    for i in agr1:
        usernames = (getUsername(i))
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        agrsheet.update(('C'+cell+':D'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating AGR First Company Now...")
                agrsheet.update(('E'+cell+':F'+cell), rank)
                cellnum += 1
def GetSecondCompanyAGR():
    cellnum = 26
    for i in agr2:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        agrsheet.update(('K'+cell+':L'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating AGR Second Company Now...")
                agrsheet.update(('M'+cell+':N'+cell), rank)
                cellnum += 1
def GetFirstCompanyARM():
    cellnum = 26
    for i in arm1:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        armsheet.update(('C'+cell+':D'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating Armoured First Company Now...")
                armsheet.update(('E'+cell+':F'+cell), rank)
                cellnum += 1
def GetSecondCompanyARM():
    cellnum = 26
    for i in arm2:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        armsheet.update(('K'+cell+':L'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating Armoured Second Company Now...")
                armsheet.update(('M'+cell+':N'+cell), rank)
                cellnum += 1
def GetFirstCompanyTHR():
    cellnum = 26
    for i in thr1:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        thrsheet.update(('C'+cell+':D'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating THR First Company Now...")
                thrsheet.update(('E'+cell+':F'+cell), rank)
                cellnum += 1
def GetSecondCompanyTHR():
    cellnum = 26
    for i in thr2:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        thrsheet.update(('K'+cell+':L'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating THR Second Company Now...")
                thrsheet.update(('M'+cell+':N'+cell), rank)
                cellnum += 1
def GetThirdCompanyTHR():
    cellnum = 26
    for i in thr3:
        usernames = getUsername(i)
        userid = str(i)
        cellnum = (cellnum)
        cell = str(cellnum)
        thrsheet.update(('S'+cell+':T'+cell), usernames)
        req = requests.get('https://groups.roblox.com/v2/users/'+userid+'/groups/roles')
        formatted = req.json()
        for e in formatted['data']:
            if e['group']['name'] == 'The Rulеrguard':
                rank = (e['role']['name'])
                print("Updating THR Third Company Now...")
                thrsheet.update(('U'+cell+':V'+cell), rank)
                cellnum += 1
options = input("Which regiment do you want to update? Type 'ALL' for all, 'THR' for Tank Hunters, 'AGR' for Armoured-Gren, and 'ARM' for Armoured. Note: All will take about 30 minutes, a Regiment will take about 5 due to rate limits.")
if options == "ALL".upper():
    print("Updating all regiments on the ORBAT, standby...")
    GetFirstCompanyAGR()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetSecondCompanyAGR()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetFirstCompanyARM()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetSecondCompanyARM()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetFirstCompanyTHR()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetSecondCompanyTHR()
    print("Company complete! Waiting 3 minutes for next company...")
    time.sleep(180)
    GetThirdCompanyTHR()
    print("All companies updated succesfully!")
    quit()
if options == "THR".upper():
    thrcompanies = input("Which companies would you like to update? Type 'ALL' for both, 'I' for first, 'II' for second, and 'III' for third.")
    if thrcompanies == "ALL".upper():
        print("Updating all THR companies now...")
        GetFirstCompanyTHR()
        time.sleep(150)
        GetSecondCompanyTHR()
        time.sleep(150)
        GetThirdCompanyTHR()
        print("All companies complete!")
        quit()
    if thrcompanies == 'I'.upper():
        print("Updating I. Company now...")
        GetFirstCompanyTHR()
        print("Complete!")
        quit()
    if thrcompanies == 'II'.upper():
        print("Updating II. Company now...")
        GetSecondCompanyTHR()
        print("Complete!")
        quit()
    if thrcompanies == 'III'.upper():
        print("Updating III. Company now...")
        GetThirdCompanyTHR()
        print("Complete!")
        quit()
    else:
        print("Not valid response, please restart script.")
        quit()
if options == "AGR".upper():
    agrcompanies = input("Which companies would you like to update? Type 'ALL' for both, 'I' for first, 'II' for second.")
    if agrcompanies == "ALL".upper():
        print("Updating all AGR companies now...")
        GetFirstCompanyAGR()
        time.sleep(150)
        GetSecondCompanyAGR()
        print("All companies complete!")
        quit()
    if agrcompanies == 'I'.upper():
        print("Updating I. Company now...")
        GetFirstCompanyAGR()
        print("Complete!")
        quit()
    if agrcompanies == 'II'.upper():
        print("Updating II. Company now...")
        GetSecondCompanyAGR()
        print("Complete!")
        quit()
    else:
        print("Not valid response, please restart script.")
        quit()
if options == "ARM".upper():
    armcompanies = input("Which companies would you like to update? Type 'ALL' for both, 'I' for first, 'II' for second.")
    if armcompanies == "ALL".upper():
        print("Updating all ARM companies now...")
        GetFirstCompanyARM()
        time.sleep(150)
        GetSecondCompanyARM()
        print("All companies complete!")
        quit()
    if armcompanies == 'I'.upper():
        print("Updating I. Company now...")
        GetFirstCompanyARM()
        print("Complete!")
        quit()
    if armcompanies == 'II'.upper():
        print("Updating II. Company now...")
        GetSecondCompanyARM()
        print("Complete!")
        quit()
    else:
        print("Not valid response, please restart script.")
        quit()
else:
    print("Not valid response, please restart script.")
    time.sleep(5)
    quit()
    
