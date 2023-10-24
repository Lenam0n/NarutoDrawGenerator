import random

class Char:
    def __init__(self):

        nameMale = (
            'Jun',
            'Van',
            'Seiei',
            'Phoenix' ,
            'Ikki',
            'Kawaki',
            'Kenichi',
            'Yoruichi',
            'Itachi',
            'Ume',
            'Subaru' ,
            'Sumeragi',
            'Albion',
            'Taiki',
            'Kaguya',
            'Goku',
            'Kaib',
            'Belo' ,
            'Tadashi',
            'Hiroyu',
            'Kotoko',
            'Fushi',
            'Hotaru',
            'Kokoro',
            'Bao' ,
            'Huang',
            'Nephrite',
            'Kenta',
            'Midori',
            'Hideki',
            'Daisuke',
            'Tanjiro' ,
            'Kamado',
            'Masumi',
            'Shun',
            'Bankuro',
            'Hideki', 
            'Gohan', 
            'Ken', 
            'Miyuki'
        )
        
        nameFemale = (  
            'Arisa',
            'Hotaru',
            'Acilia', 
            'Betty',
            'Temari', 
            'Banshee',
            'Mei',
            'Setsuna',
            'Jiro', 
            'Shinobu', 
            'Rin', 
            'Teru',
            'Mikami', 
            'Sayuri', 
            'Rio', 
            'Kuro', 
            'Asami', 
            'Shuji', 
            'Aika', 
            'Shizuko', 
            'Velvet', 
            'Norio', 
            'Susumu', 
            'Chiharu', 
            'Kaori', 
            'Nori', 
            'Chieko', 
            'Kyo', 
            'Momiji', 
            'Juvia', 
            'Rie', 
            'Shinn', 
            'Asuka', 
            'Kin', 
            'Minoru', 
            'Masayuki', 
            'Nel', 
            'Tien', 
            'Yua', 
            'Mikio'
        )
        
        nameFamily = (
            'Satō',
            'Suzuki',
            'Takahashi',
            'Tanaka',
            'Watanabe',
            'Itō',
            'Yamamoto',
            'Nakamura',
            'Kobayashi',
            'Katō',
            'Uchiha',
            'Hirano',
            'Kitade',
            'Mizuki',
            'Nishikawa',
            'Ishihara',
            'Matsumoto',
            'Suzuki',
            'Takeuchi',
            'Tanemura',
            'Watanabe',
            'Uke',
            'Amuro',
            'Hinamori',
            'Koda',
            'Ogata',
            'Isana',
            'Shibasaki',
            'Shiobara',
            'Miwa',
            'Yoshizumi',
            'Shinohara',
            'Shima',
            'Mio',
            'Moro',
            'Momono',
            'Monozaki',
            'Ozaki',
            'Furukawa',
            'Ibuki',
            'Tanaka',
            'Ichinose',
            'Yamada',
            'Nekono',
            'Shiina',
            'Miura',
            'Komura',
            'Takagi',
            'Toyama',
            'Sakai',
            'Kiyohara',
            'Miyagi',
            'Ohya',
            'Masaya',
            'Nanao',
            'Yoshinagi',
            'Naegi',
            'Ayatsuji',
            'Takarai'
        )
        
        naruto_Dorf_select = (
            'Kirigakure',
            'Konohagakure',
            'Kumogakure',
            'Iwagakure',
            'Sunagakure',
            'Amegakure',
            'Ishigakure',
            'Kusagakure',
            'Otogakure',
            'Shimogakure',
            'Takigakure',
            'Tanigakure',
            'Yugakure'
        ) 
        
        Waffen = (
            None,
            'Kusarigama',
            'Sai',
            'Kunai',
            'Shuriken',
            'Kanabō',
            'Katana',
            'Schlagringe',
            'Bogen',
            'Schriftrolle',
            'Dolch',
            'Speer',
            'Bisento',
            'Daishō',
            'Kyoketsu-shoge',
            'Fächer',
            'Draht'
        ) 
        
        genders = (
            'Male',
            'Female'
        )
        
        anzahl_Elemente = (
            1,
            2,
            3,
            4,
            5
        )
        
        alleElemente = [
            'Wind',
            'Blitz',
            'Erde',
            'Wasser',
            'Feuer'
        ]
        
        besonderheit = (
            'None',
            'Sharingan',
            'Mangekyo Sharingan',
            'Ethernal - Mangekyo Sharingan',
            'Rinne Sharingan',
            'Byakugan',
            'Rinnegan',
            'Jogan',
            'Tenseigan'
            )
        
        ElementKombi = {
            '2Elemente': 
             {
                'Feuer&Wasser' : 'Siedungs',
                'Erde&Wasser' : 'Holz',
                'Blitz&Wasser' : 'Sturm',
                'Wasser&Wind' : 'Eis',
                'Erde&Feuer' : 'Lava',
                'Blitz&Feuer' : '',
                'Feuer&Wind' : 'Hitze',
                'Blitz&Erde' : 'Explosion',
                'Erde&Wind' : 'Magnet',
                'Blitz&Wind' : '',
                
        },'3Elemente':
             {
                'Feuer&Wasser&Wind' : '',
                'Erde&Wasser&Wind' : '',
                'Blitz&Wasser&Wind' : '',
                'Erde&Feuer&Wasser' : '',
                'Blitz&Feuer&Wasser' : '',
                'Blitz&Erde&Wasser' : '', 
                'Erde&Feuer&Wind' : 'Staub',
                'Blitz&Feuer&Wind' : '',
                'Blitz&Erde&Feuer' : '',
                'Blitz&Erde&Wind' : '',
                
        },'4Elemente':
             {
                'Blitz&Feuer&Wasser&Wind' : '',
                'Blitz&Erde&Wasser&Wind' : '',
                'Erde&Feuer&Wasser&Wind' : '',
                'Blitz&Erde&Feuer&Wind' : '',
                
        },'5Elemente':
             {
                'Blitz&Erde&Feuer&Wasser&Wind' : '',
        }}

        
        April = Juni = September = November = 30
        Januar = März = Mai = Juli = August = Oktober = Dezember = 31 
        Februar = 28
        
        Months = {
                'allMonths': [Januar,Februar,März,April,Mai,Juni,Juli,August,September,Oktober,November,Dezember],
                            'allMonthsString': ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'],
                'Months30':  ['April','Juni','September','November'],
                'Months31':  ['Januar','März','Mai','Juli','August','Oktober','Dezember']
            }

        
        besonderheit_Oods_1 = (87, 5, 0.3, 0.2, 0.1, 4, 0.4, 1, 1)
        Element_Oods_1 = (90.099, 8.89, 1, 0.01, 0.001)
        Weapon_Oods_1 = (23.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5)

        
        def shuffle(a):
            val = random.randrange(0,len(a))
            result = a[val]
            return result

        def elements(a):
            Chars_Element = []
            multibleEle = []
            if a == 1:
                Chars_Element = [shuffle(alleElemente)]
            if a == 2:
                Chars_Element = [shuffle(alleElemente)]
                multibleEle = alleElemente.copy()
                multibleEle.remove(str(Chars_Element[0]))
                Chars_Element.append(shuffle(multibleEle))
            if a == 3:
                Chars_Element = [shuffle(alleElemente)]
                multibleEle = alleElemente.copy()
                multibleEle.remove(str(Chars_Element[0]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[1]))
                Chars_Element.append(shuffle(multibleEle))
        
            if a == 4:
                Chars_Element = [shuffle(alleElemente)]
                multibleEle = alleElemente.copy()
                multibleEle.remove(str(Chars_Element[0]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[1]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[2]))
                Chars_Element.append(shuffle(multibleEle))
            if a == 5:
                Chars_Element = [shuffle(alleElemente)]
                multibleEle = alleElemente.copy()
                multibleEle.remove(str(Chars_Element[0]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[1]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[2]))
                Chars_Element.append(shuffle(multibleEle))
                multibleEle.remove(str(Chars_Element[3]))
                Chars_Element.append(shuffle(multibleEle))
                
            return(Chars_Element)
                
        def SumForJutsu():
            a = []

            def sum_to_n(n, size, limit=None):
                """Produce all lists of `size` positive integers in decreasing order
                that add up to `n`."""
                
                if size == 1:
                    yield [n]
                    return
                if limit is None:
                    limit = n
                start = (n + size - 1) // size
                stop = min(limit, n - size + 1) + 1
                for i in range(start, stop):
                    for tail in sum_to_n(n - i, size - 1, i):
                        yield [i] + tail
                        
            for partition in sum_to_n(100, 3,100):
                a.append(partition)
        
            random.shuffle(a)
            random.shuffle(a[1])
            return a[1]
        
        
        
        
        def Checker(db,Oods,draws):
            a = random.choices(db, weights = Oods, k=draws)
            return a[0]
            
        def nameGen(a):
            if a == genders[0]:
                b = shuffle(nameMale)
                return b
            else:
                b = shuffle(nameFemale)
                return b
        
        def ElementKombiCheck():    
            def ElementKombination():
                self.Element.sort()
                if self.numElements == 1:
                    return None
                elif self.numElements == 2:
                    a = self.Element[0] + '&' + self.Element[1]
                    b = str(self.numElements) + 'Elemente'
                    return a , b
                elif self.numElements == 3:
                    a = self.Element[0] + '&' + self.Element[1] + '&' + self.Element[2]
                    b = str(self.numElements) + 'Elemente'
                    return a , b
                elif self.numElements == 4:
                    a = self.Element[0] + '&' + self.Element[1] + '&' + self.Element[2] + '&' + self.Element[3]
                    b = str(self.numElements) + 'Elemente'
                    return a , b
                elif self.numElements == 5:
                    a = self.Element[0] + '&' + self.Element[1] + '&' + self.Element[2] + '&' + self.Element[3] + '&' + self.Element[4]
                    b = str(self.numElements) + 'Elemente'
                    return a , b
                else:
                    return None

            
            
            
            abc = ElementKombination()
            if abc != None:
                a = abc[0]
                b = abc[1]
                return ElementKombi[b][a] + 'versteck'
            else:
                return self.Element[0] + 'versteck'
                
                    

        def TalentAjustments():
            if self.Weapon != None and 'Schriftrolle' and 'Fächer' and 'Bogen':
                self.Tai += 20

            if self.numElements == 2:
                self.Nin += 7
            elif self.numElements == 3:
                self.Nin += 35
            elif self.numElements == 4:
                self.Nin += 50
                
            if self.Besonderheit != None:
                self.Tai += 15
                self.Gen += 15
                self.Nin += 15
                
            
            while self.Nin > 100:
                self.Nin -= 10
            while self.Nin < 40:
                self.Nin += 10

            while self.Tai > 100:
                self.Tai -= 10
            while self.Tai < 40:
                self.Tai += 10
                
            if self.Tai > 90 and self.Gen or self.Nin > 80:
                self.Gen -= 10
                self.Nin -= 10
                
            if self.Besonderheit == None:
                self.Tai -= 10
                self.Gen -= 10
                self.Nin -= 10
                
            if self.Besonderheit == 'Sharingan':
                self.Gen += 20
                while self.Gen > 100:
                    self.Gen -= 8
                while self.Gen < 72:
                    self.Gen += 10
                
            while self.Tai > 90 and self.Besonderheit == None :
                self.Tai -= 5
            
            while self.Gen > 85 and self.Besonderheit == None :
                self.Gen -= 10
            
            while self.Nin > 80 and self.Besonderheit == None :
                self.Nin -= 10

            if self.numElements == 5:
                self.Nin = 101
                self.Tai += 15
                self.Gen += 15


        def statsRandomizer(attribute,reps,range,lowest):
            '''
            First Value : Median Value \n
            Second Value : Times of Reps \n
            Third Value : Range of Changes \n
            Fouth Value : Lowest possible Value \n
            '''
            def rangeRandomizer():
                a = bool(random.randrange(0,2))
                if a == False: 
                    a = -1
                else:
                    a = 1
                return a
            i = 1
            changed_val = 0
            changed_val = attribute + rangeRandomizer() * random.randrange(range)
            while i < reps:
                changed_val = changed_val + rangeRandomizer() * random.randrange(range)
                while changed_val < lowest:
                    changed_val = attribute + rangeRandomizer() * random.randrange(range)
                i += 1
            return changed_val
        def statsWrapper(b,c,y):
            '''
            First Value : Times of Reps \n
            Second Value : Range of Changes \n
            Third Value : height or weight \n
            Fouth Value : 
            '''
            if y == 'height':
                if self.Gender == 'Female':
                    a = 165
                    d = 152
                else:
                    a = 178
                    d = 165
            elif y == 'weight':
                if self.Gender == 'Female':
                    if self.age <= 16:
                        a = 50
                        d = 38
                    elif self.age > 16:
                        a = 72
                        d = 61
                elif self.Gender == 'Male':
                    if self.age < 16:
                        a = 57
                        d = 42
                    elif self.age >= 16:
                        a = 87
                        d = 74
                    
            rdmVal = statsRandomizer(a,b,c,d)
            
            if y == 'height':
                rdmVal = rdmVal / 100
                rdmVal = str(rdmVal) + 'm'
                
            elif y == 'weight':
                rdmVal = str(rdmVal) + 'kg'
            
            return rdmVal
        def sternzeichenCheck(d,m,mI,y):
            monate = Months['allMonthsString'].index(m)
            i = -1
            a = 0
            while i < monate: 
                a += Months['allMonths'][i]
                i += 1

            dateadd = a
            
            if dateadd >= 1 and dateadd <= 20:
                sternzeichen = 'Steinbock'
            elif dateadd >= 21 and dateadd <= 50:
                sternzeichen = 'Wassermann'
            elif dateadd >= 51 and dateadd <= 79:
                sternzeichen = 'Fische'
            elif dateadd >= 80 and dateadd <= 110:
                sternzeichen = 'Widder'
            elif dateadd >= 111 and dateadd <= 140:
                sternzeichen = 'Stier'
            elif dateadd >= 141 and dateadd <= 172:
                sternzeichen = 'Zwillinge'
            elif dateadd >= 173 and dateadd <= 203:
                sternzeichen = 'Krebs'
            elif dateadd >= 204 and dateadd <= 235:
                sternzeichen = 'Löwe'
            elif dateadd >= 236 and dateadd <= 266:
                sternzeichen = 'Jungfrau'
            elif dateadd >= 267 and dateadd <= 296:
                sternzeichen = 'Waage'
            elif dateadd >= 297 and dateadd <= 326:
                sternzeichen = 'Skorpion'
            elif dateadd >= 327 and dateadd <= 355:
                sternzeichen = 'Schütze'
            elif dateadd >= 356 and dateadd <= 365:
                sternzeichen = 'Steinbock'

            return sternzeichen
            
        def bday():
            day = random.randint(0,31)
            m = random.randint(0,11)
            year = today - self.age
        
            month = Months['allMonthsString'][m]


            if day < 10:
                day = str(0) + str(day)
            if day == 31:
                a = random.randint(0,len(Months['Months31']) - 1)
                month = Months['Months31'][a]    
            #i = 0
            #ifschaltjahr
            #while i < self.age:
            #    i += 1
                
                
            #if ifschaltjahr %400 != 0: return
            #else:
            #    if ifschaltjahr %4 == 0 and ifschaltjahr %100 !=0:
                    
            #    elif ifschaltjahr %100 == 0 and ifschaltjahr %400 !=0:

                
            #schaltjahr abfrage
            
            b = str(day) + '/' + str(month) + '/' + str(year)
            return b , day , month , m , year

        
     
        today = 2022
        self.Gender = shuffle(genders)
        self.Name = nameGen(self.Gender)
        self.age = statsRandomizer(17,5,4,13)
        bdaypass = bday()
        self.birthday = bdaypass[0]
        self.sternzeichen = sternzeichenCheck(bdaypass[1],bdaypass[2],bdaypass[3],bdaypass[4])
        self.height = statsWrapper(6,2,'height')
        self.weight = statsWrapper(6,2,'weight')
        self.Family = shuffle(nameFamily)
        self.Dorf = shuffle(naruto_Dorf_select)
        self.numElements = Checker(anzahl_Elemente,Element_Oods_1,1)
        self.Element = elements(self.numElements)
        self.Besonderheit = Checker(besonderheit,besonderheit_Oods_1,1)   
        self.Weapon = Checker(Waffen,Weapon_Oods_1,1)
        self.Tai = SumForJutsu()[0]
        self.Gen = SumForJutsu()[1]
        self.Nin = SumForJutsu()[2]
        self.Versteck = ElementKombiCheck()
            
        TalentAjustments()
    def Char_print(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print(f'Name:            {self.Name} {self.Family}\nGeschlecht:      {self.Gender}\nAge:             {self.age}\nBrithday:        {self.birthday}\nSternzeichen:    {self.sternzeichen}\nHeight:          {self.height}\nWeight:          {self.weight}\nDorf:            {self.Dorf}\n')
        print('_______________________________________________\n')
        print(f'Elementbegabung:  {self.Element}\nElementversteck:  {self.Versteck}\nDojutsu:          {self.Besonderheit}\nWaffe:            {self.Weapon}\n')
        print('_______________________________________________\n')
        print(f'Jutsu Talentierung: \n Tai-Jutsu:  {self.Tai}%\n Gen-Jutsu:  {self.Gen}%\n Nin-Jutsu:  {self.Nin}%\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        


char1 = Char()
#char2 = Char()
#char3 = Char()
#char4 = Char()
#char5 = Char()
#char6 = Char()
#char7 = Char()
#char8 = Char()

char1.Char_print()
#char2.Char_print()
#char3.Char_print()
#char4.Char_print()
#char5.Char_print()
#char6.Char_print()
#char7.Char_print()
#char8.Char_print()

#print(char1.age)
#print(char2.age)
#print(char3.age)
#print(char4.age)
#print(char5.age)
#print(char6.age)
#print(char7.age)
#print(char8.age)

