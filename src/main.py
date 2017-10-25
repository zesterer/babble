import random, hashlib

chars = "abcdefghijklmnopqrstuvwxyz ,."
magic = 196476518425569350908159093697625613931917425769373595128268593485891482267453843714274253499285099054826923876950342482658617940838450229157658639414794804670320463716225041888992135149665106971698326083744245639940150902405095241274304788860201459902959250499788180362318186326694081085910506658007659262878072470824440568574176847856290389368123777628485425995401256075467225343406976105734424531117131299675527727421076139035326581346147677734706435117879851604435054921432251172788730896477117410918911212275361362817701328402613982259371485463639201752678569723441074006629461617153165498535915033325912590432679528861885424895729943127550703258037959874261110443362579869862068261445611105803680872634073441930419674187046405611369690777180169632413381324469455318040049014742917246469460222435208902298519267771868312240882150772707365145262505021550449555251846799795000195578899659742420036551672031505736260570585830890716031676640023234603314400546789645809783601515946116516740252883889175710525400862755162857234667745908610506197273670743213080790835412920485861132588916332269980458376938146747985634999099434222519627477582027330933857265635695560115653501629739379914967225366124249936498319131932377849349106592299842178621252224240863497213861143407028026082963255120633310556440399289783834984908192201814824349550826490915315899624209299839684959734101813071755689407269195808826440931310613436212970078335955604652561376058215918526186359112422030632864317557276191198457732837783207794383625919242517462952841470198844654619428968466889006822750710119616219765358059002444567974674868966983810243368203790786104345396222937901143259306595951776028087030045512864225119082569661938079551485533624437334277382705217242302458492382632162314698452059313372594727496344825549177511340667594459388231247593069966110245060502376490649875661088015287730589744450591784982336551689254117936830259688249390422220077345333236595965356000848036967628743020324788861711522978498234587179338402183300178188756419906277763662799587129511086459289548353522232156335864442607182335843310733150424742646062012886767979209065133586851475167756921691930990525820895137663772019377026575608309741637165961269041959183198441782392600445641719126712292219075184610918621590022863953727213920662568841951923538790872987988509159284497087412791302262713759750520774697977716612897156539813844424545475391244408436129229676399818220904864947822669123007978572337602964215968174928849278648602025459600917655219384692517456837417041623588469155164322347432672787814649191689463439795298943378447277812266215058768642402584713939903635089845743084034102864711333891986873311824498051129995481100264227330863682865292330896353072698130178032176850617092366003174447169945451524704326406178401102209380643777212633170972693304930307475968000207176395900534122410415510804370756707934842652500585417219561484239300959243499752365276255769391249316163370429046042840805732737354477330215611848300126778386528151796045646521480967719770069346435240188672343775595354071697118379216889185688484456803403780259222829166118606983940678906256412742461747515025646380022009917885081561265650409850193385861169270136081568073370473280344851254124861535695600920664032551682810859563117616603922980859251397598196151409979051113184214756905923193172878599979971631634745379902306639341054945748458949716196227504227847589629637742425987935457242840867044761088425923043168137704742450847147324437568356526248792520942467255462233410649482532787896660641411540743510038497320071811329724363274923939611774862472761853414665856176685261950548178016275055463400629762708065575161061376601913475434797549769351828319158586174790980963632806096053396648603815771577944421444045097298539484962415816277642110236278289271048540225783859422916879937563761131204555255819350897534948297890701337862446199415257934338252167973057450651262707843722698547146159841287419741355371535220868373094886989944888425304040271024354905088301595005500438992223179683378089665056838534440537870857571497427170913413041070316997592866865265326282177371293274647264156733097294335124244156990786729037961565471365915894221304781709981317558566910006305325310984385585033118020894984502097524468819416657878905370645293882268514693095336054046433919333929447211908373183120426303185952318073654706559739249917232530394515337289039768864966739951207009614355905825779359795284633095390273952704414524031046533958937305208325282306792309771569625854195917455561846179909442712791985890338841622543420661139318911324299252107239485523540839616288102389560084543425372419203143256990849598050263492438671971509511183992518689012269052750349614749869054100815621247039256123334321765078454114109035665452997865412563881582793533575598743842811815392491106119687235768191803893434734221911713081897322608908301764824597562774482377351571951096977500930647196236051819485604741827125433442747447772975669032617792995723517118340100933465345040425315659995669872357740854223977919315357087029137917787832252508143492884148176514684278045134741999550378491069995310527614008756794956714321343095930647113859095100154589905872117331535250730303281413695890298380314149911639838391358483524112606231317951600387007817349367637217259873220652103022782367364079518995289254152908566666237017198302232185243872158453581355244086089205193969772256838272344043045907533090120751731113719765293991487880706705029038925652631216272877467765481377929286244042022010398460182762560913454840566912592937922343693370182425101351176421690669968819214972770302043872856467214123348962378177088695449972166948033009042828898178763106551005183397922277145857387928125150987716763586539639317063373002250328187834016802477000564960880729771052264730787861946184531540964363647068436824001990562920125847129523444958830375043101499049119926303275830021000416046714905942187980370383959486615597710826864388061216899698137219512653263463659090799013335969923243998252545588002912214505243016307393865833171963448257074893004462635346113658135125808729068524291467897488457330686525386949935601999871963707988619206812314171574296922550016745389115364869628157009625439629045791583356239265741208577569652093866288204841389495010621561365809454632144648085159279585350348748796603723967844926341350259345108269690832468953298995063883972139244540248846548476097316282017667380810555947303423030778525590774692158825804707373631948309578654403758800509182159009237950937118456617038255205031065368933103620466931078088908872705329781847765053711536250293455966100431983642088055133906574915014414580972911682157242852284242921356311003791518018380564048248084595973088301096802100442377778929447772743398175831636580133546028167785983333203611053545529990570831428952121544272645468907352002173194478134130101603055170954745467763621833443128325327868345830471174549042256811937455823191437782060979040221609572429940437060269290182962403376802295902310555769304032269678005035879199504598253922804366337694825180148985346375410751278825297692266581058681979436164813309489252496346083409709214427639048935529419092868860977393379986948197465507785687288855348486082204509363429669573421456653763657357118560629438887928862589883467002501552527938049854674294289740555655441009713344623092998450624819093591729404913910566732283308832992374079671772297038920266818550587339866278858347747548788323128035930152134954978074882274553389869477427614807140962090232409640218262570580688067025839447346746185247986383564609621716225859571214627705656689911451994247871525234471898178623996083625706171110944214450693494719834622017867712144492156764833803795415372644763781557111760244860947046445055372693586200692367927606400863071527102636996262052571732243641507503998713760650403152487860994828788363511231761456737936645352662239200723165485064219699981929963600663290751769908661202043006975126344430136327734271589284354949032309771115992245523973185420767321054503856971508468596159130708198204757212684100543858693976194055927930093786830713700030849124716804707819290223352655250538873438356962991641356161408679150425794571672372521750438694448889980496085705521821966757846441286232746472641567330972943351242441569907867290379615654713659158942213047817099813175585669100063053253109843855850331180208949845020975244688194166578789053706452938822685146930953360540464339193339294472119083731831204263031859523180736547065597392499172325303945153372890397688649667399512070096143559058257793597952846330953902739527044145240310465339589373052083252823067923097715696258541959174555618461799094427127919858903388416225434206611393189113242992521072394855235408396162881023895600845434253724192031432569908495980502634924386719715095111839925186890122690527503496147498690541008156212470392561233343217650784541141090356654529978654125638815827935335755987438428118153924911061196872357681918038934347342219117130818973226089083017648245975627744823773515719510969775009306471962360518194856047418271254334427474477729756690326177929957235171183401009334653450404253156599956698723577408542239779193153570870291379177878322525081434928841481765146842780451347419995503784910699953105276140087567949567143213430959306471138590951001545899058721173315352507303032814136958902983803141499116398383913584835241126062313179516003870078173493676372172598732206521030227823673640795189952892541529085666662370171983022321852438721584535813552440860892051939697722568382723440430459075330901207517311137197652939914878807067050290389256526312162728774677654813779292862440420220103984601827625609134548405669125929379223436933701824251013511764216906699688192149727703020438728564672141233489623781770886954499721669480330090428288981787631065510051833979222771458573879281251509877167635865396393170633730022503281878340168024770005649608807297710522647307878619461845315409643636470684368240019905629201258471295234449588303750431014990491199263032758300210004160467149059421879803703839594866155977108268643880612168996981372195126532634636590907990133359699232439982525455880029122145052430163073938658331719634482570748930044626353461136581351258087290685242914678974884573306865253869499356019998719637079886192068123141715742969225500167453891153648696281570096254396290457915833562392657412085775696520938662882048413894950106215613658094546321446480851592795853503487487966037239678449263413502593451082696908324689532989950638839721392445402488465484760973162820176673808105559473034230307785255907746921588258047073736319483095786544037588005091821590092379509371184566170382552050310653689331036204669310780889088727053297818477650537115362502934559661004319836420880551339065749150144145809729116821572428522842429213563110037915180183805640482480845959730883010968021004423777789294477727433981758316365801335460281677859833332036110535455299905708314289521215442726454689073520021731944781341301016030551709547454677636218334431283253278683458304711745490422568119374558231914377820609790402216095724299404370602692901829624033768022959023105557693040322696780050358791995045982539228043663376948251801489853463754107512788252976922665810586819794361648133094892524963460834097092144276390489355294190928688609773933799869481974655077856872888553484860822045093634296695734214566537636573571185606294388879288625898834670025015525279380498546742942897405556554410097133446230929984506248190935917294049139105667322833088329923740796717722970389202668185505873398662788583477475487883231280359301521349549780748822745533898694774276148071409620902324096402182625705806880670258394473467461852479863835646096217162258595712146277056566899114519942478715252344718981786239960836257061711109442144506934947198346220178677121444921567648338037954153726447637815571117602448609470464450553726935862006923679276064008630715271026369962620525717322436415075039987137606504031524878609948287883635112317614567379366453526622392007231654850642196999819299636006632907517699086612020430069751263444301363277342715892843549490323097711159922455239731854207673210545038569715084685961591307081982047572126841005438586939761940559279300937868307137000308491247168047078192902233526552505388734383569629916413561614086791504257945716723725217504386944488899804960857055218219667578464412862
page_size = 64
max_index = 29 ** page_size

def pad(text):
	random.seed(int(hashlib.md5(text.encode()).hexdigest(), 16))
	while len(text) < page_size:
		if random.randint(0, 2) == 1:
			text = random.choice(chars) + text
		else:
			text = text + random.choice(chars)
	return text

def index2text(index):
	index = (index + (magic % max_index)) % max_index

	s = chars[index % 29]
	for i in range(1, page_size):
		s += chars[int(index // (29 ** i)) % 29]
	
	return s

def text2index(text):
	inv = 0
	for c in text:
		ind = chars.find(c)
		if ind != -1:
			inv = inv * 29 + ind
	
	return (max_index + inv - (magic % max_index)) % max_index

def goto():
	room = int(input("Which room (1 - infinity)? "))
	wall = int(input("Which wall (1 - 4)? "))
	shelf = int(input("Which shelf (1 - 5)? "))
	volume = int(input("Which volume (1 - 32)? "))
	page = int(input("Which page (1 - 410)? "))
	
	index = (((((room - 1) * 4 + (wall - 1)) * 5 + (shelf - 1)) * 32 + (volume - 1)) * 410 + (page - 1)) % max_index
	
	#print("Your index is " + str(index))
	print("Your text is:\n" + index2text(index))

def search():
	text = str(input("What do you want to search for? "))
	
	text = pad(text)
	
	#print("Your search text is " + text)
	
	index = text2index(index2text(text2index(text)))
	
	#print("The index is " + str(index))
	
	print("The page is " + str(index % 410 + 1))
	index //= 410
	print("The volume is " + str(index % 32 + 1))
	index //= 32
	print("The shelf is " + str(index % 5 + 1))
	index //= 5
	print("The wall is " + str(index % 4 + 1))
	index //= 4
	print("The room is " + str(index + 1))
	
	#index = (((((room - 1) * 4 + (wall - 1)) * 5 + (shelf - 1)) * 32 + (volume - 1)) * 410 + (page - 1)) % max_index

def help():
	print("- Possible commands -")
	print("  - help: Display this screen")
	print("  - exit: Exit Babble")
	print("  - goto: Display the contents of a specific page")
	print("  - search: Search for a specific length of text")

def iface():
	print("- Welcome to Babble -")
	print("- Type 'help' for more info -")

	while True:
		inp = str(input("> "))
		
		if inp == "exit":
			break
		elif inp == "goto":
			goto()
		elif inp == "search":
			search()
		elif inp == "help":
			help()
		else:
			print("Unknown command '" + inp + "'")
	
	print("Exiting Babble...")

if __name__ == "__main__":
	iface()
