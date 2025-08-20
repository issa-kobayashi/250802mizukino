import streamlit as st
from PIL import Image
# imageﾊpip install pillowｶﾞ必要 pil
import time
import datetime


x=int(0)
y=int(0)
n=int(0)
n1=int(0)
a=int(0)
n2c=int(0)


def step1one():
	global x
	global y
	global n 
	global n1
	global n2c
	
	time.sleep(0.1)
	global image0
	global image1
	global image2
	global image3
	global image4
	global image5
	global image6
	global image7
	global image8
	global image9
	
	
	global name00
	global name01
	
	global image20
	global image21
	global image22
	global image23
	global image24
	global image25
	global image26
	global image27
	global image28
	global image29
	global image30
		
	global name20
	global name21
	
	if n==0 :

		image0=Image.open('./data250802re/250802_160649.jpg')
		image1=Image.open('./data250802re/250802_160653.jpg')
		image2=Image.open('./data250802re/250802_160758.jpg')
		image3=Image.open('./data250802re/250802_160801.jpg')
		image4=Image.open('./data250802re/250802_160804.jpg')
		name00='250802_160649.jpg','250802_160653.jpg','250802_160758.jpg','250802_160801.jpg','250802_160804.jpg'
		     
	
		image5=Image.open('./data250802re/250802_160809.jpg') 
		image6=Image.open('./data250802re/250802_160830.jpg') 
		image7=Image.open('./data250802re/250802_160832.jpg') 
		image8=Image.open('./data250802re/250802_160834.jpg')
		image9=Image.open('./data250802re/250802_160837.jpg')
		name01='250802_160809.jpg','250802_160830.jpg','250802_160832.jpg','250802_160834.jpg','250802_160837.jpg'
		

	if n==1 :
		image0=Image.open('./data250802re/250802_160838.jpg')
		image1=Image.open('./data250802re/250802_160840.jpg') 
		image2=Image.open('./data250802re/250802_160843.jpg') 
		image3=Image.open('./data250802re/250802_160845.jpg')
		image4=Image.open('./data250802re/250802_160851.jpg')     
		
		name00='250802_160838.jpg','250802_160840.jpg','250802_160843.jpg','250802_160845.jpg','250802_160851.jpg'
		

		image5=Image.open('./data250802re/250802_160854.jpg')
		image6=Image.open('./data250802re/250802_160856.jpg') 
		image7=Image.open('./data250802re/250802_160905.jpg') 
		image8=Image.open('./data250802re/250802_160919.jpg')  
		image9=Image.open('./data250802re/250802_160920.jpg')
		name01='250802_160854.jpg','250802_160856.jpg','250802_160905.jpg','250802_160919.jpg','250802_162920.jpg'
		

	if n==2 :
		image0=Image.open('./data250802re/250802_162929.jpg')
		image1=Image.open('./data250802re/250802_162933.jpg') 
		image2=Image.open('./data250802re/250802_163021.jpg') 
		image3=Image.open('./data250802re/250802_163023.jpg') 
		image4=Image.open('./data250802re/250802_163112.jpg')  
		name00='250802_162929.jpg','250802_162933.jpg','250802_163021.jpg','250802_163023.jpg','250802_163112.jpg'
		
	
	
	
		image5=Image.open('./data250802re/250802_163127.jpg')
		image6=Image.open('./data250802re/250802_163152.jpg') 
		image7=Image.open('./data250802re/250802_163155.jpg') 
		image8=Image.open('./data250802re/250802_164551.jpg')
		image9=Image.open('./data250802re/250802_164554.jpg')   
		name01='250802_163127.jpg','250802_163152.jpg','250802_163155.jpg','250802_164551.jpg','250802_164554.jpg'
	
	
	if n==3 :
		image0=Image.open('./data250802re/250802_164626.jpg')
		image1=Image.open('./data250802re/250802_165645.jpg') 
		image2=Image.open('./data250802re/250802_165649.jpg') 
		image3=Image.open('./data250802re/250802_165653.jpg')
		image4=Image.open('./data250802re/250802_165703.jpg')   
		name00='250802_164626.jpg','250802_165645.jpg','250802_165649.jpg','250802_165653.jpg','250802_165703.jpg'
	
	

		image5=Image.open('./data250802re/250802_165750.jpg')
		image6=Image.open('./data250802re/250802_165815.jpg') 
		image7=Image.open('./data250802re/250802_165827.jpg') 
		image8=Image.open('./data250802re/250802_165934.jpg')
		image9=Image.open('./data250802re/250802_165946.jpg')   
		name01='250802_165750.jpg','250802_16815.jpg','250802_165827.jpg','250802_165934.jpg','250802_165946.jpg'
	
	
	if n==4 :
		image0=Image.open('./data250802re/250802_165949.jpg')
		image1=Image.open('./data250802re/250802_165951.jpg') 
		image2=Image.open('./data250802re/250802_165956.jpg') 
		image3=Image.open('./data250802re/250802_170001.jpg')
		image4=Image.open('./data250802re/250802_170004.jpg')   
		name00='250802_165949.jpg','250802_165951.jpg','250802_165956.jpg','250802_170001.jpg','250802_170004.jpg'
	
	
		image5=Image.open('./data250802re/250802_170036.jpg')
		image6=Image.open('./data250802re/250802_170038.jpg') 
		image7=Image.open('./data250802re/250802_170144.jpg') 
		image8=Image.open('./data250802re/250802_170146.jpg')
		image9=Image.open('./data250802re/250802_170148.jpg')   
		name01='250802_165949.jpg','250802_165951.jpg','250802_165956.jpg','250802_170001.jpg','250802_170004.jpg'
	
	
	if n==5 :
		image0=Image.open('./data250802re/250802_170151.jpg')
		image1=Image.open('./data250802re/250802_170203.jpg')
		image2=Image.open('./data250802re/250802_171310.jpg')
		image3=Image.open('./data250802re/250802_171320.jpg')
		image4=Image.open('./data250802re/250802_171324.jpg')
		name00='250802_170151.jpg','250802_170203.jpg','250802_171310.jpg','250802_171320.jpg','250802_171324.jpg'

		image1=Image.open('./data250802re/250802_171341.jpg')
		image2=Image.open('./data250802re/250802_171404.jpg')
		image3=Image.open('./data250802re/250802_171405.jpg')
		image4=Image.open('./data250802re/250802_171514.jpg')
		image5=Image.open('./data250802re/250802_171516.jpg')
		name01='250802_171341.jpg','250802_171404.jpg	','250802_171405.jpg','250802_171514.jpg','250802_171516.jpg'

		
		
	if n==6:	
		image0=Image.open('./data250802re/250802_171552.jpg')
		image1=Image.open('./data250802re/250802_171616.jpg')
		image2=Image.open('./data250802re/250802_171622.jpg')
		image3=Image.open('./data250802re/250802_173613.jpg')
		image4=Image.open('./data250802re/250802_173617.jpg')
		name00='250802_171552.jpg','250802_171616.jpg','250802_171622.jpg','250802_173613.jpg','250802_173617.jpg'

		
	
		image5=Image.open('./data250802re/250802_173641.jpg')
		image6=Image.open('./data250802re/250802_173645.jpg')
		image7=Image.open('./data250802re/250802_173650.jpg')
		image8=Image.open('./data250802re/250802_173656.jpg')
		image9=Image.open('./data250802re/250802_173658.jpg')
		name01='250802_173641.jpg','250802_173645.jpg','250802_173650.jpg','250802_173656.jpg','250802_173658.jpg'

		
	if n==7:
		image0=Image.open('./data250802re/250802_173704.jpg')
		image1=Image.open('./data250802re/250802_173707.jpg')
		image2=Image.open('./data250802re/250802_173719.jpg')
		image3=Image.open('./data250802re/250802_173720.jpg')
		image4=Image.open('./data250802re/250802_173721.jpg')
		name00='250802_173704.jpg','250802_173707.jpg','250802_173719.jpg','250802_173720.jpg','250802_173721.jpg'

	

		image5=Image.open('./data250802re/250802_173723.jpg')
		image6=Image.open('./data250802re/250802_173727.jpg')
		image7=Image.open('./data250802re/250802_173733.jpg')
		image8=Image.open('./data250802re/250802_173747.jpg')
		image9=Image.open('./data250802re/250802_173759.jpg')
		name01='250802_173723.jpg','250802_173727.jpg','250802_173733.jpg','250802_173747.jpg','250802_173759.jpg'

	
	if n==8:
		image1=Image.open('./data250802re/250802_173807.jpg')
		image2=Image.open('./data250802re/250802_173808.jpg')
		image3=Image.open('./data250802re/250802_173855.jpg')
		image4=Image.open('./data250802re/250802_173903.jpg')
		image5=Image.open('./data250802re/250802_173905.jpg')
		name00='250802_173807.jpg','250802_173808.jpg','250802_173855.jpg','250802_173903.jpg','250802_173905.jpg'



		image5=Image.open('./data250802re/250802_173925.jpg')
		image6=Image.open('./data250802re/250802_173944.jpg')
		image7=Image.open('./data250802re/250802_174215.jpg')
		image8=Image.open('./data250802re/250802_174223.jpg')
		image9=Image.open('./data250802re/250802_174251.jpg')
		name01='250802_173925.jpg','250802_173944.jpg','250802_174215.jpg','250802_174223.jpg','250802_174251.jpg'

	
	if n==9:
		image0=Image.open('./data250802re/250802_174355.jpg')
		image1=Image.open('./data250802re/250802_174403.jpg')
		image2=Image.open('./data250802re/250802_174410.jpg')
		image3=Image.open('./data250802re/250802_174414.jpg')
		image4=Image.open('./data250802re/250802_174433.jpg')
		name00='250802_174355.jpg','250802_174403.jpg','250802_174410.jpg','250802_174414.jpg','250802_174433.jpg'
		
		

		image5=Image.open('./data250802re/250802_174436.jpg')
		image6=Image.open('./data250802re/250802_174625.jpg')
		image7=Image.open('./data250802re/250802_174627.jpg')
		image8=Image.open('./data250802re/250802_174630.jpg')
		image9=Image.open('./data250802re/250802_174637.jpg')
		name01='250802_174436.jpg','250802_174625.jpg','250802_174627.jpg','250802_174630.jpg','250802_174637.jpg'

	
	if n==10:
		image0=Image.open('./data250802re/250802_174726.jpg')
		image1=Image.open('./data250802re/250802_174737.jpg')
		image2=Image.open('./data250802re/250802_174743.jpg')
		image3=Image.open('./data250802re/250802_180410.jpg')
		image4=Image.open('./data250802re/250802_180416.jpg')
		name00='250802_174726.jpg','250802_174737.jpg','250802_174743.jpg','250802_180410.jpg','250802_180416.jpg'

	

		image5=Image.open('./data250802re/250802_180417.jpg')
		image6=Image.open('./data250802re/250802_180425.jpg')
		image7=Image.open('./data250802re/250802_180448.jpg')
		image8=Image.open('./data250802re/250802_180656.jpg')
		image9=Image.open('./data250802re/250802_180658.jpg')
		name01='250802_180417.jpg','250802_180425.jpg','250802_180448.jpg','250802_180656.jpg','250802_180658.jpg'

	
	if n==11:
		image0=Image.open('./data250802re/250802_180709.jpg')
		image1=Image.open('./data250802re/250802_180928.jpg')
		image2=Image.open('./data250802re/250802_180939.jpg')
		image3=Image.open('./data250802re/250802_180946.jpg')
		image4=Image.open('./data250802re/250802_181525.jpg')
		name00='250802_180709.jpg	','250802_180928.jpg','250802_180939.jpg','250802_180946.jpg','250802_181525.jpg'


		image5=Image.open('./data250802re/250802_181531.jpg')
		image6=Image.open('./data250802re/250802_181533.jpg')
		image7=Image.open('./data250802re/250802_181554.jpg')
		image8=Image.open('./data250802re/250802_181602.jpg')
		image9=Image.open('./data250802re/250802_182203.jpg')
		name01='250802_181531.jpg','250802_181533.jpg','250802_181554.jpg','250802_181602.jpg','250802_182203.jpg'

	if n==12:
		image0=Image.open('./data250802re/250802_182207.jpg')
		image1=Image.open('./data250802re/250802_190126.jpg')
		image2=Image.open('./data250802re/250802_190132.jpg')
		image3=Image.open('./data250802re/250802_190138.jpg')
		image4=Image.open('./data250802re/250802_190226.jpg')
		name00='250802_182207.jpg','250802_190126.jpg','250802_190132.jpg','250802_190138.jpg','250802_190226.jpg'

	

		image5=Image.open('./data250802re/250802_190228.jpg')
		image6=Image.open('./data250802re/250802_190234.jpg')
		image7=Image.open('./data250802re/250802_190252.jpg')
		image8=Image.open('./data250802re/250802_190254.jpg')
		image9=Image.open('./data250802re/250802_190300.jpg')
		name01='250802_190228.jpg','250802_190234.jpg','250802_190252.jpg','250802_190254.jpg','250802_190300.jpg'

	if n==13:
		image0=Image.open('./data250802re/250802_190301.jpg')
		image1=Image.open('./data250802re/250802_190303.jpg')
		image2=Image.open('./data250802re/250802_190316.jpg')
		image3=Image.open('./data250802re/250802_190328.jpg')
		image4=Image.open('./data250802re/250802_190340.jpg')
		name00='250802_190301.jpg','250802_190303.jpg','250802_190316.jpg','250802_190328.jpg','250802_190340.jpg'


		image5=Image.open('./data250802re/250802_190345.jpg')
		image6=Image.open('./data250802re/250802_190402.jpg')
		image7=Image.open('./data250802re/250802_190406.jpg')
		image8=Image.open('./data250802re/250802_190412.jpg')
		image9=Image.open('./data250802re/250802_190414.jpg')
		name01='250802_190345.jpg','250802_190402.jpg','250802_190406.jpg','250802_190412.jpg','250802_190414.jpg'

	
	if n==14:
		image0=Image.open('./data250802re/250802_190440.jpg')
		image1=Image.open('./data250802re/250802_190442.jpg')
		image2=Image.open('./data250802re/250802_190500.jpg')
		image3=Image.open('./data250802re/250802_190543.jpg')
		image4=Image.open('./data250802re/250802_190547.jpg')
		name00='250802_190440.jpg','250802_190442.jpg','250802_190500.jpg','250802_190543.jpg','250802_190547.jpg'


	
		image5=Image.open('./data250802re/250802_190551.jpg')
		image6=Image.open('./data250802re/250802_190613.jpg')
		image7=Image.open('./data250802re/250802_190615.jpg')
		image8=Image.open('./data250802re/250802_190626.jpg')
		image9=Image.open('./data250802re/250802_190641.jpg')
		name01='250802_190551.jpg','250802_190613.jpg','250802_190615.jpg','250802_190626.jpg','250802_190641.jpg'

	if n==15:
		image0=Image.open('./data250802re/250802_193440.jpg')
		image1=Image.open('./data250802re/250802_193445.jpg')
		image2=Image.open('./data250802re/250802_193449.jpg')
		image3=Image.open('./data250802re/250802_193637.jpg')
		image4=Image.open('./data250802re/250802_193712.jpg')
		name00='250802_193440.jpg','250802_193445.jpg','250802_193449.jpg','250802_193637.jpg','250802_193712.jpg'


		image5=Image.open('./data250802re/250802_193718.jpg')
		image6=Image.open('./data250802re/250802_193719.jpg')
		image7=Image.open('./data250802re/250802_193746.jpg')
		image8=Image.open('./data250802re/250802_193751.jpg')
		image9=Image.open('./data250802re/250802_193806.jpg')
		name00='250802_193718.jpg','250802_193719.jpg','250802_193746.jpg','250802_193751.jpg','250802_193806.jpg'

	if n==16:
		image0=Image.open('./data250802re/250802_194244.jpg')
		image1=Image.open('./data250802re/250802_194256.jpg')
		image2=Image.open('./data250802re/250802_194306.jpg')
		image3=Image.open('./data250802re/250802_194314.jpg')
		image4=Image.open('./data250802re/250802_194321.jpg')

		name00='250802_194244.jpg','250802_194256.jpg','250802_194306.jpg','250802_194314.jpg','250802_194321.jpg'

		image5=Image.open('./data250802re/250802_194244.jpg')
		image6=Image.open('./data250802re/250802_194256.jpg')
		image7=Image.open('./data250802re/250802_194306.jpg')
		image8=Image.open('./data250802re/250802_194314.jpg')
		image9=Image.open('./data250802re/250802_194321.jpg')

		name01='250802_194244.jpg','250802_194256.jpg','250802_194306.jpg','250802_194314.jpg','250802_194321.jpg'

	
	
	
	
	
	
	st.image(image0,width=200)
	st.image(image1,width=200)
	st.image(image2,width=200)
	st.image(image3,width=200)
	st.image(image4,width=200)
	
	st.image(image5,width=200)
	st.image(image6,width=200)
	st.image(image7,width=200)
	st.image(image8,width=200)
	st.image(image9,width=200)
	
	
	
	
	
	
	
	
	time.sleep(0.1)
	
	

def step2one():
#************************************************************
	global x
	global y
	global n 
	global n1
	global n2c

	#print(f'def step two ｽﾃｯﾌﾟ2の処理 y= n2c=: ')
	time.sleep(0.1)
	global image20
	global image21
	global image22
	global image23
	global image24
	
	global name20 
	
	global image25
	global image26
	global image27
	global image28
	global image29
	
	global name21
	
	
	if n==0:
		n2c=1
	
	if n==2:
		n2c=3

	if n==3:
		n2c=4
		
	
	if n==4:
		n2c=5
	
	if n==6:
		n2c=7

	if n==7:
		n2c=8

	
	if n==8:
		n2c=9
	
	if n==10:
		n2c=11
	
	if n==12:
		n2c=13

	if n==13:
		n2c=14

	
	if n==14:
		n2c=15
	
	if n==16:
		n2c=17
	
	if n==18:
		n2c=19	
	
	if n==20:
		n2c=21
	
	if n==22:
		n2c=23

	if n==23:
		n2c=24

	

	
	
	
	
	
	
	
	
	
	
	time.sleep(0.1)
	if n2c==0 :
		image20=Image.open('./data250802re/250802_160649.jpg') 
		image21=Image.open('./data250802re/250802_160653.jpg') 
		image22=Image.open('./data250802re/250802_160758.jpg') 
		image23=Image.open('./data250802re/250802_160801.jpg') 
		image24=Image.open('./data250802re/250802_160804.jpg')
		name00='250802_160649.jpg','250802_160653.jpg','250802_160758.jpg','250802_160801.jpg','250802_160804.jpg'

		     
	
		image25=Image.open('./data250802re/250802_160809.jpg') 
		image26=Image.open('./data250802re/250802_160830.jpg') 
		image27=Image.open('./data250802re/250802_160832.jpg') 
		image28=Image.open('./data250802re/250802_160834.jpg')
		image29=Image.open('./data250802re/250802_160837.jpg')
		name01='250802_160809.jpg','250802_160830.jpg','250802_160832.jpg','250802_160834.jpg','250802_160837.jpg'
		

	if n2c==1 :
		image20=Image.open('./data250802re/250802_160838.jpg')
		image21=Image.open('./data250802re/250802_160840.jpg') 
		image22=Image.open('./data250802re/250802_160843.jpg') 
		image23=Image.open('./data250802re/250802_160845.jpg')
		image24=Image.open('./data250802re/250802_160851.jpg')     
		name00='250802_160838.jpg','250802_160840.jpg','250802_160843.jpg','250802_160845.jpg','250802_160851.jpg'
		

		image25=Image.open('./data250802re/250802_160854.jpg')
		image26=Image.open('./data250802re/250802_160856.jpg') 
		image27=Image.open('./data250802re/250802_160905.jpg') 
		image28=Image.open('./data250802re/250802_160919.jpg')  
		image29=Image.open('./data250802re/250802_160920.jpg')
		name01='250802_160854.jpg','250802_160856.jpg','250802_160905.jpg','250802_160919.jpg','250802_162920.jpg'
		

	if n2c==2 :
		image20=Image.open('./data250802re/250802_162929.jpg')
		image21=Image.open('./data250802re/250802_162933.jpg') 
		image22=Image.open('./data250802re/250802_163021.jpg') 
		image23=Image.open('./data250802re/250802_163023.jpg') 
		image24=Image.open('./data250802re/250802_163112.jpg')  
		name00='250802_162929.jpg','250802_162933.jpg','250802_163021.jpg','250802_163023.jpg','250802_163112.jpg'
		
	
	
	
		image25=Image.open('./data250802re/250802_163127.jpg')
		image26=Image.open('./data250802re/250802_163152.jpg') 
		image27=Image.open('./data250802re/250802_163155.jpg') 
		image28=Image.open('./data250802re/250802_164551.jpg')
		image29=Image.open('./data250802re/250802_164554.jpg')   
		name01='250802_163127.jpg','250802_163152.jpg','250802_163155.jpg','250802_164551.jpg','250802_164554.jpg'
	
	
	if n2c==3 :
		image20=Image.open('./data250802re/250802_164626.jpg')
		image21=Image.open('./data250802re/250802_165645.jpg') 
		image22=Image.open('./data250802re/250802_165649.jpg') 
		image23=Image.open('./data250802re/250802_165653.jpg')
		image24=Image.open('./data250802re/250802_165703.jpg')   
		name00='250802_164626.jpg','250802_165645.jpg','250802_165649.jpg','250802_165653.jpg','250802_165703.jpg'
	
	

		image25=Image.open('./data250802re/250802_165750.jpg')
		image26=Image.open('./data250802re/250802_165815.jpg') 
		image27=Image.open('./data250802re/250802_165827.jpg') 
		image28=Image.open('./data250802re/250802_165934.jpg')
		image29=Image.open('./data250802re/250802_165946.jpg')   
		name01='250802_165750.jpg','250802_16815.jpg','250802_165827.jpg','250802_165934.jpg','250802_165946.jpg'
	
	
	if n2c==4 :
		image20=Image.open('./data250802re/250802_165949.jpg')
		image21=Image.open('./data250802re/250802_165951.jpg') 
		image22=Image.open('./data250802re/250802_165956.jpg') 
		image23=Image.open('./data250802re/250802_170001.jpg')
		image24=Image.open('./data250802re/250802_170004.jpg')   
		name00='250802_165949.jpg','250802_165951.jpg','250802_165956.jpg','250802_170001.jpg','250802_170004.jpg'
	
	
		image25=Image.open('./data250802re/250802_170036.jpg')
		image26=Image.open('./data250802re/250802_170038.jpg') 
		image27=Image.open('./data250802re/250802_170144.jpg') 
		image28=Image.open('./data250802re/250802_170146.jpg')
		image29=Image.open('./data250802re/250802_170148.jpg')   
		name01='250802_165949.jpg','250802_165951.jpg','250802_165956.jpg','250802_170001.jpg','250802_170004.jpg'
	
	
	if n2c==5 :
		image20=Image.open('./data250802re/250802_170151.jpg')
		image21=Image.open('./data250802re/250802_170203.jpg')
		image22=Image.open('./data250802re/250802_171310.jpg')
		image23=Image.open('./data250802re/250802_171320.jpg')
		image24=Image.open('./data250802re/250802_171324.jpg')
		name00='250802_170151.jpg','250802_170203.jpg','250802_171310.jpg','250802_171320.jpg','250802_171324.jpg'

		image25=Image.open('./data250802re/250802_171341.jpg')
		image26=Image.open('./data250802re/250802_171404.jpg')
		image27=Image.open('./data250802re/250802_171405.jpg')
		image28=Image.open('./data250802re/250802_171514.jpg')
		image29=Image.open('./data250802re/250802_171516.jpg')
		name01='250802_171341.jpg','250802_171404.jpg	','250802_171405.jpg','250802_171514.jpg','250802_171516.jpg'

		
		
	if n2c==6:	
		image20=Image.open('./data250802re/250802_171552.jpg')
		image21=Image.open('./data250802re/250802_171616.jpg')
		image22=Image.open('./data250802re/250802_171622.jpg')
		image23=Image.open('./data250802re/250802_173613.jpg')
		image24=Image.open('./data250802re/250802_173617.jpg')
		name00='250802_171552.jpg','250802_171616.jpg','250802_171622.jpg','250802_173613.jpg','250802_173617.jpg'

		
	
		image25=Image.open('./data250802re/250802_173641.jpg')
		image26=Image.open('./data250802re/250802_173645.jpg')
		image27=Image.open('./data250802re/250802_173650.jpg')
		image28=Image.open('./data250802re/250802_173656.jpg')
		image29=Image.open('./data250802re/250802_173658.jpg')
		name01='250802_173641.jpg','250802_173645.jpg','250802_173650.jpg','250802_173656.jpg','250802_173658.jpg'

		
	if n2c==7:
		image20=Image.open('./data250802re/250802_173704.jpg')
		image21=Image.open('./data250802re/250802_173707.jpg')
		image22=Image.open('./data250802re/250802_173719.jpg')
		image23=Image.open('./data250802re/250802_173720.jpg')
		image24=Image.open('./data250802re/250802_173721.jpg')
		name00='250802_173704.jpg','250802_173707.jpg','250802_173719.jpg','250802_173720.jpg','250802_173721.jpg'

	

		image25=Image.open('./data250802re/250802_173723.jpg')
		image26=Image.open('./data250802re/250802_173727.jpg')
		image27=Image.open('./data250802re/250802_173733.jpg')
		image28=Image.open('./data250802re/250802_173747.jpg')
		image29=Image.open('./data250802re/250802_173759.jpg')
		name01='250802_173723.jpg','250802_173727.jpg','250802_173733.jpg','250802_173747.jpg','250802_173759.jpg'

	
	if n2c==8:
		image20=Image.open('./data250802re/250802_173807.jpg')
		image21=Image.open('./data250802re/250802_173808.jpg')
		image22=Image.open('./data250802re/250802_173855.jpg')
		image23=Image.open('./data250802re/250802_173903.jpg')
		image24=Image.open('./data250802re/250802_173905.jpg')
		name00='250802_173807.jpg','250802_173808.jpg','250802_173855.jpg','250802_173903.jpg','250802_173905.jpg'



		image25=Image.open('./data250802re/250802_173925.jpg')
		image26=Image.open('./data250802re/250802_173944.jpg')
		image27=Image.open('./data250802re/250802_174215.jpg')
		image28=Image.open('./data250802re/250802_174223.jpg')
		image29=Image.open('./data250802re/250802_174251.jpg')
		name01='250802_173925.jpg','250802_173944.jpg','250802_174215.jpg','250802_174223.jpg','250802_174251.jpg'

	
	if n2c==9:
		image20=Image.open('./data250802re/250802_174355.jpg')
		image21=Image.open('./data250802re/250802_174403.jpg')
		image22=Image.open('./data250802re/250802_174410.jpg')
		image23=Image.open('./data250802re/250802_174414.jpg')
		image24=Image.open('./data250802re/250802_174433.jpg')
		name00='250802_174355.jpg','250802_174403.jpg','250802_174410.jpg','250802_174414.jpg','250802_174433.jpg'
		
		

		image25=Image.open('./data250802re/250802_174436.jpg')
		image26=Image.open('./data250802re/250802_174625.jpg')
		image27=Image.open('./data250802re/250802_174627.jpg')
		image28=Image.open('./data250802re/250802_174630.jpg')
		image29=Image.open('./data250802re/250802_174637.jpg')
		name01='250802_174436.jpg','250802_174625.jpg','250802_174627.jpg','250802_174630.jpg','250802_174637.jpg'

	
	if n2c==10:
		image20=Image.open('./data250802re/250802_174726.jpg')
		image21=Image.open('./data250802re/250802_174737.jpg')
		image22=Image.open('./data250802re/250802_174743.jpg')
		image23=Image.open('./data250802re/250802_180410.jpg')
		image24=Image.open('./data250802re/250802_180416.jpg')
		name00='250802_174726.jpg','250802_174737.jpg','250802_174743.jpg','250802_180410.jpg','250802_180416.jpg'

	

		image25=Image.open('./data250802re/250802_180417.jpg')
		image26=Image.open('./data250802re/250802_180425.jpg')
		image27=Image.open('./data250802re/250802_180448.jpg')
		image28=Image.open('./data250802re/250802_180656.jpg')
		image29=Image.open('./data250802re/250802_180658.jpg')
		name01='250802_180417.jpg','250802_180425.jpg','250802_180448.jpg','250802_180656.jpg','250802_180658.jpg'

	
	if n2c==11:
		image20=Image.open('./data250802re/250802_180709.jpg')
		image21=Image.open('./data250802re/250802_180928.jpg')
		image22=Image.open('./data250802re/250802_180939.jpg')
		image23=Image.open('./data250802re/250802_180946.jpg')
		image24=Image.open('./data250802re/250802_181525.jpg')
		name00='250802_180709.jpg	','250802_180928.jpg','250802_180939.jpg','250802_180946.jpg','250802_181525.jpg'


		image25=Image.open('./data250802re/250802_181531.jpg')
		image26=Image.open('./data250802re/250802_181533.jpg')
		image27=Image.open('./data250802re/250802_181554.jpg')
		image28=Image.open('./data250802re/250802_181602.jpg')
		image29=Image.open('./data250802re/250802_182203.jpg')
		name01='250802_181531.jpg','250802_181533.jpg','250802_181554.jpg','250802_181602.jpg','250802_182203.jpg'

	if n2c==12:
		image20=Image.open('./data250802re/250802_182207.jpg')
		image21=Image.open('./data250802re/250802_190126.jpg')
		image22=Image.open('./data250802re/250802_190132.jpg')
		image23=Image.open('./data250802re/250802_190138.jpg')
		image24=Image.open('./data250802re/250802_190226.jpg')
		name00='250802_182207.jpg','250802_190126.jpg','250802_190132.jpg','250802_190138.jpg','250802_190226.jpg'

	

		image25=Image.open('./data250802re/250802_190228.jpg')
		image26=Image.open('./data250802re/250802_190234.jpg')
		image27=Image.open('./data250802re/250802_190252.jpg')
		image28=Image.open('./data250802re/250802_190254.jpg')
		image29=Image.open('./data250802re/250802_190300.jpg')
		name01='250802_190228.jpg','250802_190234.jpg','250802_190252.jpg','250802_190254.jpg','250802_190300.jpg'

	if n2c==13:
		image20=Image.open('./data250802re/250802_190301.jpg')
		image21=Image.open('./data250802re/250802_190303.jpg')
		image22=Image.open('./data250802re/250802_190316.jpg')
		image23=Image.open('./data250802re/250802_190328.jpg')
		image24=Image.open('./data250802re/250802_190340.jpg')
		name00='250802_190301.jpg','250802_190303.jpg','250802_190316.jpg','250802_190328.jpg','250802_190340.jpg'


		image25=Image.open('./data250802re/250802_190345.jpg')
		image26=Image.open('./data250802re/250802_190402.jpg')
		image27=Image.open('./data250802re/250802_190406.jpg')
		image28=Image.open('./data250802re/250802_190412.jpg')
		image29=Image.open('./data250802re/250802_190414.jpg')
		name01='250802_190345.jpg','250802_190402.jpg','250802_190406.jpg','250802_190412.jpg','250802_190414.jpg'

	
	if n2c==14:
		image20=Image.open('./data250802re/250802_190440.jpg')
		image21=Image.open('./data250802re/250802_190442.jpg')
		image22=Image.open('./data250802re/250802_190500.jpg')
		image23=Image.open('./data250802re/250802_190543.jpg')
		image24=Image.open('./data250802re/250802_190547.jpg')
		name00='250802_190440.jpg','250802_190442.jpg','250802_190500.jpg','250802_190543.jpg','250802_190547.jpg'


	
		image25=Image.open('./data250802re/250802_190551.jpg')
		image26=Image.open('./data250802re/250802_190613.jpg')
		image27=Image.open('./data250802re/250802_190615.jpg')
		image28=Image.open('./data250802re/250802_190626.jpg')
		image29=Image.open('./data250802re/250802_190641.jpg')
		name01='250802_190551.jpg','250802_190613.jpg','250802_190615.jpg','250802_190626.jpg','250802_190641.jpg'

	if n2c==15:
		image20=Image.open('./data250802re/250802_193440.jpg')
		image21=Image.open('./data250802re/250802_193445.jpg')
		image22=Image.open('./data250802re/250802_193449.jpg')
		image23=Image.open('./data250802re/250802_193637.jpg')
		image24=Image.open('./data250802re/250802_193712.jpg')
		name00='250802_193440.jpg','250802_193445.jpg','250802_193449.jpg','250802_193637.jpg','250802_193712.jpg'


		image25=Image.open('./data250802re/250802_193718.jpg')
		image26=Image.open('./data250802re/250802_193719.jpg')
		image27=Image.open('./data250802re/250802_193746.jpg')
		image28=Image.open('./data250802re/250802_193751.jpg')
		image29=Image.open('./data250802re/250802_193806.jpg')
		name00='250802_193718.jpg','250802_193719.jpg','250802_193746.jpg','250802_193751.jpg','250802_193806.jpg'

	if n2c==16:
		image20=Image.open('./data250802re/250802_194244.jpg')
		image21=Image.open('./data250802re/250802_194256.jpg')
		image22=Image.open('./data250802re/250802_194306.jpg')
		image23=Image.open('./data250802re/250802_194314.jpg')
		image24=Image.open('./data250802re/250802_194321.jpg')

		name00='250802_194244.jpg','250802_194256.jpg','250802_194306.jpg','250802_194314.jpg','250802_194321.jpg'

		image25=Image.open('./data250802re/250802_194244.jpg')
		image26=Image.open('./data250802re/250802_194256.jpg')
		image27=Image.open('./data250802re/250802_194306.jpg')
		image28=Image.open('./data250802re/250802_194314.jpg')
		image29=Image.open('./data250802re/250805_074401.jpg')

		name01='250802_194244.jpg','250802_194256.jpg','250802_194306.jpg','250802_194314.jpg','250805_074401.jpg'

	
	
	
	
	
	
	st.image(image20,width=200)
	st.image(image21,width=200)
	st.image(image22,width=200)
	st.image(image23,width=200)
	st.image(image24,width=200)
	
	st.image(image25,width=200)
	st.image(image26,width=200)
	st.image(image27,width=200)
	st.image(image28,width=200)
	st.image(image29,width=200)
	
	
	
	
	
	
	
	
	time.sleep(0.1)

#縦に分轄
col1,col2=st.columns(2)

with col1:

#submit_btn=st.form_submit_button (f'切替')
	submit_btn0=st.button('切替0')
	submit_btn2=st.button('切替2')
	submit_btn4=st.button('切替4')
	submit_btn6=st.button('切替6')
	submit_btn8=st.button('切替8')
	
	submit_btn0=st.button('切替10')
	submit_btn2=st.button('切替12')
	submit_btn4=st.button('切替14')
	submit_btn6=st.button('切替16')
	
	if submit_btn0 :
		n=0
		time.sleep(0.1)
		
	if submit_btn2 :
		n=2
		time.sleep(0.1)

	if submit_btn4 :
		n=4
		time.sleep(0.1)
	
	if submit_btn6 :
		n=6	
		time.sleep(0.1)
		
	if submit_btn8 :
		n=8

	if submit_btn10 :
		n=10
		time.sleep(0.1)
		
	if submit_btn12 :
		n=12
		time.sleep(0.1)

	if submit_btn14 :
		n=14
		time.sleep(0.1)
	
	if submit_btn16 :
		n=16	
		time.sleep(0.1)
		











	step1one()
		#関数 def =することで実行される
	st.text(f'ﾌﾟﾛｾｽ1 {name00}')     
	st.text(f'ﾌﾟﾛｾｽ1 {name01}')
         

with col2:
	st.subheader('みずき野紹介')
        
	st.text('田んぼに囲まれたとても静かな街です｡')
	st.write('250802みずき野祭り')    
	step2one()  
	#関数 def =することで実行される
	st.text(f'ﾌﾟﾛｾｽ2 {name20}')
	st.text(f'ﾌﾟﾛｾｽ2 {name21}')
	time.sleep(0.1)

