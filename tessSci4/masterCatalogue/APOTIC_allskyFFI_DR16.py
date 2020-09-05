import astropy.io.ascii as ascii
from astropy.table import Table, join

#Jamie Tayar 2020/09/04 join TIC+APOGEE in the simplest way possible
#borrows from mergelistsFe2.py



#read in TIC
tic1=Table.read("../v7.0/TESS13_jtayar_Tlt13.csv", format="ascii", delimiter=',') 


#add the 2M in front of 2MASS ID to make it APOGEE ID
tic=Table(tic1.filled()['id', 'TWOMASS', 'tmag'], dtype=['a20', 'a20','f'])
for i in range(len(tic[ 'TWOMASS'])):
	tic[ 'TWOMASS'][i]=('2M'+str(tic[ 'TWOMASS'][i])) # jt add str() part 5/5/2019
tic['TWOMASS'].name='APOGEE_ID'
tic['id'].name='TIC_ID'
tic['tmag'].name='TESS_mag'

#read in APOGEE
apogee=Table.read("allStar-r12-l33.fits", format="fits")

#do a join on the two catalogs: inner/left/right/outer depending on need
apotic=join(tic,apogee,join_type='inner')

#write out file
apotic.write('APOTIC_allskyTlt13_vI.0.2.fits', format='fits')
