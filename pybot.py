import praw

reddit = praw.Reddit(client_id = 'FhCZAoozfF60nQ', client_secret = 'qT_sfXUwNI5IIVgoqSAgpEKaWUo', user_agent = 'rougndraft', username = 'BrightnessShallanVin', password = 'Waterband')

# reddit = create_reddit_object()

pennystocks_subred = reddit.subreddit('pennystocks')
wallstreetbets_subred = reddit.subreddit('wallstreetbets')
thewallstreet_subred = reddit.subreddit('thewallstreet')
tradevol_subred = reddit.subreddit('tradevol') 

subs = [pennystocks_subred, wallstreetbets_subred]

for subreddit in subs:
    hot = subreddit.hot(limit=5)
    new = subreddit.new(limit=5)
    top = subreddit.top(limit=5)    
    for post in hot:
        # if post.selftext contains a_stock_syms[i]:
        #     add it to a count dict
        print(f'{post.subreddit_name_prefixed} \n {post.title} \n at: {post.shortlink} \n {post.selftext} \n upvotes: {post.ups} \n downvotes: {post.downs} \n # of comments: {post.num_comments} \n score:{post.score} \n')
        for comment in post.comments:
            if not 'MoreComments':
                print(comment.body)
        #    if comment.body contains a_stock_sims[i]:
        #     add them to a count dict
        #     find highest counts
        #     return count and mention
            

# contr = subreddit.controversial(limit=5)
# gild = subreddit.gilded(limit=5)


    

a_stock_syms = ['AAN','AAP','AAT','AB','ABB','ABBV','ABC','ABEV','ABG','ABM','ABML','ABR','ABR-A','ABR-B','ABR-C','ABT','ACA','ACB','ACC','ACCO','ACEL','ACH','ACI','ACM','ACN','ACN.U','ACND','ACP','ACRE','ACV','ADC','ADCT','ADM','ADNT','ADSW','ADT','ADX','AEB','AEFC','AEG','AEL','AEL-A','AEL-B','AEP-C','AER','AER','AFB','AFC','AFG','AFGB','AFGC','AFGD','AFGH','AFI','AFL','AFT','AG','AGCO','AGD','AGI','AGM','AGM-A','AGM-C','AGM-D','AGM-E','AGM-F','AGM.A','AGO','AGO-B','AGO-E','AGO-F','AGR','AGRO','AGS','AGX','AHS','AHH','AHH-A','AHL-C','AHL-D','AHL-E','AHT','AHT-D','AHT-F','AHT-G','AHT-H','AHT-I','AI-B','AI-C','AIC','AIF','AIG','AIG-A','AIG.W','AIN','AIO','AIT','AIV','AIW','AIZ','AIZP','AJG','AJRD','AJX','AJXA','AKO.A','AKO.B','AKR','AL','AL-A','ALB','ALC','ALG','ALI-A','ALI-B','ALI-E','ALK','ALL','ALL-B','ALL-G','ALL-H','ALL-I','ALL-Y','ALLE','ALP-Q','ALSN','ALT.W','ALTG','ALU.U','ALU.W','ALUS','ALV','ALX','AMB.W','AMBC','AMC','AMCR','AME','AMG','AMH','AMH-D','AMH-E','AMH-F','AMH-G','AMH-H','AMK','AMN','AMOV','AMPY','AMRC','AMRX','AMT','AMX','ANET','ANF','ANH','ANH-A','ANH-B','ANH-C','ANTM','AOD','AON','AON.U','AOS','APAM','APD','APH','APHA','APLE','APO','APO-A','APO-B','APRN','APT-A','APTS','APTV','AQN','AQNA','AQNB','AQUA','AR','ARA','ARC','ARCH','ARCO','ARD','ARDC','ARE-A','ARES','ARG-A','ARGD','ARGO','ARI','ARK','ARLO','ARMK','ARNC','AROC','ARR','ARR-C','ARW','ASA','ASB','ASB-C','ASB-D','ASB-E','ASB-F','ASC','ASG','ASGI','ASGN','ASIX','ASR','ASX','ATC-D','ATC-E','ATC-G','ATC-H','ATC-I','ATCO','ATEN','ATGE','ATH','ATH-A','ATH-B','ATH-C','ATHM','ATI','ATKR','ATO','ATR','ATTO','ATUS','ATV','AU','AUY','AVAL','AVB','AVD','AVK','AVLR','AVNS','AVNT','AVT-A','AVTR','AVY','AVYA','AWF','AWI','AWK','AWP','AX','AXL','AXO','AXP','AXR','AXS','AXS-E','AXTA','AYI','AYX','AZEK','AZN','AZO','AZRE','AZUL','AZZ']

b_stock_syms = ['B','BA','BABA','BAC','BAC-A','BAC-B','BAC-C','BAC-E','BAC-K','BAC-L','BAC-M','BAC-N','BAF','BAH','BAK','BAN-D','BAN-E','BANC','BAP','BAX','BB','BBAR','BBD','BBDC','BBDO','BBF','BBK','BBL','BBN','BBU','BBVA','BBW','BBX','BBY','BC','BC-A','BC-B','BC-C','BCC','BCE','BCEI','BCH','BCO','BCS','BCSF','BCX','BDC','BDJ','BDN','BDX','BDXB','BEDU','BEKE','BEN','BEP','BEP-A','BEPC','BERY','BF.A','BFAM','BFK','BFO','BFS','BFS-D','BFS-E','BFT.U','BFY','BFZ','BG','BGB','BGH','BGIO','BGR','BGS','BGSF','BGT','BGX','BGY','BH','BH.A','BHC','BHE','BHK','BHLB','BHP','BHR','BHR-B','BHR-D','BHV','BHVN','BIF','BIO.B','BIP','BIPC','BITA','BJ','BK','BK-C','BKD','BKE','BKI','BKK','BKN','BKR','BKT','BKU','BLD','BLE','BLK','BLL','BLW','BLX','BMA','BME','BMEZ','BMI','BML-G','BML-H','BML-J','BML-L','BMO','BMR.U','BMR.W','BMRG','BMY','BMY.P','BNED','BNS','BNY','BOE','BOH','BOOT','BORR','BP','BPMP','BPT','BQH','BR','BRBR','BRC','BRFS','BRK.A','BRK.B','BRMK','BRT','BRX','BSA','BSAC','BSBR','BSD','BSE','BSIG','BSL','BSM','BSMX','BSN.U','BST','BSTZ','BSX','BSX-A','BTA','BTE','BTI','BTO','BTT','BTU','BTZ','BUD','BUI','BURL','BV','BVN','BW','BWA','BWG','BWXT','BX','BXC','BXG','BXMT','BXMX','BXP','BXP-B','BXS-A','BYM','BZH','BZM']


    