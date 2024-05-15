

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


if __name__ == "__main__":
 # Texto de exemplo
    Europe()
    #EUA()