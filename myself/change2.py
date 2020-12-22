

"""
:class LongMarch5SeriesLaunchVehicle  长征5号运载火箭
param   category    类别
param   TheCountry  所属国家
param   DevelopmentOrganization 研制单位
param   CurrentState    目前状态
param   LEOCarryingCapacity LEO运载能力
param   GTOCarryingCapacity GTO运载能力
param   TheLengthOfTheArrow 箭体长度
param   DesignReliability   设计可靠度

function    __init__                初始化，点火
function    ProcedureTurn           程序转弯
function    BoostersOff             助推器脱离
function    FairingOff              整流罩脱离
function    TwoStageEngineShutdown  二级发动机关闭
function    SecondaryGnition        二级发动机二次点火
function    StarArrowSeparation     星箭分离

"""


class LongMarch5SeriesLaunchVehicle():
    Category = 'Large carrier rocket'
    TheCountry = 'China'
    DevelopmentOrganization = 'China Academy of Launch Vehicle Technology'
    CurrentState = 'active service'
    LEOCarryingCapacity = '25 tons'
    GTOCarryingCapacity = '14 tons'
    TheLengthOfTheArrow = '56.97 meters'
    DesignReliability = '98%'

    def __init__(self):
        print('长征5号点火！')

    def ProcedureTurn(self):
        print('起飞后17s')
        print('程序转弯')
        print('目的是沿着地球倾斜度飞行，以节省火箭燃料')

    def BoostersOff(self):
        print('飞行到约174秒')
        print('火箭四个助推器完成任务')
        print('与火箭主体脱离')

    def FairingOff(self):
        print('285秒')
        print('此时长征五号已经飞出大气层')
        print('保护有效载荷的顶部整流罩结束了自己的使命')
        print('与火箭分离')

    def TwoStageEngineShutdown(self):
        print('约753秒')
        print('二级发动机关闭')
        print('火箭进入滑行阶段')

    def SecondaryGnition(self):
        print('约1355秒')
        print('二级发动机进行二次点火')

    def StarArrowSeparation(self):
        print('约1714秒')
        print('火箭二级发动机在达到预定目标后停止工作')
        print('96秒以后')
        print('星箭分离')
        print('火箭将有效载荷送到预定轨道')
        print('长征五号火箭就此完成了它的全部使命')

    def getCategory(self):
        return self.Category

    def setCategory(self, category):
        self.Category = category

    def getTheCountry(self):
        return self.TheCountry

    def setTheCountry(self, country):
        self.TheCountry = country

    def getDevelopmentOrganization(self):
        return self.DevelopmentOrganization

    def setDevelopmentOrganization(self, organization):
        self.DevelopmentOrganization = organization

    def getCurrentState(self):
        return self.CurrentState

    def setCurrentState(self, state):
        self.CurrentState = state

    def getLEOCarryingCapacity(self):
        return self.LEOCarryingCapacity

    def setLEOCarryingCapacity(self, LEO):
        self.LEOCarryingCapacity = LEO

    def getGTOCarryingCapacity(self):
        return self.GTOCarryingCapacity

    def setGTOCarryingCapacity(self, GTO):
        self.GTOCarryingCapacity = GTO

    def getTheLengthOfTheArrow(self):
        return self.TheLengthOfTheArrow

    def setTheLengthOfTheArrow(self, length):
        self.TheLengthOfTheArrow = length

    def getDesignReliability(self):
        return self.DesignReliability

    def setDesignReliability(self, ability):
        self.DesignReliability = ability


"""
:class  Ascenders   上升器
param   StorageDevice   存储设备

function    __init__    初始化
function    setStorageDevice    将采集到的月球土壤放入存储装置中
function    getStorageDevice    将月球土壤送入其他设备
function    TakeOff             上升器起飞，进入环月轨道
function    RendezvousandDocking    上升器与轨道器和返回器组合体交会对接，将样品容器安全转移至返回器中
function    Separation          升器与轨道器和返回器组合体成功分离
function    ControlledFallMonths    上升器受控落月

"""


class Ascenders():
    StorageDevice = ''

    def __init__(self):
        self.StorageDevice = '空'

    def setStorageDevice(self):
        self.StorageDevice = '采集到的月球土壤'

    def getStorageDevice(self):
        return self.StorageDevice

    def TakeOff(self):
        print('嫦娥五号上升器3000N发动机工作约6分钟')
        print('成功将携带样品的上升器送入到预定环月轨道')

    def RendezvousandDocking(self):
        print('嫦娥五号上升器成功与轨道器和返回器组合体交会对接')
        print('将样品容器安全转移至返回器中')

    def Separation(self):
        print('嫦娥五号上升器与轨道器和返回器组合体成功分离')

    def ControlledFallMonths(self):
        print('嫦娥五号上升器按照地面指令受控离轨')
        print('降落在月面经度0度、南纬30度附近的预定落点')


"""
:class  Lander  着陆器

function    VariableThrustEngine    变推力发动机
function    AttitudeAdjustment      姿态调整
function    ObstacleDetection       障碍自动检测
function    Falling                 下降
function    LunarSoilStructureDetector  月壤结构探测
function    ScrapingoftheSoil       机械臂在月球表面抓取土壤
function    DrilledSoil             钻具钻取土壤
function    TranslateSoil           将月球土壤送入上升器
"""


class Lander():
    def VariableThrustEngine(self):
        print('变推力发动机启动')
        print('将探测器相对月球速度从约1.7千米/秒降为零')

    def AttitudeAdjustment(self):
        print('进行快速姿态调整')
        print('逐渐接近月表')

    def ObstacleDetection(self):
        print('进行障碍自动检测')

    def Falling(self):
        print('选定着陆点后')
        print('开始避障下降和缓速垂直下降')

    def LunarSoilStructureDetector(self):
        print('开启月壤结构探测仪')

    def ScrapingoftheSoil(self):
        print('机械臂在月球表面抓取土壤')

    def DrilledSoil(self):
        print('钻具钻取土壤')

    def TranslateSoil(self):
        print('将月球土壤送入上升器')


"""
:class  Returner    返回器
param   Stroage     存储月球土壤
function    setStroage      放入月球土壤
function    getStroage      取出月球土壤
function    SeparatedfromOrbiter    返回器与轨道器分离
function    SlowDown        减速
function    Recycling       返回器回收

"""


class Returner():
    Stroage = ''

    def setStroage(self):
        self.Stroage = '月球土壤'

    def getStroage(self):
        return self.Stroage

    def SeparatedfromOrbiter(self):
        print('接近地球大约5000公里高度时')
        print('返回器与轨道器分离')
        print('返回器将独自以每秒约11公里的第二宇宙速度返回地球')

    def SlowDown(self):
        print('返回器进入地球大气层')
        print('减速后将再次跳出大气层并第二次进入大气层')
        print('返回器再入地球大气层的速度将从十几公里每秒降低到七公里多每秒')
        print('这是科技人员设计的半弹道跳跃式返回办法')
        print('相当于在太空“打水漂”')
        print('以安全落地')

    def Recycling(self):
        print('返回器回收')


"""
:class  轨道器

function    MovetoMoon  地月转移
function    BrakingatPerilune   近月制动
function    Separation      与着陆器和上升器分离
function    KeepTrack       轨道器携返回器留轨
function    Docking         与上升器对接
function    DetachfromRiser 轨道器与上升器分离
function    MonthtoTransfer 轨道器月地转移
function    ReleaseReturner 释放返回器

"""


class Orbiter():
    def MovetoMoon(self):
        print('地月转移')

    def BrakingatPerilune(self):
        print('近月制动')

    def Separation(self):
        print('与着陆器和上升器分离')

    def KeepTrack(self):
        print('轨道器携返回器留轨')

    def Docking(self):
        print('与上升器对接')
        print('将月球土壤样品转移')

    def DetachfromRiser(self):
        print('轨道器与上升器分离')

    def MonthtoTransfer(self):
        print('轨道器月地转移')

    def ReleaseReturner(self):
        print('释放返回器')


"""
:class  ChangE_5    嫦娥5号
param   ascenders   上升器
param   lander      着陆器
param   returner    返回器
param   orbiter     轨道器
"""


class ChangE_5():
    ascenders = Ascenders()
    lander = Lander()
    returner = Returner()
    orbiter = Orbiter()

    """
    轨道器：
    地月转移
    近月制动
    与着陆区和上升器分离
    轨道器留轨
    """
    orbiter.MovetoMoon()
    orbiter.BrakingatPerilune()
    orbiter.Separation()
    orbiter.KeepTrack()

    """
    着陆器：
    启动变推力发动机
    姿态调整
    障碍自动检测
    避障下降和缓速垂直下降
    开启月壤结构探测仪
    机械臂在月球表面抓取土壤
    钻具钻取土壤
    将月球土壤送入上升器
    """
    lander.VariableThrustEngine()
    lander.AttitudeAdjustment()
    lander.ObstacleDetection()
    lander.Falling()
    lander.LunarSoilStructureDetector()
    lander.ScrapingoftheSoil()
    lander.DrilledSoil()
    lander.TranslateSoil()

    """
    上升器:
    存储采集到的月球土壤
    将携带样品的上升器送入到预定环月轨道
    上升器与轨道器和返回器组合体交会对接，将样品容器安全转移至返回器
    上升器与轨道器和返回器组合体分离
    上升器按照地面指令受控离轨降落
    """
    ascenders.setStorageDevice()
    ascenders.TakeOff()
    ascenders.RendezvousandDocking()
    ascenders.Separation()
    ascenders.ControlledFallMonths()

    """
    轨道器:
    月地转移
    释放返回器
    """
    orbiter.MonthtoTransfer()
    orbiter.ReleaseReturner()

    """
    返回器:
    返回器与轨道器分离
    半弹道跳跃式返回办法减速
    返回器回收
    """
    returner.SeparatedfromOrbiter()
    returner.SlowDown()
    returner.Recycling()


if __name__ == '__main__':
    change5 = ChangE_5()

