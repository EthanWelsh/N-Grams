# N-Grams

##Install
```
$ pip install git+https://github.com/EthanWelsh/N-Grams.git
```

OR

```
$ git clone https://github.com/EthanWelsh/N-Grams.git
$ pip install -r requirements.txt
```

##Run
```
python3 main.py <filename>
```
IE:
```
python3 main.py hw1_samplein.txt
```

## 2. Intrinsic Evaluation
```
python ngram.py 3s train.txt dev.txt test.txt
Average perplexity over all sentences: 7.16788 using the following lambdas: (0.98241372299209306, 4.1330750372837589e-12, 0.18466026783388856)
6.20572 : <s> b a , a a </s>
7.13254 : <s> b a h </s>
8.54297 : <s> b a , i </s>
7.73486 : <s> a b , j k , b a </s>
6.22332 : <s> a a , a b , b </s>
```


## 3. Extrinsic Evaluation
```
<s> My morning's work has not been wasted , since it has proved that he has the very strongest motives for standing in the way of anything of the sort </s>
	=> <s> My morning's work has not been neglected , since it has proved that he has the very strongest motives for standing in the way of anything of the sort </s>
********
<s> It was furred outside by a thick layer of dust , and damp and worms had eaten through the wood , so that a crop of livid fungi was growing on the inside of it </s>
	=> <s> It was furred outside by a thick layer of dust , and damp and worms had eaten through the wood , so that a crop of livid fungi was running on the inside of it </s>
********
<s> Presently he emerged , looking even more flurried than before </s>
	=> <s> Presently he emerged , looking even more numerous than before </s>
********
<s> I stared at it horror-stricken , not knowing what was about to issue from it </s>
	=> <s> I stared at it afterwards , not knowing what was about to issue from it </s>
********
<s> The furniture was scattered about in every direction , with dismantled shelves and open drawers , as if the lady had hurriedly ransacked them before her flight </s>
	=> <s> The furniture was scattered about in every direction , with dismantled shelves and open drawers , as if the lady had hurriedly taught them before her flight </s>
********
<s> Round one of his hands he had a handkerchief wrapped , which was mottled all over with bloodstains </s>
	=> <s> Round one of his hands he had a gun wrapped , which was mottled all over with bloodstains </s>
********
<s> During two years I have had three consultations and one small job , and that is absolutely all that my profession has brought me </s>
	=> <s> During two years I have had three fishes and one small job , and that is absolutely all that my profession has brought me </s>
********
<s> His characteristic talk , with its keen observance of detail and subtle power of inference held me amused and enthralled </s>
	=> <s> His characteristic talk , with its keen instincts of detail and subtle power of inference held me amused and enthralled </s>
********
<s> Ferguson remained outside , and the colonel ushered me in </s>
	=> <s> Ferguson remained outside , and the emperor ushered me in </s>
********
<s> He turned the two best rooms of the first floor into a sitting-room and bedroom for himself </s>
	=> <s> He turned the two best feelings of the first floor into a sitting-room and bedroom for himself </s>
********
<s> After throwing down your paper , which was the action which drew my attention to you , you sat for half a minute with a vacant expression </s>
	=> <s> After throwing down your paper , which was the sword which drew my attention to you , you sat for half a minute with a vacant expression </s>
********
<s> These good people were absolutely ignorant that their land contained that which was quite as valuable as a gold-mine </s>
	=> <s> These good people were absolutely ignorant that their land contained that which was quite as delightful as a gold-mine </s>
********
<s> There were several people on the pavement at the time , but the greeting appeared to come from a slim youth in an ulster who had hurried by </s>
	=> <s> There were several people on the sofa at the time , but the greeting appeared to come from a slim youth in an ulster who had hurried by </s>
********
<s> When his body had been carried from the cellar we found ourselves still confronted with a problem which was almost as formidable as that with which we had started </s>
	=> <s> When his body had been carried from the cellar we found ourselves still confronted with a problem which was almost as quick as that with which we had started </s>
********
<s> There was something that touched me as I read this letter , something pitiable in the reiterated appeals to bring Holmes </s>
	=> <s> There was something that touched me as I read this letter , something mysterious in the reiterated appeals to bring Holmes </s>
********
<s> I rose and examined carefully the different billets of wood which were scattered round the floor </s>
	=> <s> I rose and examined carefully the different stages of wood which were scattered round the floor </s>
********
<s> It may be that the solution of the one may prove to be the solution of the other </s>
	=> <s> It may be that the solution of the one may choose to be the solution of the other </s>
********
<s> I stooped under the rude lintel , and there he sat upon a stone outside , his gray eyes dancing with amusement as they fell upon my astonished features </s>
	=> <s> I stooped under the rude lintel , and there he sat upon a nail outside , his gray eyes dancing with amusement as they fell upon my astonished features </s>
********
<s> I was tortured and tried to get away , and was captured and tortured again </s>
	=> <s> I was tortured and tried to get away , and was nurtured and tortured again </s>
********
<s> He carries some creature about with him in that box ; about which the landlady seemed to be in considerable trepidation , for she had never seen an animal like it </s>
	=> <s> He carries some information about with him in that box ; about which the landlady seemed to be in considerable trepidation , for she had never seen an animal like it </s>
********
<s> With a stout bearing , therefore , though her manner had shaken me more than I cared to confess , I still shook my head and declared my intention of remaining where I was </s>
	=> <s> With a stout stick , therefore , though her manner had shaken me more than I cared to confess , I still shook my head and declared my intention of remaining where I was </s>
********
<s> I act entirely from a sense of public duty </s>
	=> <s> I act differently from a sense of public duty </s>
********
<s> You have all the cleverness which makes a successful man </s>
	=> <s> You have all the cleverness which makes a tired man </s>
********
<s> When I saw him that afternoon so enwrapped in the music at St. James's Hall I felt that an evil time might be coming upon those whom he had set himself to hunt down </s>
	=> <s> When I saw him that afternoon so enwrapped in the doorway at St. James's Hall I felt that an evil time might be coming upon those whom he had set himself to hunt down </s>
********
<s> The cries , which had sunk down into a hoarse , inarticulate shouting , came from the room which we had first visited </s>
	=> <s> The cries , which had rolled down into a hoarse , inarticulate shouting , came from the room which we had first visited </s>
********
<s> It's about five in the morning , you know , that suicides are most common </s>
	=> <s> It's about five in the morning , you know , that libraries are most common </s>
********
<s> Shortly after our return to England my mother died she was killed eight years ago in a railway accident near Crewe </s>
	=> <s> Shortly after our return to England my mother died she was born eight years ago in a railway accident near Crewe </s>
********
<s> It could only be a small one , or it would have been remarked upon at the coroner's inquiry </s>
	=> <s> It could only be a small one , or it would have been dashed upon at the coroner's inquiry </s>
********
<s> It was a delicate point , and it widened the field of my inquiry </s>
	=> <s> It was a delicate point , and it fetched the field of my inquiry </s>
********
<s> The stage lost a fine actor , even as science lost an acute reasoner , when he became a specialist in crime </s>
	=> <s> The stage lost a fine estate , even as science lost an acute reasoner , when he became a specialist in crime </s>
********
<s> For answer Holmes pushed back the frill of black lace which fringed the hand that lay upon our visitor's knee </s>
	=> <s> For answer Holmes sank back the frill of black lace which fringed the hand that lay upon our visitor's knee </s>
********
<s> As I descended , my old ally , the guard , came out of the room and closed the door tightly behind him </s>
	=> <s> As I descended , my old ally , the moon , came out of the room and closed the door tightly behind him </s>
********
<s> The inspector had lit his lantern , and by its light we could see the two doors , the curtain , the lamp , and the suit of Japanese mail as he had described them </s>
	=> <s> The inspector had bent his lantern , and by its light we could see the two doors , the curtain , the lamp , and the suit of Japanese mail as he had described them </s>
********
<s> I sprang from my bed , wrapped a shawl round me , and rushed into the corridor </s>
	=> <s> I sprang from my bed , using a shawl round me , and rushed into the corridor </s>
********
<s> I did not know about a projected divorce between herself and her husband </s>
	=> <s> I did not know about a projected marriage between herself and her husband </s>
********
<s> I confess that they quite surpass my expectations , and that I am utterly unable to account for your result </s>
	=> <s> I confess that they quite enjoyed my expectations , and that I am utterly unable to account for your result </s>
********
<s> Why should I slink away without having carried out my commission , and without the payment which was my due </s>
	=> <s> Why should I slink away without having carried out my commission , and without the countenance which was my due </s>
********
<s> She could trust her own guardianship , but she could not tell what indirect or political influence might be brought to bear upon a business man </s>
	=> <s> She could trust her own guardianship , but she could not tell what handsome or political influence might be brought to bear upon a business man </s>
********
<s> He said a few words to each candidate as he came up , and then he always managed to find some fault in them which would disqualify them </s>
	=> <s> He said a few words to each candidate as he came up , and then he always managed to find some fault in them which would teach them </s>
********
<s> And into her sitting-room , which was the very room which I suspected </s>
	=> <s> And into her pocket , which was the very room which I suspected </s>
********
<s> To rake this up couldn't help our poor master , and it's well to go carefully when there's a lady in the case </s>
	=> <s> To rake this up couldn't help our poor master , and it's well to go downstairs when there's a lady in the case </s>
********
<s> That cold , incisive , ironical voice could belong to but one man in all the world </s>
	=> <s> That cold , hungry , ironical voice could belong to but one man in all the world </s>
********
<s> As he dangled from the hook it was exaggerated and intensified until he was scarce human in his appearance </s>
	=> <s> As he emerged from the hook it was exaggerated and intensified until he was scarce human in his appearance </s>
********
<s> It is probable that he will be away all day , and that there would be nothing to disturb you </s>
	=> <s> It is probable that he will be away all day , and that there would be nothing to offer you </s>
********
<s> I interpret all languages or nearly all but as I am a Greek by birth and with a Grecian name , it is with that particular tongue that I am principally associated </s>
	=> <s> I interpret all languages or nearly all but as I am a Greek by birth and with a Grecian name , it is with that particular dream that I am principally associated </s>
********
<s> A few good cases and the reputation which I had won in the hospital brought me rapidly to the front , and during the last few years I have made him a rich man </s>
	=> <s> A few good knives and the reputation which I had won in the hospital brought me rapidly to the front , and during the last few years I have made him a rich man </s>
********
<s> At the time that I wrote this letter to Sir Charles I had learned that there was a prospect of my regaining my freedom if certain expenses could be met </s>
	=> <s> At the time that I wrote this letter to Sir Charles I had learned that there was a source of my regaining my freedom if certain expenses could be met </s>
********
<s> This girl had been devoted to him </s>
	=> <s> This girl had been addressed to him </s>
********
<s> Having found nothing they tried to divert suspicion by making it appear to be an ordinary burglary , to which end they carried off whatever they could lay their hands upon </s>
	=> <s> Having found nothing they tried to divert suspicion by making it appear to be an ordinary closet , to which end they carried off whatever they could lay their hands upon </s>
********
<s> I have it from the same source that you are both an orphan and a bachelor and are residing alone in London </s>
	=> <s> I have it from the same source that you are both an orphan and a bachelor and are walking alone in London </s>
********
<s> Finally , with a shamefaced apology for his weakness , he rose once more </s>
	=> <s> Finally , with a shamefaced apology for his kindness , he rose once more </s>
********
<s> His slippers , too , were gone , but his boots were left behind </s>
	=> <s> His slippers , too , were gone , but his feelings were left behind </s>
********
<s> The freckles started out on the lady's face </s>
	=> <s> The freckles started out on the Federal face </s>
********
<s> When I went upstairs with him he pointed to several footprints upon the light carpet </s>
	=> <s> When I went upstairs with him he pointed to several accidents upon the light carpet </s>
********
<s> It was the most preposterous position in which I ever found myself in my life , and it was the thought of it that started me laughing just now </s>
	=> <s> It was the most important position in which I ever found myself in my life , and it was the thought of it that started me laughing just now </s>
********
<s> It gave even my hardened nerves a shudder to look at it </s>
	=> <s> It gave even my familiar nerves a shudder to look at it </s>
********
<s> So much is fairly clear </s>
	=> <s> So much is falling clear </s>
********
<s> I took off the kettle and blew out the lamp , for the water was spurting over the floor </s>
	=> <s> I took off the roof and blew out the lamp , for the water was spurting over the floor </s>
********
<s> Nor was the fact of the wound being on the back of his head a fatal objection to this , as he might have turned to avoid the blow </s>
	=> <s> Nor was the fact of the box being on the back of his head a fatal objection to this , as he might have turned to avoid the blow </s>
********
<s> We even traced them as far as Reading , but could get no farther , for they had covered their traces in a way that showed that they were very old hands </s>
	=> <s> We even judged them as far as Reading , but could get no farther , for they had covered their traces in a way that showed that they were very old hands </s>
********
<s> For half an hour I sat with straining ears </s>
	=> <s> For half an hour I sat with closed ears </s>
********
<s> I thought of the convict out upon the bleak , cold , shelterless moor </s>
	=> <s> I thought of the convict out upon the bleak , cold , dazzling moor </s>
********
<s> No doubt his blackmailing case is absorbing all his faculties </s>
	=> <s> No doubt his blackmailing case is inside all his faculties </s>
********
<s> It's not been fed for two days </s>
	=> <s> It's not been built for two days </s>
********
<s> It brought me to the very threshold of the old door </s>
	=> <s> It brought me to the very verge of the old door </s>
********
<s> Holmes was for the moment as startled as I. His hand closed like a vice upon my wrist in his agitation </s>
	=> <s> Holmes was for the moment as thin as I. His hand closed like a vice upon my wrist in his agitation </s>
********
<s> So interested was he that I had to repeat some of it twice before he was satisfied </s>
	=> <s> So interested was he that I had to buy some of it twice before he was satisfied </s>
********
<s> The wind was howling outside , and the rain was beating and splashing against the windows </s>
	=> <s> The wind was howling outside , and the rain was beating and staggering against the windows </s>
********
<s> On the contrary , for a small street in a quiet neighbourhood , it was remarkably animated </s>
	=> <s> On the contrary , for a small street in a quiet mood , it was remarkably animated </s>
********
<s> It was locked , but the key had been left on the outside </s>
	=> <s> It was locked , but the dream had been left on the outside </s>
********
<s> All was exactly as I left it , save only that the papers which had been committed to my care had been taken from the desk on which they lay </s>
	=> <s> All was exactly as I left it , save only that the feelings which had been committed to my care had been taken from the desk on which they lay </s>
********
<s> At one side of this was a squat , brass-bound wooden box , the lid of which was hinged upwards , with this curious old-fashioned key projecting from the lock </s>
	=> <s> At one side of this was a squat , brass-bound wooden box , the existence of which was hinged upwards , with this curious old-fashioned key projecting from the lock </s>
********
<s> For myself , my term of service in India had trained me to stand heat better than cold , and a thermometer of 90 was no hardship </s>
	=> <s> For myself , my term of service in India had invited me to stand heat better than cold , and a thermometer of 90 was no hardship </s>
********
<s> Joseph Harrison is my name , and as Percy is to marry my sister Annie I shall at least be a relation by marriage </s>
	=> <s> Joseph Harrison is my name , and as Percy is to marry my sister Annie I shall at least be a queen by marriage </s>
********
<s> I clambered out upon the sill , but I hesitated to jump until I should have heard what passed between my saviour and the ruffian who pursued me </s>
	=> <s> I clambered out upon the sill , but I hesitated to jump until I should have heard what passed between my saviour and the ruffian who allowed me </s>
********
<s> In my haste I thrust the key into my pocket , and dropped my stick while I was chasing Teddy , who had run up the curtain </s>
	=> <s> In my haste I thrust the key into my pocket , and repeated my stick while I was chasing Teddy , who had run up the curtain </s>
********
<s> I did not gain very much , however , by my inspection </s>
	=> <s> I did not remain very much , however , by my inspection </s>
********
<s> His grandfather was a royal duke , and he himself has been to Eton and Oxford </s>
	=> <s> His grandfather was a royal palace , and he himself has been to Eton and Oxford </s>
********
<s> He will not even go out of his way to verify his own solutions , and would rather be considered wrong than take the trouble to prove himself right </s>
	=> <s> He will not even go out of his way to preserve his own solutions , and would rather be considered wrong than take the trouble to prove himself right </s>
********
<s> I've never breathed a word about it yet to mortal man </s>
	=> <s> I've never missed a word about it yet to mortal man </s>
********
<s> And when he speaks of Irene Adler , or when he refers to her photograph , it is always under the honourable title of the woman </s>
	=> <s> And when he hears of Irene Adler , or when he refers to her photograph , it is always under the honourable title of the woman </s>
********
<s> It was the clank of the levers and the swish of the leaking cylinder </s>
	=> <s> It was the clank of the levers and the swish of the meek cylinder </s>
********
<s> It was indeed a gigantic one , and capable of exercising enormous pressure </s>
	=> <s> It was indeed a gigantic one , and capable of exercising actual pressure </s>
********
<s> You may then walk to the end of the street , and I will rejoin you in ten minutes </s>
	=> <s> You may then walk to the end of the street , and I will kill you in ten minutes </s>
********
<s> Yet this emaciation seemed to be his natural habit , and due to no disease , for his eye was bright , his step brisk , and his bearing assured </s>
	=> <s> Yet this emaciation seemed to be his natural feelings , and due to no disease , for his eye was bright , his step brisk , and his bearing assured </s>
********
<s> I gave a trifle myself </s>
	=> <s> I gave a rock myself </s>
********
<s> The shape of some monstrous villainy , half seen , half guessed , loomed through the darkness which had girt me so long </s>
	=> <s> The shape of some monstrous villainy , half seen , half falling , loomed through the darkness which had girt me so long </s>
********
<s> Within was a small , square room , in which the three of us could hardly get at one time </s>
	=> <s> Within was a small , noble room , in which the three of us could hardly get at one time </s>
********
<s> Half way down this staircase is a small landing , with another passage running into it at right angles </s>
	=> <s> Half way down this island is a small landing , with another passage running into it at right angles </s>
********
<s> It was only after a painful and prolonged scene that she was ejected by the butler and the footman </s>
	=> <s> It was only after a painful and prolonged scene that she was startled by the butler and the footman </s>
********
<s> It is inconceivable that this fellow could have made two such vindictive enemies as these appear to be without knowing of it </s>
	=> <s> It is likely that this fellow could have made two such vindictive enemies as these appear to be without knowing of it </s>
********
<s> He is a man of no physical courage , as they are well aware from their experience the other night </s>
	=> <s> He is a man of no physical courage , as they are well aware from their infancy the other night </s>
********
<s> Sherlock Holmes was not very communicative during the long drive and lay back in the cab humming the tunes which he had heard in the afternoon </s>
	=> <s> Sherlock Holmes was not very communicative during the long nights and lay back in the cab humming the tunes which he had heard in the afternoon </s>
********
<s> There was no furniture save a little pallet bed , a small table , and a basketful of linen </s>
	=> <s> There was no escape save a little pallet bed , a small table , and a basketful of linen </s>
********
<s> It may prove the simplest matter in the world , but all the same at first glance this is just a little curious , is it not </s>
	=> <s> It may prove the simplest matter in the world , but all the same at first glance this is just a little pale , is it not </s>
********
<s> They undoubtedly showed that the affair was much deeper than was at first conjectured </s>
	=> <s> They undoubtedly showed that the journey was much deeper than was at first conjectured </s>
********
<s> I beg you to remember that no one knows where you are , and that , whether you are in this carriage or in my house , you are equally in my power </s>
	=> <s> I beg you to remember that no one knows where you are , and that , whether you are in this carriage or in my house , you are interested in my power </s>
********
<s> His dress was quiet and sombre a black frock-coat , dark trousers , and a touch of color about his necktie </s>
	=> <s> His dress was quiet and sombre a black frock-coat , dark trousers , and a touch of sadness about his necktie </s>
********
<s> These were all factors which had to be taken into consideration , and yet none of them got quite to the heart of the matter </s>
	=> <s> These were all creatures which had to be taken into consideration , and yet none of them got quite to the heart of the matter </s>
********
<s> Holmes pulled a large sheet of tissue-paper out of his pocket and carefully unfolded it upon his knee </s>
	=> <s> Holmes pulled a large sheet of carpet out of his pocket and carefully unfolded it upon his knee </s>
********
<s> As it was , he suffered a long term of imprisonment and afterwards returned to England a morose and disappointed man </s>
	=> <s> As it was , he suffered a long term of imprisonment and afterwards returned to England a brave and disappointed man </s>
********
<s> Your interview with the lady has cleared the situation very much </s>
	=> <s> Your interview with the lady has cleared the food very much </s>
********
<s> The country roads seem to be not very good in that part of the world , for we lurched and jolted terribly </s>
	=> <s> The country roads seem to be not very good in that part of the world , for we ate and jolted terribly </s>
********
<s> It's not a very large affair , and of late years it has not done more than just give me a living </s>
	=> <s> It's not a very large picture , and of late years it has not done more than just give me a living </s>
********
<s> He was a man of singular habits , shunning company and very seldom going out </s>
	=> <s> He was a man of singular habits , keeping company and very seldom going out </s>
********
<s> It was almost dark before we found ourselves in Pall Mall , at the rooms of Mr. Melas </s>
	=> <s> It was almost dark before we found ourselves in Pall Mall , at the bottom of Mr. Melas </s>
********
<s> The brother scribbled a note upon a leaf of his pocket-book , and , ringing the bell , he handed it to the waiter </s>
	=> <s> The brother scribbled a note upon a leaf of his wine , and , ringing the bell , he handed it to the waiter </s>
********
<s> Of course he must recall the snake before the morning light revealed it to the victim </s>
	=> <s> Of course he must cross the snake before the morning light revealed it to the victim </s>
********
<s> He had trained it , probably by the use of the milk which we saw , to return to him when summoned </s>
	=> <s> He had trained it , probably by the use of the emotions which we saw , to return to him when summoned </s>
********
<s> I sat down upon a keg in the corner and thought the whole matter carefully over </s>
	=> <s> I sat down upon a sword in the corner and thought the whole matter carefully over </s>
********
<s> Don't you see that the converse is equally valid </s>
	=> <s> Don't you see that the plate is equally valid </s>
********
<s> If the former , she had probably transferred the photograph to his keeping </s>
	=> <s> If the former , she had probably assumed the photograph to his keeping </s>
********
<s> it's a wicked world , and when a clever man turns his brains to crime it is the worst of all </s>
	=> <s> it's a wonderful world , and when a clever man turns his brains to crime it is the worst of all </s>
********
<s> The thieves ransacked the library and got very little for their pains </s>
	=> <s> The thieves enjoyed the library and got very little for their pains </s>
********
<s> He was a solicitor and was using my room as a temporary convenience until his new premises were ready </s>
	=> <s> He was a solicitor and was composing my room as a temporary convenience until his new premises were ready </s>
********
<s> The wound upon the dead man was , as I was able to determine with absolute confidence , fired from a revolver at the distance of something over four yards </s>
	=> <s> The wound upon the dead man was , as I was able to determine with absolute confidence , fired from a trial at the distance of something over four yards </s>
********
<s> I could tell from his expression that he was on a hot scent , and yet I could not in the least imagine in what direction his inferences were leading him </s>
	=> <s> I could tell from his expression that he was on a hot bath , and yet I could not in the least imagine in what direction his inferences were leading him </s>
********
<s> The walls were of wood , but the floor consisted of a large iron trough , and when I came to examine it I could see a crust of metallic deposit all over it </s>
	=> <s> The walls were of wood , but the floor consisted of a large iron trough , and when I came to examine it I could see a couple of metallic deposit all over it </s>
********
<s> The last red streaks had faded away in the west and night had settled upon the moor </s>
	=> <s> The last red grass had faded away in the west and night had settled upon the moor </s>
********
<s> Two hours passed slowly away , and then , suddenly , just at the stroke of eleven , a single bright light shone out right in front of us </s>
	=> <s> Two hours passed slowly away , and then , suddenly , just at the extremity of eleven , a single bright light shone out right in front of us </s>
********
<s> You remember the small affair of Uriah and Bathsheba </s>
	=> <s> You remember the small piece of Uriah and Bathsheba </s>
********
<s> I endeavoured to tie my handkerchief round it , but there came a sudden buzzing in my ears , and next moment I fell in a dead faint among the rose-bushes </s>
	=> <s> I endeavoured to tie my handkerchief round it , but there came a sudden flash in my ears , and next moment I fell in a dead faint among the rose-bushes </s>
********
<s> His whole face sharpened away into nose and chin , and the skin of his cheeks was drawn quite tense over his outstanding bones </s>
	=> <s> His whole face sharpened away into nose and chin , and the skin of his cheeks was lying quite tense over his outstanding bones </s>
********
<s> He was off in one of those hysterical outbursts which come upon a strong nature when some great crisis is over and gone </s>
	=> <s> He was off in one of those useful outbursts which come upon a strong nature when some great crisis is over and gone </s>
********
<s> Once or twice we drifted into talk , and I can remember that more than once he expressed a keen interest in my methods of observation and inference </s>
	=> <s> Once or twice we drifted into talk , and I can remember that more than once he noticed a keen interest in my methods of observation and inference </s>
********
<s> We had come out upon Oxford Street and I had ventured some remark as to this being a roundabout way to Kensington , when my words were arrested by the extraordinary conduct of my companion </s>
	=> <s> We had come out upon Oxford Street and I had ventured some remark as to this being a roundabout way to Kensington , when my words were startled by the extraordinary conduct of my companion </s>
********
<s> Your task is confined to that </s>
	=> <s> Your task is welcome to that </s>
********
<s> The sight of the safe , the saucer of milk , and the loop of whipcord were enough to finally dispel any doubts which may have remained </s>
	=> <s> The sight of the safe , the saucer of milk , and the rights of whipcord were enough to finally dispel any doubts which may have remained </s>
********
<s> I was a happy and successful man , Mr. Holmes , and on the eve of being married , when a sudden and dreadful misfortune wrecked all my prospects in life </s>
	=> <s> I was a happy and successful man , Mr. Holmes , and on the eve of being married , when a sudden and dreadful misfortune caused all my prospects in life </s>
********
<s> The garden and the stables of course have a separate staff </s>
	=> <s> The garden and the stables of course have a steel staff </s>
********
<s> The skylight above was open , and the prisoner gone </s>
	=> <s> The skylight above was open , and the laws gone </s>
********
<s> He insisted upon my climbing into his dog-cart , and he gave me a lift homeward </s>
	=> <s> He insisted upon my climbing into his dog-cart , and he gave me a visit homeward </s>
********
<s> But I have heard , Mr. Holmes , that you can see deeply into the manifold wickedness of the human heart </s>
	=> <s> But I have heard , Mr. Holmes , that you can see deeply into the firm wickedness of the human heart </s>
********
<s> This must be the burrow where the stranger lurked </s>
	=> <s> This must be the difference where the stranger lurked </s>
********
<s> More than one person fainted at the mere sight of him , so terrible was the effect </s>
	=> <s> More than one person knocked at the mere sight of him , so terrible was the effect </s>
********
<s> Was she his client , his friend , or his mistress </s>
	=> <s> Was she his opportunity , his friend , or his mistress </s>
********
<s> I trust that I am not more dense than my neighbours , but I was always oppressed with a sense of my own stupidity in my dealings with Sherlock Holmes </s>
	=> <s> I trust that I am not more powerful than my neighbours , but I was always oppressed with a sense of my own stupidity in my dealings with Sherlock Holmes </s>
********
<s> The same porter was on duty , I found , as had been there when I arrived </s>
	=> <s> The same cloud was on duty , I found , as had been there when I arrived </s>
********
<s> It cost me something in foolscap , and I had pretty nearly filled a shelf with my writings </s>
	=> <s> It cost me something in foolscap , and I had pretty nearly filled a tumbler with my writings </s>
********
<s> A splendid park with fine old timber surrounds the house , and the lake , to which my client had referred , lay close to the avenue , about two hundred yards from the building </s>
	=> <s> A splendid devil with fine old timber surrounds the house , and the lake , to which my client had referred , lay close to the avenue , about two hundred yards from the building </s>
********
<s> It had wandered on to the moor and had never come back </s>
	=> <s> It had wandered on to the hotel and had never come back </s>
********
<s> The maid had loved the butler , but had afterwards had cause to hate him </s>
	=> <s> The maid had loved the porch , but had afterwards had cause to hate him </s>
********
<s> You still smoke the Arcadia mixture of your bachelor days then </s>
	=> <s> You still smoke the Arcadia mixture of your wretched days then </s>
********
<s> A depleted bank account had caused me to postpone my holiday , and as to my companion , neither the country nor the sea presented the slightest attraction to him </s>
	=> <s> A depleted bank account had caused me to pursue my holiday , and as to my companion , neither the country nor the sea presented the slightest attraction to him </s>
********
<s> Then suddenly he plunged forward , wrung my hand , and congratulated me warmly on my success </s>
	=> <s> Then suddenly he plunged forward , ate my hand , and congratulated me warmly on my success </s>
********
<s> Luck had been against us again and again in this inquiry , but now at last it came to my aid </s>
	=> <s> Luck had been against us again and again in this mood , but now at last it came to my aid </s>
********
<s> It is your commonplace , featureless crimes which are really puzzling , just as a commonplace face is the most difficult to identify </s>
	=> <s> It is your commonplace , inevitable crimes which are really puzzling , just as a commonplace face is the most difficult to identify </s>
********
<s> Between your brandy and your bandage , I feel a new man </s>
	=> <s> Between your brandy and your permission , I feel a new man </s>
********
<s> It would be a sharp-eyed coroner , indeed , who could distinguish the two little dark punctures which would show where the poison fangs had done their work </s>
	=> <s> It would be a mysterious coroner , indeed , who could distinguish the two little dark punctures which would show where the poison fangs had done their work </s>
********
<s> Everything was working in my favour , and I swore that it should not be through lack of energy or perseverance that I should miss the chance which fortune had thrown in my way </s>
	=> <s> Everything was born in my favour , and I swore that it should not be through lack of energy or perseverance that I should miss the chance which fortune had thrown in my way </s>
********
<s> Mr. Jabez Wilson started up in his chair , with his forefinger upon the paper , but his eyes upon my companion </s>
	=> <s> Mr. Jabez Wilson started up in his chair , with his dogs upon the paper , but his eyes upon my companion </s>
********
<s> You say yourself that the horse was fresh and glossy when you got in </s>
	=> <s> You say yourself that the horse was fresh and beaten when you got in </s>
********
<s> With tingling nerves but a fixed purpose , I sat in the dark recess of the hut and waited with sombre patience for the coming of its tenant </s>
	=> <s> With tingling nerves but a fixed purpose , I sat in the dark recess of the hut and fought with sombre patience for the coming of its tenant </s>
********
<s> We compress the earth into bricks , so as to remove them without revealing what they are </s>
	=> <s> We compress the earth into bricks , so as to remove them without hearing what they are </s>
********
<s> Peering in , we could see that the only light in the room came from a dull blue flame which flickered from a small brass tripod in the centre </s>
	=> <s> Peering in , we could see that the only light in the room came from a dull blue flame which descended from a small brass tripod in the centre </s>
********
<s> The younger had left us , but he suddenly returned through another door , leading with him a gentleman clad in some sort of loose dressing-gown who moved slowly towards us </s>
	=> <s> The younger had left us , but he suddenly returned through another door , leading with him a gentleman seated in some sort of loose dressing-gown who moved slowly towards us </s>
********
<s> Her rich tints made the white face of her companion the more worn and haggard by the contrast </s>
	=> <s> Her rich leaves made the white face of her companion the more worn and haggard by the contrast </s>
********
<s> We are at present , Doctor as no doubt you have divined in the cellar of the City branch of one of the principal London banks </s>
	=> <s> We are at present , Doctor as no doubt you have divined in the cellar of the City branch of one of the Athenian London banks </s>
********
<s> Each daughter can claim an income of 250 pounds , in case of marriage </s>
	=> <s> Each daughter can claim an opinion of 250 pounds , in case of marriage </s>
********
<s> Over the wide expanse there was no sound and no movement </s>
	=> <s> Over the wide Pacific there was no sound and no movement </s>
********
<s> More than one person fainted at the mere sight of him , so terrible was the effect </s>
	=> <s> More than one person fainted at the mere sight of him , so eager was the effect </s>
********
<s> Holmes had sat up upon the couch , and I saw him motion like a man who is in need of air </s>
	=> <s> Holmes had sat up upon the couch , and I saw him lie like a man who is in need of air </s>
********
<s> From north , south , east , and west every man who had a shade of red in his hair had tramped into the city to answer the advertisement </s>
	=> <s> From north , south , east , and west every man who had a shade of red in his hair had crept into the city to answer the advertisement </s>
********
<s> He went out again , therefore , through the window , and having obtained the help of a policeman and of a medical man , he returned </s>
	=> <s> He went out again , therefore , through the window , and having spent the help of a policeman and of a medical man , he returned </s>
********
<s> All my medical instincts rose up against that laugh </s>
	=> <s> All my future instincts rose up against that laugh </s>
********
<s> The matter was so prearranged that it is my belief that they brought with them some sort of block or pulley which might serve as a gallows </s>
	=> <s> The matter was so intense that it is my belief that they brought with them some sort of block or pulley which might serve as a gallows </s>
********
<s> She was about to renew her entreaties when a door slammed overhead , and the sound of several footsteps was heard upon the stairs </s>
	=> <s> She was about to renew her entreaties when a door slammed to-morrow , and the sound of several footsteps was heard upon the stairs </s>
********
<s> He lay back without wincing , though he bit his lip from time to time </s>
	=> <s> He lay back without pity , though he bit his lip from time to time </s>
********
<s> The barren scene , the sense of loneliness , and the mystery and urgency of my task all struck a chill into my heart </s>
	=> <s> The barren scene , the sense of loneliness , and the glory and urgency of my task all struck a chill into my heart </s>
********
<s> It was absolutely certain , therefore , in spite of her denial , that she must know something of the matter </s>
	=> <s> It was absolutely certain , therefore , in spite of her honour , that she must know something of the matter </s>
********
<s> Surely the explanation of all this could not be as innocent as she would have me believe </s>
	=> <s> Surely the explanation of all this could not be as yellow as she would have me believe </s>
********
<s> At the end were the signatures of the high dignitaries who had signed it </s>
	=> <s> At the end were the relics of the high dignitaries who had signed it </s>
********
<s> And this was the singular case of the Grecian Interpreter , the explanation of which is still involved in some mystery </s>
	=> <s> And this was the singular case of the Grecian Interpreter , the possibility of which is still involved in some mystery </s>
********
<s> From one of these I picked a battle-axe , and then , leaving my candle behind me , I crept on tiptoe down the passage and peeped in at the open door </s>
	=> <s> From one of these I picked a battle-axe , and then , leaving my wrists behind me , I crept on tiptoe down the passage and peeped in at the open door </s>
********
<s> The walls were carefully sounded , and were shown to be quite solid all round , and the flooring was also thoroughly examined , with the same result </s>
	=> <s> The walls were carefully sounded , and were shown to be quite solid all round , and the wood was also thoroughly examined , with the same result </s>
********
<s> Besides , we must be prompt , for this marriage may mean a complete change in her life and habits </s>
	=> <s> Besides , we must be wonderful , for this marriage may mean a complete change in her life and habits </s>
********
<s> I placed my revolver , cocked , upon the top of the wooden case behind which I crouched </s>
	=> <s> I placed my revolver , cocked , upon the top of the law case behind which I crouched </s>
********
<s> But we have more assured reasons than that for supposing it </s>
	=> <s> But we have more Pagan reasons than that for supposing it </s>
********
<s> If you leave , you forfeit your whole position forever </s>
	=> <s> If you leave , you murder your whole position forever </s>
********
<s> In an instant I was stunned with a blow and bound hand and foot </s>
	=> <s> In an instant I was satisfied with a blow and bound hand and foot </s>
********
<s> The rapidity with which such a poison would take effect would also , from his point of view , be an advantage </s>
	=> <s> The rapidity with which such a fool would take effect would also , from his point of view , be an advantage </s>
********
<s> But there were ample signs that I had not come upon a false scent </s>
	=> <s> But there were eighty signs that I had not come upon a false scent </s>
********
<s> I rose , and , making my excuses , escaped from the house </s>
	=> <s> I rose , and , making my society , escaped from the house </s>
********
<s> It rained hard this afternoon , as you know , and my patients were the only people who called </s>
	=> <s> It rained hard this afternoon , as you know , and my clothes were the only people who called </s>
********
<s> I was just balancing whether I should run for it , or whether I should perch behind her landau when a cab came through the street </s>
	=> <s> I was just commencing whether I should run for it , or whether I should perch behind her landau when a cab came through the street </s>
********
<s> A man always finds it hard to realize that he may have finally lost a woman's love , however badly he may have treated her </s>
	=> <s> A man always finds it hard to realize that he may have finally lost a woman's love , however badly he may have fixed her </s>
********
<s> The woman's story hung coherently together , and all my questions were unable to shake it </s>
	=> <s> The woman's story hung coherently together , and all my limbs were unable to shake it </s>
********
<s> What was this nocturnal expedition , and why should I go armed </s>
	=> <s> What was this nocturnal law , and why should I go armed </s>
********
<s> My companion let down the window , and I caught a glimpse of a low , arched doorway with a lamp burning above it </s>
	=> <s> My companion let down the window , and I caught a glimpse of a low , winding doorway with a lamp burning above it </s>
********
<s> Now and then I hazarded some remark to break the monotony of the journey , but the colonel answered only in monosyllables , and the conversation soon flagged </s>
	=> <s> Now and then I allowed some remark to break the monotony of the journey , but the colonel answered only in monosyllables , and the conversation soon flagged </s>
********
<s> We know that there is someone who has the facts if we can only find her </s>
	=> <s> We know that there is nobody who has the facts if we can only find her </s>
********
<s> He had his hand under the other's arm as they entered , and helped him to a chair with a tenderness which one would hardly have expected from his appearance </s>
	=> <s> He had his hand under the other's arm as they entered , and helped him to a chair with a sensation which one would hardly have expected from his appearance </s>
********
<s> I suppose there would be no chance of a train back </s>
	=> <s> I suppose there would be no chance of a horse's back </s>
********
<s> As I gave a last hurried glance around , I saw a thin line of yellow light between two of the boards , which broadened and broadened as a small panel was pushed backward </s>
	=> <s> As I gave a last adoring glance around , I saw a thin line of yellow light between two of the boards , which broadened and broadened as a small panel was pushed backward </s>
********
<s> The telescope , a formidable instrument mounted upon a tripod , stood upon the flat leads of the house </s>
	=> <s> The telescope , a dangerous instrument mounted upon a tripod , stood upon the flat leads of the house </s>
********
<s> Perhaps , Mr. Wilson , you would have the great kindness to recommence your narrative </s>
	=> <s> Perhaps , Mr. Wilson , you would have the great kindness to reward your narrative </s>
********
<s> Why should she fight against every admission until it was forced from her </s>
	=> <s> Why should she fight against every taste until it was forced from her </s>
********
<s> The shock has made her half-witted , but I understand that she was never very bright </s>
	=> <s> The shock has made her uncomfortable , but I understand that she was never very bright </s>
********
<s> The servants deny having seen it before , but among the numerous curiosities in the house it is possible that it may have been overlooked </s>
	=> <s> The servants remembered having seen it before , but among the numerous curiosities in the house it is possible that it may have been overlooked </s>
********
<s> The air had turned chill and we withdrew into the hut for warmth </s>
	=> <s> The air had turned pale and we withdrew into the hut for warmth </s>
********
<s> You can understand that , living the life which I have described , we were little likely to see anyone of our own age and position </s>
	=> <s> You can understand that , living the life which I have arrived , we were little likely to see anyone of our own age and position </s>
********
<s> A small taper on the edge of the table shed a feeble light which sufficed to show me that he was fully dressed </s>
	=> <s> A small taper on the edge of the table shed a feeble light which goes to show me that he was fully dressed </s>
********
<s> You may not be aware that the deduction of a man's age from his writing is one which has brought to considerable accuracy by experts </s>
	=> <s> You may not be aware that the absence of a man's age from his writing is one which has brought to considerable accuracy by experts </s>
********
<s> Hayter was a fine old soldier who had seen much of the world , and he soon found , as I had expected , that Holmes and he had much in common </s>
	=> <s> Hayter was a fine old dog who had seen much of the world , and he soon found , as I had expected , that Holmes and he had much in common </s>
********
<s> What passion of hatred can it be which leads a man to lurk in such a place at such a time </s>
	=> <s> What passion of hatred can it be which leads a man to grow in such a place at such a time </s>
********
<s> The man is by trade a conjurer and performer , going round the canteens after nightfall , and giving a little entertainment at each </s>
	=> <s> The man is by trade a conjurer and performer , going round the canteens after nightfall , and giving a little basket at each </s>
********
<s> We were in time to overtake the major before he reached the corner </s>
	=> <s> We were in time to cultivate the major before he reached the corner </s>
********
<s> I ran to her and threw my arms round her , but at that moment her knees seemed to give way and she fell to the ground </s>
	=> <s> I ran to her and threw my arms round her , but at that moment her health seemed to give way and she fell to the ground </s>
********
<s> These are daring men , and though we shall take them at a disadvantage , they may do us some harm unless we are careful </s>
	=> <s> These are simply men , and though we shall take them at a disadvantage , they may do us some harm unless we are careful </s>
********
<s> Far away came the sharp clink of a boot striking upon a stone </s>
	=> <s> Far away came the sharp edge of a boot striking upon a stone </s>
********
<s> The lake there is eight feet deep , and you can imagine our feelings when we saw that the trail of the poor demented girl came to an end at the edge of it </s>
	=> <s> The lake there is eight feet deep , and you can imagine our feelings when we saw that the descendants of the poor demented girl came to an end at the edge of it </s>
********
<s> She was never , as I think I have said , ostentatiously affectionate , but she was heard by the coachman chatting with the Colonel in a friendly fashion </s>
	=> <s> She was never , as I think I have said , ostentatiously handsome , but she was heard by the coachman chatting with the Colonel in a friendly fashion </s>
********
<s> You see , at the commencement of an investigation it is something to know that your client is in close contact with some one who , for good or evil , has an exceptional nature </s>
	=> <s> You see , at the commencement of an investigation it is something to know that your uncle is in close contact with some one who , for good or evil , has an exceptional nature </s>
********
<s> I began to understand what my friend meant when he said that his brother possessed even keener faculties that he did himself </s>
	=> <s> I began to understand what my friend meant when he said that his brother possessed even keener impudence that he did himself </s>
********
<s> We stepped , as it were , right out of the carriage and into the hall , so that I failed to catch the most fleeting glance of the front of the house </s>
	=> <s> We stepped , as it were , right out of the carriage and into the hall , so that I failed to catch the most lively glance of the front of the house </s>
********
<s> The terror of his face lay in his eyes , however , steel gray , and glistening coldly with a malignant , inexorable cruelty in their depths </s>
	=> <s> The terror of his face lay in his eyes , however , steel gray , and glistening coldly with a malignant , inexorable justice in their depths </s>
********
<s> She had flung into the lake a bag containing some curious contents </s>
	=> <s> She had fallen into the lake a bag containing some curious contents </s>
********
<s> A vague pathway among the boulders led to the dilapidated opening which served as a door </s>
	=> <s> A vague pathway among the boulders led to the dilapidated pouch which served as a door </s>
********
<s> For many years I have been the chief Greek interpreter in London , and my name is very well known in the hotels </s>
	=> <s> For many years I have been the chief Greek counter in London , and my name is very well known in the hotels </s>
********
<s> She stared at us with defiant eyes , and then , suddenly recognizing me , an expression of absolute astonishment came over her face </s>
	=> <s> She stared at us with defiant eyes , and then , suddenly watching me , an expression of absolute astonishment came over her face </s>
********
<s> He laughed very heartily , with a high , ringing note , leaning back in his chair and shaking his sides </s>
	=> <s> He laughed very heartily , with a high , faint note , leaning back in his chair and shaking his sides </s>
********
<s> The smarting of it recalled in an instant all the particulars of my night's adventure , and I sprang to my feet with the feeling that I might hardly yet be safe from my pursuers </s>
	=> <s> The smarting of it arrived in an instant all the particulars of my night's adventure , and I sprang to my feet with the feeling that I might hardly yet be safe from my pursuers </s>
********
<s> She had been terribly excited immediately after his disappearance </s>
	=> <s> She had been terribly arrested immediately after his disappearance </s>
********
<s> Then I , rather imprudently , wished you good-night , and started for the Temple to see my husband </s>
	=> <s> Then I , rather imprudently , wished you arrived , and started for the Temple to see my husband </s>
********
<s> It is very natural that the pledge of secrecy which we have exacted from you should have aroused your curiosity </s>
	=> <s> It is very natural that the pledge of secrecy which we have exacted from you should have killed your curiosity </s>
********
<s> I was pained at the mistake , for I knew how keenly Holmes would feel any slip of the kind </s>
	=> <s> I was pained at the ceiling , for I knew how keenly Holmes would feel any slip of the kind </s>
********
<s> The man leaned over and pulled up the front of a kind of hutch in the corner </s>
	=> <s> The man leaned over and pulled up the front of a kind of fatality in the corner </s>
********
<s> If this man were inside it I should find out from his own lips , at the point of my revolver if necessary , who he was and why he had dogged us so long </s>
	=> <s> If this man were inside it I should find out from his own lips , at the point of my misfortune if necessary , who he was and why he had dogged us so long </s>
********
<s> The bedrooms in this wing are on the ground floor , the sitting-rooms being in the central block of the buildings </s>
	=> <s> The bedrooms in this neighbourhood are on the ground floor , the sitting-rooms being in the central block of the buildings </s>
********
<s> If I lay on my face the weight would come upon my spine , and I shuddered to think of that dreadful snap </s>
	=> <s> If I lay on my face the enemy would come upon my spine , and I shuddered to think of that dreadful snap </s>
********
<s> Was there a police-station anywhere near </s>
	=> <s> Was there a police-station lying near </s>
********
<s> He was very willing to have a holiday , so we shut the business up and started off for the address that was given us in the advertisement </s>
	=> <s> He was very willing to have a holiday , so we spent the business up and started off for the address that was given us in the advertisement </s>
********
<s> Besides , I knew that my assistant was a good man , and that he would see to anything that turned up </s>
	=> <s> Besides , I knew that my mistress was a good man , and that he would see to anything that turned up </s>
********
<s> I understand that it was on a professional matter that you wished to speak to me </s>
	=> <s> I understand that it was on a plain matter that you wished to speak to me </s>
********
<s> I cannot recall when I have seen anything so fine' He took a step backward , cocked his head on one side , and gazed at my hair until I felt quite bashful </s>
	=> <s> I cannot recall when I have seen anything so fine' He took a step backward , cocked his head on one side , and glanced at my hair until I felt quite bashful </s>
********
<s> Your eyes turned across to the unframed portrait of Henry Ward Beecher which stands upon the top of your books </s>
	=> <s> Your eyes turned across to the unframed portrait of Henry Ward Beecher which burst upon the top of your books </s>
********
<s> I mean to teach them in these parts that law is law , and that there is a man here who does not fear to invoke it </s>
	=> <s> I mean to teach them in these parts that law is law , and that there is a man here who does not fear to store it </s>
********
<s> One piece , about three feet in length , had a very marked indentation at one end , while several were flattened at the sides as if they had been compressed by some considerable weight </s>
	=> <s> One piece , about three feet in length , had a very marked indentation at one end , while several were flattened at the sides as if they had been stimulated by some considerable weight </s>
********
<s> At last she looked up with something reckless and defiant in her manner </s>
	=> <s> At last she looked up with something warm and defiant in her manner </s>
********
<s> My friend was an enthusiastic musician , being himself not only a very capable performer but a composer of no ordinary merit </s>
	=> <s> My friend was an enthusiastic cow , being himself not only a very capable performer but a composer of no ordinary merit </s>
********
<s> That was bad enough , for all that the coroner said </s>
	=> <s> That was bad enough , for all that the dog said </s>
********
<s> I am an interpreter , as perhaps my neighbor there has told you </s>
	=> <s> I am an indemnity , as perhaps my neighbor there has told you </s>
********
<s> Now , there is no one more easy to trace than a schoolmaster </s>
	=> <s> Now , there is no one more easy to guess than a schoolmaster </s>
********
<s> They were all three standing in a knot in front of the altar </s>
	=> <s> They were all three standing in a nest in front of the altar </s>
********
<s> The crate upon which I sit contains 2,000 napoleons packed between layers of lead foil </s>
	=> <s> The crate upon which I sit contains 2,000 napoleons packed between facts of lead foil </s>
********
<s> His aversion to women and his disinclination to form new friendships were both typical of his unemotional character , but not more so than his complete suppression of every reference to his own people </s>
	=> <s> His aversion to women and his disinclination to form new friendships were both typical of his charming character , but not more so than his complete suppression of every reference to his own people </s>
********
<s> I lounged up the side aisle like any other idler who has dropped into a church </s>
	=> <s> I lounged up the side aisle like any other aunt who has dropped into a church </s>
********
<s> My heart is lightened already since I have confided my trouble to you </s>
	=> <s> My heart is falling already since I have confided my trouble to you </s>
********
<s> The ceiling of this small chamber is really the end of the descending piston , and it comes down with the force of many tons upon this metal floor </s>
	=> <s> The ceiling of this small chamber is really the end of the descending piston , and it comes down with the force of many thousands upon this metal floor </s>
********
<s> And yet if it were on the lawn , I wonder that you did not hear it also </s>
	=> <s> And yet if it were on the morrow , I wonder that you did not hear it also </s>
********
<s> This we have now been doing for some time , and in order to help us in our operations we erected a hydraulic press </s>
	=> <s> This we have now been doing for some time , and in order to help us in our hearts we erected a hydraulic press </s>
********
<s> She then called for Miss Morrison , a young lady who lives in the next villa , and the two went off together to their meeting </s>
	=> <s> She then called for Miss Morrison , a young lady who lives in the next generation , and the two went off together to their meeting </s>
********
<s> One morning , at a little before seven o'clock , I was awakened by the maid tapping at the door to announce that two men had come from Paddington and were waiting in the consulting-room </s>
	=> <s> One morning , at a little before seven o'clock , I was protected by the maid tapping at the door to announce that two men had come from Paddington and were waiting in the consulting-room </s>
********
<s> No case , however , in which Holmes was engaged has ever illustrated the value of his analytical methods so clearly or has impressed those who were associated with him so deeply </s>
	=> <s> No case , however , in which Holmes was engaged has ever overlooked the value of his analytical methods so clearly or has impressed those who were associated with him so deeply </s>
********
<s> My wife had already gone upstairs , and the sound of the locking of the hall door some time before told me that the servants had also retired </s>
	=> <s> My wife had already gone upstairs , and the sound of the discovery of the hall door some time before told me that the servants had also retired </s>
********
<s> And that was how a great scandal threatened to affect the kingdom of Bohemia , and how the best plans of Mr. Sherlock Holmes were beaten by a woman's wit </s>
	=> <s> And that was how a great scandal threatened to chastise the kingdom of Bohemia , and how the best plans of Mr. Sherlock Holmes were beaten by a woman's wit </s>
********
<s> Holmes and the Inspector led us round it until we came to the side gate , which is separated by a stretch of garden from the hedge which lines the road </s>
	=> <s> Holmes and the Inspector led us round it until we came to the side gate , which is watered by a stretch of garden from the hedge which lines the road </s>
********
<s> It was an old rickety door and gave at once before our united strength </s>
	=> <s> It was an old gray door and gave at once before our united strength </s>
********
<s> We will be shown into the sitting-room to wait for the lady , but it is probable that when she comes she may find neither us nor the photograph </s>
	=> <s> We will be thrown into the sitting-room to wait for the lady , but it is probable that when she comes she may find neither us nor the photograph </s>
********
<s> The law is upon his side , and every day I am faced by the possibility that he may force me to live with him </s>
	=> <s> The law is upon his side , and every day I am amused by the possibility that he may force me to live with him </s>
********
<s> Without a word he grasped my arm and hurried me into a carriage , the door of which was standing open </s>
	=> <s> Without a word he grasped my arm and hurried me into a gallop , the door of which was standing open </s>
********
<s> It contained a loaf of bread , a tinned tongue , and two tins of preserved peaches </s>
	=> <s> It contained a loaf of bread , a tinned tongue , and two pairs of preserved peaches </s>
********
<s> In my inmost heart I believed that I could succeed where others failed , and now I had the opportunity to test myself </s>
	=> <s> In my inmost heart I believed that I could forget where others failed , and now I had the opportunity to test myself </s>
********
<s> My sister and I , you will recollect , were twins , and you know how subtle are the links which bind two souls which are so closely allied </s>
	=> <s> My sister and I , you will recollect , were twins , and you know how violent are the links which bind two souls which are so closely allied </s>
********
<s> Pray interrupt me if there is any inference which is not perfectly clear to you </s>
	=> <s> Pray interrupt me if there is any evil which is not perfectly clear to you </s>
********
<s> With an apology for my intrusion , I was about to withdraw when Holmes pulled me abruptly into the room and closed the door behind me </s>
	=> <s> With an apology for my intrusion , I was about to strike when Holmes pulled me abruptly into the room and closed the door behind me </s>
********
<s> I came in by train this morning , and on inquiring at Paddington as to where I might find a doctor , a worthy fellow very kindly escorted me here </s>
	=> <s> I came in by train this morning , and on arriving at Paddington as to where I might find a doctor , a worthy fellow very kindly escorted me here </s>
********
<s> She writhed as one who is in terrible pain , and her limbs were dreadfully convulsed </s>
	=> <s> She writhed as one who is in terrible danger , and her limbs were dreadfully convulsed </s>
********
<s> His broad black hat , his baggy trousers , his white tie , his sympathetic smile , and general look of peering and benevolent curiosity were such as Mr. John Hare alone could have equalled </s>
	=> <s> His broad black hat , his baggy trousers , his white tie , his cunning smile , and general look of peering and benevolent curiosity were such as Mr. John Hare alone could have equalled </s>
********
<s> I say normal cases , because ill-health and physical weakness reproduce the signs of old age , even when the invalid is a youth </s>
	=> <s> I say normal cases , because ill-health and physical weakness reproduce the reign of old age , even when the invalid is a youth </s>
********
<s> She left her room , therefore , and came into mine , where she sat for some time , chatting about her approaching wedding </s>
	=> <s> She left her room , therefore , and came into mine , where she sat for some time , playing about her approaching wedding </s>
********
<s> In an instant his strange headgear began to move , and there reared itself from among his hair the squat diamond-shaped head and puffed neck of a loathsome serpent </s>
	=> <s> In an instant his strange agony began to move , and there reared itself from among his hair the squat diamond-shaped head and puffed neck of a loathsome serpent </s>
********
<s> That is his main fault , but on the whole he's a good worker </s>
	=> <s> That is his favourite fault , but on the whole he's a good worker </s>
********
<s> I had never seen my friend's face so grim or his brow so dark as it was when we turned from the scene of this investigation </s>
	=> <s> I had never seen my friend's face so clean or his brow so dark as it was when we turned from the scene of this investigation </s>
********
<s> I have one of my Baker Street boys mounting guard over him who would stick to him like a burr , go where he might </s>
	=> <s> I have one of my Baker Street boys mounting guard over him who would stick to him like a deer , go where he might </s>
********
<s> From within he produced a crumpled piece of paper , and old-fashioned brass key , a peg of wood with a ball of string attached to it , and three rusty old disks of metal </s>
	=> <s> From within he wore a crumpled piece of paper , and old-fashioned brass key , a peg of wood with a ball of string attached to it , and three rusty old disks of metal </s>
********
<s> There was nothing markedly abnormal in any of these conditions , which harmonized with my former experiences </s>
	=> <s> There was nothing markedly abnormal in any of these conditions , which mingled with my former experiences </s>
********
<s> The machine goes readily enough , but there is some stiffness in the working of it , and it has lost a little of its force </s>
	=> <s> The machine goes readily enough , but there is some stiffness in the habit of it , and it has lost a little of its force </s>
********
<s> He loved to lie in the very centre of five millions of people , with his filaments stretching out and running through them , responsive to every little rumor or suspicion of unsolved crime </s>
	=> <s> He loved to lie in the very centre of five millions of people , with his fleet stretching out and running through them , responsive to every little rumor or suspicion of unsolved crime </s>
********
<s> But his next remark took a weight from my mind </s>
	=> <s> But his next blow took a weight from my mind </s>
********
<s> The least appearance of opposition struck fire out of the old autocrat </s>
	=> <s> The least appearance of speech struck fire out of the old autocrat </s>
********
<s> But then , when I found how I had betrayed myself , I began to think </s>
	=> <s> But then , when I found how I had studied myself , I began to think </s>
********
<s> An important addition has been made during the last week to the list of the prizes which have been borne away by these charming invaders </s>
	=> <s> An important revolution has been made during the last week to the list of the prizes which have been borne away by these charming invaders </s>
********
<s> I found the black tor upon which I had seen the solitary watcher , and from its craggy summit I looked out myself across the melancholy downs </s>
	=> <s> I found the black tor upon which I had seen the solitary confinement , and from its craggy summit I looked out myself across the melancholy downs </s>
********
<s> I made excellent arrangements , and they are only delayed one day upon their way </s>
	=> <s> I made excellent spirits , and they are only delayed one day upon their way </s>
********
<s> He had heard nothing , and the affair remained a complete mystery </s>
	=> <s> He had heard nothing , and the devil remained a complete mystery </s>
********
<s> Beside it lay some cooking utensils and a bucket half-full of water </s>
	=> <s> Beside it lay some cooking utensils and a bucket capable of water </s>
********
<s> It was not merely that Holmes changed his costume </s>
	=> <s> It was not sorry that Holmes changed his costume </s>
********
<s> I do not think that I have ever seen so thin a man </s>
	=> <s> I do not think that I have ever seen so marked a man </s>
********
<s> The animal has been moving , and we have the length of its stride </s>
	=> <s> The animal has been granted , and we have the length of its stride </s>
********
<s> Naturally enough she ran down to tell the cook , and the two women with the coachman came up into the hall and listened to the dispute which was still raging </s>
	=> <s> Naturally enough she ran down to tell the cook , and the two women with the coachman came up into the hall and listened to the astonishment which was still raging </s>
********
<s> Then he turned down the lamp , and we were left in darkness </s>
	=> <s> Then he turned down the Beggar , and we were left in darkness </s>
********
<s> He had evidently been carried down by two persons , one of whom had remarkably small feet and the other unusually large ones </s>
	=> <s> He had scarcely been carried down by two persons , one of whom had remarkably small feet and the other unusually large ones </s>
********
<s> For a moment is seemed to me that there must be some radical mistake in my calculations </s>
	=> <s> For a moment is seemed to me that there must be some radical wound in my calculations </s>
********
<s> He had spotted the place </s>
	=> <s> He had performed the place </s>
********
<s> On his evidence Cartwright was hanged and the other three got fifteen years apiece </s>
	=> <s> On his evidence Cartwright was confused and the other three got fifteen years apiece </s>
********
<s> It would indeed be a triumph for me if I could run him to earth where my master had failed </s>
	=> <s> It would indeed be a match for me if I could run him to earth where my master had failed </s>
********
<s> This man strikes even deeper , but I think , Watson , that we shall be able to strike deeper still </s>
	=> <s> This man strikes even honest , but I think , Watson , that we shall be able to strike deeper still </s>
********
<s> You may believe , then , that I was in my consulting-room when , at the appointed hour , the page showed in the patient </s>
	=> <s> You may believe , then , that I was in my memory when , at the appointed hour , the page showed in the patient </s>
********
<s> I shall give directions that you may remain behind when the others go , so that you may copy it at your leisure without fear of being overlooked </s>
	=> <s> I shall give directions that you may ride behind when the others go , so that you may copy it at your leisure without fear of being overlooked </s>
********
<s> Would she not have made an admirable queen </s>
	=> <s> Would she not have made an enormous queen </s>
********
<s> You see that we hold all the cards , and we have only to fear some sudden act of violence on their part </s>
	=> <s> You see that we hold all the cards , and we have only to fear some sudden act of walking on their part </s>
********
<s> My friend hardly glanced up as I entered , and I , seeing that his investigation must be of importance , seated myself in an arm-chair and waited </s>
	=> <s> My friend hardly glanced up as I entered , and I , seeing that his servants must be of importance , seated myself in an arm-chair and waited </s>
********
<s> I have made a small study of tattoo marks and have even contributed to the literature of the subject </s>
	=> <s> I have made a small herd of tattoo marks and have even contributed to the literature of the subject </s>
********
<s> Were it not for the ugly wound upon my hand , all that had passed during those dreadful hours might have been an evil dream </s>
	=> <s> Were it not for the growing wound upon my hand , all that had passed during those dreadful hours might have been an evil dream </s>
********
<s> Besides , I can read in a man's eye when it is his own skin that he is frightened for </s>
	=> <s> Besides , I can read in a man's eye when it is his own opinion that he is frightened for </s>
********
<s> She never said a word until we were at the door here , when she took me by the hand and begged me to tell no one what had happened </s>
	=> <s> She never said a word until we were at the door here , when she took me by the hand and kissed me to tell no one what had happened </s>
********
<s> He proved to be a blackguard and deserted her </s>
	=> <s> He proved to be a blackguard and pressed her </s>
********
<s> The butler brought me my coffee into the library , and I took the chance to ask him a few questions </s>
	=> <s> The butler brought me my entrance into the library , and I took the chance to ask him a few questions </s>
********
<s> He might slip away from us in the crowd of Regent Street , but it would puzzle him to do so upon the lonely moor </s>
	=> <s> He might slip away from us in the history of Regent Street , but it would puzzle him to do so upon the lonely moor </s>
********
<s> As he turned towards us the glint of the light showed me that he was wearing glasses </s>
	=> <s> As he turned towards us the edge of the light showed me that he was wearing glasses </s>
********
<s> Some chalk marks over the waistcoat pocket were the only signs of billiards which I could see in one of them </s>
	=> <s> Some chalk wheels over the waistcoat pocket were the only signs of billiards which I could see in one of them </s>
********
<s> At eleven o'clock she rose to leave me , but she paused at the door and looked back </s>
	=> <s> At eleven o'clock she rose to leave me , but she glanced at the door and looked back </s>
********
<s> The new century will have come , however , before the story can be safely told </s>
	=> <s> The new current will have come , however , before the story can be safely told </s>
********
<s> There was no slit through which a knife could be passed to raise the bar </s>
	=> <s> There was no slit through which a knife could be passed to join the bar </s>
********
<s> Holmes walked slowly round and examined each and all of them with the keenest interest </s>
	=> <s> Holmes walked slowly round and embraced each and all of them with the keenest interest </s>
********
<s> For three hours we strolled about together , watching the ever-changing kaleidoscope of life as it ebbs and flows through Fleet Street and the Strand </s>
	=> <s> For three hours we strolled about together , leaving the ever-changing kaleidoscope of life as it ebbs and flows through Fleet Street and the Strand </s>
********
<s> The smoke and shouting were enough to shake nerves of steel </s>
	=> <s> The smoke and literature were enough to shake nerves of steel </s>
********
<s> It was , of course , of the very first importance that they should not be reminded of the existence of this paper , otherwise they would naturally destroy it without delay </s>
	=> <s> It was , of course , of the very first importance that they should not be suspected of the existence of this paper , otherwise they would naturally destroy it without delay </s>
********
<s> The photograph becomes a double-edged weapon now </s>
	=> <s> The photograph becomes a slow weapon now </s>
********
<s> It had been hacked or torn right out from the roots </s>
	=> <s> It had been seduced or torn right out from the roots </s>
********
<s> Several discs of metal , old coins apparently , such as I hold here , were scattered over the bottom of the box , but it contained nothing else </s>
	=> <s> Several discs of metal , old coins apparently , such as I hold here , were leaning over the bottom of the box , but it contained nothing else </s>
********
<s> He is as brave as a bulldog and as tenacious as a lobster if he gets his claws upon anyone </s>
	=> <s> He is as brave as a knife and as tenacious as a lobster if he gets his claws upon anyone </s>
********
<s> We should not have troubled you , only that our friend who speaks Greek and who began these negotiations has been forced to return to the East </s>
	=> <s> We should not have troubled you , only that our friend who speaks Greek and who began these sentiments has been forced to return to the East </s>
********
<s> It is not a common experience among employers in this age </s>
	=> <s> It is not a common thief among employers in this age </s>
********
<s> He sat at my side in silence all the time , and I was aware , more than once when I glanced in his direction , that he was looking at me with great intensity </s>
	=> <s> He sat at my side in silence all the time , and I was aware , more than once when I engaged in his direction , that he was looking at me with great intensity </s>
********
<s> Major Murphy , to whom I owe most of my facts , assures me that he has never heard of any misunderstanding between the pair </s>
	=> <s> Major Murphy , to whom I owe most of my neck , assures me that he has never heard of any misunderstanding between the pair </s>
********
<s> They saw that I must know all about it , you see , and the sudden change from absolute security to complete despair made them perfectly desperate </s>
	=> <s> They saw that I must know all about it , you see , and the sudden change from absolute indifference to complete despair made them perfectly desperate </s>
********
<s> It is conceivable that you may even have read some account of the matter </s>
	=> <s> It is impossible that you may even have read some account of the matter </s>
********
<s> Some three hours or so afterwards we were all in the train together , bound from Reading to the little Berkshire village </s>
	=> <s> Some three hours or so evidently we were all in the train together , bound from Reading to the little Berkshire village </s>
********
<s> I have no wish to commit you to anything without your having it all laid before you </s>
	=> <s> I have no wish to carry you to anything without your having it all laid before you </s>
********
<s> We are spies in an enemy's country </s>
	=> <s> We are treated in an enemy's country </s>
********
<s> It was furnished partly as a sitting and partly as a bedroom , with flowers arranged daintily in every nook and corner </s>
	=> <s> It was furnished partly as a sitting and partly as a bedroom , with flowers arranged comfortably in every nook and corner </s>
********
<s> A collection of my trifling achievements would certainly be incomplete which contained no account of this very singular business </s>
	=> <s> A collection of my trifling achievements would certainly be discovered which contained no account of this very singular business </s>
********
<s> As I ran down the passage , my sister's door was unlocked , and revolved slowly upon its hinges </s>
	=> <s> As I ran down the passage , my sister's door was unlocked , and paced slowly upon its hinges </s>
********
<s> You will remember that on hearing the sound of the quarrel she descended and returned with the other servants </s>
	=> <s> You will remember that on hearing the sound of the staircase she descended and returned with the other servants </s>
********
<s> Still , of course , if you would like to draw out of the business , there is plenty of time to do so </s>
	=> <s> Still , of course , if you would like to wear out of the business , there is plenty of time to do so </s>
********
<s> At first I thought that she had not recognised me , but as I bent over her she suddenly shrieked out in a voice which I shall never forget , 'Oh , my God </s>
	=> <s> At first I thought that she had not touched me , but as I bent over her she suddenly shrieked out in a voice which I shall never forget , 'Oh , my God </s>
********
<s> Our visitor bore every mark of being an average commonplace British tradesman , obese , pompous , and slow </s>
	=> <s> Our visitor bore every mark of being an average commonplace British tradesman , obese , blind , and slow </s>
********
<s> God help those who wander into the great mire now , for even the firm uplands are becoming a morass </s>
	=> <s> God help those who wander into the great ocean now , for even the firm uplands are becoming a morass </s>
********
<s> But , you know , I have been trained as an actress myself </s>
	=> <s> But , you know , I have been trained as an Elephant myself </s>
********
<s> You will observe that the hour mentioned upon it is the very time at which the poor fellow met his fate </s>
	=> <s> You will observe that the hour closed upon it is the very time at which the poor fellow met his fate </s>
********
<s> Out of this landing opened the drawing-room and several bedrooms , including those of Mr. Cunningham and his son </s>
	=> <s> Out of this landing opened the valise and several bedrooms , including those of Mr. Cunningham and his son </s>
********
<s> He went over to the door , and turning the lock he examined it in his methodical way </s>
	=> <s> He went over to the door , and turning the fish he examined it in his methodical way </s>
********
<s> I rubbed one of them on my sleeve , however , and it glowed afterwards like a spark in the dark hollow of my hand </s>
	=> <s> I rubbed one of them on my sleeve , however , and it glowed afterwards like a feather in the dark hollow of my hand </s>
********
<s> He was once a schoolmaster in the north of England </s>
	=> <s> He was once a crack in the north of England </s>
********
<s> I have only one other incident to record upon this tempestuous and melancholy day </s>
	=> <s> I have only one other incident to record upon this excellent and melancholy day </s>
********
<s> Was he our malignant enemy , or was he by chance our guardian angel </s>
	=> <s> Was he our splendid enemy , or was he by chance our guardian angel </s>
********
<s> Who were these German people , and what were they doing living in this strange , out-of-the-way place </s>
	=> <s> Who were these German people , and what were they doing living in this strange , impossible place </s>
********
<s> He was of a sickly color , and his thin , sandy hair seemed to bristle up with the intensity of his emotion </s>
	=> <s> He was of a sickly color , and his thin , sandy hair seemed to bristle up with the exception of his emotion </s>
********
<s> Rain had fallen on the night before and we examined the lawn and the paths all round the house , but in vain </s>
	=> <s> Rain had fallen on the night before and we examined the duke and the paths all round the house , but in vain </s>
********
<s> I was feeling drowsy and stupid , partly from my dinner and also from the effects of a long day's work </s>
	=> <s> I was feeling powerful and stupid , partly from my dinner and also from the effects of a long day's work </s>
********
<s> I rushed madly from the room on to the landing </s>
	=> <s> I rushed gently from the room on to the landing </s>
********
<s> For all they cared it might have been me , instead of my effigy , which these rascals burned at the stake </s>
	=> <s> For all they cared it might have been me , instead of my childhood , which these rascals burned at the stake </s>
********
<s> Holmes cut the cord and removed the transverse bar </s>
	=> <s> Holmes cut the bread and removed the transverse bar </s>
********
<s> Far away we could hear the deep tones of the parish clock , which boomed out every quarter of an hour </s>
	=> <s> Far away we could hear the deep shadow of the parish clock , which boomed out every quarter of an hour </s>
********
<s> The Colonel possessed a varied collection of weapons brought from the different countries in which he had fought , and it is conjectured by the police that his club was among his trophies </s>
	=> <s> The Colonel possessed a varied collection of letters brought from the different countries in which he had fought , and it is conjectured by the police that his club was among his trophies </s>
********
<s> You must lock yourself up from him to-night </s>
	=> <s> You must judge yourself up from him to-night </s>
********
<s> Is that a place where a shepherd would be likely to take his station </s>
	=> <s> Is that a place where a Canadian would be likely to take his station </s>
********
<s> I often take advantage of the freedom which it gives </s>
	=> <s> I often take advantage of the mountain which it gives </s>
********
<s> He would try by a few attentions to make his peace with the girl Howells , and then would engage her as his accomplice </s>
	=> <s> He would try by a few attentions to make his peace with the girl Howells , and then would accompany her as his accomplice </s>
********
<s> For days on end , when the mood was on him , he has been sunk in the deepest gloom </s>
	=> <s> For days on end , when the mood was on him , he has been published in the deepest gloom </s>
********
<s> The ejaculation had been drawn from my companion by the fact that our door had been suddenly dashed open , and that a huge man had framed himself in the aperture </s>
	=> <s> The ejaculation had been drawn from my companion by the fact that our door had been suddenly dragged open , and that a huge man had framed himself in the aperture </s>
********
<s> No sound came from within , and at the silence Holmes' face clouded over </s>
	=> <s> No sound came from within , and at the silence Holmes' face bent over </s>
********
<s> Sherlock Holmes stopped at a door some little distance from the Carlton , and , cautioning me not to speak , he led the way into the hall </s>
	=> <s> Sherlock Holmes stopped at a door some little distance from the Carlton , and , approaching me not to speak , he led the way into the hall </s>
********
<s> Holmes had brought up a long thin cane , and this he placed upon the bed beside him </s>
	=> <s> Holmes had brought up a long thin nose , and this he placed upon the bed beside him </s>
********
<s> You don't comply with the conditions if you budge from the office during that time </s>
	=> <s> You don't stick with the conditions if you budge from the office during that time </s>
********
<s> The ceiling was only a foot or two above my head , and with my hand upraised I could feel its hard , rough surface </s>
	=> <s> The ceiling was only a foot or two above my head , and with my hand Shortly I could feel its hard , rough surface </s>
********
<s> Then he did the same with the wood-work with which the chamber was panelled </s>
	=> <s> Then he did the same with the speed with which the chamber was panelled </s>
********
<s> I have frequently gained my first real insight into the character of parents by studying their children </s>
	=> <s> I have frequently gained my first real insight into the character of Scripture by studying their children </s>
********
<s> He's in hiding , too , but he's not a convict as far as I can make out </s>
	=> <s> He's in Scotland , too , but he's not a convict as far as I can make out </s>
********
<s> Again and again I have taken a problem to him , and have received an explanation which has afterwards proved to be the correct one </s>
	=> <s> Again and again I have taken a problem to him , and have received an invitation which has afterwards proved to be the correct one </s>
********
<s> It was a serious thing to be in the power of this spiteful old busybody </s>
	=> <s> It was a pleasant thing to be in the power of this spiteful old busybody </s>
********
<s> Whatever his crimes , he has suffered something to atone for them </s>
	=> <s> Whatever his crimes , he has forgotten something to atone for them </s>
********
<s> But not one word shall they have from me , and I bind you to secrecy also , Dr. Watson </s>
	=> <s> But not one word shall they have from me , and I promise you to secrecy also , Dr. Watson </s>
********
<s> He has been very attentive to us , and hardly a day has passed that he has not called at the Hall to see how we were getting on </s>
	=> <s> He has been very difficult to us , and hardly a day has passed that he has not called at the Hall to see how we were getting on </s>
********
<s> Then he vanished over the hill </s>
	=> <s> Then he bent over the hill </s>
********
<s> Holmes walked slowly , taking keen note of the architecture of the house </s>
	=> <s> Holmes walked slowly , taking keen note of the sons of the house </s>
********
<s> They have given up the chase there , and he can lie quiet until the ship is ready for him </s>
	=> <s> They have given up the aisle there , and he can lie quiet until the ship is ready for him </s>
********
<s> He had usually a great many letters , for he was a public man and well known for his kind heart , so that everyone who was in trouble was glad to turn to him </s>
	=> <s> He had usually a great many apologies , for he was a public man and well known for his kind heart , so that everyone who was in trouble was glad to turn to him </s>
********
<s> There he was , sure enough , a small urchin with a little bundle upon his shoulder , toiling slowly up the hill </s>
	=> <s> There he was , sure enough , a small urchin with a little cloud upon his shoulder , toiling slowly up the hill </s>
********
<s> The point is a simple one , but the Inspector had overlooked it because he had started with the supposition that these county magnates had had nothing to do with the matter </s>
	=> <s> The point is a simple one , but the Inspector had touched it because he had started with the supposition that these county magnates had had nothing to do with the matter </s>
********
<s> I should like to have his opinion of the case , though the authorities assure me that nothing more can be done </s>
	=> <s> I should like to have his share of the case , though the authorities assure me that nothing more can be done </s>
********
<s> At Waterloo we were fortunate in catching a train for Leatherhead , where we hired a trap at the station inn and drove for four or five miles through the lovely Surrey lanes </s>
	=> <s> At Waterloo we were fortunate in choosing a train for Leatherhead , where we hired a trap at the station inn and drove for four or five miles through the lovely Surrey lanes </s>
********
<s> It was a homely little room , with a low ceiling and a gaping fireplace , after the fashion of old country-houses </s>
	=> <s> It was a regular little room , with a low ceiling and a gaping fireplace , after the fashion of old country-houses </s>
********
<s> Too large for easy concealment about a woman's dress </s>
	=> <s> Too large for easy conversation about a woman's dress </s>
********
<s> An instant later I heard him running down , and he burst into my consulting-room like a man who is mad with panic </s>
	=> <s> An instant later I heard him running down , and he sank into my consulting-room like a man who is mad with panic </s>
********
<s> It did wonders both in the Crimea and the Mutiny , and has since that time distinguished itself upon every possible occasion </s>
	=> <s> It did wonders both in the Crimea and the Mutiny , and has since that time prepared itself upon every possible occasion </s>
********
<s> It was worth an effort to find out , and for that object we all went up to the house </s>
	=> <s> It was worth an effort to find out , and for that event we all went up to the house </s>
********
<s> Holmes flung open the door and rushed in , but he was out again in an instant , with his hand to his throat </s>
	=> <s> Holmes flung open the door and peered in , but he was out again in an instant , with his hand to his throat </s>
********
<s> But I want to find out about them , and who they are , and what their object was in playing this prank if it was a prank upon me </s>
	=> <s> But I want to find out about them , and who they are , and what their fate was in playing this prank if it was a prank upon me </s>
********
<s> I have no doubt at all that a family mannerism can be traced in these two specimens of writing </s>
	=> <s> I have no doubt at all that a family possession can be traced in these two specimens of writing </s>
********
<s> The instant that I had crossed the threshold the door slammed heavily behind us , and I heard faintly the rattle of the wheels as the carriage drove away </s>
	=> <s> The instant that I had crossed the threshold the door slammed somewhere behind us , and I heard faintly the rattle of the wheels as the carriage drove away </s>
********
<s> The lady looked quickly up with an angry gleam in her hazel eyes </s>
	=> <s> The lady looked quickly up with an occasional gleam in her hazel eyes </s>
********
<s> They say that away down in the village , and even in the distant parsonage , that cry raised the sleepers from their beds </s>
	=> <s> They say that away down in the village , and even in the distant parsonage , that cry raised the cup from their beds </s>
********
<s> Half a guinea if you do it in twenty minutes </s>
	=> <s> Half a mile if you do it in twenty minutes </s>
********
<s> The bell-rope hangs from the wire just to the right of my desk </s>
	=> <s> The bell-rope hangs from the scene just to the right of my desk </s>
********
<s> One side of the window was open , which I understand was quite usual in the summer-time , and he passed without difficulty into the room </s>
	=> <s> One side of the window was open , which I understand was quite usual in the woods , and he passed without difficulty into the room </s>
********
<s> Again and again I cross-questioned her , but I could never get past that point </s>
	=> <s> Again and again I finished her , but I could never get past that point </s>
********
<s> The house was just such as I had pictured it from Sherlock Holmes' succinct description , but the locality appeared to be less private than I expected </s>
	=> <s> The house was just such as I had replaced it from Sherlock Holmes' succinct description , but the locality appeared to be less private than I expected </s>
********
<s> We were at breakfast when the Colonel's butler rushed in with all his propriety shaken out of him </s>
	=> <s> We were at breakfast when the Colonel's train rushed in with all his propriety shaken out of him </s>
********
<s> I slept at Baker Street that night , and we were engaged upon our toast and coffee in the morning when the King of Bohemia rushed into the room </s>
	=> <s> I slept at Baker Street that night , and we were forced upon our toast and coffee in the morning when the King of Bohemia rushed into the room </s>
********
<s> There is something in it which fascinates me extremely </s>
	=> <s> There is something in it which possesses me extremely </s>
********
<s> The chimney is wide , but is barred up by four large staples </s>
	=> <s> The chimney is wide , but is higher up by four large staples </s>
********
<s> Altogether there are eight maids , the cook , the butler , two footmen , and a boy </s>
	=> <s> Altogether there are eight maids , the lake , the butler , two footmen , and a boy </s>
********
<s> He actually sat crying in an arm-chair , and I could hardly get him to speak coherently </s>
	=> <s> He actually sat smiling in an arm-chair , and I could hardly get him to speak coherently </s>
********
<s> Then I carefully paced off five to the east and two to the south </s>
	=> <s> Then I carefully brushed off five to the east and two to the south </s>
********
<s> Sherlock Holmes and I had no difficulty in engaging a bedroom and sitting-room at the Crown Inn </s>
	=> <s> Sherlock Holmes and I had no difficulty in opening a bedroom and sitting-room at the Crown Inn </s>
********
<s> Then he reseated himself in his chair and looked them over with a gleam of satisfaction in his eyes </s>
	=> <s> Then he shut himself in his chair and looked them over with a gleam of satisfaction in his eyes </s>
********
<s> My clothes were all sodden with dew , and my coat-sleeve was drenched with blood from my wounded thumb </s>
	=> <s> My clothes were all tattered with dew , and my coat-sleeve was drenched with blood from my wounded thumb </s>
********
<s> There was something subtly wrong with the face , some coarseness of expression , some hardness , perhaps , of eye , some looseness of lip which marred its perfect beauty </s>
	=> <s> There was something subtly wrong with the face , some coarseness of expression , some speaking , perhaps , of eye , some looseness of lip which marred its perfect beauty </s>
********
<s> I see him every day through my telescope upon the roof </s>
	=> <s> I see him every day through my fingers upon the roof </s>
********
<s> It will end in my being conveyed into the house </s>
	=> <s> It will end in my being blown into the house </s>
********
<s> I was weary of our little sitting-room and gladly acquiesced </s>
	=> <s> I was aware of our little sitting-room and gladly acquiesced </s>
********
<s> Twice he struck at the chamber door without any reply from within </s>
	=> <s> Twice he struck at the chamber door without any danger from within </s>
********
<s> His hands and feet were securely strapped together , and he bore over one eye the marks of a violent blow </s>
	=> <s> His hands and feet were securely strapped together , and he bore over one eye the fate of a violent blow </s>
********
<s> Throwing aside my cigarette , I closed my hand upon the butt of my revolver and , walking swiftly up to the door , I looked in </s>
	=> <s> Throwing aside my opinion , I closed my hand upon the butt of my revolver and , walking swiftly up to the door , I looked in </s>
********
<s> And yet it would be the blackest treachery to Holmes to draw back now from the part which he had intrusted to me </s>
	=> <s> And yet it would be the innocent treachery to Holmes to draw back now from the part which he had intrusted to me </s>
********
<s> As I set it down again , after having examined it , my heart leaped to see that beneath it there lay a sheet of paper with writing upon it </s>
	=> <s> As I set it down again , after having examined it , my heart leaped to see that beneath it there lay a sheet of paper with snow upon it </s>
********
<s> One of them fired a shot , the other dropped , and the murderer rushed across the garden and over the hedge </s>
	=> <s> One of them fired a shot , the other dropped , and the smoke rushed across the garden and over the hedge </s>
********
<s> I implored the colonel to let me out , but the remorseless clanking of the levers drowned my cries </s>
	=> <s> I implored the action to let me out , but the remorseless clanking of the levers drowned my cries </s>
********
<s> But , first , as I am rather shaken by the knocking about which I had in the dressing-room , I think that I shall help myself to a dash of your brandy , Colonel </s>
	=> <s> But , first , as I am rather shaken by the knocking about which I had in the dressing-room , I think that I shall help myself to a piece of your brandy , Colonel </s>
********
<s> Mr. Cunningham , looking out of his bedroom , saw the fellow as he gained the road , but lost sight of him at once </s>
	=> <s> Mr. Cunningham , looking out of his reign , saw the fellow as he gained the road , but lost sight of him at once </s>
********
<s> I threw myself , screaming , against the door , and dragged with my nails at the lock </s>
	=> <s> I threw myself , besides , against the door , and dragged with my nails at the lock </s>
********
<s> I rushed across the bedroom , flung open the window , and looked out </s>
	=> <s> I rushed across the lawn , flung open the window , and looked out </s>
********
<s> The lady , against whom naturally the strongest suspicion rested , was removed to her room , still in a state of insensibility </s>
	=> <s> The lady , against whom naturally the strongest suspicion rested , was addressed to her room , still in a state of insensibility </s>
********
<s> Nothing would induce me to help the police in any way </s>
	=> <s> Nothing would induce me to help the reader in any way </s>
********
<s> He looked round him with a furtive and stealthy air , as one who dreads pursuit </s>
	=> <s> He looked round him with a calm and stealthy air , as one who dreads pursuit </s>
********
<s> Indeed , it was almost mesmeric , the effect which this giggling ruffian had produced upon the unfortunate linguist , for he could not speak of him save with trembling hands and a blanched cheek </s>
	=> <s> Indeed , it was almost deferential , the effect which this giggling ruffian had produced upon the unfortunate linguist , for he could not speak of him save with trembling hands and a blanched cheek </s>
********
<s> Five little livid spots , the marks of four fingers and a thumb , were printed upon the white wrist </s>
	=> <s> Five little livid spots , the row of four fingers and a thumb , were printed upon the white wrist </s>
********
<s> Of course , if they had been merely after plunder they would at least have made some attempt to search for it </s>
	=> <s> Of course , if they had been merely after breakfast they would at least have made some attempt to search for it </s>
********
<s> On the third morning , however he did not appear , as was his custom , after breakfast to receive my instructions for the day </s>
	=> <s> On the third morning , however he did not appear , as was his custom , after listening to receive my instructions for the day </s>
********
<s> The flush had faded in an instant , and a deathly face was before me </s>
	=> <s> The flush had crept in an instant , and a deathly face was before me </s>
********
<s> Here we dismissed our cab , and made our way up the drive together </s>
	=> <s> Here we cudgeled our cab , and made our way up the drive together </s>
********
<s> I was the only passenger who got out there , and there was no one upon the platform save a single sleepy porter with a lantern </s>
	=> <s> I was the only passenger who got out there , and there was no one upon the platform save a single sleepy peon with a lantern </s>
********
<s> It may stop his gossip </s>
	=> <s> It may trust his gossip </s>
********
<s> You must not interfere , come what may </s>
	=> <s> You must not omit , come what may </s>
********
<s> I heard a gentle sound of movement , and then all was silent once more , though the smell grew stronger </s>
	=> <s> I heard a gentle sound of blows , and then all was silent once more , though the smell grew stronger </s>
********
<s> My companion was a powerful , broad-shouldered young fellow , and , apart from the weapon , I should not have had the slightest chance in a struggle with him </s>
	=> <s> My companion was a powerful , broad-shouldered young fellow , and , apart from the cradle , I should not have had the slightest chance in a struggle with him </s>
********
<s> Miss Irene , or Madame , rather , returns from her drive at seven </s>
	=> <s> Miss Irene , or Madame , rather , shot from her drive at seven </s>
********
<s> He was deadly pale and terribly emaciated , with the protruding , brilliant eyes of a man whose spirit was greater than his strength </s>
	=> <s> He was deadly pale and terribly profane , with the protruding , brilliant eyes of a man whose spirit was greater than his strength </s>
********
<s> These articles , with two small wicker-work chairs , made up all the furniture in the room save for a square of Wilton carpet in the centre </s>
	=> <s> These articles , with two small walking chairs , made up all the furniture in the room save for a square of Wilton carpet in the centre </s>
********
<s> Upon the floor , close to the body , was lying a singular club of hard carved wood with a bone handle </s>
	=> <s> Upon the floor , close to the body , was lying a singular mixture of hard carved wood with a bone handle </s>
********
<s> The more formal we made the visit the less information we might obtain </s>
	=> <s> The more formal we made the mistake the less information we might obtain </s>
********
<s> He took a small piece of torn paper from a note-book and spread it out upon his knee </s>
	=> <s> He took a small piece of torn paper from a pencil and spread it out upon his knee </s>
********
<s> The incidents of the next few days are indelibly graven upon my recollection , and I can tell them without reference to the notes made at the time </s>
	=> <s> The incidents of the next few days are probably graven upon my recollection , and I can tell them without reference to the notes made at the time </s>
********
<s> I had been casting round for some excuse by which I could get away from his gossip , but now I began to wish to hear more of it </s>
	=> <s> I had been casting round for some passage by which I could get away from his gossip , but now I began to wish to hear more of it </s>
********
<s> I measured out the distance , which brought me almost to the wall of the house , and I thrust a peg into the spot </s>
	=> <s> I measured out the distance , which brought me almost to the wall of the house , and I formed a peg into the spot </s>
********
<s> A small side door led into the whitewashed corridor from which the three bedrooms opened </s>
	=> <s> A small side door led into the whitewashed corridor from which the three guards opened </s>
********
<s> I had the hint from Holmes that this smooth-faced pawnbroker's assistant was a formidable man a man who might play a deep game </s>
	=> <s> I had the hint from Holmes that this smooth-faced pawnbroker's assistant was a younger man a man who might play a deep game </s>
********
<s> These walls are thick , and it is conceivable that his shriek , if he had time to utter one , was unheard </s>
	=> <s> These walls are narrow , and it is conceivable that his shriek , if he had time to utter one , was unheard </s>
********
<s> My nets are closing upon him , even as his are upon Sir Henry , and with your help he is already almost at my mercy </s>
	=> <s> My nets are written upon him , even as his are upon Sir Henry , and with your help he is already almost at my mercy </s>
********
<s> As to the photograph , your client may rest in peace </s>
	=> <s> As to the photograph , your opinion may rest in peace </s>
********
<s> The policeman and I agreed that our best plan would be to seize the woman before she could get rid of the papers , presuming that she had them </s>
	=> <s> The policeman and I agreed that our best plan would be to relinquish the woman before she could get rid of the papers , presuming that she had them </s>
********
<s> He held in his hand a sheet of blue paper , scrawled over with notes and figures </s>
	=> <s> He held in his hand a chorus of blue paper , scrawled over with notes and figures </s>
********
<s> And yet I suppressed all appearance of interest </s>
	=> <s> And yet I learned all appearance of interest </s>
********
<s> Therefore something had occurred between seven-thirty and nine o'clock which had completely altered her feelings towards him </s>
	=> <s> Therefore something had occurred between Bombay and nine o'clock which had completely altered her feelings towards him </s>
********
<s> The roadway was blocked with the immense stream of commerce flowing in a double tide inward and outward , while the footpaths were black with the hurrying swarm of pedestrians </s>
	=> <s> The roadway was blocked with the hot stream of commerce flowing in a double tide inward and outward , while the footpaths were black with the hurrying swarm of pedestrians </s>
********
<s> The book , however , had been left in the billiard-room , so I pulled on my dressing-gown and started off to get it </s>
	=> <s> The book , however , had been left in the billiard-room , so I decided on my dressing-gown and started off to get it </s>
********
<s> He has died within ten seconds of being bitten </s>
	=> <s> He has died within ten degrees of being bitten </s>
********
<s> He is not a bad fellow , though an absolute imbecile in his profession </s>
	=> <s> He is not a bad fellow , though an absolute faith in his profession </s>
********
<s> I am a dangerous man to fall foul of </s>
	=> <s> I am a dying man to fall foul of </s>
********
<s> Besides this preliminary outlay , he must be prepared to keep himself for some years , and to hire a presentable carriage and horse </s>
	=> <s> Besides this practical outlay , he must be prepared to keep himself for some years , and to hire a presentable carriage and horse </s>
********
<s> Holmes rushed at the bell-pull , tore back a small sliding shutter , and , plunging in his hand , pulled out a photograph and a letter </s>
	=> <s> Holmes rushed at the bell-pull , tore back a small hay shutter , and , plunging in his hand , pulled out a photograph and a letter </s>
********
<s> A few minutes later we were joined by a short , stout man whose olive face and coal-black hair proclaimed his Southern origin , though his speech was that of an educated Englishman </s>
	=> <s> A few minutes later we were joined by a short , stout man whose olive face and coal-black hair touched his Southern origin , though his speech was that of an educated Englishman </s>
********
<s> Well , there is nothing very instructive in all this </s>
	=> <s> Well , there is nothing very punctual in all this </s>
********
<s> There were two guides given us to start with , an oak and an elm </s>
	=> <s> There were two guides given us to dine with , an oak and an elm </s>
********
<s> I could see that she was pretty , and from the gloss with which the light shone upon her dark dress I knew that it was a rich material </s>
	=> <s> I could see that she was pretty , and from the gloss with which the light shone upon her dark eyebrows I knew that it was a rich material </s>
********
<s> I could only move it slightly , and it was with the aid of one of the constables that I succeeded at last in carrying it to one side </s>
	=> <s> I could only move it slightly , and it was with the exception of one of the constables that I succeeded at last in carrying it to one side </s>
********
<s> They had each been stabbed , it seems , and the Hungarian police were of opinion that they had quarreled and had inflicted mortal injuries upon each other </s>
	=> <s> They had each been stabbed , it seems , and the Hungarian police were of opinion that they had eaten and had inflicted mortal injuries upon each other </s>
********
<s> The chances are that she would be as averse to its being seen by Mr. Godfrey Norton , as our client is to its coming to the eyes of his princess </s>
	=> <s> The chances are that she would be as averse to its being seen by Mr. Godfrey Norton , as our government is to its coming to the eyes of his princess </s>
********
<s> It came out upon the landing opposite to a second more ornamental stair which came up from the front hall </s>
	=> <s> It came out upon the mountain opposite to a second more ornamental stair which came up from the front hall </s>
********
<s> Holmes's voice sank as he answered </s>
	=> <s> Holmes's voice shot as he answered </s>
********
<s> Your mission today has justified itself , and yet I could almost wish that you had not left his side </s>
	=> <s> Your mission today has impressed itself , and yet I could almost wish that you had not left his side </s>
********
<s> And your address had been given me </s>
	=> <s> And your worship had been given me </s>
********
<s> Then you hand over to me three quarters of what you earn , and you keep the other quarter for yourself </s>
	=> <s> Then you hand over to me three quarters of what you dry , and you keep the other quarter for yourself </s>
********
<s> Add to that the length of neck and head , and you get a creature not much less than two feet long probably more if there is any tail </s>
	=> <s> Add to that the length of neck and head , and you get a bite not much less than two feet long probably more if there is any tail </s>
********
<s> His hair and whiskers were shot with gray , and his face was all crinkled and puckered like a withered apple </s>
	=> <s> His hair and whiskers were shot with gray , and his face was all crinkled and chattering like a withered apple </s>
********
<s> Someone in the next room had lit a dark-lantern </s>
	=> <s> Someone in the next room had covered a dark-lantern </s>
********
<s> He appeared to be deformed , for he carried his head low and walked with his knees bent </s>
	=> <s> He appeared to be honest , for he carried his head low and walked with his knees bent </s>
********
<s> The King may do what he will without hindrance from one whom he has cruelly wronged </s>
	=> <s> The King may do what he will without moving from one whom he has cruelly wronged </s>
********
<s> Mr. Alec stopped to see if he could help the dying man , and so the villain got clean away </s>
	=> <s> Mr. Alec stopped to see if he could help the dying man , and so the baby got clean away </s>
********
<s> When I thought of the heavy rains and looked at the gaping roof I understood how strong and immutable must be the purpose which had kept him in that inhospitable abode </s>
	=> <s> When I thought of the heavy step and looked at the gaping roof I understood how strong and immutable must be the purpose which had kept him in that inhospitable abode </s>
********
<s> To the logician all things should be seen exactly as they are , and to underestimate one's self is as much a departure from truth as to exaggerate one's own powers </s>
	=> <s> To the logician all things should be seen exactly as they are , and to maintain one's self is as much a departure from truth as to exaggerate one's own powers </s>
********
<s> There is no communication between them , but they all open out into the same corridor </s>
	=> <s> There is no difference between them , but they all open out into the same corridor </s>
********
<s> For the moment I could proceed no farther in that direction , but must turn back to that other clue which was to be sought for among the stone huts upon the moor </s>
	=> <s> For the moment I could proceed no farther in that direction , but must turn back to that other phrase which was to be sought for among the stone huts upon the moor </s>
********
<s> Otherwise your energy and attention must be dissipated instead of being concentrated </s>
	=> <s> Otherwise your energy and attention must be rewarded instead of being concentrated </s>
********
<s> She married an artist named Lyons , who came sketching on the moor </s>
	=> <s> She married an artist named Lyons , who came crawling on the moor </s>
********
<s> As we ran towards it the vague outline hardened into a definite shape </s>
	=> <s> As we ran towards it the vague outline folded into a definite shape </s>
********
<s> You must find your own ink , pens , and blotting-paper , but we provide this table and chair </s>
	=> <s> You must find your own ink , pens , and blotting-paper , but we owe this table and chair </s>
********
<s> Not a whisper , not a rustle , rose now from the dark figure over which we stooped </s>
	=> <s> Not a soldier , not a rustle , rose now from the dark figure over which we stooped </s>
********
<s> I was still rather raw over the deception which had been practised upon me , but the warmth of Holmes's praise drove my anger from my mind </s>
	=> <s> I was still rather drunk over the deception which had been practised upon me , but the warmth of Holmes's praise drove my anger from my mind </s>
********
<s> Mr. Alec , however , was a dangerous man to play games of that sort with </s>
	=> <s> Mr. Alec , however , was a clever man to play games of that sort with </s>
********
<s> The point under discussion was , how far any singular gift in an individual was due to his ancestry and how far to his own early training </s>
	=> <s> The point under discussion was , how far any singular gift in an individual was due to his pride and how far to his own early training </s>
********
<s> I don't think I ever drove faster , but the others were there before us </s>
	=> <s> I don't think I ever remembered faster , but the others were there before us </s>
********
<s> We found Holmes pacing up and down in the field , his chin sunk upon his breast , and his hands thrust into his trousers pockets </s>
	=> <s> We found Holmes pacing up and down in the field , his chin sunk upon his knees , and his hands thrust into his trousers pockets </s>
********
<s> You , of course , saw that everyone in the street was an accomplice </s>
	=> <s> You , of course , saw that scene in the street was an accomplice </s>
********
<s> I have tried to reconstruct it from the measurements </s>
	=> <s> I have tried to fling it from the measurements </s>
********
<s> I rushed towards it and pulled at the handle , but it was quite secure , and did not give in the least to my kicks and shoves 'Hullo' I yelled 'Hullo </s>
	=> <s> I rushed towards it and pulled at the handle , but it was quite empty , and did not give in the least to my kicks and shoves 'Hullo' I yelled 'Hullo </s>
********
<s> There are many men in London , you know , who , some from shyness , some from misanthropy , have no wish for the company of their fellows </s>
	=> <s> There are many men in London , you know , who , some from Greenwich , some from misanthropy , have no wish for the company of their fellows </s>
********
<s> In one of these wings the windows were broken and blocked with wooden boards , while the roof was partly caved in , a picture of ruin </s>
	=> <s> In one of these occasions the windows were broken and blocked with wooden boards , while the roof was partly caved in , a picture of ruin </s>
********
<s> It was the same good friend whose warning I had so foolishly rejected </s>
	=> <s> It was the same good friend whose warning I had so strangely rejected </s>
********
<s> It was a quiet , little , plainly furnished room , with a round table in the centre , on which several German books were scattered </s>
	=> <s> It was a quiet , little , plainly distinguished room , with a round table in the centre , on which several German books were scattered </s>
********
<s> He had a very dark , fearsome face , and a gleam in his eyes that comes back to me in my dreams </s>
	=> <s> He had a very dark , yellow face , and a gleam in his eyes that comes back to me in my dreams </s>
********
<s> He unwound the handkerchief and held out his hand </s>
	=> <s> He unwound the gun and held out his hand </s>
********
<s> In the last century , however , four successive heirs were of a dissolute and wasteful disposition , and the family ruin was eventually completed by a gambler in the days of the Regency </s>
	=> <s> In the last century , however , four successive prisoners were of a dissolute and wasteful disposition , and the family ruin was eventually completed by a gambler in the days of the Regency </s>
********
<s> On the table stood a dark-lantern with the shutter half open , throwing a brilliant beam of light upon the iron safe , the door of which was ajar </s>
	=> <s> On the table stood a log with the shutter half open , throwing a brilliant beam of light upon the iron safe , the door of which was ajar </s>
********
<s> I had risen from my seat and was knocking out the ashes of my pipe when I suddenly heard the clang of the bell </s>
	=> <s> I had risen from my seat and was knocking out the ashes of my tongue when I suddenly heard the clang of the bell </s>
********
<s> I had no opportunity to tell the baronet what I had learned about Mrs. Lyons upon the evening before , for Dr. Mortimer remained with him at cards until it was very late </s>
	=> <s> I had no objection to tell the baronet what I had learned about Mrs. Lyons upon the evening before , for Dr. Mortimer remained with him at cards until it was very late </s>
********
<s> In normal cases one can place a man in his true decade with tolerable confidence </s>
	=> <s> In normal cases one can place a man in his true operations with tolerable confidence </s>
********
<s> But the girl held true to me , and it seemed that I would have had her when the Mutiny broke out , and all hell was loose in the country </s>
	=> <s> But the girl held true to me , and it seemed that I would have had her when the moon broke out , and all hell was loose in the country </s>
********
<s> On the last occasion he had remarked that if my friend would only come with me he would be glad to extend his hospitality to him also </s>
	=> <s> On the last occasion he had discovered that if my friend would only come with me he would be glad to extend his hospitality to him also </s>
********
<s> A young man , very pale and worn , was lying upon a sofa near the open window , through which came the rich scent of the garden and the balmy summer air </s>
	=> <s> A young man , very pale and worn , was lying upon a sofa near the open window , through which came the rich spoils of the garden and the balmy summer air </s>
********
<s> The manor-house is , as I have already said , very old , and only one wing is now inhabited </s>
	=> <s> The manor-house is , as I have already said , very old , and only one object is now inhabited </s>
********
<s> Yet , with all this , you made me reveal what you wanted to know </s>
	=> <s> Yet , with all this , you made me thank what you wanted to know </s>
********
<s> A low moan had fallen upon our ears </s>
	=> <s> A low blow had fallen upon our ears </s>
********
<s> As to reward , my profession is its own reward ; but you are at liberty to defray whatever expenses I may be put to , at the time which suits you best </s>
	=> <s> As to reward , my profession is its own reward ; but you are at liberty to mention whatever expenses I may be put to , at the time which suits you best </s>
********
<s> Now , on the other side of this narrow wing runs the corridor from which these three rooms open </s>
	=> <s> Now , on the other side of this surprising wing runs the corridor from which these three rooms open </s>
********
<s> Matters were in this state , when a new development quite drew our attention away from the original mystery </s>
	=> <s> Matters were in this state , when a new development quite drew our attention away from the mere mystery </s>
********
<s> The unknown might be lurking there , or he might be prowling on the moor </s>
	=> <s> The unknown might be lurking there , or he might be inflicted on the moor </s>
********
<s> Thrust it into his pocket , most likely , never noticing that a corner of it had been left in the grip of the corpse </s>
	=> <s> Thrust it into his pocket , most likely , never noticing that a corner of it had been left in the shape of the corpse </s>
********
<s> As it is , I feel that young man's grip on my throat now , and the father has twisted my wrist round in the effort to get the paper out of my hand </s>
	=> <s> As it is , I feel that young man's grip on my throat now , and the father has twisted my cap round in the effort to get the paper out of my hand </s>
********
<s> It is most refreshingly unusual </s>
	=> <s> It is most frequently unusual </s>
********
<s> But sometimes a letter may be legible even when burned </s>
	=> <s> But sometimes a letter may be enjoyed even when burned </s>
********
<s> It was evident that a chisel or strong knife had been thrust in , and the lock forced back with it </s>
	=> <s> It was evident that a lord or strong knife had been thrust in , and the lock forced back with it </s>
********
<s> If you examine this scrap with attention you will come to the conclusion that the man with the stronger hand wrote all his words first , leaving blanks for the other to fill up </s>
	=> <s> If you examine this scrap with attention you will come to the conclusion that the man with the stronger hand wrote all his words first , leaving books for the other to fill up </s>
********
<s> I had stooped and was scraping at this to see exactly what it was when I heard a muttered exclamation in German and saw the cadaverous face of the colonel looking down at me </s>
	=> <s> I had studied and was scraping at this to see exactly what it was when I heard a muttered exclamation in German and saw the cadaverous face of the colonel looking down at me </s>
********
<s> The firemen had been much perturbed at the strange arrangements which they had found within , and still more so by discovering a newly severed human thumb upon a window-sill of the second floor </s>
	=> <s> The firemen had been much amused at the strange arrangements which they had found within , and still more so by discovering a newly severed human thumb upon a window-sill of the second floor </s>
********
<s> His clothes , his watch , and even his money were in his room , but the black suit which he usually wore was missing </s>
	=> <s> His clothes , his watch , and even his money were in his room , but the black cloud which he usually wore was missing </s>
********
<s> In order to negotiate with him they have to get an interpreter , and they pitch upon this Mr. Melas , having used some other one before </s>
	=> <s> In order to remonstrate with him they have to get an interpreter , and they pitch upon this Mr. Melas , having used some other one before </s>
********
<s> I should be very much obliged if you would slip your revolver into your pocket </s>
	=> <s> I should be very much obliged if you would appreciate your revolver into your pocket </s>
********
<s> A meeting of the Guild had been held that evening at eight , and Mrs. Barclay had hurried over her dinner in order to be present at it </s>
	=> <s> A meeting of the Guild had been held that evening at eight , and Mrs. Barclay had ridden over her dinner in order to be present at it </s>
********
<s> I expect that within an hour matters will come to a head </s>
	=> <s> I expect that within an hour Lucy will come to a head </s>
********
<s> I noticed her pass , but I had no special reason for watching her </s>
	=> <s> I noticed her pass , but I had no special reason for disliking her </s>
********
<s> I shall call with the King to-morrow , and with you , if you care to come with us </s>
	=> <s> I shall call with the King summer , and with you , if you care to come with us </s>
********
<s> His secret was a shameful one , and he could not bring himself to divulge it </s>
	=> <s> His secret was a shameful one , and he could not bring himself to forget it </s>
********
<s> Miss Hunter screamed and shrunk against the wall at the sight of him , but Sherlock Holmes sprang forward and confronted him </s>
	=> <s> Miss Hunter screamed and supported against the wall at the sight of him , but Sherlock Holmes sprang forward and confronted him </s>
********
<s> Their reason for choosing so unusual an hour for a consultation was obviously to insure that there should be no other patient in the waiting-room </s>
	=> <s> Their reason for choosing so unusual an hour for a battle was obviously to insure that there should be no other patient in the waiting-room </s>
********
<s> When a woman thinks that her house is on fire , her instinct is at once to rush to the thing which she values most </s>
	=> <s> When a woman thinks that her house is on fire , her investigation is at once to rush to the thing which she values most </s>
********
<s> There was a chair just under the lamp , and the elderly man motioned that I should sit in it </s>
	=> <s> There was a chair just under the lamp , and the elderly man discovered that I should sit in it </s>
********
<s> We could see the marks in the wood where it had been pushed in </s>
	=> <s> We could see the Negroes in the wood where it had been pushed in </s>
********
<s> You can imagine my exultation , Watson , when within two inches of my peg I saw a conical depression in the ground </s>
	=> <s> You can imagine my virtue , Watson , when within two inches of my peg I saw a conical depression in the ground </s>
********
<s> The lamps had been lit , but the blinds had not been drawn , so that I could see Holmes as he lay upon the couch </s>
	=> <s> The lamps had been disturbed , but the blinds had not been drawn , so that I could see Holmes as he lay upon the couch </s>
********
<s> I am a light sleeper , and it has awakened me </s>
	=> <s> I am a light sleeper , and it has commanded me </s>
********
<s> In an instant it was obvious that we had at last come upon the true place , and that we had not been the only people to visit the spot recently </s>
	=> <s> In an instant it was impossible that we had at last come upon the true place , and that we had not been the only people to visit the spot recently </s>
********
<s> Already I was unable to stand erect , when my eye caught something which brought a gush of hope back to my heart </s>
	=> <s> Already I was unable to stand erect , when my eye caught something which brought a pair of hope back to my heart </s>
********
<s> Have your pistol ready in case we should need it </s>
	=> <s> Have your honour ready in case we should need it </s>
********
<s> He dived his arm down to the bottom of the chest , and brought up a small wooden box with a sliding lid , such as children's toys are kept in </s>
	=> <s> He dived his arm down to the bottom of the mountains , and brought up a small wooden box with a sliding lid , such as children's toys are kept in </s>
********
<s> During my school-days I had been intimately associated with a lad named Percy Phelps , who was of much the same age as myself , though he was two classes ahead of me </s>
	=> <s> During my absence I had been intimately associated with a lad named Percy Phelps , who was of much the same age as myself , though he was two classes ahead of me </s>
********
<s> It might or might not bite the occupant , perhaps she might escape every night for a week , but sooner or later she must fall a victim </s>
	=> <s> It might or might not disdain the occupant , perhaps she might escape every night for a week , but sooner or later she must fall a victim </s>
********
<s> He has nerve and he has knowledge </s>
	=> <s> He has yelled and he has knowledge </s>
********
<s> And Holmes' fears came to be realised , for from that day to this no word has ever been heard either of the beautiful woman , the sinister German , or the morose Englishman </s>
	=> <s> And Holmes' worst came to be realised , for from that day to this no word has ever been heard either of the beautiful woman , the sinister German , or the morose Englishman </s>
********
<s> I can distinctly remember that as we did so there came three chimes from a neighboring clock </s>
	=> <s> I can distinctly remember that as we did so there came three centuries from a neighboring clock </s>
********
<s> I should not wish a smarter assistant , Mr. Holmes ; and I know very well that he could better himself and earn twice what I am able to give him </s>
	=> <s> I should not wish a smarter duke , Mr. Holmes ; and I know very well that he could better himself and earn twice what I am able to give him </s>
********
<s> With much labour we separated them and carried him , living but horribly mangled , into the house </s>
	=> <s> With much labour we separated them and carried him , living but horribly intelligent , into the house </s>
********
<s> No one could pass these shutters if they were bolted </s>
	=> <s> No one could pass these letters if they were bolted </s>
********
<s> When you raise your cry of fire , it will be taken up by quite a number of people </s>
	=> <s> When you recall your cry of fire , it will be taken up by quite a number of people </s>
********
<s> The butler was standing very pale but very collected before us </s>
	=> <s> The butler was standing very tall but very collected before us </s>
********
<s> Nor would it be entirely incompatible with most of the words overhead </s>
	=> <s> Nor would it be entirely covered with most of the words overhead </s>
********
<s> I shall stand behind this crate , and do you conceal yourselves behind those </s>
	=> <s> I shall stand behind this crate , and do you conceal nobody behind those </s>
********
<s> The letter had , as I said , been burned and it was not all legible </s>
	=> <s> The letter had , as I said , been closed and it was not all legible </s>
********
<s> But I see that the enemy's preparations have gone so far that we cannot risk the presence of a light </s>
	=> <s> But I see that the enemy's bullets have gone so far that we cannot risk the presence of a light </s>
********
<s> I paid the man and hurried into the church </s>
	=> <s> I paid the man and rode into the church </s>
********
<s> Sherlock Holmes had listened to this long narrative with an intentness which showed me that his interest was keenly aroused </s>
	=> <s> Sherlock Holmes had listened to this long narrative with an emphasis which showed me that his interest was keenly aroused </s>
********
<s> Such an excursion could not be kept secret </s>
	=> <s> Such an earthquake could not be kept secret </s>
********
<s> I fainted when it was done , and I think that I must have been senseless for a long time </s>
	=> <s> I fainted when it was done , and I think that I must have been mistaken for a long time </s>
********
<s> Then he threw himself down into the chair opposite , and drew up his knees until his fingers clasped round his long , thin shins </s>
	=> <s> Then he threw himself down into the chair opposite , and drew up his spirits until his fingers clasped round his long , thin shins </s>
********
<s> It was certainly more roomy than the ordinary four-wheeled disgrace to London , and the fittings , though frayed , were of rich quality </s>
	=> <s> It was certainly more roomy than the ordinary four-wheeled disgrace to London , and the rivers , though frayed , were of rich quality </s>
********
<s> I had let myself go , and was hanging by the hands to the sill , when his blow fell </s>
	=> <s> I had let myself go , and was hailed by the hands to the sill , when his blow fell </s>
********
<s> Then Sherlock Holmes pulled down from the shelf one of the ponderous commonplace books in which he placed his cuttings </s>
	=> <s> Then Sherlock Holmes tumbled down from the shelf one of the ponderous commonplace books in which he placed his cuttings </s>
********
<s> I should like , for example , to see how far the windows of the bedrooms command the front </s>
	=> <s> I should like , for example , to see how far the knowledge of the bedrooms command the front </s>
********
<s> Holmes waved away the compliment , though his smile showed that it had pleased him </s>
	=> <s> Holmes waved away the turf , though his smile showed that it had pleased him </s>
********
<s> They all agreed that only two voices were to be heard , those of Barclay and of his wife </s>
	=> <s> They all agreed that only two chairs were to be heard , those of Barclay and of his wife </s>
********
<s> A coachman and two maids form the staff of servants </s>
	=> <s> A coachman and two policemen form the staff of servants </s>
********
<s> My attention was speedily drawn , as I have already remarked to you , to this ventilator , and to the bell-rope which hung down to the bed </s>
	=> <s> My attention was speedily mollified , as I have already remarked to you , to this ventilator , and to the bell-rope which hung down to the bed </s>
********
<s> That frightful cry turned the blood to ice in my veins </s>
	=> <s> That frightful cry turned the blood to remain in my veins </s>
********
<s> We had reached the same crowded thoroughfare in which we had found ourselves in the morning </s>
	=> <s> We had reached the same crowded sepulchre in which we had found ourselves in the morning </s>
********
<s> Finally he took the bell-rope in his hand and gave it a brisk tug </s>
	=> <s> Finally he took the key in his hand and gave it a brisk tug </s>
********
<s> Suddenly , however , as I ran , a deadly dizziness and sickness came over me </s>
	=> <s> Suddenly , however , as I ran , a curious dizziness and sickness came over me </s>
********
<s> He had ceased to moan as we laid him down , and a glance showed me that for him at least our aid had come too late </s>
	=> <s> He had ceased to moan as we laid him down , and a glance showed me that for him at least our enemies had come too late </s>
********
<s> Ferguson appeared to be a morose and silent man , but I could see from the little that he said that he was at least a fellow-countryman </s>
	=> <s> Ferguson appeared to be a prince and silent man , but I could see from the little that he said that he was at least a fellow-countryman </s>
********
<s> I realized it as I drove back and noted how hill after hill showed traces of the ancient people </s>
	=> <s> I realized it as I smiled back and noted how hill after hill showed traces of the ancient people </s>
********
<s> In the evening I put on my waterproof and I walked far upon the sodden moor , full of dark imaginings , the rain beating upon my face and the wind whistling about my ears </s>
	=> <s> In the evening I put on my waterproof and I walked far upon the nearest moor , full of dark imaginings , the rain beating upon my face and the wind whistling about my ears </s>
********
<s> I keep it only to safeguard myself , and to preserve a weapon which will always secure me from any steps which he might take in the future </s>
	=> <s> I keep it only to hide myself , and to preserve a weapon which will always secure me from any steps which he might take in the future </s>
********
<s> Don't you dare to meddle with my affairs </s>
	=> <s> Don't you dare to fight with my affairs </s>
********
<s> He was unable , however , to make his way in , and the maids were too distracted with fear to be of any assistance to him </s>
	=> <s> He was unable , however , to make his way in , and the stars were too distracted with fear to be of any assistance to him </s>
********
<s> The other was a very small , dark fellow , with his hat pushed back and several packages under his arm </s>
	=> <s> The other was a very small , dark fellow , with his hat pushed back and several eunuchs under his arm </s>
********
<s> We had a small scene this morning after breakfast </s>
	=> <s> We had a small yard this morning after breakfast </s>
********
<s> It is to recompense you for any inconvenience that we are paying to you , a young and unknown man , a fee which would buy an opinion from the very heads of your profession </s>
	=> <s> It is to befall you for any inconvenience that we are paying to you , a young and unknown man , a fee which would buy an opinion from the very heads of your profession </s>
********
<s> Then I put out my hand and was about to shake the man , who was still sleeping soundly , when a bell over his head rang loudly , and he woke with a start </s>
	=> <s> Then I put out my hand and was about to shake the man , who was still burning soundly , when a bell over his head rang loudly , and he woke with a start </s>
********
<s> It appears to be a fragment torn from a larger sheet </s>
	=> <s> It appears to be a fragment suffered from a larger sheet </s>
********
<s> Between ourselves , I think Mr. Holmes had not quite got over his illness yet </s>
	=> <s> Between ourselves , I think Mr. Holmes had not quite got over his glasses yet </s>
********
<s> We had occasion some months ago to strengthen our resources and borrowed for that purpose 30,000 napoleons from the Bank of France </s>
	=> <s> We had occasion some months ago to strengthen our honour and borrowed for that purpose 30,000 napoleons from the Bank of France </s>
********
<s> The boards round and the panelling of the walls were of brown , worm-eaten oak , so old and discoloured that it may have dated from the original building of the house </s>
	=> <s> The boards round and the shadow of the walls were of brown , worm-eaten oak , so old and discoloured that it may have dated from the original building of the house </s>
********
<s> Let me pass , I say' He dashed her to one side , and , rushing to the window , cut at me with his heavy weapon </s>
	=> <s> Let me pass , I say' He bade her to one side , and , rushing to the window , cut at me with his heavy weapon </s>
********
<s> It was a wonderfully silent house </s>
	=> <s> It was a mere silent house </s>
********
<s> I tell you that he is a clever and dangerous man </s>
	=> <s> I tell you that he is a delicate and dangerous man </s>
********
<s> He was a dashing , jovial old soldier in his usual mood , but there were occasions on which he seemed to show himself capable of considerable violence and vindictiveness </s>
	=> <s> He was a dashing , jovial old soldier in his usual mood , but there were occasions on which he seemed to show himself capable of considerable tact and vindictiveness </s>
********
<s> He was acutely uneasy if he were absent from her for a day </s>
	=> <s> He was acutely uneasy if he were falling from her for a day </s>
********
<s> I found him much troubled over the disappearance of his little spaniel </s>
	=> <s> I found him much reading over the disappearance of his little spaniel </s>
********
<s> There is a comfortable sofa </s>
	=> <s> There is a Methodist sofa </s>
********
<s> The back door was open , and as he came to the foot of the stairs he saw two men wrestling together outside </s>
	=> <s> The back door was open , and as he came to the foot of the forest he saw two men wrestling together outside </s>
********
<s> A maid rushed across and threw open the window </s>
	=> <s> A maid talked across and threw open the window </s>
********
<s> It was one of the main arteries which conveyed the traffic of the City to the north and west </s>
	=> <s> It was one of the main arteries which surrounded the traffic of the City to the north and west </s>
********
<s> I was instantly aroused , and , with the two footmen , started off at once in search of the missing girl </s>
	=> <s> I was instantly asleep , and , with the two footmen , started off at once in search of the missing girl </s>
********
<s> So far I could follow their actions as if I had actually seen them </s>
	=> <s> So far I could lose their actions as if I had actually seen them </s>
********
<s> A ventilator is made , a cord is hung , and a lady who sleeps in the bed dies </s>
	=> <s> A ventilator is made , a battle is hung , and a lady who sleeps in the bed dies </s>
********
<s> He was tractable enough , though his son was a perfect demon , ready to blow out his own or anybody else's brains if he could have got to his revolver </s>
	=> <s> He was tractable enough , though his son was a perfect knight , ready to blow out his own or anybody else's brains if he could have got to his revolver </s>
********
<s> On reaching Scotland Yard , however , it was more than an hour before we could get Inspector Gregson and comply with the legal formalities which would enable us to enter the house </s>
	=> <s> On reaching Scotland Yard , however , it was more than an hour before we could get Inspector Gregson and comply with the legal obstacles which would enable us to enter the house </s>
********
<s> All my unspoken instincts , my vague suspicions , suddenly took shape and centred upon the naturalist </s>
	=> <s> All my unspoken instincts , my blind suspicions , suddenly took shape and centred upon the naturalist </s>
********
<s> It was several miles off , but I could distinctly see a small dark dot against the dull green and gray </s>
	=> <s> It was several miles off , but I could scarcely see a small dark dot against the dull green and gray </s>
********
<s> We laid him upon the drawing-room sofa , and having dispatched the sobered Toller to bear the news to his wife , I did what I could to relieve his pain </s>
	=> <s> We laid him upon the drawing-room windows , and having dispatched the sobered Toller to bear the news to his wife , I did what I could to relieve his pain </s>
********
<s> But incredulity and indifference were evidently my strongest cards </s>
	=> <s> But incredulity and indifference were evidently my drinking cards </s>
********
<s> Admiration was , I repeat , the first impression </s>
	=> <s> Admiration was , I shouted , the first impression </s>
********
<s> Left his lodgings at ten o'clock at night , and has not been heard of since </s>
	=> <s> Left his finger at ten o'clock at night , and has not been heard of since </s>
********
<s> What is to me a means of livelihood is to him the merest hobby of a dilettante </s>
	=> <s> What is to me a means of amusement is to him the merest hobby of a dilettante </s>
********
<s> Sitting in the billiard-room I more than once heard the sound of voices raised , and I had a pretty good idea what the point was which was under discussion </s>
	=> <s> Sitting in the summer I more than once heard the sound of voices raised , and I had a pretty good idea what the point was which was under discussion </s>
********
<s> Within there was a small corridor , which ended in a very massive iron gate </s>
	=> <s> Within there was a small corridor , which ended in a very French iron gate </s>
********
<s> For a moment or two I sat breathless , hardly able to believe my ears </s>
	=> <s> For a moment or two I sat reading , hardly able to believe my ears </s>
********
<s> But a singular interruption brought us to a standstill </s>
	=> <s> But a singular fortune brought us to a standstill </s>
********
<s> Then , when I flash a light upon them , close in swiftly </s>
	=> <s> Then , when I wrote a light upon them , close in swiftly </s>
********
<s> I am sorry to have interrupted you </s>
	=> <s> I am sorry to have killed you </s>
********
<s> We had hardly reached the hall when we heard the baying of a hound , and then a scream of agony , with a horrible worrying sound which it was dreadful to listen to </s>
	=> <s> We had hardly reached the hall when we heard the click of a hound , and then a scream of agony , with a horrible worrying sound which it was dreadful to listen to </s>
********
<s> Sorry to see that you've had the British workman in the house </s>
	=> <s> Sorry to see that you've had the British Museum in the house </s>
********
<s> Even after I became suspicious , I found it hard to think evil of such a dear , kind old clergyman </s>
	=> <s> Even after I became suspicious , I found it hard to think highly of such a dear , kind old clergyman </s>
********
<s> His life was irregular , but in one respect he was regularity itself </s>
	=> <s> His life was empty , but in one respect he was regularity itself </s>
********
<s> He was all right , as far as money went , but in his deposit he had given her what looked like a bad florin </s>
	=> <s> He was all right , as far as money went , but in his pocket he had given her what looked like a bad florin </s>
********
<s> The bottle was downstairs in my laboratory , so leaving my patient seated in his chair , I ran down to get it </s>
	=> <s> The bottle was interested in my laboratory , so leaving my patient seated in his chair , I ran down to get it </s>
********
<s> Suddenly a door opened at the other end of the passage , and a long , golden bar of light shot out in our direction </s>
	=> <s> Suddenly a door opened at the other end of the castle , and a long , golden bar of light shot out in our direction </s>
********
<s> It was a perfect day , with a bright sun and a few fleecy clouds in the heavens </s>
	=> <s> It was a lucky day , with a bright sun and a few fleecy clouds in the heavens </s>
********
<s> I fastened the rod on end , marked out the direction of the shadow , and measured it </s>
	=> <s> I fastened the rod on end , marked out the direction of the shadow , and taught it </s>
********
<s> An elderly man with a red face and shaking limbs came staggering out at a side door </s>
	=> <s> An elderly man with a red face and shaking limbs came pouring out at a side door </s>
********
<s> The lash , however , was curled upon itself and tied so as to make a loop of whipcord </s>
	=> <s> The lash , however , was thrown upon itself and tied so as to make a loop of whipcord </s>
********
<s> About nine o'clock the light among the trees was extinguished , and all was dark in the direction of the Manor House </s>
	=> <s> About nine o'clock the light among the trees was warm , and all was dark in the direction of the Manor House </s>
********
<s> Had he observed a carriage the night before waiting for me </s>
	=> <s> Had he observed a vision the night before waiting for me </s>
********
<s> Then I walked across to the window , hoping that I might catch some glimpse of the country-side , but an oak shutter , heavily barred , was folded across it </s>
	=> <s> Then I walked across to the window , hoping that I might catch some glimpse of the country-side , but an oak sapling , heavily barred , was folded across it </s>
********
<s> But the evening has brought a breeze with it </s>
	=> <s> But the evening has brought a fault with it </s>
********
<s> I am only , of course , giving you the leading results now of my examination of the paper </s>
	=> <s> I am only , of course , giving you the leading spirits now of my examination of the paper </s>
********
<s> Suddenly , amid all the hubbub of the gale , there burst forth the wild scream of a terrified woman </s>
	=> <s> Suddenly , amid all the glow of the gale , there burst forth the wild scream of a terrified woman </s>
********
<s> An hour and half had elapsed before the Inspector returned alone </s>
	=> <s> An hour and half had arrived before the Inspector returned alone </s>
********
<s> The object which had caught his eye was a small dog lash hung on one corner of the bed </s>
	=> <s> The object which had caught his eye was a small dog lash dragged on one corner of the bed </s>
********
399 of 1040 correct
Overall average: 38.3653846153846%
dev: 39.2307692307692%
test: 37.5%
```
