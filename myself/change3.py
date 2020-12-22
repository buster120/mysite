"""

嫦娥五号任务的全过程:Change5LandedOnTheMoon
param   Category    类别
param   TheCountry  所属国家
param   DevelopmentOrganization 研制单位
param   CurrentState    目前状态
param   LEOCarryingCapacity LEO运载能力
param   GTOCarryingCapacity GTO运载能力
param   TheLengthOfTheArrow 箭体长度
param   DesignReliability   设计可靠度


运载发射:CarrierLaunch
地月转移:EarthMoonTransfer
近月制动:BrakingInRecentMonths
环月飞行:LunarFlight
月面下降:LunarDescent
月面采样:LunarSampling
月面上升:LunarAscent
交会对接:RendezvousAndDocking
环月等待:LunarWaiting
月地转移:LunarGroundTransfer
轨道分离:OrbitalSeparation
再入回收:ReentryAndRecovery

"""

"""
模拟长征5号登月返回全过程：
运载发射
地月转移
近月制动
环月飞行
月面下降
月面采样
月面上升
交会对接
环月等待
月地转移
轨道分离
再入回收

"""
class Change5LandedOnTheMoon():

    Category = 'Large carrier rocket'
    TheCountry='China'
    DevelopmentOrganization = 'China Academy of Launch Vehicle Technology'
    CurrentState = 'active service'
    LEOCarryingCapacity = '25 tons'
    GTOCarryingCapacity = '14 tons'
    TheLengthOfTheArrow = '56.97 meters'
    DesignReliability = '98%'


    def __init__(self,reason):
        self.reason=reason
        #reason决定是否说出选择发射地点的原因


    def Process(self):
    #嫦娥五号任务的全过程
        print('嫦娥五号任务的全过程如下：\n')


    def CarrierLaunch(self): #reason
    #运载发射
        print('运载发射!!!')
        print('长征五号所在的国家是'+self.TheCountry)
        print('带上实验仪器')
        print('带上返回时所需要的燃料和助推器')
        print('火箭很重，重量高达8.2吨')
        print('发射地点：海南文昌')
        if self.reason:
            print("选择文昌的原因有两点：")
            print('第一，文昌靠近赤道，借着地球的自转可以获得更大的推力')
            print("第二，长征五号太胖了，我们管它叫'胖五'")
        print('\n')


    def EarthMoonTransfer(self):
    #地月转移
        print('地月转移!!!')
        print('火箭点火一脚油门，冲着月球直线飞过去好不好呢？')
        print('好是好，但这么干实在是太费燃料了，火箭得一直加速才能保持直线运行，没有哪个国家能耗得起。')
        print('卫星也是，直着飞你就得一直点火，不点火就会慢慢减速，最后被地球引力拉回来。')
        print('但是围着地球转不耗费能量，')
        print('到变轨点的时候加一下速，卫星跳到更高的轨道，跳几次之后，就能到地月霍曼转移轨道上')
        print('嫦娥一号是经过三次变轨才跳到霍曼转移轨道')
        print('嫦娥二号是经过一次变轨才跳到霍曼转移轨道')
        print('嫦娥三号是经过一次变轨才跳到霍曼转移轨道')
        print('嫦娥四号是经过一次变轨才跳到霍曼转移轨道')
        print('嫦娥五号重8.2吨，比嫦娥四号可胖多了，四号才3吨重，小玉兔140公斤')
        print('嫦娥五号是经过2次变轨后才跳到霍曼转移轨道的！')
        print('\n')


    def BrakingInRecentMonths(self):
    #近月制动
        print('近月制动!!!')
        print('所谓近月制动，就是指靠近月球的时候，需要踩刹车减速。')
        print('这是因为地月距离远，探测器一路上以非常快的速度奔向月球。')
        print('不过，月球的引力是很小的，只有地球的六分之一。')
        print('所以，要想探测器被月球的引力捕获绕着月球转，就要将飞行速度，降低到月球的逃逸速度，也就是2.38km/s以下。')
        print('这个减速要减得恰到好处，减得少了就会从月球身旁擦肩而过。')
        print('减得猛了，速度太慢就有可能直接掉在月球上。')
        print('可以说，近月制动是探测器飞行过程中，最为关键的一次轨道控制。')
        print('\n')


    def LunarFlight(self):
    #环月飞行
        print('环月飞行!!!')
        print('既然要登陆月球，那么为什么探测器不一鼓作气直接登陆，而是还要转上几圈呢？')
        print('主要有四个原因：')
        print('首先，刚刚被月球捕获后的探测器，还处在距离月球比较远的轨道上，所以还需要逐渐减速，以减小轨道半径，减小探测器与月面的距离。')
        print('其次，减速之后到达的环月轨道，往往并不会精确的经过我们预计的着陆点，随便降落那是不行的，所以还需要一些时间来调整轨道的位置。')
        print('第三个原因是，在地球上发射是有时间窗口的，地球不转到特定位置不能发射，还得看天气，比如来台风了就不能发射。')
        print('最后一个原因是，着陆前还要进行各项测试工作。')
        print('\n')


    def LunarDescent(self):
    #月面下降
        print('月面下降!!!')
        print('等到轨道调整好了，位置、高度、地面光照、时机都OK了，阳光温热、岁月静好，接下来就可以下降着陆了。')
        print('在这里，我们得首先介绍一下嫦娥五号探测器的具体构造')
        print('由于五号还要返回地球，所以要比四号复杂的多。')
        print('嫦娥五号探测器由轨道器、返回器、着陆器和上升器4个器组成。')
        print('两两一组。')
        print('轨道器、返回器是一组，着陆器和上升期算一组。')
        print('首先，着陆器载着上升器下到月面进行采样，采样后的样品被装进上升器，然后点火升空与轨返组合体结合，残忍地留下着陆器独守月面。')
        print('然后样品转移到返回器，再残忍丢掉没用的上升器。')
        print('之后，有翅膀的轨道器带着返回器回地球，到达大气层后，把返回器扔回来，任务完成。')
        print('去的时候800多吨，回来的时候，就是一个返回器，带2公斤月球土壤。')
        print('下面我们就具体看看，嫦娥五号是怎么完成月面下降的。')
        print('当嫦娥五号探测器进入高度200公里的环月圆轨道准备下降的时候，会一气之下把自己拆成两部分。')
        print('一部分叫做轨返组合体，由轨道器和返回器组成，这一部分是不参与着陆的，在天上转圈等着。')
        print('另一部分叫做着陆上升组合体，由上升器和着陆器组成。')
        print('根据计划，具体的降落地点是月球最大的月海——风暴洋北缘的吕姆克山附近。')
        print('为什么选在这儿呢？科学家指出，这是因为，风暴洋地区形成时间相对较晚，是研究月球构成的绝佳地点。')
        print('另外，此处距离美国“阿波罗计划”的6次着陆点有较远的距离，距离大概都在1000多公里之外，所以说不定会有新的发现。')
        print('我们要选择平整的地方降落，还要找土壤厚的地方。')
        print('结果显示，在这片区域中，土壤最深处有十多米，这些地方就是合适的着陆点。')
        print('选好位置之后，就可以开始下降了。')
        print('与之前的几次探月任务一样，整个下落过程是着陆器自主完成的，')
        print('它会自己判断高度，自己知道什么时候减速，自己决定该去哪不该去哪。')
        print('\n')


    def LunarSampling(self):
    #月面采样
        print('月面采样!!!')

        print('成功软着陆之后，探测器会按照计划取月球土壤样品。')

        print('这次的取样安排了两种方式，一种是用电铲铲取土壤，也就是挖一锹。')

        print('另外它还带个钻机，在月球上打个孔，打孔过程中就套进去一管土，预计深2米，这2米长都会原样带回来，')

        print('我们钻了一个孔，相当于把几亿年的月球土壤都带了一些样本，非常划算。')

        print('两种样本将一共重2公斤。')

        print('以上说的每一步都非常不容易，那可不是在地球上。')

        print('没有人在现场操作，而且，月球没有大气，挖掘机的润滑油会瞬间蒸发；')

        print('月球温度太高，或者太低，热胀冷缩效果明显，在地球上能自由伸缩，到月球上可能就卡住了；')

        print('月球重力小，往下一使劲，铲子没下去，铲车飞起来了，这都是要考虑到的。')

        print('还有各种宇宙辐射影响电路，月球灰尘堵塞，等等一大堆问题，有无数的困难需要克服。')

        print('费这么大劲怎么就取这么点土呢？多挖点不行吗？')

        print('我们现在还没这个能力。能安全带回2公斤已经不错了。')

        print('苏联三次成功无人登月，一共只带回来355克。')

        print('美国6次载人成功登月，每次都带回来很多月球土壤和岩石，一共是381公斤。')

        print('如果按50公斤一个人来算，美国相当于带回来7个大人和一个小孩。')

        print('1978年，美国国家安全事务顾问布热津斯基来访中国，曾经赠送给我国1克重的月球土壤')

        print('就这么点土壤，我们得拿放大镜看，那还分成2半，一半收藏在北京天文馆，一半用来研究。')

        print('就凭这 0.5 克月球土壤，我们国家的科研人员那是翻来覆去研究了几十年，并硬是写出了11篇论文。')

        print('\n')

    def LunarAscent(self):
    #月面上升
        print('月面上升!!!')
        print('月球表面土壤采样完成之后，全部的样品会放在上升器里，进行无污严密封装。')
        print('随后，上升器携带着这些月球土特产起飞，进入15km×180km的近月椭圆轨道。')
        print('这个上升器，其实就相当于一个小型的月面发射的火箭。')
        print('在地球发射火箭，得有一个发射场，搭一个发射架，')
        print('一群人忙活很长时间，竖起火箭，各种调试，加装燃料，然后才是点火，收架子，起飞。')
        print('但在月球上，这些全都没有，降落在哪，就在那挖土，然后起飞。')
        print('拿嫦娥五号的几个腿找平，这些都得自动完成，然后自动点火发射。')
        print('挖土的起飞之后，留在月面上的登陆器除了当发射架以外，还有其他实验任务，')
        print('具体什么探测中子、低频电磁波之类的就不提了，关键是它弹出一面国旗。')
        print('只用1秒钟，月球的五星红旗尺寸为2米×0.9米，这么大一共只有12克，而且永不退色。')
        print('\n')

    def RendezvousAndDocking(self):
    #交会对接
        print('交会对接!!!')

        print('上升器从月球表面起飞后，只能进行短距离的飞行。')

        print('起飞之后就要继续变轨，与在月球轨道转圈的轨道器实现交会对接。')

        print('这是“针尖”对“针尖”的对接，地球上根本无法提供数据和测控支持，全看它们自己的本事。')

        print('整个对接过程有5千米，140米和20米这三个关键停泊点，在这三个位置上，探测器都会停一停看一看，并做出一系列的位置调整。')

        print('直到轨道器和上升器越来越近，然后啪一下，用小爪给钩住。')

        print('对接成功后，上升器会将样品转移到返回器的样品舱内。注意，这是个关键步骤。')

        print('\n')

    def LunarWaiting(self):
    #环月等待
        print('环月等待!!!')
        print('就跟去月球前在地球绕圈一样，这回是在月球打秋千，寻找在变轨点加速的时机。')
        print('之前留下着陆器，现在还要扔下上升器，就把肚子里那点土和外壳留着。')
        print('苏联三次只带回来355克土壤的原因就是缺少这一步，它是把上升器整个带回来了，带着这个多余的上升器返回地球就要多耗费能量。')
        print('发射能力限制住了你最多只能带多少燃料，这就把返回的能量限制住了，唯一的办法，只能少带。')
        print('而我们相当于卡车把货运来，我们把卡车扔掉，只留货物，这样才实现2公斤的运载。')
        print('这叫样品容器转移。转移之后，就剩轨道器和返回器。上升器是留在轨道上吗？')
        print('不是，它没有必要围着月亮一直转，它的使命已经完成，它的结果是受控落月。')
        print('\n')
    def LunarGroundTransfer(self):
    #月地转移
        print('月地转移!!!')
        print('还走月地霍曼转移轨道。')
        print('轨道器最后一次点火加速。')
        print('飞奔回地球。')
        print('\n')

    def OrbitalSeparation(self):
    #轨道分离
        print('轨道分离!!!')
        print('距离地球5000公里的时候，把轨道器再扔了')
        print('不过你要说轨道器把返回器扔了也行，反正是它们俩分开了。')
        print('\n')

    def ReentryAndRecovery(self):
    #再入回收
        print('再入回收!!!')

        print('最危险的时刻实际是在最后。')

        print('表面看起来，把返回器扔回地球这件事，实在太简单了，瞄准地球一扔不就完了？那么明显的目标，还怕打不着吗？')
        print('问题在于，速度太快了。')
        print('能不能太空刹车呢？开始就说了，太空没法刹车，刹车一种方式是耗费燃料的喷火，但这个时候的燃料需要带着去月球，又从月球返回来，要给两次加速一次减速增加负担，实在是成本太高')
        print('我们根本没法打这个预算，实际到第11步的时候，返回燃料就已经用光了。没有刹车燃料。')
        print('那不减速行不行呢？不行。')
        print('如果从月球直接杀回地球，那飞船的速度已经到了每秒11.2公里的第二宇宙速度，比卫星速度还高1.44倍。')
        print('卫星回来都烧成那样，这个返回器直接砸下来就会变成一颗流星。没落地就得烧光。')
        print('那不白忙活了吗？')
        print('我们玩一把绝的。大气层打水漂。专业术语叫半弹道跳跃式再入返回。')
        print('就是严格控制返回角度，在大气层里先打一个水漂，让速度减下来，然后会被弹飞，这个时候，再启动返回器的发动机，给重新压回大气层，这次的速度达到安全返回条件了。')
        print('这个难点是严格控制角度，角度大了，返回器就崩飞了；')
        print('角度小了，返回器就直接砸地球上烧毁，误差要控制在正负0.2°。')
        print('几乎是差一点都不行。')
        print('然后再像普通卫星一样，调整姿态，隔热层朝下落回大气层，突破等离子黑障，然后自动开伞，安全降落。')
        print('实现这一步，嫦娥五号的任务才算圆满完成。')
        print('\n')


class Change5():
    change=Change5LandedOnTheMoon(1)

    change.Process()
    #全过程
    change.CarrierLaunch()
    #运载发射
    change.EarthMoonTransfer()
    #地月转移
    change.BrakingInRecentMonths()
    #近月制动
    change.LunarFlight()
    #环月飞行
    change.LunarDescent()
    #月面下降
    change.LunarSampling()
    #月面采样
    change.LunarAscent()
    #月面上升
    change.RendezvousAndDocking()
    #交会对接
    change.LunarWaiting()
    #环月等待
    change.LunarGroundTransfer()
    #月地转移
    change.OrbitalSeparation()
    #轨道分离
    change.ReentryAndRecovery()
    #再入回收

if __name__ == '__main__':
    Change5()
