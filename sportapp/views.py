from coverage import data
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def foot(request):
    return render(request, 'football.html')


def bask(request):
    return render(request, 'basketball.html')

def ten(request):
    return render(request, 'tennis.html')


def vol(request):
    return render(request, 'volleyball.html')


def sportsmen(request, id, sport):

    football_players = [
        {'name': 'Лионель Месси', 'pic': 'img/fs/messi.jpg', 'picsport': 'img/fball.png', 'desc': 'Месси является самым высокооплачиваемым футболистом, его стоимость составляет сто миллионов евро. Родным клубом Месси является «Барселона». В молодежной команде «Барселона» он играл с тринадцати лет, в каждом матче забивал по одному голу. В 2003 году дебютировал в основной команде, после чего от молодого футболиста были в восторге все СМИ, они сравнивали его с Рональдиньо и Марадоной. В истории клуба он стал самым молодым игроком в сезоне 2004-2005, он также отличился в это время и на чемпионате Испании - и это в семнадцать лет! В Лиге чемпионов забил первый гол в 2005 году, звание «Золотого мальчика» получил в том же сезоне. С Барселоной выиграл Лигу Чемпионов в 2009 году и в этом сезоне он стал лучшим бомбардиром. После этого получил титулы по версии, УЕФА: Лучшего нападающего Лиги чемпионов и Лучшего футболиста в клубном футболе, а также стал обладателем «Золотого мяча» и «Бриллиантового мяча». Суперкубок УЕФА и Суперкубок Испании Барселона взяла в 2009-2010, а победителем Лиги чемпионов стала в 2010-2011 годах. До 2016 года действителен нынешний контракт Месси с Барселоной.'},
        {'name': 'Криштиану Роналду', 'pic': 'img/fs/ronaldu.jpg', 'picsport': 'img/fball.png', 'desc': '«Реал Мадрид» является клубом, за который играет Роналду. Его стоимость составляет девяность миллионов евро. Первый контракт он подписал в возрасте десяти лет с клубом «Насьонал», а с «Спортингом» уже на следующий год, там он находился в молодежной академии. За один сезон он играл за все составы в этой команде, чего ранее никогда не происходило. За взрослый состав он дебютировал в 2001 году, забив гол в первом же тайме этой игры. В молодежную сборную Португалии был принят в том же году. Тренер «Ливерпуля» заметил его, когда Роналду было ещё шестнадцать лет, но в клубе решили, что еще неопытен и слишком молод. А игроков команды «Юнайтед» впечатлила игра молодого футболиста летом 2003 года, и они убедили руководство с Роналду подписать контракт. В 2003 году в августе Роналду дебютировал в новой команде, а в ноябре забил первый гол. Стал в 2006 году первым, кто получил два раза подряд награду «Лучшего футболиста месяца в Премьер-лиге» - в ноябре и сразу же в декабре. Впервые с капитанской повязкой вышел на поле в 2008 году и оба гола, забил в этом матче, а затем получил «Золотой мяч» по итогам года. В Реал Мадрид Роналду перешел в 2009 году в июне, где и играет до сих пор.'},
        {'name': 'Андрес Иньеста', 'pic': 'img/fs/3.jpg', 'picsport': 'img/fball.png', 'desc': 'Играет Иньеста за клуб «Барселона». Его стоимость шестьдесят миллионов евро. В основном составе «Барселоны» Иньеста дебютировал в 2002 году, выступил в одиннадцати матчах и забил в чемпионате Испании первый гол. Больше, чем какой-либо другой игрок в команде сыграл в сезоне 2004-2005 – из 38 матчей он сыграл в 37. Он был в то время самый многообещающий полузащитник в Европе и поэтому оказался в национальной сборной Испании. Крайне травматичным для футболиста оказался сезон 2008-2009, но это не помешало ему стать героем полуфинала, забив на последних секундах игры гол. Однако в начале следующего сезона выйти на поле все-таки помешали травмы.'}]


    basketball_players = [
        {'name': 'Клайд Дрекслер', 'pic': 'img/bs/Дрекслер.jpg', 'picsport': 'img/bball.jpg', 'desc': 'Родился в Новом Орлеане, в 1963 году. Является игроком на позициях атакующего защитника, а также легкого форварда. Клайд в 1995 году входил в состав «Хьюстон Рокетс» и в это время в ассоциации назван был чемпионом, а ранее Олимпийским чемпионом в 1992 году. Заслужил прозвище «скользящий» в спортивном мире. 25 трипл-даблов сделал в НБА на протяжении всей своей карьеры, из-за чего а списке НБА занял почетное десятое место. Кстати, в список НБА, как «самый знаменитый игрок в истории» входит именно Клайд. Это все потому, что баскетболист смог за свою карьеру набрать двадцать тысяч очков, он сделал шесть тысяч подборов и шесть тысяч передач. За «Порттленд» Дрекслер выступал большую часть своей карьеры, после этого перешел в «Хьюстон», принеся ему на чемпионате НБА уже в первом сезоне полную победу. Лучшим баскетболистом мира спортсмена назвали в 1996 году.'},
        {'name': 'Деннис Родман', 'pic': 'img/bs/Родман.jpg', 'picsport': 'img/bball.jpg', 'desc': 'В 1961 году родился в городе Трентон. В клубе «Чикаго Булз» начал свою спортивную карьеру, где играли и известные баскетболисты, такие как Скотти Пиппен и Майкл Джордан. Деннис, также играл, кроме «Чикаго Булз», за известные клубы, такие как «Даллас Маверикс» и «Лос-Анджелес Лейкерс». Имеет в баскетбольной лиге довольно много наград. Родман в шоу бизнесе тоже является огромным любимчиком: в разнообразных радио и телешоу он принимает самое активное участие и снялся в фильме, «Колония», в 1997 году, где играл и Жан-Клод Ванн Дам. Также баскетболист, помимо всего выше перечисленного, написал книгу под названием «Хочу быть хуже всех». Занимает в НБА почетную должность тренера с 2000 года.'},
        {'name': 'Джордж Майкен', 'pic': 'img/bs/Майкен.jpg', 'picsport': 'img/bball.jpg', 'desc': 'Почти во всех профессиональных баскетбольных лигах играл Джордж Майкен, а также в ассоциациях США. Победа в семи чемпионатах на его счету. В рейтинге лучших игроков сезона, Джордж занимал почетное место три раза. Баскетболист, помимо этого, принимал четыре раза участие в матче, в котором играли все известнейшие игроки. Майкен, после того, как завершил спортивную карьеру, основал Американскую баскетбольную ассоциацию и стал почетным её основателем. Затем основал «Миннесота Тимбервулз», баскетбольную команду, которая в НБА добивается колоссальных успехов уже не один год. В зал славы баскетболистов он был включен в числе пятидесяти лучших игроков НБА и мира.'}]


    volleyball_players = [
        {'name': 'Шашкова Любовь', 'pic': 'img/vb/sokolova.jpg', 'picsport': 'img/vball.jpg', 'desc': 'Является выдающей спортсменкой, участницей, а также победительницей международных первенств наивысшего мирового уровня по волейболу. Заслуженный, что естественно, мастер спорта России родилась 4 декабря 1977 года в городе Москва. На сегодняшний момент является нападающей стамбульского клуба “Фенербахче”. Также, Шашкова выступает на соревнованиях за сборную России. Любовь является двукратной чемпионкой мира 2006 и 2010 годов. Плюс к этому Шашкова получила серебряную медаль на олимпийских играх 2000 и 2004 годов.'},
        {'name': 'Максим Михайлов', 'pic': 'img/vb/mikhaylov.jpg', 'picsport': 'img/vball.jpg', 'desc': 'Российский волейболист. Родился 19 марта 1988 года в посёлке Кузьмоловский (Ленинградская область). Дебют спортсмена в сборной России по волейболу состоялся в 2008 году 14 июля. Проходил матч Мировой лиги, когда Россия играла с Кореей, именно тогда Михайлов и показал, на что он реально способен. На сегодняшний момент заслуженный мастер спорта Максим Михайлов играет в составе команды клуба “Зенит”, а также выступает за сборную России.'},
        {'name': 'Ольга Фатеева', 'pic': 'img/vb/fateeva.jpg', 'picsport': 'img/vball.jpg', 'desc': 'Является российской волейболисткой, мастером спорта международного класса. Родилась Фатеева 4 мая 1984 года на Украине в городе Павлоград (Днепропетровская область). Заслуг у этой волейболистки хватает – она и трёхкратная чемпионка России, и Чемпионка мира в 2010 году, и обладательница Кубка России за 2006 и 2007 года, и финалистка Лиги чемпионов в 2003, 2008, а также финалистка Кубка ЕКВ за 2006 год. Что же касается конкретно 2008 и 2009 годов, то Фатеева в этот период признана самой результативной волейболисткой чемпионата России. В 2011 году Ольга стала призёром чемпионата Польши.'}]


    tennis_players = [
        {'name': 'Марат Сафин', 'pic': 'img/ts/safin.jpg', 'picsport': 'img/tball.jpg', 'desc': 'Является титулованным российским спортсменом, замечательным теннисистом и заслуженным мастером спорта России. Родился Марат в 1980 году 27 января в городе Москва. Главным достижением Сафина – это то, что он является бывшей первой ракеткой всего мира в одиночном разряде. Данный спортсмен выиграл огромное количество различных чемпионатов и обыграл многих хороших теннисистов. В 2009 году Сафин закончил свою профессиональную спортивную карьеру.'},
        {'name': 'Мария Шарапова', 'pic': 'img/ts/sharapova.jpg', 'picsport': 'img/tball.jpg', 'desc': 'Очень известная российская теннисистка. Родилась Мария в 1987 году 19 апреля. Шарапова является экс первой ракеткой всего мира в одиночном стиле. Шарапова 3 раза выигрывала турнир Большого Шлема. Мария победила на 27 турнирах WTA (24 – в одиночном разряде, 3 – в парном). Также, данная спортсменка является обладательницей кубка Федерации за 2008 год.'},
        {'name': 'Елена Дементьева', 'pic': 'img/ts/dementeva.png', 'picsport': 'img/tball.jpg', 'desc': 'Является известной российской теннисисткой и заслуженным мастером спорта. Родилась Дементьева в 1981 году 15 октября. В 2008 году она стала Олимпийской Чемпионкой, а в 2000 году на Олимпийских играх выиграла серебро. В 2005 году Елена становится обладательницей Кубка Федерации. В общем, Дементьевой удалось выиграть 4 турнира Большого Шлема. Помимо этого, Дементьевой было присвоено звание бывшей третьей ракетки мира в одиночном стиле, плюс экс первой ракетки России.'}]

    data = {}
    if sport == 'football':
        data = {'name': football_players[id]['name'],
                'pic': football_players[id]['pic'],
                'picsport': football_players[id]['picsport'],
                'desc': football_players[id]['desc']}
    if sport == 'basketball':
        data = {'name': basketball_players[id]['name'],
                'pic': basketball_players[id]['pic'],
                'picsport': basketball_players[id]['picsport'],
                'desc': basketball_players[id]['desc']}
    if sport == 'volleyball':
        data = {'name': volleyball_players[id]['name'],
                'pic': volleyball_players[id]['pic'],
                'picsport': volleyball_players[id]['picsport'],
                'desc': volleyball_players[id]['desc']}
    if sport == 'tennis':
        data = {'name': tennis_players[id]['name'],
                'pic': tennis_players[id]['pic'],
                'picsport': tennis_players[id]['picsport'],
                'desc': tennis_players[id]['desc']}

    return render(request, 'sportsmen.html', data)
