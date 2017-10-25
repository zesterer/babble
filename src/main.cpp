#include <inf.hpp>

#include <iostream>

intmax_t page_size = 256;
std::string charset = "abcdefghijklmnopqrstuvwxyz ,.";
inf magic;
const char* magic_str = "196476518425569350908159093697625613931917425769373595128268593485891482267453843714274253499285099054826923876950342482658617940838450229157658639414794804670320463716225041888992135149665106971698326083744245639940150902405095241274304788860201459902959250499788180362318186326694081085910506658007659262878072470824440568574176847856290389368123777628485425995401256075467225343406976105734424531117131299675527727421076139035326581346147677734706435117879851604435054921432251172788730896477117410918911212275361362817701328402613982259371485463639201752678569723441074006629461617153165498535915033325912590432679528861885424895729943127550703258037959874261110443362579869862068261445611105803680872634073441930419674187046405611369690777180169632413381324469455318040049014742917246469460222435208902298519267771868312240882150772707365145262505021550449555251846799795000195578899659742420036551672031505736260570585830890716031676640023234603314400546789645809783601515946116516740252883889175710525400862755162857234667745908610506197273670743213080790835412920485861132588916332269980458376938146747985634999099434222519627477582027330933857265635695560115653501629739379914967225366124249936498319131932377849349106592299842178621252224240863497213861143407028026082963255120633310556440399289783834984908192201814824349550826490915315899624209299839684959734101813071755689407269195808826440931310613436212970078335955604652561376058215918526186359112422030632864317557276191198457732837783207794383625919242517462952841470198844654619428968466889006822750710119616219765358059002444567974674868966983810243368203790786104345396222937901143259306595951776028087030045512864225119082569661938079551485533624437334277382705217242302458492382632162314698452059313372594727496344825549177511340667594459388231247593069966110245060502376490649875661088015287730589744450591784982336551689254117936830259688249390422220077345333236595965356000848036967628743020324788861711522978498234587179338402183300178188756419906277763662799587129511086459289548353522232156335864442607182335843310733150424742646062012886767979209065133586851475167756921691930990525820895137663772019377026575608309741637165961269041959183198441782392600445641719126712292219075184610918621590022863953727213920662568841951923538790872987988509159284497087412791302262713759750520774697977716612897156539813844424545475391244408436129229676399818220904864947822669123007978572337602964215968174928849278648602025459600917655219384692517456837417041623588469155164322347432672787814649191689463439795298943378447277812266215058768642402584713939903635089845743084034102864711333891986873311824498051129995481100264227330863682865292330896353072698130178032176850617092366003174447169945451524704326406178401102209380643777212633170972693304930307475968000207176395900534122410415510804370756707934842652500585417219561484239300959243499752365276255769391249316163370429046042840805732737354477330215611848300126778386528151796045646521480967719770069346435240188672343775595354071697118379216889185688484456803403780259222829166118606983940678906256412742461747515025646380022009917885081561265650409850193385861169270136081568073370473280344851254124861535695600920664032551682810859563117616603922980859251397598196151409979051113184214756905923193172878599979971631634745379902306639341054945748458949716196227504227847589629637742425987935457242840867044761088425923043168137704742450847147324437568356526248792520942467255462233410649482532787896660641411540743510038497320071811329724363274923939611774862472761853414665856176685261950548178016275055463400629762708065575161061376601913475434797549769351828319158586174790980963632806096053396648603815771577944421444045097298539484962415816277642110236278289271048540225783859422916879937563761131204555255819350897534948297890701337862446199415257934338252167973057450651262707843722698547146159841287419741355371535220868373094886989944888425304040271024354905088301595005500438992223179683378089665056838534440537870857571497427170913413041070316997592866865265326282177371293274647264156733097294335124244156990786729037961565471365915894221304781709981317558566910006305325310984385585033118020894984502097524468819416657878905370645293882268514693095336054046433919333929447211908373183120426303185952318073654706559739249917232530394515337289039768864966739951207009614355905825779359795284633095390273952704414524031046533958937305208325282306792309771569625854195917455561846179909442712791985890338841622543420661139318911324299252107239485523540839616288102389560084543425372419203143256990849598050263492438671971509511183992518689012269052750349614749869054100815621247039256123334321765078454114109035665452997865412563881582793533575598743842811815392491106119687235768191803893434734221911713081897322608908301764824597562774482377351571951096977500930647196236051819485604741827125433442747447772975669032617792995723517118340100933465345040425315659995669872357740854223977919315357087029137917787832252508143492884148176514684278045134741999550378491069995310527614008756794956714321343095930647113859095100154589905872117331535250730303281413695890298380314149911639838391358483524112606231317951600387007817349367637217259873220652103022782367364079518995289254152908566666237017198302232185243872158453581355244086089205193969772256838272344043045907533090120751731113719765293991487880706705029038925652631216272877467765481377929286244042022010398460182762560913454840566912592937922343693370182425101351176421690669968819214972770302043872856467214123348962378177088695449972166948033009042828898178763106551005183397922277145857387928125150987716763586539639317063373002250328187834016802477000564960880729771052264730787861946184531540964363647068436824001990562920125847129523444958830375043101499049119926303275830021000416046714905942187980370383959486615597710826864388061216899698137219512653263463659090799013335969923243998252545588002912214505243016307393865833171963448257074893004462635346113658135125808729068524291467897488457330686525386949935601999871963707988619206812314171574296922550016745389115364869628157009625439629045791583356239265741208577569652093866288204841389495010621561365809454632144648085159279585350348748796603723967844926341350259345108269690832468953298995063883972139244540248846548476097316282017667380810555947303423030778525590774692158825804707373631948309578654403758800509182159009237950937118456617038255205031065368933103620466931078088908872705329781847765053711536250293455966100431983642088055133906574915014414580972911682157242852284242921356311003791518018380564048248084595973088301096802100442377778929447772743398175831636";
inf max_index = 29;

unsigned int randint = 1337;
void seed(unsigned int s)
{
	randint = s;
}

unsigned int randi()
{
	randint = randint * 22123713 + 82191023;
	randint ^= 22919281392143;
	return randint % 65536;
}

unsigned int hash(const char* s)
{
	unsigned int hash = 0;
	while (*(s++) != '\0')
		hash = (*s * 337271 + 21317) ^ hash;
	return hash;
}

std::string index2text(inf index)
{
	inf nindex = index + magic;
	nindex %= max_index;
	
	std::string text = "";
	for (intmax_t i = 0; i < page_size; i ++)
	{
		text += charset[(nindex % 29).num()];
		nindex /= 29;
	}
	
	return text;
}

inf text2index(std::string text)
{
	inf inv = 0;
	for (intmax_t i = text.length(); i > 0; i --)
	{
		size_t pos = charset.find_first_of(text[i - 1]);
		if (pos != std::string::npos)
		{
			inv *= 29;
			inv += (pos % 29);
		}
	}
	
	inv = (max_index + inv - magic);
	inv %= max_index;
	return inv;
}

std::string pad(std::string text, int mode = 0)
{
	switch(mode)
	{
		case 0:
			while (text.length() < (size_t)page_size)
				text += ' ';
			break;
		
		case 1:
		{
			seed(hash(text.c_str()));
			while (text.length() < (size_t)page_size)
			{
				if (randi() % 100 < 50)
					text += charset[randi() % 29];
				else
					text = std::string(&charset[randi() % 29], 1) + text;
			}
		}
		break;
		
		default:
			break;
	}
	
	return text;
}

void read()
{
	std::string hex;
	int wall, shelf, volume, page;
	
	std::cout << "Which hexagon? "; std::cin >> hex;
	std::cout << "Which wall? (1 - 4) "; std::cin >> wall;
	std::cout << "Which shelf? (1 - 5) "; std::cin >> shelf;
	std::cout << "Which volume? (1 - 32) "; std::cin >> volume;
	std::cout << "Which page? (1 - 410) "; std::cin >> page;
	
	inf index;
	index.set(hex, 16);
	index = (index * 4) + wall - 1;
	index = (index * 5) + shelf - 1;
	index = (index * 32) + volume - 1;
	index = (index * 410) + page - 1;
	
	//std::cout << "The index is " << index.str() << std::endl;
	
	std::cout << "The text is:" << std::endl << index2text(index) << std::endl;
}

void find()
{
	std::string text;
	int search_mode;
	std::cout << "What text should we find? "; std::cin >> text;
	std::cout << "What search mode should we use? (0 = exact, 1 = any) "; std::cin >> search_mode;
	
	text = pad(text, search_mode);
	
	inf index = text2index(text);
	
	//std::cout << "Text is " << text;
	
	//std::cout << "Index is " << index.str() << std::endl;
	
	std::cout << "Page is " << (index % 410 + 1).str() << std::endl;
	index /= 410;
	std::cout << "Volume is " << (index % 32 + 1).str() << std::endl;
	index /= 32;
	std::cout << "Shelf is " << (index % 5 + 1).str() << std::endl;
	index /= 5;
	std::cout << "Wall is " << (index % 4 + 1).str() << std::endl;
	index /= 4;
	std::cout << "Hexagon is " << index.str(16) << std::endl;
}

void help()
{
	std::cout << "Available commands:" << std::endl;
	std::cout << " - help   Show this prompt" << std::endl;
	std::cout << " - exit   Exit Babble" << std::endl;
	std::cout << " - read   Read a specific page in the library" << std::endl;
	std::cout << " - find   Find a piece of text in the library" << std::endl;
}

int iface()
{
	std::cout << "Welcome to Babble" << std::endl << "Type 'help' for more info" << std::endl;
	while (true)
	{
		std::string inp;
		std::cout << "> ";
		std::cin >> inp;
		
		if (inp == "exit")
			break;
		else if (inp == "help")
			help();
		else if (inp == "read")
			read();
		else if (inp == "find")
			find();
		else
			std::cout << "Unknown command " << inp << std::endl;
	}
	
	return 0;
}

int main(int argc, char* argv[])
{
	(void)argc;
	(void)argv;
	
	max_index = max_index.pow(page_size);
	magic.set(magic_str);
	magic %= max_index;
	
	return iface();
}