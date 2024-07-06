from caltopo_python import CaltopoSession
import time
import json

def pucb(*args):
    print("pucb called with args "+str(args))

def gucb(*args):
    print("gucb called with args "+str(args))

def nfcb(*args):
    print("nfcb called with args "+str(args))

def dfcb(*args):
    print("dfcb called with args "+str(args))

# open a session
cts=CaltopoSession('caltopo.com',
# cts=CaltopoSession('localhost:8080',
        configpath='../../cts.ini',
        # mapID='[NEW]',
        # mapID='[NEW]new4240',
        # mapID='[NEW]SAR:new4240',
        # mapID='[NEW]test:new4240',
        # mapID='QDJKMQQ',
        # mapID='CA4L4',
        # mapID='DEKFJ',
        # syncInterval=10,
        # syncDumpFile='syncDump',
        sync=False,
        # propertyUpdateCallback=pucb,
        # geometryUpdateCallback=gucb,
        # newFeatureCallback=nfcb,
        # deletedFeatureCallback=dfcb,
account='caver456@gmail.com')

# cts.addLine([[39,-120],[39.1,-120]],'a')
# cts.addLine([[39,-120,1,2],[39.1,-120,1,2]],'b')

# cts.addLine([[-120.1,39],[-120.1,39.1]],'a')
# cts.addLine([[-120.1,39,1,2],[-120.1,39.1,1,2]],'b')

# cts.addLine([[80,80,1,2],[80.1,80,1,1,2]],'a')

# cts.getFeatures('Shape')
# print('account data:')
# d=cts.getAccountData()
# with open('accountData.json','w') as f:
#         json.dump(d,f,indent=3)
# print(json.dumps(cts.getMapList('NCSSAR'),indent=3))
# print(json.dumps(cts.getAllMapLists(),indent=3))
# print('title:'+cts.getMapTitle('DEKFJ'))
# print('group accounts:'+str(cts.getGroupAccountTitles()))

cts.openMap('DEKFJ')
# cts.openMap('QDJKMQQ')
# cts._stop() # stop sync
# time.sleep(120)

##############
# test feature creation methods
##############
# fid=cts.addFolder('newFolder')
# cts.addMarker(39,-120,'newMarker',description='desc',color='#00FF00',symbol='fire',size=4,folderId=fid)
# cts.addLine([[-120,39],[-120.1,39.1],[-120,39.1]],title='newLine',description='desc',width=8,opacity=0.6,pattern='M12 -7M0 5M9 0A3 3 0 1 0 6 0 A3 3 0 0 0 9 0,2,20,T;M0 0L12 0,15,20',folderId=fid)
# cts.addPolygon([[-120.2,39],[-120.3,39.1],[-120.2,39.1]],title='newPoly',description='desc2',strokeOpacity=0.4,strokeWidth=1,fillOpacity=0.8,stroke='#FF00FF',fill='#00FF00')
# op1=cts.addOperationalPeriod('1',color='#222222')
# cts.addLineAssignment([[-120,39.2],[-120.1,39.3],[-120,39.3]],
#         number='101',
#         letter='AA',
#         opId=op1,
#         resourceType='GROUND_1',
#         teamSize=5,
#         priority='HIGH',
#         responsivePOD='MEDIUM',
#         unresponsivePOD='HIGH',
#         cluePOD='LOW',
#         description='assignmentAA',
#         previousEfforts='None',
#         transportation='self',
#         timeAllocated='6hrs',
#         primaryFrequency='BANNER',
#         secondaryFrequency='TAC1',
#         preparedBy='SAR35',
#         status='PREPARED')
# cts.addAreaAssignment([[-120,39.4],[-120.1,39.5],[-120,39.5]],
#         letter='AB',
#         opId=op1,
#         resourceType='GROUND_3',
#         teamSize=5,
#         priority='MEDIUM',
#         responsivePOD='MEDIUM',
#         unresponsivePOD='HIGH',
#         cluePOD='LOW',
#         description='assignmentAB',
#         previousEfforts='None2',
#         transportation='self2',
#         timeAllocated='8hrs',
#         primaryFrequency='BANNER2',
#         secondaryFrequency='TAC12',
#         preparedBy='SAR352',
#         status='PREPARED')
# cts.addAppTrack([[-120,39.6],[-120.1,39.7],[-120,39.7]],
#         title='apptrack1',
#         description='t101')


##############
# test feature query methods
##############

# print(str(cts.getFeatures('Assignment')))
# print(str(cts.getFeature(title='AB')))


##############
# test feature editing methods
##############

# aa=cts.getFeature(title='AA 101')
# cts.editFeature(id=aa['id'],properties={'description':'other'})
# # nm=cts.getFeature(title='newMarker')
# cts.moveMarker([-119.9,39],title='newMarker')
# cts.editMarkerDescription('newDesc2',title='newMarker')

##############
# test feature deletion methods
##############

# cts.delFeature(aa)
# cts.delFeatures(cts.getFeatures(featureClass='Marker'))
# cts.delMarkers(cts.getFeatures(featureClass='Marker'))

# cts.addMarker(39,-120,'newMarker2',description='desc2',color='#00FF00',symbol='a:1',rotation=38,size=2)

# r=cts.s.get('https://caltopo.com/sideload/account/'+cts.accountId+'.json?json=%7Bfull:+true%7D')

# print('request sent:'+str(r.url))
# print('r:'+str(r))
# if r:
#         print(str(r.status_code)+':'+str(r.text))

# print('getting account data...')
# ad=cts.getAccountData()
# print('account data:')
# print(json.dumps(ad,indent=3))

# ml=cts.getMapList(groupAccountTitle='NCSSAR')
# ml=cts.getAllMapLists()
# print('Map lists:')
# print(json.dumps(ml,indent=3))

# print(str(cts.getMapTitle('CA4L4')))
# print(str(cts.getGroupAccountTitles()))

# print('creating map...')
# r=cts.openMap('[NEW]')
# print('r: '+str(r))

# cts=CaltopoSession('caltopo.com',
#         configpath='../../cts.ini',
#         mapID='CA4L4',
#         account='caver456@gmail.com')

# markers=cts.getFeatures(featureClass='Marker')

# cts.openMap('[NEW]newMap')

# cts.addPolygon([[-120,39],[-120.1,39.1],[-120.1,39]],'a')
# cts.addPolygon([[39,-120.2],[39.1,-120.3],[39,-120.3]],'b')
# time.sleep(10)
# op1=cts.addOperationalPeriod('3',color='#2222FF',strokeWidth=4,fillOpacity=0.8)
# time.sleep(10)
# cts.editFeature(op1,properties={'title':'1b'})
# time.sleep(10)
# cts.addAreaAssignment([[-120.3,39.3],[-120.4,39.4],[-120.5,39]],letter='AA',opId=op1)

######################
# test _validatePoints
######################
#  - marker, line, and polygon
#  - 2-element points and 4-element points
#  - all-obviously-valid, one-obviously-swapped, one-of-each
#  - cts.validatePoints: modify, warn, False


# cts.validatePoints='warn'

# cts.addMarker(39,-120,'a')
# cts.addMarker(-120.1,39.1,'b')

# testList=[
#         [[-120,39],[-120.1,39],[-120,39.1]], # all valid
#         [[39,-120],[39,-120.1],[39.1,-120]], # all swapped
#         [[39,-120],[-120.1,39],[-120,39.1]],  # mixed
#         [[50,50],[50.1,50],[50,50.1]], # all ambiguous
#         [[-120,39,1],[-120.1,39,1],[-120,39.1,1]], # all valid (3-element)
#         [[39,-120,1],[39,-120.1,1],[39.1,-120,1]], # all swapped (3-element)
#         [[39,-120,1],[-120.1,39,1],[-120,39.1,1]],  # mixed (3-element)
#         [[50,50,1],[50.1,50,1],[50,50.1,1]], # all ambiguous (3-element)
#         [[-120,39,1,2],[-120.1,39,1,2],[-120,39.1,1,2]], # all valid (4-element)
#         [[39,-120,1,2],[39,-120.1,1,2],[39.1,-120,1,2]], # all swapped (4-element)
#         [[39,-120,1,2],[-120.1,39,1,2],[-120,39.1,1,2]],  # mixed (4-element)
#         [[50,50,1,2],[50.1,50,1,2],[50,50.1,1,2]] # all ambiguous (4-element)
# ]
# for pointsList in testList:
#         # print('\n\ninitial points:'+json.dumps(pointsList,indent=3))
#         # print('validated points:'+json.dumps(cts._validatePoints(pointsList),indent=3))
#         cts.addLine(pointsList,'testLine')
#         cts.addPolygon(pointsList,'testPolygon')

# # from caltopo_python_authTest import CaltopoSession
# import logging
# import sys
# import time
# import json



# print('startup')

# logging.basicConfig(stream=sys.stdout,level=logging.INFO)

# cts=CaltopoSession('localhost:8080','FAB')
# cts=CaltopoSession('localhost:8080','CM1') # CTD: geomTest / geomTest.json - geomTestOrig=CGA
# cts=CaltopoSession('caltopo.com','UMEPJ', # web: geomTest / geomTest.json - geomTestOrig=HB0U
#         configpath='../../cts.ini',
#         account='caver456@gmail.com',
#         # sync=False,
#         syncDumpFile='../../HB0U.txt')
#         # propUpdateCallback=pucb,
#         # geometryUpdateCallback=gucb,
#         # newObjectCallback=nocb,
#         # deletedObjectCallback=docb)

# open a mapless web session, then get the map list, then associate the session with a map
# cts=CaltopoSession('caltopo.com','[NEW]', # web: geomTest / geomTest.json - geomTestOrig=HB0U
# cts=CaltopoSession('caltopo.com','44H1C', # web: geomTest / geomTest.json - geomTestOrig=HB0U
# mapID='MVLDC' # writable map
# mapID='N3U63', # non-writable map, from SDL 10/26/23
# mapID='50503' # secret map from IC training, owned by ncssaradm
# mapID='MGVG3' # secret map owned by me

# mapID='PVTGT'
# # mapID='DHFSB'
# cts=CaltopoSession('caltopo.com', # web: mapless
#         configpath='../../cts.ini',
#         account='caver456@gmail.com',
#         mapID=mapID,
#         cacheDumpFile=mapID+'_cache.txt',
#         caseSensitiveComparisons=True,
#         sync=False)
        # syncDumpFile='../../HB0U.txt')



# cts.cut('AB','zz') # cut area assignment using line
# cts.cut('AA','z2')
# cts.cut('AA','z3')
# cts.cut('AA','z')
# cts.cut('z4','z5')
# cts.cut('z4:1','z6')

# cts.addMarker(39,-120,'testMarker')

# open a mapless web session, then get the map list, then associate the session with a map
# cts=CaltopoSession('localhost:8080',accountId='11UEE9')

# this line adds a marker to the opened web map, with a signed POST request:
# cts.addMarker(39,-120,'abcde')

# cts=CaltopoSession('caltopo.com',
#         configpath='../../cts.ini',
#         # mapID='PVTGT',
#         # mapID='MAA8J', # sharing=URL
#         # mapID='QPQ91', # sharing=public
#         # mapID='1H0U6', # sharing=secret
#         mapID='KC1CM', # sharing=private
#         account='caver456@gmail.com',
#         sync=False)

# markers=cts.getFeatures(featureClass='Marker')
# test all argument configurations to all del... functions
# 1a. delMarker(feature)
# 1b. delMarker(id)
# 2a. delMarkers(features)
# 2b. delMarkers(ids)
# 3a. delFeature(feature)
# 3b. delFeature(id)
# 3b1. delFeature(id,class) (correct class)
# 3b2. delFeature(id,class) (incorrect class)
# 4a. delFeatures(features)
# 4b. delFeatures(idAndClassList)

# # 1a. delMarker(feature)
# for marker in markers:
#     cts.delMarker(marker)

# # 1b. delMarker(id)
# for marker in markers:
#     cts.delMarker(marker['id'])

# 2a. delMarkers(features)
# cts.delMarkers(markers)

# # 2b. delMarkers(ids)
# cts.delMarkers([m['id'] for m in markers])

# # 3a. delFeature(feature)
# for marker in markers:
#     cts.delFeature(marker)

# # 3b. delFeature(id)
# for marker in markers:
#     cts.delFeature(marker['id'])

# # 3b1. delFeature(id,class) (correct class)
# for marker in markers:
#     cts.delFeature(marker['id'],'Marker')

# # 3b2. delFeature(id,class) (incorrect class) = requests should fail gracefully
# for marker in markers:
#     cts.delFeature(marker['id'],'Shape')

# # 4a. delFeatures(features)
# cts.delFeatures(markers)

# # 4b. delFeatures(idAndClassList)
# cts.delFeatures([{'id':m['id'],'class':m['properties']['class']} for m in markers])

# all del... QA passed 5-17-24

# print(json.dumps(markers,indent=3))
# delList=[]
# for marker in markers:
#     delList.append({'id':marker['id'],'class':'Marker'})
# cts.delFeatures(idAndClassList=delList)
# cts.delMarkers([marker['id'] for marker in markers])
# cts.delMarkers(markers)

# with open('acct.txt','w') as outfile:
#     outfile.write(json.dumps(cts.accountData,indent=3))

# cts.moveMarker([-121.026,38.885],title='a')
# cts.moveMarker([-121.036,38.885],id='7dddf464-e54f-483a-8cc9-9fa224d8e334')
# cts.editMarkerDescription('testDescription2',id='7dddf464-e54f-483a-8cc9-9fa224d8e334')
# cts.editMarkerDescription('testDescription3',title='a')
# with open('test.txt','w') as testLog:
#     testLog.write('current map title: '+str(cts.getMapTitle()))
#     testLog.write('\n\n'+json.dumps(cts.mapData,indent=3))
    # testLog.write('Name of PVTGT:'+cts.getMapTitle('PVTGT'))
    # testLog.write('\n***\nGroup memberships:\n'+str(cts.getGroupAccountTitles()))
    # testLog.write('\n***\nAll group map lists:\n'+json.dumps(cts.getAllMapLists(),indent=3))
    # testLog.write('\n***\nAll map lists including personal:\n'+json.dumps(cts.getAllMapLists(includePersonal=True),indent=3))
    # # cts.getAccountData(fromFileName='acct_since_0-mai.json')
    # testLog.write('\n***\naccountData:\n'+json.dumps(cts.accountData,indent=3))
    # testLog.write('\n***\nSAR Training maps:\n'+json.dumps(cts.getMapList('SAR Training'),indent=3))
    # testLog.write('\n***\nNCSSAR maps:\n'+json.dumps(cts.getMapList('NCSSAR'),indent=3))
    # testLog.write('\n***\nSAR Training maps:\n'+json.dumps(cts.getMapList('SAR Training',titlesOnly=True),indent=3))
    # testLog.write('\n***\ngroupAccounts:\n'+json.dumps(cts.groupAccounts,indent=3))
    # testLog.write('\n***\npersonalAccounts:\n'+json.dumps(cts.personalAccounts,indent=3))
# print('\nTest MAI Incident maps:\n'+json.dumps(cts.getMapList('Test MAI Incident'),indent=3))


# cts.openMap('44H1C')
# cts.openMap('J80')

# attempt to write to non-writable map
# cts.openMap('N3U63') # non-writable map, from SDL 10/26/23
# cts.addFolder('tmgFolder')
# cts.addMarker(39,-120,'tmgMarker')
# cts.addLine([[39,-120],[39.1,-120.1]],'tmgLine')
# cts.addPolygon([[39,-120],[39.1,-120.1],[39,-120.1]],'tmgPolygon')
# cts.addLineAssignment([[39.2,-120.2],[39.1,-120.1]],'tmgLineAssignment')
# cts.addAreaAssignment([[39.3,-120.3],[39.4,-120.4],[39,-120.5]],'tmgAreaAssignment')
# cts.addAppTrack([[39.6,-120.6],[39.7,-120.7]],'tmgAppTrack')

# cts.editFeature(className='Folder',title='Clues',properties={'title':'tmgCluesFolder'})
# exact case:
# cts.editFeature(className='Marker',title='Z',properties={'title':'tmgZ'})
# cts.editFeature(className='Shape',title='line1',properties={'title':'tmgLine1'})
# cts.editFeature(className='Shape',title='poly1',properties={'title':'tmgPoly1'})
# cts.editFeature(className='Assignment',letter='AreaAssign1',properties={'title':'tmgAreaAssign1'})
# cts.editFeature(className='Assignment',letter='LineAssign1',properties={'title':'tmgLineAssign1'})

# cts.caseSensitiveComparisons=True

# mismatched case:
# cts.editFeature(className='Marker',title='z',properties={'title':'tmgZ'})
# cts.editFeature(className='Shape',title='lIne1',properties={'title':'tmgLine1'})
# cts.editFeature(className='Shape',title='pOly1',properties={'title':'tmgPoly1'})
# cts.editFeature(className='Assignment',letter='ArEaAssign1',properties={'title':'tmgAreaAssign1'})
# cts.editFeature(className='Assignment',letter='LiNeAssign1',properties={'title':'tmgLineAssign1'})

####################
# geometry operations tests
# start by deleting all objects / with a blank map,
# then import geomTest.json

cts.cut('AC 103','b0') # cut area assignment using line
cts.cut('a1','b1') # cut polygon using line; preserve folder
cts.cut('a2','b2') # cut line using line
cts.cut('a3','b3') # cut line using line (multiple intersections)

cts.expand('a4','b4') # expand polygon using polygon (partial crossing)
cts.cut('AD 111','b00') # cut line using line (preserve attrinutes)
cts.cut('a5','b5') # cut polygon using polygon (preserve attributes)
cts.cut('a6','b6') # cut line using polygon
cts.expand('a7','b7') # expand polygon using polygon (complete crossing)
cts.cut('a8','b8') # cut polygon using line
cts.expand('a9','b9') # expand polygon (partial crossing)

# arguments are features
a10=cts.getFeatures(title='a10')[0]
b10=cts.getFeatures(title='b10')[0]
cts.cut(a10,b10)

# arguments are id strings
a11id=cts.getFeatures(title='a11')[0]['id']
b11id=cts.getFeatures(title='b11')[0]['id']
cts.expand(a11id,b11id)

cts.cut('a12','b12')
cts.expand('a13','b13')
cts.crop('a14','b14') # crop line using polygon
cts.crop('a15','b15') # crop line using area assignment
cts.crop('a16','b16') # crop polygon (multiple intersections)

# objects don't intersect - make sure we return gracefully
cts.expand('a11','a13')
cts.cut('a11','a6')
cts.crop('a14','b15')

# objects don't exist = make sure we return gracefully
cts.cut('foo','bar')
cts.expand('foo','bar')
cts.crop('foo','bar') 

cts.cut('a1','bar')
cts.expand('a1','bar')
cts.crop('a1','bar')

# getBounds at this point might not include all recent features!
assignments=cts.getFeatures('Assignment',forceRefresh=True)
print('assignments:'+str([a['properties']['title'] for a in assignments]))
print(str(cts.getBounds(assignments,0)))

# cts._refresh()

# assignments=cts.getFeatures('Assignment')
# print('assignments:'+str([a['properties']['title'] for a in assignments]))
# print(str(cts.getBounds(assignments,0)))



#### twoify test
# a=[
#    [
#       -121.1133059877452,
#       39.30596151413845
#    ],
#    [
#       -121.11791109653225,
#       39.30575648321715
#    ],
#    [
#       -121.11675901750955,
#       39.307236931228026
#    ],
#    [
#       -121.1189477000657,
#       39.310424652426924
#    ],
#    [
#       -121.11839298070474,
#       39.312954607507756
#    ],
#    [
#       -121.1138031892344,
#       39.31337594231999
#    ],
#    [
#       -121.1133059877452,
#       39.30596151413845
#    ]
# ]
# a=cts._twoify(a)
# print('after _twoify:'+json.dumps(a,indent=3))

# QA of .buffer2 and .intersection2 would be a bit more complicated
#  since they operate on shapely geometries, rather than caltopo features.
#  That means they would be much less likely to be called externally
#  (maybe they should actually be internal methods?) and probably don't need QA
#  before release of 2.0.0.

# cts.buffer2('a17',0.001)
# cts.intersection2('a18','b18')

# time.sleep(20) # to show that sync is still going

# print('\n\nadding folder')
# fid=cts.addFolder('MyFolder')
# print('\n\nadding marker: stuff')
# stuffID=cts.addMarker(39,-120,'stuff')
# time.sleep(15)
# cts.editMarkerDescription('abc',stuffID)

# print('\n\nadding marker: myStuff')
# myStuffID=cts.addMarker(39.01,-120.01,'myStuff',folderId=fid)
# print('\n\ngetting markers')
# r=cts.getFeatures('Marker')
# print('\n\nr:'+str(r))
# print('\n\nmoving the marker after a pause:'+myStuffID)
# time.sleep(30)
# print('\n\nmoving marker: myStuff')
# cts.moveMarker(39.02,-120.02,existingId=myStuffID)
# cts.addMarker(39.02,-120.02,'myStuff',existingId=myStuffID)
# print('\n\ndeleting "stuff" after a pause:')
# time.sleep(15)
# print('\n\ndeleting marker: stuff')
# cts.delMarker(stuffID)
# print('\n\ndone')

# j={}
# id='64acc33f-464d-47d0-9b5c-37f2aee81044'
# cts.editAreaAssignmentNumber('123',existingId=id)
# j['id']=id
# j['properties']={}
# j['properties']['number']='111'
# cts.sendRequest('post','assignment',j,id=id,returnJson='ID')