# ------------------------------------------------------
# -------------------- points_input.py --------------------
# ------------------------------------------------------
import sys
from PyQt5.QtWidgets import  QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.pylab as plt
import numpy as np

    
class Points_Input(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent) 
        self.TRAIN_BUTTON = QWidget
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        

        # Creating de graph
        self.fig = plt.figure(2)
        self.ax = plt.subplot()
        self.canvas = FigureCanvas(self.fig)  
        self.canvas.setFocus()
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.layout.addWidget(self.canvas) 
         
        self.init_graph()

        self.classes = []
        self.selected_class = []
        self.points = {}

        self.plane = []
        self.maped = True
        
        self.canvas.draw()
    
    def onclick(self, event):
        plt.figure(2)

        if self.maped:
            self.algorithm.input_layer = [event.xdata, event.ydata]
            class_output = self.algorithm.forward()
            class_type = self.class_type(class_output)
            self.ax.scatter(event.xdata, event.ydata, s=10, c=self.classes[class_type][1], marker='o')
        elif self.selected_class:
            plt.scatter(event.xdata, event.ydata, s=10, marker='o', c=self.selected_class[1])
            
            if self.selected_class[0] in self.points.keys():
                self.points.get(self.selected_class[0]).append([event.xdata, event.ydata])
            else:
                self.points[self.selected_class[0]] = [[event.xdata, event.ydata]]

        self.canvas.draw()

        if len(self.points.keys()) >= 3:
            self.TRAIN_BUTTON.setEnabled(True)

    def update_scatter_colors(self):
        plt.figure(2)
        self.ax = plt.gca()
        if not self.maped:
            self.clearPlot()
        for _class in self.points.items():
            points = _class[1]
            for point in points:
                plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

        self.canvas.draw()

    def init_graph(self):
        plt.figure(2)
        # plt.tight_layout()
        self.ax = plt.gca()
        self.fig.set_facecolor('#323232')
        self.ax.grid(zorder=0)
        self.ax.set_axisbelow(True)
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        self.ax.set_xticks(range(-5,6))
        self.ax.set_yticks(range(-5,6))
        self.ax.axhline(y=0, color='#323232')
        self.ax.axvline(x=0, color='#323232')
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.tick_params(axis='x', colors='#b1b1b1')
        self.ax.tick_params(axis='y', colors='#b1b1b1')

    def clearPlot(self):
        self.maped = False
        plt.figure(2)
        plt.clf()
        self.init_graph()
        self.canvas.draw()

    def set_donut(self):
        self.selected_class.clear()
        self.points.clear()
        self.clearPlot()

        SIZE = 10

        class_a = np.linspace(2.5,4.5,8)
        class_b = np.linspace(1.5,2,4)
        class_c = np.linspace(.2,1,5)

        theta = np.linspace(0, 2*np.pi, 60)
        for rad in class_a:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[0][1])           
                if self.classes[0][0] in self.points.keys():
                    self.points.get(self.classes[0][0]).append([x1, x2])
                else:
                    self.points[self.classes[0][0]] = [[x1, x2]]
        theta = np.linspace(0, 2*np.pi, 30)
        for rad in class_b:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[1][1])
                if self.classes[1][0] in self.points.keys():
                    self.points.get(self.classes[1][0]).append([x1, x2])
                else:
                    self.points[self.classes[1][0]] = [[x1, x2]]
        theta = np.linspace(0, 2*np.pi, 10)
        for rad in class_c:
            for t in theta:
                x1 = rad*np.cos(t)
                x2 = rad*np.sin(t)
                self.ax.scatter(x1, x2, s=SIZE, c=self.classes[2][1])
                if self.classes[2][0] in self.points.keys():
                    self.points.get(self.classes[2][0]).append([x1, x2])
                else:
                    self.points[self.classes[2][0]] = [[x1, x2]]
        self.canvas.draw()

    def set_map(self):
        self.selected_class.clear()
        self.points.clear()
        self.clearPlot()

        map = {'1': [[-0.4813362410180009, 0.6367826942149781], [-0.7544243096977539, 0.24755223526818781], [-0.9763083655000528, 0.12778901713071367], [-1.3688724642271977, -0.26144144181607665], [-1.522484502859558, -0.5009678780910249], [-1.6419605329069498, -0.8901983370378153], [-1.6078245243219813, -1.1896063823815002], [-1.4030084728121661, -1.5488960367939226], [-1.0275123783775069, -2.147712127481293], [-0.7544243096977539, -2.147712127481293], [-0.22531617663073256, -1.9980081048094505], [0.13311191351144291, -1.788422473068871], [0.6622200465784642, -1.5788368413282914], [0.8329000895033092, -1.069843164244027], [1.1059881581830622, -0.6207310962284991], [1.0718521495980928, -0.021915005541128352], [1.0547841453056082, 0.786486716886821], [0.8158320852108245, 0.9361907395586639], [0.4232679864836806, 1.355362003039823], [-0.0546361337058876, 0.7266051078180844], [-0.49840424531048555, 0.09784821259634491], [-0.7373563054052692, -0.2913822463504454], [-0.9421723569150835, -0.7105535098316045], [-1.1128523998399293, -0.920139141572184], [-0.9592403612075682, -1.3093696005189743], [-0.7544243096977539, -1.5488960367939226], [-0.3447922066781244, -1.638718450397028], [0.1501799178039276, -1.3093696005189743], [0.3549959693137419, -1.1896063823815002], [0.5939480294085255, -0.7704351189003411], [0.6622200465784642, -0.2913822463504454], [0.5598120208235562, 0.18767062619945118], [0.18431592638889605, 0.30743384433692533], [-0.24238418092321723, -0.4710270735566562], [-0.6008122710653927, -0.9800207506409206], [-0.5325402538954549, -1.0399023597096582], [0.01363588346405109, -0.8901983370378153], [0.30379195643628876, -0.35126385541918204], [0.18431592638889605, -0.32132305088481417], [-0.5496082581879387, -0.5009678780910249]], '2': [[-1.2152604255948365, 0.9062499350242952], [-1.6419605329069498, 0.9661315440930318], [-2.0174566273416104, 1.1457763712992435], [-2.3929527217762705, 1.2655395894367167], [-2.6148367775785695, 1.5649476347804026], [-2.8025848247958995, 1.774533266520982], [-2.973264867720745, 2.22364533453651], [-3.075672893475652, 2.5829349889489315], [-3.161012914938075, 3.0320470569644584], [-3.1098089020606214, 4.0200936065986195], [-3.1098089020606214, 4.079975215667357], [-3.161012914938075, 4.738672915423464], [-2.870856841965838, 4.768613719957832], [-2.666040790456023, 4.7087321108890965], [-2.136932657389002, 4.738672915423464], [-1.5907565200294966, 4.469205674614148], [-1.07871639125496, 4.559028088217254], [-0.6520162839428467, 4.5889688927516215], [0.11604390921895824, 4.918317742629675], [-0.22531617663073256, 4.529087283682884], [0.5598120208235562, 4.529087283682884], [1.174260175353, 4.738672915423464], [1.2596001968154233, 4.738672915423464], [-2.751380811918446, 3.810507974858041], [-2.6148367775785695, 3.241632688705039], [-2.290544696021363, 2.493112575345826], [-1.983320618756641, 2.103882116399035], [-1.7443685586618578, 1.774533266520982], [-1.4883484942745895, 1.5350068302460338], [-1.1128523998399293, 1.3254211985054543], [-0.6690842882353305, 1.3254211985054543], [-0.36186021097060905, 1.5948884393147704], [0.20138393068138072, 2.463171770811458], [0.5598120208235562, 2.373349357208353], [1.0889201538905775, 2.0440005073302983], [-2.1881366702664558, 3.7506263657893033], [-1.6590285371994344, 2.7625798161551423], [-1.2493964341798058, 1.9841188982615616], [-0.8226963268676917, 2.103882116399035], 
        [-0.9421723569150835, 2.792520620689512], [-1.1981924213023518, 3.4212775159112496], [-1.4371444813971355, 3.780567170323671], [-0.5496082581879387, 3.63086314765183], [-0.31065619809315503, 3.241632688705039], [-0.5496082581879387, 2.7326390116207744], [0.6110160337010102, 3.9901528020642516], [0.679288050870948, 3.6009223431174604], [0.20138393068138072, 3.211691884170671], [0.30379195643628876, 3.7506263657893033], [1.0889201538905775, 2.8224614252238798], [1.2596001968154233, 2.373349357208353], [1.3961442311552998, 1.6248292438491392], [1.4644162483252376, 1.2355987849023489], [1.7033683084200213, 1.8942964846584562], [1.7033683084200213, 2.253586139070878], [1.6180282869575988, 2.6128757934832993], [1.4132122354477836, 3.690744756720566], [1.2937362054003918, 3.7506263657893033], [1.6350962912500835, 4.109916020201725], [1.8569803470523825, 3.4212775159112496], [2.0105923856847427, 2.6128757934832993], [1.942320368514805, 1.8643556801240875], [1.6350962912500835, 0.45713786700876735], [1.3790762268628152, -0.3812046599535508], [1.5497562697876601, -1.1297247733127636], [1.9764563770997743, -0.4410862690222874], [2.1812724286095886, -0.17161902821297126], [2.812788587431516, 1.1457763712992435], [2.164204424317104, 1.2954803939710855], [2.1300684157321346, 0.6068418896806103], [2.386088480119403, 0.786486716886821], [2.590904531629217, 0.8164275214211898], [2.659176548799156, 1.654770048383508], [2.437292492996857, 1.9841188982615616]], '3': [[1.9764563770997743, 4.559028088217254], [2.164204424317104, 3.900330388461146], [2.5226325144592803, 3.241632688705039], [2.6762445530916406, 2.6128757934832993], [2.915196613186424, 2.073941311864667], [3.0688086518187845, 1.5350068302460338], [2.983468630356363, 0.9062499350242952], [2.7957205831390315, 0.06790740806197704], [2.539700518751765, -0.5309086826253937], [2.369020475826918, -0.8003759234347099], [2.1812724286095886, -1.1596655778471323], [2.044728394269712, -1.5788368413282914], [1.9252523642223203, -1.908185691206345], [1.8228443384674131, -2.0578897138781875], [1.6863003041275366, -2.5369425864280837], [1.4644162483252376, 
        -3.40522591792477], [1.3449402182778458, -3.824397181405929], [1.3108042096928765, -3.9741012040777717], [1.3278722139853611, -4.303450053955825], [1.720436312712506, -4.782502926505722], [1.993524381392259, -4.842384535574459], [2.369020475826918, -4.872325340108827], [3.137080668988723, -4.752562121971353], [3.5467127720083518, -4.483094881162037], [3.956344875027982, -4.692680512902616], [4.451316999510034, -4.483094881162037], [4.724405068189787, -4.542976490230774], [4.792677085359724, -3.2555218952529277], [4.912153115407117, -2.117771322946924], [4.792677085359724, -1.638718450397028], [4.639065046727364, 0.008025798993239519], [4.673201055312333, 0.4271970624743986], [4.707337063897302, 0.8463683259555577], [4.843881098237178, 2.1637637254677724], [4.843881098237178, 2.6128757934832993], [4.929221119699601, 4.0200936065986195], 
        [4.809745089652209, 4.409324065545411], [4.314772965170157, 4.678791306354727], [3.973412879320467, 4.648850501820359], [3.4443047462534455, 4.738672915423464], [2.915196613186424, 4.7087321108890965], [2.3007484586569813, 4.858436133560938], [2.556768523044248, 4.1398568247360945], [2.932264617478909, 3.5410407340487247], [3.4443047462534455, 3.5709815385830925], [3.922208866443013, 3.5709815385830925], [4.348908973755126, 3.5410407340487247], [3.358964724791022, 4.1398568247360945], [3.751528823518168, 2.5829349889489315], [3.137080668988723, 2.3134677481396153], [3.6661888020557445, 2.1937045300021403], [4.109956913660342, 2.0440005073302983], [4.1611609265377965, 1.2355987849023489], [3.751528823518168, 0.8164275214211898], [3.4955087591308995, 0.3373746488712932], [3.085876656111269, -0.1416782236786025], [2.6933125573841252, -0.5907902916941303], [2.4202244887043722, -1.4590736231908172], [2.266612450072012, -2.566883390962452], [2.0105923856847427, -3.1656994816498223], [1.8228443384674131, -3.5249891360622443], [1.993524381392259, -3.914219595009035], [2.317816462949464, -4.033982813146509], [2.6762445530916406, -3.914219595009035], [2.932264617478909, -3.854337985940298], [4.058752900782888, -3.5549299405966126], [2.6933125573841252, -3.1357586771154535], [3.2736247033286006, -3.1956402861841906], [3.3931007333759915, -3.824397181405929], [4.127024917952827, -3.9741012040777717], [4.297704960877672, -2.4770609773593466], [3.5467127720083518, -2.626765000031189], [3.256556699036116, -2.3572977592218725], [2.7445165702615792, -2.0578897138781875], [3.085876656111269, -1.339310405053343], [3.751528823518168, -0.4710270735566562], [4.178228930830281, -0.4710270735566562], [4.024616892197919, -1.339310405053343], [3.4955087591308995, -2.1776529320156612], [4.24650094800022, -0.7704351189003411], [3.580848780593321, -1.2494879914502377]], '4': [[1.1913281796454847, -1.4291328186564485], [1.2083961839379693, -1.9980081048094505], [1.0377161410131235, -2.447120172824978], [0.7987640809183398, -3.1656994816498223], [0.6451520422859796, -3.794456376871561], [0.4744719993611337, -3.8842787904746663], [0.06483989634150422, -4.123805226749615], [-0.0546361337058876, -4.21362764035272], [-0.3277242023856397, -4.542976490230774], [0.2696559478513194, -4.812443731040091], [0.4744719993611337, -4.842384535574459], [0.6622200465784642, -2.2974161501531354], [0.3549959693137419, -2.507001781893715], [0.01363588346405109, -2.746528218168663], [-0.3277242023856397, -2.746528218168663], [-0.8226963268676917, -2.5968241954968203], [-1.5566205114445273, -2.507001781893715], [-1.8297085801242803, -2.117771322946924], [-1.9662526144641568, -1.5189552322595539], [-2.2393406831439093, -1.7285408640001334], [-2.478292743238693, -1.8483040821376076], [-2.6831087947485077, -2.2974161501531354], [-2.9903328720132296, -2.8962322408405057], [-3.3658289664478893, -3.5848707451309814], [-3.4853049964952816, -3.764515572337192], [-3.8095970780524877, -4.123805226749615], [-3.9120051038073953, -4.123805226749615], [-4.321637206827024, -4.513035685696405], [-4.714201305554169, -4.842384535574459], [-4.475249245459385, -4.902266144643196], [-3.7071890522975806, -4.812443731040091], [-3.6047810265426734, -4.812443731040091], [-2.870856841965838, -4.483094881162037], [-2.358816713191301, -4.692680512902616], [-1.846776584416765, -3.9741012040777717], [-1.5395525071520426, -4.093864422215246], [-1.2323284298873212, -3.9741012040777717], [-1.07871639125496, -4.063923617680878], [-0.7202883011127845, -4.303450053955825], [-0.583744266772908, -4.782502926505722], [-1.0445803826699906, -4.812443731040091], [-1.300600447057259, -4.752562121971353], [-1.6078245243219813, -4.722621317436984], [-2.256408687436394, -4.513035685696405], [-2.478292743238693, -4.722621317436984], [-2.7172448033334766, -4.662739708368248], [-3.041536884890683, -3.734574767802824], [-2.785516820503415, -3.495048331527876], [-2.2393406831439093, -2.327356954687504], [-2.3076127003138476, -2.626765000031189], [-2.4612247389462083, -3.01599545897798], [-1.9150486015867028, -3.0758770680467165], [-1.6078245243219813, -3.3154035043216648], [-0.7714923139902385, -2.986054654443611], [-0.6178802753578774, -2.926173045374874], [-0.0546361337058876, -3.1656994816498223], [0.11604390921895824, -3.2255810907185594], [0.25258794355883474, -3.2555218952529277], [-0.1911801680457632, -3.7046339632684555], [-0.44720023243303153, -3.5848707451309814], [-0.856832335452661, -3.5848707451309814], [-1.0445803826699906, -3.5848707451309814], [-1.5395525071520426, -3.5848707451309814], [-2.631904781871054, -3.465107526993507], [-2.290544696021363, -3.794456376871561], [-2.5465647604086312, -4.033982813146509], [-2.1540006616814864, -3.734574767802824]], '5': [[-1.795572571539311, 0.21761143073381906], [-2.1198646530965175, -0.2315006372817079], [-2.1881366702664558, -0.32132305088481417], [-2.444156734653724, -0.7105535098316045], [-2.666040790456023, -1.0997839687783948], [-2.9561968634282603, -1.6686592549313968], [-3.3316929578629204, -2.3572977592218725], [-3.6047810265426734, -2.8064098272374], [-4.133889159609694, -3.465107526993507], [-4.4581812411669, -3.734574767802824], [-4.7824733227241065, -3.9741012040777717], [-4.662997292676716, -3.1357586771154535], [-4.765405318431623, 
        -2.9561138499092428], [-4.748337314139138, -2.2974161501531354], [-4.5605892669218075, -1.219547186915869], [-4.611793279799262, -0.6806127052972357], [-4.731269309846653, -0.2315006372817079], [-4.731269309846653, 0.45713786700876735], [-4.748337314139138, 1.20565798036798], [-4.799541327016591, 1.774533266520982], [-4.594725275506777, 2.8224614252238798], [-4.765405318431623, 3.2715734932394067], [-4.594725275506777, 4.738672915423464], [-4.86781334418653, 4.4392648700797785], [-4.850745339894045, 4.2296792383392], [-4.4581812411669, 4.858436133560938], [-4.338705211119509, 4.82849532902657], [-4.08268514673224, 4.768613719957832], [-3.7242570565900652, 4.798554524492202], [-3.5877130222501887, 4.559028088217254], [-3.690121048005096, 3.9901528020642516], [-3.7071890522975806, 3.5709815385830925], [-3.6047810265426734, 3.091928666033196], [-3.570645017957704, 2.7026982070864065], [-3.502373000787766, 2.103882116399035], [-3.3999649750328587, 1.20565798036798], [-3.1268769063531057, 0.8763091304899264], [-2.6831087947485077, 0.7266051078180844], [-2.478292743238693, 0.5170194760775049], [-2.3929527217762705, 0.36731545340566196], [-2.597768773286085, -0.08179661460986587], [-2.819652829088384, -0.3812046599535508], [-3.1439449106455903, -0.8303167279690786], [-3.673053043712611, -1.4590736231908172], [-3.997345125269818, -2.2974161501531354], [-4.202161176779632, -2.626765000031189], [-4.304569202534539, -2.566883390962452], [-4.099753151024725, -1.8183632776032397], [-4.031481133854787, -1.1896063823815002], [-4.150957163902179, -0.8901983370378153], [-4.270433193949571, -0.32132305088481417], [-4.304569202534539, 0.4870786715431361], [-4.2875011982420554, 1.4451844166429284], [-4.389909223996963, 2.4332309662770886], [-4.406977228289447, 2.8823430342926173], [-4.236297185364601, 3.930271192995514], [-4.202161176779632, 3.3015142977737764], [-4.065617142439756, 2.7625798161551423], [-3.8949370995149106, 2.1937045300021403], [-3.8608010909299413, 1.2954803939710855], [-3.6218490308351576, 0.5170194760775049], [-3.3316929578629204, 0.09784821259634491], [-3.0927408977681368, -0.1416782236786025], [-2.887924846258322, -0.2315006372817079], [-3.2122169278155286, -0.7404943143659732], [-3.3999649750328587, -0.7704351189003411], [-3.6389170351276423, -1.0997839687783948], [-3.8437330866374566, -1.489014427725186], [-3.8095970780524877, -0.6506719007628678], [-3.758393065175034, -0.5608494871597616], [-3.9290731080998795, -0.05185581007549711], [-4.099753151024725, 0.4271970624743986], [-4.270433193949571, 0.9960723486274006], [-4.355773215411993, 1.6847108529178767], [-4.406977228289447, 2.253586139070878]]}



        class_a = map['1']
        class_b = map['2']
        class_c = map['3']
        class_d = map['4']
        class_e = map['5']

        size = 10

        for item in class_a:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[0][1])
        for item in class_b:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[1][1])
        for item in class_c:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[2][1])
        for item in class_d:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[3][1])
        for item in class_e:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[4][1])

        self.points = map

        self.canvas.draw()

    def set_xor(self):
        self.selected_class.clear()
        self.points.clear()
        self.clearPlot()

        xor = {'1': [[-1.8809125930017339, 0.30743384433692533], [-1.6078245243219813, 0.2774930398025566], [-1.2152604255948365, 0.3972562579400307], [-0.8226963268676917, 0.2774930398025566], [-0.3959962195555784, 0.21761143073381906], [-0.17411216375327943, 0.3373746488712932], [-0.20824817233824788, 0.9062499350242952], [-0.20824817233824788, 1.4451844166429284], [-0.20824817233824788, 1.8643556801240875], [-1.0957843955474447, 1.7445924619866133], [-0.6690842882353305, 1.8344148755897187], [-0.4813362410180009, 1.80447407105535], [-1.4542124856896201, 1.774533266520982], [-1.7785045672468263, 1.8643556801240875], [-1.846776584416765, 1.654770048383508], [-1.8809125930017339, 1.20565798036798], [-1.8638445887092492, 0.6966643032837156], [-1.5054164985670742, 0.6367826942149781], [-1.4712804899821048, 1.2355987849023489], [-1.1981924213023518, 1.4451844166429284], [-0.8226963268676917, 1.2655395894367167], [-0.5666762624804234, 1.355362003039823], [-0.4813362410180009, 1.085894762230506], [-0.6520162839428467, 0.8463683259555577], [-0.9763083655000528, 0.8763091304899264], [-1.2493964341798058, 0.8463683259555577], [-0.5154722496029702, 0.5469602806118727], [0.09897590492647357, -0.26144144181607665], [0.09897590492647357, -0.7404943143659732], [0.13311191351144291, -1.2794287959846065], [0.11604390921895824, -1.3093696005189743], [0.16724792209641226, -1.7584816685345022], [0.4061999821911959, -1.7584816685345022], [0.7475600680408867, -1.7584816685345022], [0.7134240594559174, -1.6986000594657655], [1.1571921710605153, -1.6986000594657655], [1.6180282869575988, -1.8483040821376076], [1.8399123427598978, -1.7584816685345022], [1.8569803470523825, -1.1297247733127636], [1.891116355637351, -0.5309086826253937], [1.8057763341749284, -0.17161902821297126], [1.3790762268628152, -0.2913822463504454], [0.9353081152582163, -0.11173741914423463], [0.3549959693137419, -0.17161902821297126], [0.679288050870948, -0.32132305088481417], [0.8670360980882785, -0.35126385541918204], [0.6110160337010102, -0.5907902916941303], [0.6110160337010102, -0.7404943143659732], [0.679288050870948, -1.0399023597096582], [0.9353081152582163, -1.3093696005189743], [1.276668201107908, -1.339310405053343], [1.2596001968154233, -0.8303167279690786], [1.0547841453056082, -0.7704351189003411], [0.38913197789871123, -1.0399023597096582], [0.32085996072877254, -0.6207310962284991], [1.498552256910207, -1.4590736231908172], [1.5156202612026917, -0.7704351189003411]], '2': [[0.18431592638889605, 1.80447407105535], [0.18431592638889605, 1.3254211985054543], [0.20138393068138072, 0.7565459123524523], [0.2184519349738654, 0.2774930398025566], [0.4232679864836806, 0.30743384433692533], [0.6280840379934949, 0.2774930398025566], [1.003580132428155, 0.30743384433692533], [1.276668201107908, 0.3972562579400307], [1.5668242740801448, 0.3373746488712932], [1.8569803470523825, 0.4271970624743986], [1.7545723212974753, 1.0260131531617693], [1.8057763341749284, 1.4751252211772972], [1.7375043170049906, 1.8344148755897187], [1.0889201538905775, 1.80447407105535], [0.5427440165310724, 1.80447407105535], [0.7475600680408867, 1.80447407105535], [1.3790762268628152, 1.774533266520982], [1.2425321925229387, 1.4152436121085596], [0.5768800251160409, 1.355362003039823], [0.7646280723333714, 1.3853028075741909], [0.6110160337010102, 1.1158355667648747], [0.5256760122385877, 0.7565459123524523], [0.730492063748402, 0.786486716886821], [0.9011721066732479, 1.1457763712992435], [1.1230561624755468, 0.8463683259555577], [1.3449402182778458, 0.8463683259555577], [1.447348244032753, 1.20565798036798], [1.5497562697876601, 1.3853028075741909], [-1.8638445887092492, -0.26144144181607665], [-1.846776584416765, -0.6806127052972357], [-1.8809125930017339, -1.1596655778471323], [-1.8126405758317956, -1.6986000594657655], [-1.6419605329069498, -1.7285408640001334], [-1.300600447057259, -1.6986000594657655], [-1.0104443740850222, -1.788422473068871], [-0.6690842882353305, -1.8183632776032397], [-0.3959962195555784, -1.8183632776032397], [-0.17411216375327943, -1.8183632776032397], [-0.20824817233824788, -1.339310405053343], [-0.20824817233824788, -0.8303167279690786], [-0.20824817233824788, -0.32132305088481417], [-0.4130642238480631, -0.20155983274734002], [-0.7202883011127845, -0.32132305088481417], [-1.1981924213023518, -0.20155983274734002], [-1.5054164985670742, -0.11173741914423463], [-1.7102325500768885, -0.5907902916941303], [-1.7102325500768885, -0.920139141572184], [-1.6078245243219813, -1.339310405053343], [-1.4542124856896201, -1.3692512095877118], [-1.1811244170098671, -1.3692512095877118], [-0.805628322575207, -1.219547186915869], [-0.7373563054052692, -1.1896063823815002], [-0.7885603182827223, -0.8003759234347099], [-1.0616483869624753, -0.6506719007628678], [-1.300600447057259, -0.7105535098316045], [-1.3347364556422283, -0.8901983370378153], [-1.0616483869624753, -1.1297247733127636], [-0.9933763697925375, -1.069843164244027], [-0.6008122710653927, -1.4590736231908172], [-0.4813362410180009, -0.6506719007628678], [-0.4642682367255162, -1.0399023597096582]], '3': [[-1.8638445887092492, 2.7326390116207744], [-1.5566205114445273, 2.7026982070864065], [-1.0445803826699906, 2.6128757934832993], [-0.7202883011127845, 2.7625798161551423], [-0.31065619809315503, 2.642816598017669], [0.16724792209641226, 2.7625798161551423], [0.45740399506864904, 2.7625798161551423], [0.7646280723333714, 2.672757402552037], [1.1059881581830622, 2.523053379880194], [1.5156202612026917, 2.523053379880194], [1.993524381392259, 2.4032901617427207], [2.1300684157321346, 2.4032901617427207], [2.2324764414870426, 2.073941311864667], [2.1983404329020733, 1.3254211985054543], [2.2495444457795273, 0.8164275214211898], 
        [2.2324764414870426, 0.3972562579400307], [2.2324764414870426, -0.17161902821297126], [2.1812724286095886, -0.6806127052972357], [2.2495444457795273, -1.1896063823815002], [2.2495444457795273, -2.0578897138781875], [2.2495444457795273, -2.4171793682906095], [2.0617963985621968, -2.5968241954968203], [1.7033683084200213, -2.5968241954968203], [1.3790762268628152, -2.626765000031189], [1.1230561624755468, -2.686646609099926], [0.6110160337010102, -2.566883390962452], [0.25258794355883474, -2.5369425864280837], [-0.3789282152630937, -2.5369425864280837], [-0.6861522925278152, -2.7165874136342945], [-1.300600447057259, -2.626765000031189], [-1.6078245243219813, -2.5968241954968203], [-2.2052046745589404, -2.5968241954968203], [-2.3929527217762705, -2.327356954687504], [-2.4612247389462083, -1.8183632776032397], [-2.375884717483786, -1.069843164244027], [-2.1881366702664558, 0.06790740806197704], [-2.2052046745589404, 0.786486716886821], [-2.2734766917288782, 1.1457763712992435], [-2.2052046745589404, 2.073941311864667], [-2.2734766917288782, 2.5829349889489315], [-2.1198646530965175, 2.6128757934832993], [-2.358816713191301, -0.2913822463504454], [-2.5124287518236623, -0.7404943143659732], [-2.9903328720132296, -0.4410862690222874], [-3.2975569492779515, 1.4751252211772972], [-3.1098089020606214, 3.0320470569644584], [-2.939128859135776, 3.3015142977737764], [-2.8367208333808684, 1.9841188982615616], [-2.9561968634282603, 0.6068418896806103], [-3.0927408977681368, -1.7584816685345022], [-3.0244688805981985, -3.1656994816498223], [-2.3929527217762705, -3.914219595009035], [-1.8979805972942185, -3.5848707451309814], [-1.795572571539311, -3.6148115496653497], [-2.853788837673353, -3.1656994816498223], [-1.624892528614466, -3.734574767802824], [-0.3789282152630937, -3.6746931587340868], [0.23551993926635006, -3.5848707451309814], [1.1059881581830622, -3.6447523541997184], [1.8740483513448671, -3.2854626997872964], [2.369020475826918, -3.2255810907185594], [2.812788587431516, -2.447120172824978], [2.8469245960164855, -1.489014427725186], [2.8469245960164855, -0.11173741914423463], [2.8469245960164855, 1.4751252211772972], [2.7274485659690946, 2.523053379880194], [2.539700518751765, 3.511099929514355], [2.2324764414870426, 3.7506263657893033], [1.4644162483252376, 3.900330388461146], [1.0206481367206397, 4.050034411132989], [-1.2152604255948365, 4.4392648700797785], [-2.0857286445115486, 4.2296792383392], [-1.9321166058791874, 3.780567170323671], [-1.5907565200294966, 3.481159124979987], [-1.1811244170098671, 3.3913367113768818], [-0.44720023243303153, 3.481159124979987], [0.2696559478513194, 3.481159124979987], [1.1230561624755468, 3.511099929514355], [1.771640325589959, 3.1518102751019335], [2.095932407147166, 2.8524022297582476], [2.71038056167661, 1.5948884393147704], [-2.3246807046063322, 3.4512183204456175], [-2.7343128076259613, 2.1937045300021403], [-3.570645017957704, 1.1457763712992435], [-3.536509009372735, -0.05185581007549711], [-3.6047810265426734, -2.0279489093438188], [-3.3316929578629204, -3.105817872581085], [-3.1268769063531057, -3.764515572337192], [-2.5807007689936, -4.183686835818351], [-1.07871639125496, -4.692680512902616], [-0.31065619809315503, -4.60285809929951], [0.7475600680408867, -4.632798903833879], [1.7033683084200213, -4.4232132720932995], [2.539700518751765, -4.4232132720932995], [3.239488694743631, -4.483094881162037], [3.7173928149331985, -3.5249891360622443], [3.734460819225683, -0.7105535098316045], [3.683256806348229, 0.21761143073381906], [3.64912079776326, 2.253586139070878], [3.580848780593321, 3.900330388461146], [3.512576763423384, 4.109916020201725], [2.2495444457795273, 4.4392648700797785], [1.003580132428155, 4.7087321108890965], [0.1501799178039276, 4.738672915423464], [-1.0104443740850222, 4.648850501820359], [-2.068660640219064, 4.529087283682884], [-2.819652829088384, 4.469205674614148], [-3.4341009836178276, 4.349442456476673], [-3.8095970780524877, 3.660803952186198], [-3.980277120977333, 1.80447407105535], [-3.7242570565900652, 0.6367826942149781], [-3.9120051038073953, -1.7584816685345022], [-3.997345125269818, -2.147712127481293], [-4.185093172487148, -2.566883390962452], [-4.219229181072117, -3.01599545897798], [-4.031481133854787, -3.5249891360622443], [-2.3929527217762705, -4.542976490230774], [3.956344875027982, -4.303450053955825], [4.24650094800022, -3.9441603995434034], [4.690269059604818, -1.638718450397028], [4.468385003802519, -0.920139141572184], [3.6149847891782905, -1.8183632776032397], [3.46137275054593, -2.447120172824978], [4.4854530080950035, 1.1158355667648747], [4.178228930830281, 3.63086314765183], [4.041684896490404, 4.888376938095307], [3.410168737668476, 3.0021062524300905], [3.376032729083507, 0.4271970624743986], [3.3931007333759915, -0.08179661460986587], [4.058752900782888, 2.792520620689512], [4.55372502526494, 
        1.9541780937271929], [-4.304569202534539, 4.0200936065986195], [-4.662997292676716, 2.373349357208353], [-4.611793279799262, 0.45713786700876735], [-4.424045232581932, -1.638718450397028], [-4.321637206827024, -2.4171793682906095], [-4.133889159609694, -3.345344308856033], [-3.8608010909299413, -2.20759373655003], [-3.5877130222501887, -1.0099615551752894], [-3.536509009372735, -0.8303167279690786], [-3.8095970780524877, 2.8524022297582476], [-3.8266650823449724, 2.8524022297582476], [4.58786103384991, -2.3872385637562408], [4.417180990925065, -3.9741012040777717], [4.4342489952175494, -4.572917294765142], [2.6933125573841252, -4.273509249421457], [2.8981286088939395, -3.345344308856033], [3.410168737668476, -2.7764690227030315]]}


        class_a = xor['1']
        class_b = xor['2']
        class_c = xor['3']


        size = 10

        for item in class_a:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[0][1])

        for item in class_b:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[1][1])

        for item in class_c:
                self.ax.scatter(item[0], item[1], s=size, c=self.classes[2][1])

        self.points = xor

        self.canvas.draw()

    def fill_plot(self, algorithm, progress_bar, size = 30, dpi = 40):
        self.algorithm = algorithm
        self.clearPlot()
        self.init_graph()
        self.colors_class_type(len(self.classes))

        progress = 20 / dpi
        progress_count = 80

        x = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
        y = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
        self.plane.clear()

        for ind, i in enumerate(y):
            self.plane.append([])
            for j in x:
                self.algorithm.input_layer = [j,i]
                class_output = self.algorithm.forward()
                class_type = self.class_type(class_output)
                self.plane[ind].append(class_type)
                self.ax.scatter(j, i, s=size, c=self.colors_class[class_type], marker='s')
            progress_count += progress
            progress_bar.setValue(progress_count)

        for _class in self.points.items():
            points = _class[1]
            for point in points:
                plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

        self.canvas.draw()
        self.maped = True

    def normalize_class(self, class_vector):
        normalized_class = list(np.zeros(len(class_vector),dtype=np.int32))
        normalized_class[class_vector.index(max(class_vector))] = 1
        return normalized_class

    def class_type(self, class_vector):
        return class_vector.index(max(class_vector))

    def colors_class_type(self, classes_count):
        colors = ['red', 'black', 'darkgreen', 'navy', 'orange', 'yellowgreen', 'fuchsia', 'gold', 'cyan', 'pink', 'brown']
        self.colors_class = []
        for _ in range(classes_count):
            color = np.random.choice(colors)
            colors.pop(colors.index(color))
            self.colors_class.append(color)


    def show_lines(self, init_layer):
        neurons_count = len(init_layer)
        

        plt.figure(2)
        plt.clf()
        # self.init_graph()
        # plt.tight_layout()

        self.fig = plt.figure(2)
        ax1 = self.fig.add_subplot(121)   #top left
        self.init_lines(self.fig, ax1)
        tetha = init_layer[0].bias
        w1 = init_layer[0].weights[0]
        w2 = init_layer[0].weights[1]
        y = [(-(tetha/w1)/(tetha/w2))*-5+(-tetha/w1),(-(tetha/w1)/(tetha/w2))*5+(-tetha/w1)]
        x = [-5,5]
        ax1.plot(x,y, c='blue')
        # ax1.plot(5,y[1], c='blue')
        # ax1.fill_between(init_layer[0].weights[0], init_layer[0].weights[1], np.max(init_layer[0].weights[1]), color='#539ecd')
        # ax1.fill_between(init_layer[0].weights[0], init_layer[0].weights[1], color='#e89a7d')
        for _class in self.points.items():
            points = _class[1]
            for point in points:
                ax1.scatter(point[0], point[1], s=5, marker='o', c=self.classes[int(_class[0])-1][1])

        ax2 = self.fig.add_subplot(122)   #top right
        self.init_lines(self.fig, ax2)
        tetha = init_layer[1].bias
        w1 = init_layer[1].weights[0]
        w2 = init_layer[1].weights[1]
        y = [(-(tetha/w1)/(tetha/w2))*-5+(-tetha/w1),(-(tetha/w1)/(tetha/w2))*5+(-tetha/w1)]
        x = [-5,5]
        ax2.plot(x,y, c='blue')
        for _class in self.points.items():
            points = _class[1]
            for point in points:
                ax2.scatter(point[0], point[1], s=5, marker='o', c=self.classes[int(_class[0])-1][1])

        self.canvas.draw()

    def show_planes(self, size = 30, dpi = 40):
        self.figure = plt.figure(2)
        plt.clf()
        self.init_graph()
        self.ax = plt.gca()

        x = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))
        y = list(np.linspace(-5+size*0.005,5-size*0.005,dpi))

        for ind_y, i in enumerate(y):
            for ind_x, j in enumerate(x):
                class_type = self.plane[ind_y][ind_x]
                self.ax.scatter(j, i, s=size, c=self.colors_class[class_type], marker='s')

        for _class in self.points.items():
            points = _class[1]
            for point in points:
                plt.scatter(point[0], point[1], s=10, marker='o', c=self.classes[int(_class[0])-1][1])

        self.canvas.draw()

    def init_lines(self, fig, ax):
        fig.set_facecolor('#323232')
        ax.grid(zorder=0)
        ax.set_axisbelow(True)
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_xticks(range(-5,6))
        ax.set_yticks(range(-5,6))
        ax.axhline(y=0, color='#323232')
        ax.axvline(x=0, color='#323232')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='x', colors='#b1b1b1')
        ax.tick_params(axis='y', colors='#b1b1b1')




        