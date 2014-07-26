# indexedmap
indexedmap.py is a tool to plot (color)indexed worldmaps from shape data using matplotlib.
The images can be used as lookup textures for country click detection or highlighting.

The required shape data can be downloaded from [naturaleathdata](http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_sovereignty.zip).

## Requirements
In addition to the shape files you need matplotlib and matplotlib-basemap.

Extract the data into the *shapes* directory:

`$ cd shapes
$ unzip ne_10m_admin_0_sovereignty.zip`

Once you have everything ready it's time for your first plot:

`
$ indexedmap.py -v
`
A new new indexed map should be generate in the *output*.
 directory
 The map will be generated using 256 grey step using the following lookup table:

## Color Mapping
`
{'PE':1,'BF':2,'FR':3,'LY':4,'BY':5,'PK':6,'ID':7,'YE':8,'MG':9,'BO':10,'CI':11,'DZ':12,'CH':13,'CM':14,'MK':15,'BW':16,'UA':17,
'KE':18,'TW':19,'JO':20,'MX':21,'AE':22,'BZ':23,'BR':24,'SL':25,'ML':26,'CD':27,'IT':28,'SO':29,'AF':30,'BD':31,'DO':32,'GW':33,
'GH':34,'AT':35,'SE':36,'TR':37,'UG':38,'MZ':39,'JP':40,'NZ':41,'CU':42,'VE':43,'PT':44,'CO':45,'MR':46,'AO':47,'DE':48,'SD':49,
'TH':50,'AU':51,'PG':52,'IQ':53,'HR':54,'GL':55,'NE':56,'DK':57,'LV':58,'RO':59,'ZM':60,'IR':61,'MM':62,'ET':63,'GT':64,'SR':65,
'EH':66,'CZ':67,'TD':68,'AL':69,'FI':70,'SY':71,'KG':72,'SB':73,'OM':74,'PA':75,'AR':76,'GB':77,'CR':78,'PY':79,'GN':80,'IE':81,
'NG':82,'TN':83,'PL':84,'NA':85,'ZA':86,'EG':87,'TZ':88,'GE':89,'SA':90,'VN':91,'RU':92,'HT':93,'BA':94,'IN':95,'CN':96,'CA':97,
'SV':98,'GY':99,'BE':100,'GQ':101,'LS':102,'BG':103,'BI':104,'DJ':105,'AZ':106,'MY':107,'PH':108,'UY':109,'CG':110,'RS':111,
'ME':112,'EE':113,'RW':114,'AM':115,'SN':116,'TG':117,'ES':118,'GA':119,'HU':120,'MW':121,'TJ':122,'KH':123,'KR':124,'HN':125,
'IS':126,'NI':127,'CL':128,'MA':129,'LR':130,'NL':131,'CF':132,'SK':133,'LT':134,'ZW':135,'LK':136,'IL':137,'LA':138,'KP':139,
'GR':140,'TM':141,'EC':142,'BJ':143,'SI':144,'NO':145,'MD':146,'LB':147,'NP':148,'ER':149,'US':150,'KZ':151,'AQ':152,'SZ':153,
'UZ':154,'MN':155,'BT':156,'NC':157,'FJ':158,'KW':159,'TL':160,'BS':161,'VU':162,'FK':163,'GM':164,'QA':165,'JM':166,'CY':167,
'PR':168,'PS':169,'BN':170,'TT':171,'CV':172,'PF':173,'WS':174,'LU':175,'KM':176,'MU':177,'FO':178,'ST':179,'AN':180,'DM':181,
'TO':182,'KI':183,'FM':184,'BH':185,'AD':186,'MP':187,'PW':188,'SC':189,'AG':190,'BB':191,'TC':192,'VC':193,'LC':194,'YT':195,
'VI':196,'GD':197,'MT':198,'MV':199,'KY':200,'KN':201,'MS':202,'BL':203,'NU':204,'PM':205,'CK':206,'WF':207,'AS':208,'MH':209,
'AW':210,'LI':211,'VG':212,'SH':213,'JE':214,'AI':215,'MF_1_':216,'GG':217,'SM':218,'BM':219,'TV':220,'NR':221,'GI':222,'PN':223,
'MC':224,'VA':225,'IM':226,'GU':227,'SG':228, 'SS':229, 'XK': 230}
`

Take a lok at the indexedmap.ini for tweaking.

![sample_image](sample/map_indexed.png)

