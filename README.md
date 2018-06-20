
# Skin-detction

# Algorithm [How it works]:
	1. First of all, read all the actual images with their corresponding mask pictures.
	2. Then for every (r, g, b) combination, find how many times this particular combination occurs as skin pixel and non_skin pixel.
	Identify non_skin pixel when the (r<150, g<150, b<150), otherwise skin
	3. Calculate probabiity for every distinct pixel.
		Lets say, for a rgb combination like 10, 20, 30
		It occurs as skin pixel 5 times and non skill pixel as 3 times.
			so, skin = 5
				non_skin = 3;

		Now probability of being skin pixel of that particluar rgb combination is (skin) / (skin + non_skin)
	
	4. Now for testing, select an unknown image. Read all the pixels of that image.
	5. If a particular rgb combinations probability of being skin is greater than a certain threshold(we assume it 0.555555) then consider that combination as skin pixel otherwise non_skin pixel. 


