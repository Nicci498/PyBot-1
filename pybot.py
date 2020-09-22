import praw

reddit = praw.Reddit(client_id = 'FhCZAoozfF60nQ', client_secret = 'qT_sfXUwNI5IIVgoqSAgpEKaWUo', user_agent = 'rougndraft', username = 'BrightnessShallanVin', password = 'Waterband')

# reddit = create_reddit_object()

pennystocks_subred = reddit.subreddit('pennystocks')
wallstreetbets_subred = reddit.subreddit('wallstreetbets')
thewallstreet_subred = reddit.subreddit('thewallstreet')
tradevol_subred = reddit.subreddit('tradevol') 

subs = [pennystocks_subred, wallstreetbets_subred]

for subreddit in subs:
    hot = subreddit.hot(limit = 5)
    new = subreddit.new(limit = 5)
    top = subreddit.top(limit = 5, time_filter = 'week')    
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
    for post in new:
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
    for post in top:
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

arr = ['1', '2', '3', '4']

AStockSym = ['AACG', 'AACQ', 'AACQU', 'AACQW', 'AAL', 'AAME', 'AAOI', 'AAON', 'AAPL', 'AAWW', 'AAXJ', 'AAXN', 'ABCB', 'ABEO', 'ABIO', 'ABMD', 'ABTX', 'ABUS', 'ACAD', 'ACAM', 'ACAMU', 'ACAMW', 'ACBI', 'ACCD', 'ACER', 'ACEVU', 'ACGL', 'ACGLO', 'ACGLP', 'ACHC', 'ACHV', 'ACIA', 'ACIU', 'ACIW', 'ACLS', 'ACMR', 'ACNB', 'ACOR', 'ACRS', 'ACRX', 'ACST', 'ACT', 'ACTG', 'ACWI', 'ACWX', 'ADAP', 'ADBE', 'ADES', 'ADI', 'ADIL', 'ADILW', 'ADMA', 'ADMP', 'ADMS', 'ADP', 'ADPT', 'ADRE', 'ADRO', 'ADSK', 'ADTN', 'ADTX', 'ADUS', 'ADVM', 'ADXN', 'ADXS', 'AEGN', 'AEHR', 'AEIS', 'AEMD', 'AERI', 'AESE', 'AEY', 'AEYE', 'AEZS', 'AFIB', 'AFIN', 'AFINP', 'AFMD', 'AFYA', 'AGBA', 'AGBAR', 'AGBAU', 'AGBAW', 'AGEN', 'AGFS', 'AGIO', 'AGLE', 'AGMH', 'AGNC', 'AGNCM', 'AGNCN', 'AGNCO', 'AGNCP', 'AGRX', 'AGTC', 'AGYS', 'AGZD', 'AHCO', 'AHPI', 'AIA', 'AIH', 'AIHS', 'AIKI', 'AIMC', 'AIMT', 'AINV', 'AIQ', 'AIRG', 'AIRR', 'AIRT', 'AIRTP', 'AIRTW', 'AKAM', 'AKBA', 'AKCA', 'AKER', 'AKRO', 'AKTS', 'AKTX', 'AKU', 'AKUS', 'ALAC', 'ALACR', 'ALACU', 'ALACW', 'ALBO', 'ALCO', 'ALDX', 'ALEC', 'ALGN', 'ALGT', 'ALIM', 'ALJJ', 'ALKS', 'ALLK', 'ALLO', 'ALLT', 'ALNA', 'ALNY', 'ALOT', 'ALPN', 'ALRM', 'ALRN', 'ALRS', 'ALSK', 'ALT', 'ALTA', 'ALTM', 'ALTR', 'ALTY', 'ALVR', 'ALXN', 'ALXO', 'ALYA', 'AMAG', 'AMAL', 'AMAT', 'AMBA', 'AMCA', 'AMCI', 'AMCIU', 'AMCIW', 'AMCX', 'AMD', 'AMED', 'AMEH', 'AMGN', 'AMHC', 'AMHCU', 'AMHCW', 'AMKR', 'AMNB', 'AMOT', 'AMPH', 'AMRB', 'AMRH', 'AMRHW', 'AMRK', 'AMRN', 'AMRS', 'AMSC', 'AMSF', 'AMSWA', 'AMTB', 'AMTBB', 'AMTD', 'AMTI', 'AMTX', 'AMWD', 'AMYT', 'AMZN', 'ANAB', 'ANAT', 'ANCN', 'ANDA', 'ANDAR', 'ANDAU', 'ANDAW', 'ANDE', 'ANGI', 'ANGL', 'ANGO', 'ANIK', 'ANIP', 'ANIX', 'ANNX', 'ANPC', 'ANSS', 'ANTE', 'ANY', 'AOSL', 'AOUT', 'APA', 'APDN', 'APEI', 'APEN', 'APEX', 'APHA', 'API', 'APLS', 'APLT', 'APM', 'APOG', 'APOP', 'APOPW', 'APPF', 'APPN', 'APPS', 'APRE', 'APTO', 'APTX', 'APVO', 'APWC', 'APXT', 'APXTU', 'APXTW', 'APYX', 'AQB', 'AQMS', 'AQST', 'ARAV', 'ARAY', 'ARCB', 'ARCC', 'ARCE', 'ARCT', 'ARDS', 'ARDX', 'AREC', 'ARGX', 'ARKR', 'ARLP', 'ARNA', 'AROW', 'ARPO', 'ARQT', 'ARTL', 'ARTLW', 'ARTNA', 'ARTW', 'ARVN', 'ARWR', 'ARYA', 'ARYB', 'ARYBU', 'ARYBW', 'ASET', 'ASFI', 'ASLN', 'ASMB', 'ASML', 'ASND', 'ASPS', 'ASPU', 'ASRT', 'ASRV', 'ASRVP', 'ASTC', 'ASTE', 'ASUR', 'ASYS', 'ATAX', 'ATCX', 'ATCXW', 'ATEC', 'ATEX', 'ATHE', 'ATHX', 'ATIF', 'ATLC', 'ATLO', 'ATNI', 'ATNX', 'ATOM', 'ATOS', 'ATRA', 'ATRC', 'ATRI', 'ATRO', 'ATRS', 'ATSG', 'ATVI', 'ATXI', 'AUB', 'AUBAP', 'AUBN', 'AUDC', 'AUPH', 'AUTL', 'AUTO', 'AUVI', 'AVAV', 'AVCO', 'AVCT', 'AVCTW', 'AVDL', 'AVEO', 'AVGO', 'AVGOP', 'AVGR', 'AVID', 'AVNW', 'AVRO', 'AVT', 'AVXL', 'AWH', 'AWRE', 'AXAS', 'AXDX', 'AXGN', 'AXGT', 'AXLA', 'AXNX', 'AXSM', 'AXTI', 'AY', 'AYLA', 'AYRO', 'AYTU', 'AZPN', 'AZRX']

BStockSym = ['B','BA','BABA','BAC','BAC-A','BAC-B','BAC-C','BAC-E','BAC-K','BAC-L','BAC-M','BAC-N','BAF','BAH','BAK','BAN-D','BAN-E','BANC','BAP','BAX','BB','BBAR','BBD','BBDC','BBDO','BBF','BBK','BBL','BBN','BBU','BBVA','BBW','BBX','BBY','BC','BC-A','BC-B','BC-C','BCC','BCE','BCEI','BCH','BCO','BCS','BCSF','BCX','BDC','BDJ','BDN','BDX','BDXB','BEDU','BEKE','BEN','BEP','BEP-A','BEPC','BERY','BF.A','BFAM','BFK','BFO','BFS','BFS-D','BFS-E','BFT.U','BFY','BFZ','BG','BGB','BGH','BGIO','BGR','BGS','BGSF','BGT','BGX','BGY','BH','BH.A','BHC','BHE','BHK','BHLB','BHP','BHR','BHR-B','BHR-D','BHV','BHVN','BIF','BIO.B','BIP','BIPC','BITA','BJ','BK','BK-C','BKD','BKE','BKI','BKK','BKN','BKR','BKT','BKU','BLD','BLE','BLK','BLL','BLW','BLX','BMA','BME','BMEZ','BMI','BML-G','BML-H','BML-J','BML-L','BMO','BMR.U','BMR.W','BMRG','BMY','BMY.P','BNED','BNS','BNY','BOE','BOH','BOOT','BORR','BP','BPMP','BPT','BQH','BR','BRBR','BRC','BRFS','BRK.A','BRK.B','BRMK','BRT','BRX','BSA','BSAC','BSBR','BSD','BSE','BSIG','BSL','BSM','BSMX','BSN.U','BST','BSTZ','BSX','BSX-A','BTA','BTE','BTI','BTO','BTT','BTU','BTZ','BUD','BUI','BURL','BV','BVN','BW','BWA','BWG','BWXT','BX','BXC','BXG','BXMT','BXMX','BXP','BXP-B','BXS-A','BYM','BZH','BZM']


    