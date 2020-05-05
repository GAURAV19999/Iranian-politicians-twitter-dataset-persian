#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('git clone https://github.com/twintproject/twint.git')
get_ipython().run_line_magic('cd', 'twint')
get_ipython().system('pip3 install . -r requirements.txt')


# In[ ]:


get_ipython().run_line_magic('cd', 'twint')


# In[ ]:


import twint
import os 

tweets_file_path = "./tweet"
def export_tweets(username):
    if os.path.isfile(tweets_file_path):
        return

    c = twint.Config()

    c.Username = username
    c.Store_csv = True
    c.Format = "Username: {username} |  Date: {date} {time}"
    c.Output = tweets_file_path
    twint.run.Search(c)


# In[ ]:


import re
import pandas as pd 


def remove_emoji(tweet):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u'\U00010000-\U0010ffff'
                               u"\u200d"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\u3030"
                               u"\ufe0f"
                               u"\u2069"
                               u"\u2066"
                               u"\u2068"
                               u"\u2067"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', tweet)




def clean_tweet(tweet):

    tweet = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})\S*', '', tweet)
    tweet = re.sub(r'@\w*', '', tweet)
    tweet = re.sub(r'[a-zA-Z]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'_', ' ', tweet)

    tweet = remove_emoji(tweet)


    return tweet


# In[ ]:


def scraping_tweets(username):
    export_tweets(username)

    data = pd.read_csv(tweets_file_path+"/tweets.csv")
    data= data['tweet'].apply(lambda x: clean_tweet(x))
    
    with open("tweets_data.txt", 'a+') as tw:
        for i in range(len(data)):
            tw.write(data[i])
            tw.write("\n")
    


# In[ ]:


twitter_account = [
                   "Khamenei_fa",
                   "Rouhani_ir",
                   "Eshaq_jahangiri",
                   "Dr_Vaezi",
                   "MB_Nobakht",
                   "azarijahromi",
                   "sm_bathaei",
                   "shariatmadari_m",
                   "BijanZanganeh",
                   "Alirabiei_ir",
                   "S_A_Salehi",
                   "ebtekarm_ir",
                   "rezarahmanii",
                   "jamshid_ansari",
                   "msoltanifar_ir",
                   "mounesan_ir",
                   "JZarif",
                   "amirnazemy",
                   "fatahi_ir",
                   "S_Pakseresht",
                   "araghchi",
                   "barari_ir",
                   "tondgouyan",
                   "sadjadb",
                   "shohre_naseri",
                   "HaniyehSamei",
                   "saeed272727",
                   "RVahidianS",
                   "shahla_osouli",
                   "torabianIR",
                   "alilarijani",
                   "ir_aref",
                   "alimotahari_ir",
                   "mah_sadeghi",
                   "behroznemati",
                   "SoroushAbolfazl",
                   "AliSari1397",
                   "mahkiaee",
                   "kolivand98",
                   "jalali_kazem",
                   "mehdi_mahdavian",
                   "mirmeysamasad",
                   "zahrasaei_ir",
                   "Badamchi_Media",
                   "AK_Hosseinzadeh",
                   "mazaniahmad",
                   "S_FatemeHoseini",
                   "a_rahimi_mp",
                   "ParvanehMafi",
                   "elyashazrati",
                   "Nahid_Tajedin",
                   "oladghobad_f",
                   "shirankhorasani",
                   "P_Salahshouri",
                   "saeidiftm",
                   "mahdi_sheykh",
                   "Zahedi_ir",
                   "ahmadamirabadi1",
                   "Drjalilrahimi",
                   "Ghheidari",
                   "TayebehSiavash",
                   "Khojasteh_ir",
                   "Jafarzadeh_ir",
                   "AliNajafi_ir",
                   "k_karampour",
                   "A_Yarmohammadi",
                   "ParsaeiB",
                   "drmdehghan",
                   "ahadazadikhah",
                   "HassanNooroozi",
                   "ahmadhematii",
                   "homayonhashemi",
                   "yagob_shivyari",
                   "yousefnejad_ir",
                   "KarimiGhodousi",
                   "zonnour",
                   "HajiDeligani",
                   "j_mohebinia",
                   "sfaridmousavi",
                   "moh_rafsanjani?lang=fa",
                   "ArvinBahare",
                   "salari_mohamad",
                   "shrbamani",
                   "HoseinNaghashi",
                   "AfshinHabibzade",
                   "AMasjedjamei",
                   "hojjat_nazari",
                   "aminimedia_ir",
                   "AliEtaMedia",
                   "MjHaghshenas",
                   "zahra_nezhad",
                   "N_Khodakarami",
                   "ElhamFakhari",
                   "hasanrasouli",
                   "HKhalilAbadi",
                   "farahani52",
                   "MMirlohii",
                   "sadrazamnouri",
                   "milani_arash",
                   "Bagheri_org",
                   "ghasemsoleimane",
                   "Azizjafaari_ir",
                   "mesbahyazdi_ir",
                   "rafsanjani_fa",
                   "Khatamimedia",
                   "Kadkhodaee_ir",
                   "HaddadAdel_ir",
                   "ir_rezaee",
                   "mb_ghalibaf",
                   "mowlaverdi",
                   "DrSaeedJalili",
                   "DrAboutalebi",
                   "Ahmadinejad_fa",
                   "Zarghami_ez",
                   "Smmirsalim",
                   "pirouzhanachi",
                   "raisi_org",
                   "ar_moezi",
                   "hesamodin1",
                   "baeidinejad",
                   "NiknamSepanta",
                   "ZahraAhmadipour",
                   "Nahavandian_ir",
                   "alamolhoda_",
                   "qasemian_ir",
                   "kabi_abbas",
                   "Panahian_IR",
                   "Hn_jalali",
                   "sadighi_ir",
                   "Qarati_ir",
                   "Ahmadkhatami_ir",
                   "HassanKhomeini",
                   "alia_peyvandi",
                   "Fassih_F",
                   "AshrafBrujerdi",
                   "alishakourirad",
                   "v_seif",
                   "Dastjerdi_ir",
                   "hojatmirzaei",
                   "hajmajid47",
                   "ZarirNegintaji",
                   "fazelmaybodi",
                   "1alpr",
                   "alirezaghanadan",
                   "hoseinipouya",
                   "HasankarimiG",
                   "mjnanakar",
                   "Shahin_Arpanahi",
                   "seyedmajidsadr2",
                   "EsmaeiliParviz",
                   "mohsenmirdamadi",
            
]


# In[ ]:



for acc in twitter_account:
    scraping_tweets(acc)

