import praw
from collections import Counter

AStockSym = ['AACG', 'AACQ', 'AACQU', 'AACQW', 'AAL', 'AAME', 'AAOI', 'AAON', 'AAPL', 'AAWW', 'AAXJ', 'AAXN', 'ABCB', 'ABEO', 'ABIO', 'ABMD', 'ABTX', 'ABUS', 'ACAD', 'ACAM', 'ACAMU', 'ACAMW', 'ACBI', 'ACCD', 'ACER', 'ACEVU', 'ACGL', 'ACGLO', 'ACGLP', 'ACHC', 'ACHV', 'ACIA', 'ACIU', 'ACIW', 'ACLS', 'ACMR', 'ACNB', 'ACOR', 'ACRS', 'ACRX', 'ACST', 'ACT', 'ACTG', 'ACWI', 'ACWX', 'ADAP', 'ADBE', 'ADES', 'ADI', 'ADIL', 'ADILW', 'ADMA', 'ADMP', 'ADMS', 'ADP', 'ADPT', 'ADRE', 'ADRO', 'ADSK', 'ADTN', 'ADTX', 'ADUS', 'ADVM', 'ADXN', 'ADXS', 'AEGN', 'AEHR', 'AEIS', 'AEMD', 'AERI', 'AESE', 'AEY', 'AEYE', 'AEZS', 'AFIB', 'AFIN', 'AFINP', 'AFMD', 'AFYA', 'AGBA', 'AGBAR', 'AGBAU', 'AGBAW', 'AGEN', 'AGFS', 'AGIO', 'AGLE', 'AGMH', 'AGNC', 'AGNCM', 'AGNCN', 'AGNCO', 'AGNCP', 'AGRX', 'AGTC', 'AGYS', 'AGZD', 'AHCO', 'AHPI', 'AIA', 'AIH', 'AIHS', 'AIKI', 'AIMC', 'AIMT', 'AINV', 'AIQ', 'AIRG', 'AIRR', 'AIRT', 'AIRTP', 'AIRTW', 'AKAM', 'AKBA', 'AKCA', 'AKER', 'AKRO', 'AKTS', 'AKTX', 'AKU', 'AKUS', 'ALAC', 'ALACR', 'ALACU', 'ALACW', 'ALBO', 'ALCO', 'ALDX', 'ALEC', 'ALGN', 'ALGT', 'ALIM', 'ALJJ', 'ALKS', 'ALLK', 'ALLO', 'ALLT', 'ALNA', 'ALNY', 'ALOT', 'ALPN', 'ALRM', 'ALRN', 'ALRS', 'ALSK', 'ALT', 'ALTA', 'ALTM', 'ALTR', 'ALTY', 'ALVR', 'ALXN', 'ALXO', 'ALYA', 'AMAG', 'AMAL', 'AMAT', 'AMBA', 'AMCA', 'AMCI', 'AMCIU', 'AMCIW', 'AMCX', 'AMD', 'AMED', 'AMEH', 'AMGN', 'AMHC', 'AMHCU', 'AMHCW', 'AMKR', 'AMNB', 'AMOT', 'AMPH', 'AMRB', 'AMRH', 'AMRHW', 'AMRK', 'AMRN', 'AMRS', 'AMSC', 'AMSF', 'AMSWA', 'AMTB', 'AMTBB', 'AMTD', 'AMTI', 'AMTX', 'AMWD', 'AMYT', 'AMZN', 'ANAB', 'ANAT', 'ANCN', 'ANDA', 'ANDAR', 'ANDAU', 'ANDAW', 'ANDE', 'ANGI', 'ANGL', 'ANGO', 'ANIK', 'ANIP', 'ANIX', 'ANNX', 'ANPC', 'ANSS', 'ANTE', 'ANY', 'AOSL', 'AOUT', 'APA', 'APDN', 'APEI', 'APEN', 'APEX', 'APHA', 'API', 'APLS', 'APLT', 'APM', 'APOG', 'APOP', 'APOPW', 'APPF', 'APPN', 'APPS', 'APRE', 'APTO', 'APTX', 'APVO', 'APWC', 'APXT', 'APXTU', 'APXTW', 'APYX', 'AQB', 'AQMS', 'AQST', 'ARAV', 'ARAY', 'ARCB', 'ARCC', 'ARCE', 'ARCT', 'ARDS', 'ARDX', 'AREC', 'ARGX', 'ARKR', 'ARLP', 'ARNA', 'AROW', 'ARPO', 'ARQT', 'ARTL', 'ARTLW', 'ARTNA', 'ARTW', 'ARVN', 'ARWR', 'ARYA', 'ARYB', 'ARYBU', 'ARYBW', 'ASET', 'ASFI', 'ASLN', 'ASMB', 'ASML', 'ASND', 'ASPS', 'ASPU', 'ASRT', 'ASRV', 'ASRVP', 'ASTC', 'ASTE', 'ASUR', 'ASYS', 'ATAX', 'ATCX', 'ATCXW', 'ATEC', 'ATEX', 'ATHE', 'ATHX', 'ATIF', 'ATLC', 'ATLO', 'ATNI', 'ATNX', 'ATOM', 'ATOS', 'ATRA', 'ATRC', 'ATRI', 'ATRO', 'ATRS', 'ATSG', 'ATVI', 'ATXI', 'AUB', 'AUBAP', 'AUBN', 'AUDC', 'AUPH', 'AUTL', 'AUTO', 'AUVI', 'AVAV', 'AVCO', 'AVCT', 'AVCTW', 'AVDL', 'AVEO', 'AVGO', 'AVGOP', 'AVGR', 'AVID', 'AVNW', 'AVRO', 'AVT', 'AVXL', 'AWH', 'AWRE', 'AXAS', 'AXDX', 'AXGN', 'AXGT', 'AXLA', 'AXNX', 'AXSM', 'AXTI', 'AY', 'AYLA', 'AYRO', 'AYTU', 'AZPN', 'AZRX', 'B','BA','BABA','BAC','BAC-A','BAC-B','BAC-C','BAC-E','BAC-K','BAC-L','BAC-M','BAC-N','BAF','BAH','BAK','BAN-D','BAN-E','BANC','BAP','BAX','BB','BBAR','BBD','BBDC','BBDO','BBF','BBK','BBL','BBN','BBU','BBVA','BBW','BBX','BBY','BC','BC-A','BC-B','BC-C','BCC','BCE','BCEI','BCH','BCO','BCS','BCSF','BCX','BDC','BDJ','BDN','BDX','BDXB','BEDU','BEKE','BEN','BEP','BEP-A','BEPC','BERY','BF.A','BFAM','BFK','BFO','BFS','BFS-D','BFS-E','BFT.U','BFY','BFZ','BG','BGB','BGH','BGIO','BGR','BGS','BGSF','BGT','BGX','BGY','BH','BH.A','BHC','BHE','BHK','BHLB','BHP','BHR','BHR-B','BHR-D','BHV','BHVN','BIF','BIO.B','BIP','BIPC','BITA','BJ','BK','BK-C','BKD','BKE','BKI','BKK','BKN','BKR','BKT','BKU','BLD','BLE','BLK','BLL','BLW','BLX','BMA','BME','BMEZ','BMI','BML-G','BML-H','BML-J','BML-L','BMO','BMR.U','BMR.W','BMRG','BMY','BMY.P','BNED','BNS','BNY','BOE','BOH','BOOT','BORR','BP','BPMP','BPT','BQH','BR','BRBR','BRC','BRFS','BRK.A','BRK.B','BRMK','BRT','BRX','BSA','BSAC','BSBR','BSD','BSE','BSIG','BSL','BSM','BSMX','BSN.U','BST','BSTZ','BSX','BSX-A','BTA','BTE','BTI','BTO','BTT','BTU','BTZ','BUD','BUI','BURL','BV','BVN','BW','BWA','BWG','BWXT','BX','BXC','BXG','BXMT','BXMX','BXP','BXP-B','BXS-A','BYM','BZH','BZM', 'CAAS', 'CABA', 'CAC', 'CACC', 'CACG', 'CAKE', 'CALA', 'CALB', 'CALM', 'CALT', 'CAMP', 'CAMT', 'CAN', 'CAPAU', 'CAPR', 'CAR', 'CARA', 'CARE', 'CARG', 'CARV', 'CARZ', 'CASA', 'CASH', 'CASI', 'CASS', 'CASY', 'CATB', 'CATC', 'CATH', 'CATM', 'CATY', 'CBAN', 'CBAT', 'CBAY', 'CBIO', 'CBLI', 'CBMB', 'CBMG', 'CBNK', 'CBPO', 'CBRL', 'CBSH', 'CBTX', 'CCAP', 'CCB', 'CCBG', 'CCCL', 'CCD', 'CCLP', 'CCMP', 'CCNC', 'CCNE', 'CCNEP', 'CCOI', 'CCRC', 'CCRN', 'CCXI', 'CDC', 'CDEV', 'CDK', 'CDL', 'CDLX', 'CDMO', 'CDMOP', 'CDNA', 'CDNS', 'CDTX', 'CDW', 'CXC', 'CDXS', 'CDZI', 'CECE', 'CEFA', 'CELC', 'CELH', 'CEMI', 'CENT', '', 'CENTA', 'CENX', 'CERC', 'CERN', 'CERS', 'CETV', 'CETX', 'CETXP', 'CETXW', 'CEVA', 'CEY', 'CEZ', 'CFA', 'CFB', 'CFBI', 'CFBK', 'CFFA', 'CFFAU', 'CFFAW', 'CFFI', 'CFFN', 'CFIIU', 'CFMS', 'CFO', 'CFRX', 'CG', 'CGBD', 'CGEN', 'CGIX', 'CGNX', 'CGO', 'CGRO', 'CGROU', 'CGROW', 'CHCI', 'CHCO', 'CHDN', 'CHEF', 'CHEK', 'CHEKZ', 'CHFS', 'CHI', 'CHKP', 'CHMA', 'CHMG', 'CHNA', 'CHNG', 'CHNGU', 'CHNR', 'CHPM', 'CHPMU', 'CHPMW', 'CHRS', 'CHRW', 'CHSCL', 'CHSCM', 'CHSCN', 'CHSCO', 'CHSCP', 'CHTR', 'CHUY', 'CHW', 'CHY', 'CIBR', 'CID', 'CIDM', 'CIGI', 'CIH', 'CIIC', 'CIICU', 'CIICW', 'CIL', 'CINF', 'CIVB', 'CIZ', 'CIZN', 'CJJD', 'CKPT', 'CLAR', 'CLBK', 'CLBS', 'CLCT', 'CLDB', 'CLDX', 'CLEU', 'CLFD', 'CLGN', 'CLIR', 'CLLS', 'CLMT', 'CLNE', 'CLOU', 'CLPS', 'CLPT', 'CLRB', 'CLRBZ', 'CLRG', 'CLRO', 'CLSD', 'CLSK', 'CLSN', 'CLUB', 'CLVS', 'CLWT', 'CLXT', 'CMBM', 'CMCO', 'CMCSA', 'CMCT', 'CMCTP', 'CME', 'CMFNL', 'CMLFU', 'CMLS', 'CMPI', 'CMPR', 'CMRX', 'CMTL', 'CNBKA', 'CNCE', 'CNCR', 'CNDT', 'CNET', 'CNFR', 'CNFRL', 'CNNB', 'CNOB', 'CNSL', 'CNSP', 'CNST', 'CNTG', 'CNTY', 'CNXN', 'COCP', 'CODA', 'CODX', 'COFS', 'COHR',', ''COHU', 'COKE', 'COLB', 'COLL', 'COLM', 'COMM', 'COMT', 'CONE', 'CONN', 'COOP', 'CORE', 'CORT', 'COST', 'COUP', 'COWN', 'COWNL', 'COWNZ', 'CPAA', 'CPAAU', 'CPAAW', 'CPAH', 'CPHC', 'CPIX', 'CPLP', 'CPRT', 'CPRX', 'CPSH', 'CPSI', 'CPSS', 'CPST', 'CPTA', 'CPTAG', 'CPTAL', 'CPZ', 'CRAI', 'CRBP', 'CRDF', 'CREE', 'CREG', 'CRESY', 'CREX', 'CREXW', 'CRIS', 'CRMT', 'CRNC', 'CRNT', 'CRNX', 'CRON', 'CROX', 'CRSA', 'CRSAU', 'CRSAW', 'CRSP', 'CRTD', 'CRTDW', 'CRTO', 'CRTX', 'CRUS', 'CRVL', 'CRVS', 'CRWD', 'CRWS', 'CSA', 'CSB', 'CSBR', 'CSCO', 'CSF', 'CSGP', 'CSGS', 'CSII', 'CSIQ', 'CSML', 'CSOD', 'CSPI', 'CSQ', 'CSSE', 'CSSEN', 'CSSEP', 'CSTE', 'CSTL', 'CSTR', 'CSWC', 'CSWCL', 'CSWI', 'CSX', 'CTAS', 'CTBI', 'CTG', 'CTHR', 'CTIB', 'CTIC', 'CTMX', 'CTRE', 'CTRM', 'CTRN', 'CTSH', 'CTSO', 'CTXR', 'CTXRW', 'CTXS', 'CUBA', 'CUE', 'CUTR', 'CVAC', 'CVBF', 'CVCO', 'CVCY', 'CVET', 'CVGI', 'CVGW', 'CVLG', 'CVLT', 'CVLY', 'CVV', 'CWBC', 'CWBR', 'CWCO', 'CWST', 'CXDC', 'CXDO', 'CXSE', 'CYAD', 'CYAN', 'CYBE', 'CYBR', 'CYCC', 'CYCCP', 'CYCN', 'CYRN', 'CYRX', 'CYTK', 'CZNC', 'CZR', 'CZWI']

SStockSym = ['SABR', 'SABRP', 'SAFM', 'SAFT', 'SAGE', 'SAIA', 'SAIIU', 'SAL', 'SALM', 'SAMA', 'SAMAU', 'SAMAW', 'SAMG', 'SANM', 'SANW', 'SAQN', 'SAQNU', 'SAQNW', 'SASR', 'SATS', 'SAVA', 'SBAC', 'SBBP', 'SBCF', 'SBFG', 'SBGI', 'SBLK', 'SBLKZ', 'SBNY', 'SBPH', 'SBRA', 'SBSI', 'SBT', 'SBUX', 'SCHL', 'SCHN', 'SCKT', 'SCON', 'SCOR', 'SCPH', 'SCPL', 'SCSC', 'SCVL', 'SCWX', 'SCYX', 'SCZ', 'SDC', 'SDG', 'SDGR', 'SDVY', 'SEAC', 'SECO', 'SEDG', 'SEED', 'SEEL', 'SEIC', 'SELB', 'SELF', 'SENEA', 'SENEB', 'SESN', 'SFBC', 'SFBS', 'SFET', 'SFIX', 'SFM', 'SFNC', 'SFST', 'SG', 'SGA', 'SGBX', 'SGC', 'SGEN', 'SGH', 'SGLB', 'SGLBW', 'SGMA', 'SGMO', 'SGMS', 'SGOC', 'SGRP', 'SGRY', 'SHBI', 'SHEN', 'SHIP', 'SHIPW', 'SHIPZ', 'SHOO', 'SHSP', 'SHV', 'SHY', 'SHYF', 'SIBN', 'SIC', 'SIEB', 'SIEN', 'SIFY', 'SIGA', 'SIGI', 'SILC', 'SILK', 'SIMO', 'SINA', 'SINO', 'SINT', 'SIRI', 'SITM', 'SIVB', 'SIVBP', 'SJ', 'SKOR', 'SKYS', 'SKYW', 'SKYY', 'SLAB', 'SLCT', 'SLDB', 'SLGG', 'SLGL', 'SLGN', 'SLM', 'SLMBP', 'SLN', 'SLNO', 'SLP', 'SLQD', 'SLRC', 'SLRX', 'SLS', 'SLVO', 'SMBC', 'SMBK', 'SMCI', 'SMCP', 'SMED', 'SMIT', 'SMMC', 'SMMCU', 'SMMCW', 'SMMF', 'SMMT', 'SMPL', 'SMSI', 'SMTC', 'SMTX', 'SNBP', 'SNBR', 'SNCA', 'SNCR', 'SND', 'SNDE', 'SNDL', 'SNDX', 'SNES', 'SNEX', 'SNFCA', 'SNGX', 'SNGXW', 'SNLN', 'SNOA', 'SNPS', 'SNSR', 'SNSS', 'SNUG', 'SNY', 'SOCL', 'SOHO', 'SOHOB', 'SOHON', 'SOHOO', 'SOHU', 'SOLO', 'SOLOW', 'SOLY', 'SONA', 'SONM', 'SONN', 'SONO', 'SOXX', 'SP', 'SPCB', 'SPFI', 'SPI', 'SPKE', 'SPKEP', 'SPLK', 'SPNE', 'SPNS', 'SPOK', 'SPPI', 'SPQQ', 'SPRO', 'SPRT', 'SPSC', 'SPT', 'SPTN', 'SPWH', 'SPWR', 'SQBG', 'SQLV', 'SQQQ', 'SRAC', 'SRACU', 'SRACW', 'SRAX', 'SRCE', 'SRCL', 'SRDX', 'SRET', 'SREV', 'SRGA', 'SRNE', 'SRPT', 'SRRA', 'SRRK', 'SRTS', 'SSB', 'SSBI', 'SSKN', 'SSNC', 'SSNT', 'SSP', 'SSPK', 'SSPKU', 'SSPKW', 'SSRM', 'SSSS', 'SSTI', 'SSYS', 'STAA', 'STAF', 'STAY', 'STBA', 'STCN', 'STFC', 'STIM', 'STKL', 'STKS', 'STLD', 'STMP', 'STND', 'STNE', 'STOK', 'STRA', 'STRL', 'STRM', 'STRO', 'STRS', 'STRT', 'STSA', 'STX', 'STXB', 'SUMR', 'SUNS', 'SUNW', 'SUPN', 'SURF', 'SUSB', 'SUSC', 'SUSL', 'SVA', 'SVACU', 'SVBI', 'SVC', 'SVMK', 'SVRA', 'SVVC', 'SWAV', 'SWBI', 'SWIR', 'SWKH', 'SWKS', 'SWTX', 'SXTC', 'SY', 'SYBT', 'SYBX', 'SYKE', 'SYNA', 'SYNC', 'SYNH', 'SYNL', 'SYPR', 'SYRS', 'TA', 'TACO', 'TACT', 'TAIT', 'TANH', 'TANNI', 'TANNL', 'TANNZ', 'TAOP', 'TARA', 'TAST', 'TATT', 'TAYD', 'TBBK', 'TBIO', 'TBK', 'TBKCP', 'TBLT', 'TBLTW', 'TBNK', 'TBPH', 'TC', 'TCBI', 'TCBIL', 'TCBIP', 'TCBK', 'TCCO', 'TCDA', 'TCF', 'TCFC', 'TCFCP', 'TCMD', 'TCOM', 'TCON', 'TCPC', 'TCRR', 'TCX', 'TDAC', 'TDACU', 'TDACW', 'TDIV', 'TEAM', 'TECH', 'TECTP', 'TEDU', 'TELA', 'TELL', 'TENB', 'TENX', 'TER', 'TESS', 'TEUM', 'TFFP', 'TFSL', 'TGA', 'TGLS', 'TGTX', 'TH', 'THBR', 'THBRU', 'THBRW', 'THCA', 'THCAU', 'THCAW', 'THCB', 'THCBU', 'THCBW', 'THFF', 'THMO', 'THRM', 'THTX', 'THWWW', 'TIG', 'TIGO', 'TIGR', 'TILE', 'TIPT', 'TITN', 'TLC', 'TLGT', 'TLND', 'TLRY', 'TLSA', 'TLT', 'TMDI', 'TMDX', 'TMUS', 'TNAV', 'TNDM', 'TNXP', 'TOPS', 'TORC', 'TOTA', 'TOTAR', 'TOTAU', 'TOTAW', 'TOUR|', 'TOWN', 'TPCO', 'TPIC', 'TPTX', 'TQQQ', 'TRCH', 'TREE', 'TRHC', 'TRIB', 'TRIL', 'TRIP', 'TRMB', 'TRMD', 'TRMK', 'TRMT', 'TRNS', 'TROW', 'TRST', 'TRUE', 'TRUP', 'TRVG', 'TRVI', 'TRVN', 'TSBK', 'TSC', 'TSCAP', 'TSCBP', 'TSCO', 'TSEM', 'TSLA', 'TSRI', 'TTD', 'TTEC', 'TTEK', 'TTGT', 'TTMI', 'TTNP', 'TTOO', 'TTTN', 'TTWO', 'TUR', 'TURN', 'TUSA', 'TUSK', 'TVTY', 'TW', 'TWCTU', 'TWIN', 'TWNK', 'TWNKW', 'TWOU', 'TWST', 'TXG', 'TXMD', 'TXN', 'TXRH', 'TYHT', 'TYME', 'TZAC', 'TZACU', 'TZACW', 'TZOO', 'UAE', 'UAL', 'UBCP', 'UBFO', 'UBOH', 'UBSI', 'UBX', 'UCBI', 'UCBIO', 'UCL', 'UCTT', 'UEIC', 'UEPS', 'UFCS', 'UFO', 'UFPI', 'UFPT', 'UG', 'UHAL', 'UIHC', 'ULBI', 'ULH', 'ULTA', 'UMBF', 'UMPQ', 'UMRX', 'UNAM', 'UNB', 'UNIT', 'UNTY', 'UONE', 'UONEK', 'UPLD', 'UPWK', 'URBN', 'URGN', 'UROV', 'USAK', 'USAP', 'USAU', 'USCR', 'USEG', 'USIG', 'USIO', 'USLB', 'USLM', 'USMC', 'USOI', 'USWS', 'USWSW', 'USXF', 'UTHR', 'UTMD', 'UTSI', 'UVSP', 'UXIN', 'VALU', 'VBFC', 'VBIV', 'VBLT', 'VBTX', 'VC', 'VCEL', 'VCIT', 'VCLT', 'VCNX', 'VCSH', 'VCTR', 'VCYT', 'VECO', 'VEON', 'VERB', 'VERBW', 'VERI', 'VERO', 'VERU', 'VERX', 'VERY', 'VETS', 'VFF', 'VG', 'VGIT', 'VGLT', 'VGSH', 'VIAC', 'VIACA', 'VIAV', 'VICR', 'VIE', 'VIGI', 'VIOT', 'VIR', 'VIRC', 'VIRT', 'VISL', 'VITL', 'VIVE', 'VIVO', 'VJET', 'VKTX', 'VKTXW', 'VLGEA', 'VLY', 'VLYPO', 'VLYPP', 'VMAC', 'VMACU', 'VMACW', 'VMBS', 'VMD', 'VNDA', 'VNET', 'VNOM', 'VNQI', 'VOD', 'VONE', 'VONG', 'VONV', 'VOXX', 'VRA', 'VRAY', 'VRCA', 'VREX', 'VRIG', 'VRM', 'VRME', 'VRMEW', 'VRNA', 'VRNS', 'VRNT', 'VRRM', 'VRSK', 'VRSN', 'VRTS', 'VRTU', 'VRTX', 'VSAT', 'VSDA', 'VSEC', 'VSMV', 'VSTA', 'VSTM', 'VTC', 'VTGN', 'VTHR', 'VTIP', 'VTNR', 'VTSI', 'VTVT', 'VTWG', 'VTWO', 'VTWV', 'VUZI', 'VVPR', 'VWOB', 'VXRT', 'VXUS', 'VYGR', 'VYMI', 'VYNE', 'WABC', 'WAFD', 'WAFU', 'WASH', 'WATT', 'WB', 'WBA', 'WBND', 'WCLD', 'WDAY', 'WDC', 'WDFC', 'WEN', 'WERN', 'WETF', 'WEYS', 'WHF', 'WHFBZ', 'WHLM', 'WHLR', 'WHLRD', 'WHLRP', 'WIFI', 'WILC', 'WIMI', 'WINA', 'WINC', 'WING', 'WINS', 'WINT', 'WIRE', 'WISA', 'WIX', 'WKEY', 'WKHS', 'WLDN', 'WLFC', 'WLTW', 'WMG', 'WMGI', 'WNEB', 'WOOD', 'WORX', 'WPRT', 'WRLD', 'WRTC', 'WSBC', 'WSBCP', 'WSBF', 'WSC', 'WSFS', 'WSG', 'WSTG', 'WSTL', 'WTBA', 'WTER', 'WTFC', 'WTFCM', 'WTFCP', 'WTRE', 'WTREP', 'WTRH', 'WVE', 'WVFC', 'WVVI', 'WVVIP', 'WW', 'WWD', 'WWR', 'WYNN', 'XAIR', 'XBIO', 'XBIOW', 'XBIT', 'XCUR', 'XEL', 'XELA', 'XELB', 'XENE', 'XENT', 'XERS', 'XFOR', 'XGN', 'XLNX', 'XLRN', 'XNCR', 'XNET', 'XOMA', 'XONE', 'XP', 'XPEL', 'XPER', 'XRAY', 'XSPA', 'XT', 'XTLB', 'YGYI', 'YGYIP', 'YI', 'YIN', 'YJ', 'YLCO', 'YLDE', 'YMAB', 'YNDX', 'YORW', 'YRCW', 'YTEN', 'YTRA', 'YVR', 'YY', 'Z', 'ZAGG', 'ZAZZT', 'ZBRA', 'ZBZZT', 'ZCMD', 'ZCZZT', 'ZEAL', 'ZEUS', 'ZG', 'ZGNX', 'ZGYH', 'ZGYHR', 'ZGYHU', 'ZGYHW', 'ZI', 'ZION', 'ZIONL', 'ZIONN', 'ZIONO', 'ZIONP', 'ZIOP', 'ZIXI', 'ZJZZT', 'ZKIN', 'ZLAB', 'ZM', 'ZNGA', 'ZNTL', 'ZS', 'ZSAN', 'ZUMZ', 'ZVO', 'ZVZZC', 'ZVZZT', 'ZWZZT', 'ZXYZ.A', 'ZXZZT', 'ZYNE', 'ZYXI']

symbols = dict.fromkeys(AStockSym, 0)

reddit = praw.Reddit(client_id = 'FhCZAoozfF60nQ', client_secret = 'qT_sfXUwNI5IIVgoqSAgpEKaWUo', user_agent = 'rougndraft', username = 'BrightnessShallanVin', password = 'Waterband')

# reddit = create_reddit_object()

pennystocks_subred = reddit.subreddit('pennystocks')
wallstreetbets_subred = reddit.subreddit('wallstreetbets')
thewallstreet_subred = reddit.subreddit('thewallstreet')
tradevol_subred = reddit.subreddit('tradevol') 

subs = [pennystocks_subred, wallstreetbets_subred]

for subreddit in subs:

    hot = subreddit.hot(limit = 25)
    new = subreddit.new(limit = 25)
    top = subreddit.top(limit = 25, time_filter = 'week')    
    mentions = Counter()

    for post in hot:
        hotPostWords = post.selftext.split()
        for word in hotPostWords:
            if word in symbols:
                print(post.shortlink)
                mentions[word] += 1
        for comment in post.comments:
            if not 'MoreComments':
                hotComments = comment.body.split()
                for comment in hotComments:
                    if word in symbols:
                        mentions[word] += 1
                
    for post in new:
        newPostWords = post.selftext.split()
        for word in newPostWords:
            if word in symbols:
                print(post.shortlink)
                mentions[word] += 1
        # print(f'{post.subreddit_name_prefixed} \n {post.title} \n at: {post.shortlink} \n {post.selftext} \n upvotes: {post.ups} \n downvotes: {post.downs} \n # of comments: {post.num_comments} \n score:{post.score} \n')
        for comment in post.comments:
            if not 'MoreComments':
                newComments = comment.body.split()
                for comment in newComments:
                    if word in symbols:
                        mentions[word] += 1

    for post in top:
        topPostWords = post.selftext.split()
        for word in topPostWords:
            if word in symbols:
                print(post.shortlink)
                mentions[word] += 1
        for comment in post.comments:
            if not 'MoreComments':
                newComments = comment.body.split()
                for comment in newComments:
                    if word in symbols:
                        mentions[word] += 1

print('TOP MENTIONS:', mentions.most_common())
            

# contr = subreddit.controversial(limit=5)
# gild = subreddit.gilded(limit=5)