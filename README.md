
# Skin-detction
A skin detection program that detects human skin using Naive Bayes algorithm

# Outcomes
Input         							|  Output
:-------------------------:|:-------------------------:
![](https://github.com/Chinmoy007/Skin-detection/blob/master/test/1.jpg)  |  ![](https://github.com/Chinmoy007/Skin-detection/blob/master/test/result.jpg)

# What I did here[How it works]:
	1. First of all, read all the actual images with their corresponding mask pictures.
	2. Then for every (r, g, b) combination, calculated how many times this particular combination occurs as skin pixel and non_skin pixel.
	We identified non_skin pixel when the (r<150, g<150, b<150), otherwise skin
	3. Calculated probabiity for every distinct pixel.
		Lets say, for a rgb combination like 10, 20, 30
		It occurs as skin pixel 5 times and non skill pixel as 3 times.
			so, skin = 5
				non_skin = 3;

		Now probability of being skin pixel of that particluar rgb combination is (skin) / (skin + non_skin)
	
	4. Now for testing, select an unknown image. Read all the pixels of that image.
	5. If a particular rgb combinations probability of being skin is greater than a certain threshold(we assume it 0.555555)
	then consider that combination as skin pixel otherwise non_skin pixel. 


`This project is not completed fully. There is still some scopes where I need to change to improve the result.`

:kissing_closed_eyes: :kissing_closed_eyes: Feel free to fork and contribute and create issues here :kissing_closed_eyes: :kissing_closed_eyes:
