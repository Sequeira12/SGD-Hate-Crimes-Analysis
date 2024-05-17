

import csv

lib = {"Anti-Black or African American":"Racist and xenophofic hate crime",
       "Anti-Asian":"Racist and xenophofic hate crime",
       "Anti-American Indian or Alaska Native":"Racist and xenophofic hate crime",
       "Anti-White":"Racist and xenophofic hate crime",
       "Anti-Hispanic or Latino":"Racist and xenophofic hate crime",
       "Anti-Lesbian (Female)":"Anti-LGBTI hate crime",
       "Anti-Transgender":"Gender-based hate crime",
       "Anti-Islamic (Muslim)":"Anti-Muslim hate crime",
       "Anti-Other Race/Ethnicity/Ancestry":"Racist and xenophofic hate crime",
       "Anti-Gay (Male)":"Anti-LGBTI hate crime",
       "Anti-Jewish":"Racist and xenophofic hate crime",
       "Anti-Bisexual":"Racist and xenophofic hate crime",
       "Anti-Multiple Races":"Racist and xenophofic hate crime",
       "Anti-Other Religion":"Other hate crime based on religion or belief",
       "Anti-Other Christian":"Anti-Christian hate crime",
        "Anti-Catholic":"Anti-Christian hate crime",
        "Anti-Physical Disability":"Disability hate crime",
        "Anti-Sikh":"Racist and xenophofic hate crime",
        "Anti-Bisexual":"Anti-LGBTI hate crime",
        "Anti-Protestant":"Racist and xenophofic hate crime",
        "Anti-Native Hawaiian or Other Pacific Islander":"Racist and xenophofic hate crime",
        "Anti-Gender Non-Conforming":"Gender-based hate crime",
        "Anti-Multiple Religions":"Other hate crime based on religion or belief",
        "Anti-Female":"Gender-based hate crime",
        "Anti-Mental Disability":"Disability hate crime",
        "Anti-Native Hawaiian or Other Pacific Islander":"Racist and xenophofic hate crime",
       "Anti-Eastern Orthodox (Russian":"Racist and xenophofic hate crime",
       "Anti-Church of Jesus Christ":"Anti-Christian hate crime",
       "Anti-Arab":"Racist and xenophofic hate crime",
       "Anti-Lesbian":"Anti-LGBTI hate crime",
       "Anti-Heterosexual":"Gender-based hate crime",
       "Anti-Male":"Gender-based hate crime",
       "Anti-Hindu":"Other hate crime based on religion or belief",
       "Anti-Atheism/Agnosticism":"Other hate crime based on religion or belief",
       "Anti-Jehovah's Witness":"Other hate crime based on religion or belief",
       "Anti-Buddhist":"Other hate crime based on religion or belief",
       }

liboffenses = {
    "Intimidation":"Threats",
    "Destruction/Damage/Vandalism of Property":"Attacks against property",
    "Simple Assault":"Violent attacks against people",
    "Aggravated Assault":"Violent attacks against people",
    "All Other Larceny":"Attacks against property",
    "Shoplifting":"Attacks against property",
    "Rape":"Violent attacks against people",
    "Kidnapping/Abduction":"Violent attacks against people",
    "Sexual Assault With An Object":"Violent attacks against people",
    "Murder and Nonnegligent Manslaughter":"Violent attacks against people",
    "Motor Vehicle Theft":"Attacks against property",
    "Theft From Motor Vehicle":"Attacks against property",
    "Fondling":"Violent attacks against people",
    "Purse-snatching":"Attacks against property",
    "Stolen Property Offenses":"Attacks against property",
    "Drug/Narcotic Violations":"Violent attacks against people",
    "Burglary/Breaking & Entering":"Attacks against property",
}

libpopulation_eua = {
     
"0":"Alaska",
"2":"Alabama","3":"Arkansas","4":"Arizona","7":"California","10":"Colorado","33":"North Dakota","32":"North Carolina","11":"Connecticut",
"12":"District of Columbia","13":"Delaware","14":"Florida","15":"Georgia","16":"Hawaii","17":"Iowa","18":"Idaho","19":"Illinois","20":"Indiana","21":"Kansas",
"22":"Kentucky","23":"Louisiana","24":"Massachusetts","25":"Maryland","26":"Maine","27":"Michingan","28":"Minnesota","29":"Missouri","30":"Mississippi",
"31":"Montana","34":"Nebraska","35":"New Hampshire","36":"New Jersey","37":"New Mexico","38":"Nevada","39":"New York","40":"Ohio","41":"Oklahoma",
"42":"Oregon","43":"Pennsylvania","44":"Rhode Island","45":"South Carolina", "46":"South Dakota", "47":"Tennessee", "48":"Texas","49":"Utah","50":"Virginia",
"51":"Vermont","52":"Washington","53":"Wisconsin","54":"West Virginia",
 "55":"Wyoming"
}


libgdp = {
    "AKPCPI":"Alaska", "ALPCPI":"Alabama","ARPCPI":"Arkansas","AZPCPI":"Arizona","CAPCPI":"California","COPCPI":"Colorado","CTPCPI":"Connecticut","DCPCPI":"District of Columbia","DEPCPI":"Delaware","FLPCPI":"Florida","GAPCPI":"Georgia","HIPCPI":"Hawaii","IAPCPI":"Iowa","IDPCPI":"Idaho","ILPCPI":"Illinois","INPCPI":"Indiana","KSPCPI":"Kansas","KYPCPI":"Kentucky","LAPCPI":"Louisiana","MAPCPI":"Massachusetts","MDPCPI":"Maryland","MEPCPI":"Maine","MIPCPI":"Michingan","MNPCPI":"Minnesota","MOPCPI":"Missouri","MSPCPI":"Mississippi","MTPCPI":"Montana","NCPCPI":"North Carolina","NDPCPI":"North Dakota","NEPCPI":"Nebraska","NHPCPI":"New Hampshire","NJPCPI":"New Jersey","NMPCPI":"New Mexico","NVPCPI":"Nevada","NYPCPI":"New York","OHPCPI":"Ohio","OKPCPI":"Oklahoma","ORPCPI":"Oregon","PAPCPI":"Pennsylvania","RIPCPI":"Rhode Island","SCPCPI":"South Carolina","SDPCPI":"South Dakota","TNPCPI":"Tennessee","TXPCPI":"Texas","UTPCPI":"Utah","VAPCPI":"Virginia","VTPCPI":"Vermont","WAPCPI":"Washington","WIPCPI":"Wisconsin","WVPCPI":"West Virginia","WYPOP_20081219":"Wyoming"
}

def EUA():

    FileNameClean = "OriginalDataSet/hate_crime_EUA.csv"
    FileName = "DataSet/hate_crime.csv"
    count = 0
    with open(FileName, 'r') as f, open(FileNameClean,"a") as FW:
            for linha in f:
                if count > 0:
                    reader = csv.reader([linha], delimiter=',', quotechar='"')
                    dados_completos = next(reader)
                    incident_id = dados_completos[0]
                    country = "United States of America"
                    state_name = dados_completos[7]
                    incident_date = dados_completos[12]
                    listdate = incident_date.split("-")
                    year = listdate[0]
                    month = listdate[1]
                    bias_desc = dados_completos[-4]
                    bias = bias_desc.split(",")
                    multiple_bias = bias[0].split(";")
                    offense_name = dados_completos[-7]
                    multiple_offense = offense_name.split(";")
                    offense_name = multiple_offense[0]
                    newlinha = incident_id  + "," + country + "," + state_name + "," + year + "," + month + ","
                    helper = newlinha
  
                    if offense_name in liboffenses:
                        for b in multiple_bias:                        
                            if b != ' Group' and b != "Unknown (offender's motivation not known)":
                                helper +=  lib[b] + "," + liboffenses[offense_name] + "\n"
                                FW.write(helper)
                                helper = newlinha

                else:
                  info = "incident_id,country,state_name,year,month,bias_desc,offense_name\n"
                  FW.write(info)
                  print("Working..\n")
                    
                count+=1
    print("Clean file United States")


def JoinEUAandEurope():
    FileNameClean = "OriginalDataSet/hate_crime_clean.csv"
    FileName = "OriginalDataSet/hate_crime_EUA.csv"
    count = 0
    with open(FileName, 'r') as f, open(FileNameClean,"a") as FW:
            for linha in f:
                if count > 0:
                    FW.write(linha)

                else:
                    info = "incident_id,country,state_name,year,month,bias_desc,offense_name\n"
                    FW.write(info)
                    print("Working..\n")
                count+=1
    FileName = "OriginalDataSet/hate_crime_europeClean.csv"
    count = 0
    with open(FileName, 'r') as f, open(FileNameClean,"a+") as FW:
            for linha in f:
                if count > 0:
                    FW.write(linha)
                else:
                    print("Workin2")
                    count+=1



                



def Europe():

    FileNameClean = "OriginalDataSet/hate_crime_europeClean.csv"
    FileName = "DataSet/hate_crime_europe.csv"
    count = 0
    with open(FileName, 'r') as f, open(FileNameClean,"a") as FW:
            for linha in f:
                if count > 0:
                    reader = csv.reader([linha], delimiter=',', quotechar='"')
                    dados_completos = next(reader)
                    date = dados_completos[0]
                    divide = date.split("-")
                    year = divide[0]
                    if(len(divide) > 1 ):
                        month = divide[1]
                    else:
                        month = ""
                    country = dados_completos[1]
                    continent = "Europe"
                    bias_desc = dados_completos[2]
                    bias = bias_desc.split(",")
                    offense = dados_completos[3]
                    typeoffense = offense.split(",")
                    for b in bias: 
                        for o in typeoffense:    
                            helper = str(count) + "," +  continent + "," +  country + "," + year + "," + month + "," +  b.strip() + "," + o.strip() + "\n"
                            FW.write(helper)
                    
                
                else:
                    info = "incident_id,country,state_name,year,month,bias_desc,offense_name\n"
                    FW.write(info)
                    print("Working...\n")
                    
                count+=1
    print("Clean file Europe")






def Clean():

    FileNameClean = "DataSet/hate_crime_europe.csv"
    FileName = "DataSet/hcrw_incidents_all-report.csv"
    count = 0
    with open(FileName, 'r') as f, open(FileNameClean,"a") as FW:
            for linha in f:
                if count > 0:
                    reader = csv.reader([linha], delimiter=',', quotechar='"')
                    dados_completos = next(reader)
                    
                    if dados_completos[1] != 'United States of America':
                        FW.write(linha)
                    count+=1
                else:
                    info = "Date,Country,Bias motivations,Type of incident,Source,Description\n"
                    FW.write(info)
                    count+=1




def cleanPopulation():
    FileNameAreaEurope = "DataSet/PopulationDataSets/totalareaEurope.csv"
    FileNameClean = "OriginalDataSet/population.csv"
    FileName = "DataSet/PopulationDataSets/populationEUA.csv"
    FileNameEurope = "DataSet/PopulationDataSets/populationEurope.csv"
    FileNameEuropeGDP = "DataSet/gdpEurope.csv"
    FileNameEUAGDP = "DataSet/gdpEua.csv"
    count = 0
    helper = {}
    helperEurope = {}
    areaEUA = {}
    gdpEurope = {}
    helperGdp = {}
    with open(FileName, 'r') as f:
        for linha in f:
            if count > 0:
                reader = csv.reader([linha], delimiter='	', quotechar='"')
                dados_completos = next(reader)
                
                for num in range(len(dados_completos)+1):
                    value = num 
                    if str(value) in libpopulation_eua.keys():
                        if libpopulation_eua[str(value)] in helper.keys():
                            
                            helper[libpopulation_eua[str(value)]].append(dados_completos[num+1].replace(".", ""))
                        else:
                            helper[libpopulation_eua[str(value)]] = [dados_completos[num+1].replace(".", "")]
                                
            else:
                reader = csv.reader([linha], delimiter='	', quotechar='"')
                dados_completos = next(reader)
               
                count+=1
    count = 0    
    with open(FileNameEurope, 'r') as f:
        for linha in f:
            if count > 0:
                reader = csv.reader([linha], delimiter=',', quotechar='"')
                dados_completos = next(reader)
                if dados_completos[2] != 'World' and dados_completos[2] != 'Gambia, The':
                    helperEurope[dados_completos[2]] = [dados_completos[8],dados_completos[9],dados_completos[10],dados_completos[11],dados_completos[12],dados_completos[13],dados_completos[14]]
            else:
               
                count+=1



    FileNameAreaUSA = "DataSet/PopulationDataSets/totalareaEUA.csv"
    count = 0
    with open(FileNameAreaUSA,"r") as f:
        for linha in f:
            reader = csv.reader([linha], delimiter='	', quotechar='"')
            dados_completos = next(reader)
 
            if count >= 1:
                area = dados_completos[3].replace(",", "")
              
                local = dados_completos[0].strip()
               
                areaEUA[local] = area
              
            count+=1
   

    areaEurope = {}
    with open(FileNameAreaEurope,"r") as f:
        for linha in f:
            reader = csv.reader([linha], delimiter=',', quotechar='"')
            dados_completos = next(reader)
            
            areaEurope[dados_completos[0].strip()] = dados_completos[2].strip()
    
    with open(FileNameEuropeGDP,"r") as f:
        for linha in f:
            reader = csv.reader([linha], delimiter=',', quotechar='"')
            dados_completos = next(reader)

            gdpEurope[dados_completos[0]] = dados_completos[-9:-2]
    gpdhelper = {}
    count = 0
    gpdfinal = {}
    with open(FileNameEUAGDP, 'r') as f:
        for linha in f:
            if count > 0:
                reader = csv.reader([linha], delimiter='	', quotechar='"')
                dados_completos = next(reader)
                
                for chaves,values in gpdhelper.items():
                    if values not in gpdfinal:
                        gpdfinal[values] = [str(dados_completos[chaves])]  # Initialize with a list containing the first value
                    else:
                        gpdfinal[values].append(str(dados_completos[chaves]))
            else:
                reader = csv.reader([linha], delimiter='	', quotechar='"')
                dados_completos = next(reader)
         
                for num in range(1,len(dados_completos)):
                    if libgdp.get(dados_completos[num]) != None:
                        gpdhelper[num] =libgdp.get(dados_completos[num])
                count+=1

    with open(FileNameClean, 'w') as FW:
        out = "EUAvsEUROPE,state_name,pop2016,pop2017,pop2018,pop2019,pop2020,pop2021,pop2022,totalarea,gdp2016,gdp2017,gdp2018,gdp2019,gdp2020,gdp2021,gdp2022\n"
        FW.write(out)
        for chave, valor in helper.items():
            out = "United States of America" + "," + chave 
            for val in valor:
                out += "," + val 
            
           
            out += "," + str(areaEUA.get(chave)) 

            lista = gpdfinal[chave]
            for num in lista:
                out += "," + num
            out += "\n"
            
            FW.write(out)
        
        for chave, valor in helperEurope.items():
            out = "Europe" + "," + chave 
            for val in valor:
                out += "," + val 
            out += "," + str(areaEurope.get(chave))
           
            lista = gdpEurope[chave]
            for num in lista:
                out += "," + num
            out += "\n"
            FW.write(out)


def cleanPopulationArea():
    FileName = "DataSet/PopulationDataSets/totalareaEurope.csv"
    areaEurope = {}
    with open(FileName,"r") as f:
        for linha in f:
            reader = csv.reader([linha], delimiter=',', quotechar='"')
            dados_completos = next(reader)
            
           
            areaEurope[dados_completos[0].strip()] = dados_completos[2].strip()
    print(areaEurope)
          
                
            
if __name__ == "__main__":
 # Texto de exemplo
    cleanPopulation()
    #EUA()