import streamlit as st
import requests

if "peta" not in st.session_state:
    st.session_state.peta = False

if "prasyarat" not in st.session_state:
    st.session_state.prasyarat = False

if "materi_prasyarat" not in st.session_state:
    st.session_state.materi_prasyarat=False

if "nilai_prasyarat" not in st.session_state:
    st.session_state.nilai_prasyarat = 0

if "materi" not in st.session_state:
    st.session_state.materi=False

if "adaptif" not in st.session_state:
    st.session_state.adaptif=False

if "kelompok" not in st.session_state:
    st.session_state.kelompok = {'kondisi1':True,'kondisi2':True,'kondisi3':False,'kondisi4':False,'kondisi5':False,
                                 'kondisi6':False,'kondisi7':False,'kondisi8':False,'kondisi9':False, 'kondisi10':False,
                                 'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False, 'kondisi15':False}

if "jawaban" not in st.session_state:
    st.session_state.jawaban = {"jawab1":0,"jawab2":0,"jawab3":0,"jawab4":0,"jawab5":0,
                                "jawab6":0,"jawab7":0,"jawab8":0,"jawab9":0,"jawab10":0}
if "lvl1" not in st.session_state:
    st.session_state.lvl1={"jwb1":'0',"jwb2":'0',"jwb3":'0',"jwb4":'0',"jwb5":'0'}

if "lvl2" not in st.session_state:
    st.session_state.lvl2={"jwb1":'0',"jwb2":'0',"jwb3":'0',"jwb4":'0',"jwb5":'0'}

if "pengecekan1" not in st.session_state:
    st.session_state.pengecekan1 = False
if "pengecekan2" not in st.session_state:
    st.session_state.pengecekan2 = False
if "cerita1" not in st.session_state:
    st.session_state.cerita1 = False
if "cerita2" not in st.session_state:
    st.session_state.cerita2 = False
if "cerita3" not in st.session_state:
    st.session_state.cerita3 = False
if "cerita4" not in st.session_state:
    st.session_state.cerita4 = False
if "cerita5" not in st.session_state:
    st.session_state.cerita5 = False
if "cerita6" not in st.session_state:
    st.session_state.cerita6 = False

kolom = st.columns(3)
with kolom[0]:
    nama = st.text_input("Nama: ")
with kolom[1]:
    kelas = st.text_input("Kelas: ")
with kolom[2]:
    sekolah = st.text_input("Sekolah: ")
    
st.markdown('''
            <style>
                #konsep{
                    font-family:"comic sans ms";
                    font-weight:bold;
                    font-size:40px;
                }
                #gambar{
                    background-image:url("https://res.cloudinary.com/dfkw4ux0e/image/upload/v1754881146/kover_mgjmyz.png");
                    width:1000px;
                    height:1000px;
                    object-fit:cover;
                }
                #gambar1{
                    background-image:url("https://res.cloudinary.com/dfkw4ux0e/image/upload/v1754892712/peta_konsep_uenvba.png");
                    width:1000px;
                    height:1000px;
                    object-fit:cover;
                    background-repeat:no-repeat;
                    background-size:cover;
                    width:600px;
                    height:800px;
                }
                .menu{
                    font-family: "snap itc";
                    font-size:25px;
                    color:yellow;
                    text-shadow:2px 2px 3px red, -2px -2px 3px blue;
                }
                .submenu{
                    font-family: "brush script mt";
                    font-size:20px;
                    color:cyan;
                    text-shadow:2px 2px 3px red, -2px -2px 3px blue;
                }
                #judul1{
                    font-family:"snap itc";
                    font-size:30px;
                    color:green;
                    text-shadow:2px 2px 3px yellow, -2px -2px 3px cyan;
                    
                }
                #latihan{
                    font-family:"bauhaus 93";
                    font-size:40px;
                    color:blue;
                    text-shadow:2px 2px 2px yellow, -2px -2px 2px cyan;
                    animation-name:animasi1;
                    animation-duration:4s;
                    animation-iteration-count: infinite;
                }
                @keyframes animasi1{
                    0%{color:blue; text-shadow:2px 2px 2px yellow, -2px -2px 2px cyan;}
                    100%{color:yellow; text-shadow:2px 2px 3px red, -2px -2px 3px green;}
                }
                .sublat1{
                    font-family:broadway;
                    font-size:20px;
                    color:red;
                }
                .sublat1::before{
                    font-family:"comic sans ms";
                    font-size:20px;
                    content:"* "; 
                    font-weight:bold;
                    color:cyan;
                }
                .label{
                    font-weight:900;
                    font-size:clamp(28px,4.6vw,46px);
                    letter-spacing:.03em;
                    color:#e0f7ff;
                    text-shadow:0 0 6px #79e4ff, 0 0 14px #79e4ff, 0 0 26px #00c2ff;
                    animation:flicker 3.5s infinite steps(60); 
                }
                @keyframes flicker{
                    0%, 18%, 20%, 22%, 25%, 53%, 57%, 100%{opacity:1; filter:brightness(1);}
                    19%, 21%, 24%, 55%{opacity:.4; filter:brightness(1.2)}
                    23%{opacity:.1; text-shadow:none}
                }
                .efek1{
                    font-family:"Bauhaus 93";
                    text-align:center;
                    font-weight:800;
                    font-size:clamp(28px,4.8vw,48px);
                    background:linear-gradient(90deg,#8a63ff,#64d2ff,#5cffb5,#ffdd57,#ff6aa2);
                    background-size:200% 100%;
                    -webkit-background-clip:text;
                    background-clip:text; color:transparent;
                    animation:hue 6s linear infinite;
                }
                @keyframes hue{
                    to{background-position:200% 0}
                }
            </style>
            ''',unsafe_allow_html=True)

def pemetaan():
    st.markdown('<div id="konsep">Peta Konsep</div>',unsafe_allow_html=True)
    st.markdown('<div id="gambar1"></div>',unsafe_allow_html=True)
    st.markdown('##### Pelajari video tentang persamaan dan pertidaksamaan satu variabel')
    st.video("https://youtu.be/OJhDRcYojt8?si=-igxq_rr3taW-Un5")
    st.markdown('##### Permainan tentang persamaan dan pertidaksamaan satu variabel')
    kode_html="""
    <!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Math Quest: Persamaan & Pertidaksamaan</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #6dd5fa, #2980b9);
      color: #fff;
      text-align: center;
      padding: 50px;
    }

    h1 {
      font-size: 2em;
      margin-bottom: 20px;
    }

    #game-box {
      background: rgba(0,0,0,0.3);
      padding: 20px;
      border-radius: 15px;
      width: 400px;
      margin: auto;
      box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }

    .btn {
      padding: 10px 20px;
      margin: 10px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-size: 16px;
      background: #27ae60;
      color: white;
      transition: 0.3s;
    }
    .btn:hover {
      background: #2ecc71;
    }

    #feedback {
      margin-top: 15px;
      font-size: 18px;
      font-weight: bold;
    }

    #score {
      margin-top: 20px;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <h1>🎮 Math Quest: Persamaan & Pertidaksamaan 🎮</h1>
  <div id="game-box">
    <p id="question">Klik "Mulai" untuk bermain!</p>
    <input type="text" id="answer" placeholder="Jawabanmu" />
    <br><br>
    <button class="btn" onclick="checkAnswer()">Jawab</button>
    <button class="btn" onclick="nextQuestion()">Soal Berikutnya</button>
    <div id="feedback"></div>
    <div id="score">Skor: 0</div>
  </div>

  <script>
    const questions = [
      {q: "2x + 5 = 11, berapakah x?", ans: 3},
      {q: "5x - 7 = 8, berapakah x?", ans: 3},
      {q: "3x + 2 < 11, nilai maksimum x adalah?", ans: 2},
      {q: "10 - 2x = 4, berapakah x?", ans: 3},
      {q: "x/2 + 4 = 7, berapakah x?", ans: 6},
      {q: "7x > 21, nilai terkecil x adalah?", ans: 4},
    ];

    let currentIndex = -1;
    let score = 0;

    function nextQuestion() {
      currentIndex = Math.floor(Math.random() * questions.length);
      document.getElementById("question").innerText = questions[currentIndex].q;
      document.getElementById("answer").value = "";
      document.getElementById("feedback").innerText = "";
    }

    function checkAnswer() {
      let userAns = document.getElementById("answer").value;
      if (userAns === "") {
        document.getElementById("feedback").innerText = "⚠️ Jawaban belum diisi!";
        return;
      }
      if (parseFloat(userAns) === questions[currentIndex].ans) {
        document.getElementById("feedback").innerText = "✅ Benar!";
        score += 10;
      } else {
        document.getElementById("feedback").innerText = "❌ Salah! Jawaban benar: " + questions[currentIndex].ans;
        score -= 5;
      }
      document.getElementById("score").innerText = "Skor: " + score;
    }
  </script>
</body>
</html>
    """
    st.components.v1.html(kode_html,height=500)

def kover():
    st.markdown('<div id="gambar"></div>',unsafe_allow_html=True)

if st.session_state.peta:
    pemetaan()
    
if st.session_state.kelompok['kondisi1']:
    kover()
if st.session_state.kelompok['kondisi2']:
    if st.sidebar.button("Peta konsep"):
        st.session_state.peta=True
        st.session_state.prasyarat = False
        st.session_state.kelompok['kondisi3']=True
        st.session_state.kelompok['kondisi1']=False
        st.session_state.adaptif=False
        st.session_state.materi = False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.rerun()

def soal_prasyarat():
    st.markdown("<div class='menu'>Soal Prasyarat</div>",unsafe_allow_html=True)
    st.markdown("<div class='submenu'>A. Operasi Bilangan Bulat dan Pecahan</div>",unsafe_allow_html=True)
    st.markdown("**1. Hitunglah:** $25-38$")
    st.session_state.jawaban['jawab1'] = st.text_input("Jawaban no.1")
    st.markdown("**2. Hitunglah:** $\\frac{2}{3}-\\frac{5}{6}$")
    st.session_state.jawaban['jawab2'] = st.text_input("Jawaban no.2")
    st.markdown("**3. Hitunglah:** $4-\\frac{7}{5}$")
    st.session_state.jawaban['jawab3'] =st.text_input("Jawaban no.3")
    st.markdown("<div class='submenu'>B. Operasi Aljabar Sederhana</div>",unsafe_allow_html=True)
    st.markdown("**4. Sederhanakan:** $3x+7x$")
    st.session_state.jawaban['jawab4']=st.text_input("Jawaban no.4")
    st.markdown("**5. Sederhanakan:** $5a-2a+4$")
    st.session_state.jawaban['jawab5'] = st.text_input("Jawaban no.5")
    st.markdown("6. jika $x=5$, hitunglah nilai dari $2x+7$")
    st.session_state.jawaban['jawab6'] = st.text_input("Jawaban no.6")
    st.markdown("<div class='submenu'>C. Sifat Keteraan</div>",unsafe_allow_html=True)
    st.markdown("7. Tentukan nilai x dari persamaan: $$x+4=10$$")
    st.session_state.jawaban['jawab7'] = st.text_input("Jawaban no.7")
    st.markdown("8. Tentukan nilai p dari persamaan: $$p-3=8$$")
    st.session_state.jawaban['jawab8'] = st.text_input("Jawaban no.8")
    st.markdown("9. Tentukan nilai y dari persamaan: $$3y=15$$")
    st.session_state.jawaban['jawab9'] = st.text_input("Jawaban no.9")
    st.markdown("10. Tentukan nilai k dari persamaan: $$\\frac{k}{4}=9$$")
    st.session_state.jawaban['jawab10'] = st.text_input("Jawaban no.10")
    skor = 0
    jwb=[]
    if st.button("Evaluasi 1"):
        kunci=[-13,-1/6,13/5,"10x","3a+4",17,6,11,5,36]
        for i in range(len(kunci)):
            if type(kunci[i])== str:
                if st.session_state.jawaban['jawab'+str(i+1)]==kunci[i]:
                    skor +=10
                    jwb.append(str(i)+". benar")
                else:
                    jwb.append(str(i)+". salah")
            else:
                if float(eval(st.session_state.jawaban['jawab'+str(i+1)]))==float(kunci[i]):
                    skor +=10
                    jwb.append(str(i)+". benar")
                else:
                    jwb.append(str(i)+". salah")

        if nama and kelas and sekolah:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdxhkFQ1ScEspHJi63Aan7nhNTdPLhIAaENpHEL1x7YZIQ2Pg/formResponse"
            data = {
            "entry.2105118839": nama,   # Ganti dengan entry ID dari form
            "entry.1000064761": kelas,   # Ganti dengan entry ID dari form
            "entry.16117725": sekolah,   # Ganti dengan entry ID dari form
            "entry.467232897": st.session_state.jawaban['jawab1'],   # Ganti dengan entry ID dari form
            "entry.47567283": st.session_state.jawaban['jawab2'],   # Ganti dengan entry ID dari form
            "entry.827650510": st.session_state.jawaban['jawab3'],   # Ganti dengan entry ID dari form
            "entry.718635572": st.session_state.jawaban['jawab4'],   # Ganti dengan entry ID dari form
            "entry.1207248362": st.session_state.jawaban['jawab5'],   # Ganti dengan entry ID dari form
            "entry.583635196": st.session_state.jawaban['jawab6'],   # Ganti dengan entry ID dari form
            "entry.60966000": st.session_state.jawaban['jawab7'],   # Ganti dengan entry ID dari form
            "entry.474515766": st.session_state.jawaban['jawab8'],   # Ganti dengan entry ID dari form
            "entry.1141432051": st.session_state.jawaban['jawab9'],   # Ganti dengan entry ID dari form
            "entry.1613081951": st.session_state.jawaban['jawab10'],   # Ganti dengan entry ID dari form
            "entry.1801227482": skor,   # Ganti dengan entry ID dari form
            }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
                
        if skor > 70:
            st.info(skor)
            st.success("Anda melanjutkan ke materi")
        else:
            st.session_state.nilai_prasyarat = skor
            st.error("Anda harus mempelajari prasyarat dengan menenkan tombol di bawah ini")
            st.session_state.kelompok['kondisi4']=False
            st.session_state.peta = False
            st.session_state.prasyarat = False
            st.session_state.materi_prasyarat = True
            st.session_state.pengecekan1 = False
            st.session_state.pengecekan2 = False
            st.session_state.cerita1=False
            st.session_state.cerita2=False
            st.session_state.cerita3=False
            st.session_state.cerita4=False
            st.session_state.cerita5=False
            st.session_state.cerita6=False
            st.rerun()
    
if st.session_state.prasyarat:
    soal_prasyarat()
if st.session_state.kelompok['kondisi3']:
    if st.sidebar.button("Prasyarat"):
        st.session_state.kelompok['kondisi4']=True
        st.session_state.peta = False
        st.session_state.adaptif=False
        st.session_state.prasyarat = True
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.rerun()
def materi_prasyarat_tampil():
    st.error("Nilai Anda: "+str(st.session_state.nilai_prasyarat))
    tulisan_html='''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #judul{
            text-align:center;
            font-family:"bauhaus 93";
            color:green;
            font-size:40px;
            text-shadow:2px 2px 2px orange, -2px -2px 2px red;
        }
        .subjudul{
            font-family:"comic sans ms";
            color:blue;
            font-weight:bold;
            font-size:25px;
            border:2px solid black;
            background-color:yellow;
            padding:10px;
            margin-top:10px;
            margin-bottom:10px;
            border-radius:10px;
        }
        .konten{
            font-size:20px;
            background-color:pink;
            border:2px solid black;
            border-radius:10px;
            box-shadow:0 0 2px 4px orange;
        }
        .contoh{
            background-color:lightskyblue;
            border-radius:5px;
            padding:5px;
            margin-right:50px;
        }
    </style>
     <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
      },
      svg: {
        fontCache: 'global'
      }
    };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js" async></script>
  <script src="https://www.geogebra.org/apps/deployggb.js"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
    <div id="judul" class="container-fluid p-5 bg-primary text-white text-center">Materi Penguasaan Prasyarat</div>
    <div class="subjudul container-fluid">Pengertian Bilangan Bulat dan Pecahan</div>
    <div class="container-fluid">
        <div class="konten">
        <ul>
            <li>Bulangan bulat: bilangan tanpa koma, meliputi bilangan negatif, nol, dan positif
                contoh:$-3, 0, 5, 17$
            </li>
            <li>
                Bilangan pecahan: bilangan yang ditulis dalam bentuk $\\frac{a}{b}$ dan $b\\neq{0}$ contoh: $\\frac{3}{4},-\\frac{7}{5},2\\frac{1}{2}$
            </li>
        </ul>
        </div>
    </div>
    <div class="subjudul">Operasi Hitung Bilangan Bulat</div>
    <div class="container-fluid">
        <div class="konten">
        <ul>
            <li>Penjumlahan dan pengurangan:
                <ul type="square">
                    <li>Jika tanda sama → jumlahkan nilainya, tanda ikut.
                        <div class="contoh">contoh: $5+7=12, 14+(-6)=-12$</div>
                    </li>
                    <li>Jika tanda berbeda → kurangi nilai yang lebih besar, tanda ikut bilangan yang lebih besar.
                        <div class="contoh">contoh: $8+(-3)=5, -9+5=-4$</div>
                    </li>
                </ul>
            </li>
            <li>Perkalian dan pembagian:
                <ul type="square">
                    <li>$positif\\times{positif}=positif$</li>
                    <li>$negatif\\times{negatif}=positif$</li>
                    <li>$negatif\\times{positif}=negatif$</li>
                    <li>$positif\\times{negatif}=negatif$</li>
                </ul>
            </li>
        </ul>
        </div>
    </div>
    <div class="subjudul">Operasi Hitung Pecahan</div>
    <div class="container-fluid">
        <div class="konten">
        <ul>
            <li>Penjumlahan/Pengurangan: samakan penyebut lalu hitung pembilangnya.
                <div class="contoh">
                    $\\frac{2}{3}+\\frac{1}{6}=\\frac{4}{6}+\\frac{1}{6}=\\frac{5}{6}$
                </div>
            </li>
            <li>
                Perkalian: kalikan pembilang dengan pembilang, penyebut dengan penyebut.
                <div class="contoh">
                     $\\frac{2}{5}+\\frac{3}{4}=\\frac{2\\times{3}}{5\\times{4}}=\\frac{6}{20}=\\frac{3}{10}$
                </div>
            </li>
            <li>
                Pembagian: ubah pembagian menjadi perkalian dengan kebalikan pecahan kedua.
                <div class="contoh">
                    $\\frac{2}{5}+\\frac{3}{4}=\\frac{2\\times{3}}{5\\times{4}}=\\frac{6}{20}=\\frac{3}{10}=\\frac{5}{6}$
                </div>
            </li>
        </ul>
        </div>
    </div>
    <div class="subjudul">Pengenalan Bentuk Aljabar</div>
    <div class="container-fluid">
        <div class="konten">
        <ul>
            <li>Pengertian: gabungan antara bilangan, variabel (huruf), dan operasi hitung.
                <div class="contoh">
                    contoh: $3x,5a+2,\\frac{y}{2}-7$
                </div>
            </li>
            <li>
                Suku sejenis: suku yang memiliki variabel dan pangkat sama.
                <div class="contoh">
                     contoh: $3x$ dan $5x$ → sejenis, bisa dijumlahkan/dikurangkan.
                </div>
            </li>
        </ul>
        </div>
    </div>
    <div class="subjudul">Sifat Kesetaraan</div>
    <div class="container-fluid">
        <div class="konten">
        Sebelum masuk PLSV formal, siswa harus bisa:
        <ul>
            <li>
                Mengisolasi variabel (memindahkan variabel ke satu sisi persamaan
            </li>
            <li>
                Menggunakan operasi invers (kebalikan) untuk mendapatkan nilai variabel.
            </li>
        </ul>
        <div class="contoh container p-3 my-3 border">
            <div>contoh: $x+5=12$.</div>
            <div>Kurangi 5 di kedua $x=7$</div>
        </div>
        </div>
    </div>
    <div class="subjudul">Menyelesaikan Persamaan Sederhana</div>
</body>
</html>
    '''
    st.components.v1.html(tulisan_html,height=2000)
if st.session_state.materi_prasyarat:
    materi_prasyarat_tampil()

def materi_tampilkan():
    st.markdown("<div id='judul1'>Persamaan Linear Satu Variabel (PLSV)</div>",unsafe_allow_html=True)
    st.image("https://asset.kompas.com/crops/tCZW4T6SVoqxPJlmXUcT9RlS0MI=/0x70:1593x1132/780x390/data/photo/2022/01/20/61e8de691fd31.png",width=400)
    st.markdown("""
    <div class='submenu'>&#128203; 1. Pengertian Persamaan Linear Satu Variabel</div>
    <ul>
        <li>Persamaan adalah kalimat matematika yang mengandung tanda sama dengan (=).</li>
        <li>Linear berarti berpangkat satu (tidak ada kuadrat, pangkat tiga, atau akar).</li>
        <li>Satu variabel artinya hanya melibatkan satu huruf (misalnya x atau y) yang nilainya belum diketahui.</li>
    </ul>
    <div>&#128073; Jadi, Persamaan Linear Satu Variabel (PLSV) adalah persamaan matematika yang hanya memiliki satu variabel dengan pangkat tertinggi satu.</div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class='submenu'>&#128203; 2. Bentuk Umum PLSV</div>
    """,unsafe_allow_html=True)
    st.latex("ax+b=0")
    st.markdown("""
    <div>dengan:</div>
    <ul>
        <li>a &ne; 0 (koefisien variabel),</li>
        <li>b bilangan real,</li>
        <li>x variabel.</li>
    </ul>
    <div>dengan:</div>
    <ul>
        <li>2x + 5 = 11</li>
        <li>3y - 7 = 9</li>
        <li>p + 9 = 20</li>
    </ul>
    <div class='submenu'>&#128203; 3. Ciri-Ciri PLSV</div>
    <ul>
        <li>Hanya ada satu variabel (x, y, p, dll).</li>
        <li>Pangkat variabel = 1.</li>
        <li>Mengandung tanda sama dengan (=).</li>
        <li>Dapat diselesaikan untuk menemukan nilai variabel.</li>
    </ul>
    <div class='submenu'>&#128203; 4. Cara Menyelesaikan PLSV</div>
    <ul>
        <li>Pisahkan variabel di satu sisi persamaan.</li>
        <li>Pindahkan suku-suku yang bukan variabel ke sisi lain dengan operasi kebalikan.</li>
        <li>Sederhanakan hasilnya.</li>
        <li>Peroleh nilai variabel.</li>
    </ul>
    <div class='submenu'>&#128203; 5. Contoh Penyelesaian</div>
    """,unsafe_allow_html=True)
    st.markdown("contoh 1: Tentukan nilai $x$ dari persamaan berikut: ")
    st.latex("3x+5=17")
    with st.expander("Lihat Penyelesaian"):
        st.markdown("kurangi ruas kiri dan kanan dengan $5$")
        st.latex("3x+5-5=17-5")
        st.latex("3x=12")
        st.markdown("bagi ruas kiri dan kanan dengan $3$")
        st.latex("\\frac{3x}{3}=\\frac{12}{3}")
        st.latex("x=4")
    st.markdown("Contoh 2: Tentukan nilai $x$ dari persamaan berikut: ")
    st.latex("7x-9=19")
    with st.expander("Lihat Penyelesaian"):
        st.markdown("Tambah ruas kiri dan kanan dengan $9$")
        st.latex("7x-9+9=19+9")
        st.latex("7x=28")
        st.markdown("bagi ruas kiri dan kanan dengan $7$")
        st.latex("\\frac{7x}{7}=\\frac{28}{7}")
        st.latex("x=4")
    st.markdown("""Contoh 3: Jumlah dua kali suatu bilangan dengan 8 sama dengan 20.
                bilangan tersebut""")
    with st.expander("Lihat Penyelesaian"):
        st.markdown("misalkan bilangan tersebut adalah x")
        st.markdown("Jumlah dua kai suatu bilangan dengan 8: $2x + 8$")
        st.markdown("Jumlah dua kai suatu bilangan dengan 8 sama dengan 20: $2x + 8 = 20$")
        st.markdown("Proses Penyelesaian")
        st.markdown("Kurangi ruas kiri dan kanan dengan $8$")
        st.latex("2x+8-8=20-8")
        st.latex("2x=12")
        st.markdown("bagi ruas kiri dan kanan dengan $2$")
        st.latex("\\frac{2x}{2}=\\frac{12}{2}")
        st.latex("x=6")
        
    st.markdown("Contoh 4: Jika $5x+4=2x+19$, tentukan nilai $x$ ")
    with st.expander("Lihat Penyelesaian"):
        st.markdown("Kurangi ruas kiri dan kanan dengan $4$")
        st.latex("5x+4-4=2x+19-4")
        st.latex("5x=2x+15")
        st.markdown("Kurangi ruas kiri dan kanan dengan $2x$")
        st.latex("5x-2x=2x+15-2x")
        st.latex("3x=15")
        st.markdown("Bagi ruas kiri dan kanan dengan $3$")
        st.latex("\\frac{3x}{3}=\\frac{15}{3}")
        st.latex("x=5")
    st.markdown("""<div id='latihan'>Latihan Soal</div>""",unsafe_allow_html=True)
    st.markdown("""<div class='sublat1'>Soal Langsung</div>""",unsafe_allow_html=True)
    st.markdown("**1. Tentukan Persamaan nilai x dari persamaan:**")
    st.latex("2x+7=15")
    st.text_input("Jawaban no. 1")
    st.markdown("**2. Selesaikan Persamaan Berikut:**")
    st.latex("9x-4=23")
    st.text_input("Jawaban no. 2")
    st.markdown("**3. Tentukan nilai x:**")
    st.latex("12=3x+6")
    st.text_input("Jawaban no. 3")
    st.markdown("**4. Jika $4x-5=11$, tentukan nilai x**")
    st.text_input("Jawaban no. 4")
    st.markdown("**5. Selesaikan persamaan:**")
    st.latex("7x+8=3x+20")
    st.text_input("Jawaban no. 5")
    st.markdown("""<div class='sublat1'>Soal Cerita</div>""",unsafe_allow_html=True)
    st.markdown("**6. Umur Dina 3 tahun lebih tua dari umur Rina. Jika jumlah umur mereka 27 tahun, tentukan umur Rina.**")
    st.text_input("Jawaban no. 6")
    st.markdown("**7. Sebuah bilangan jika dikalikan 4 hasilnya 28. Tentukan bilangan tersebut.**")
    st.text_input("Jawaban no. 7")
    st.markdown("**8. Jumlah dari 2 kali suatu bilangan dengan 5 sama dengan 19. Tentukan bilangan tersebut.**")
    st.text_input("Jawaban no. 8")
    st.markdown("**9. Harga sebuah buku tulis Rp2.500. Jika Andi membeli 4 buku tulis dan membayar Rp15.000, berapa uang kembalian Andi?**")
    st.text_input("Jawaban no. 9")
    st.markdown("**10. Selisih dua kali suatu bilangan dengan 7 adalah 15. Tentukan bilangan tersebut.**")
    st.text_input("Jawaban no. 10")
if st.session_state.materi:
    materi_tampilkan()
if st.session_state.kelompok['kondisi4']:
    if st.sidebar.button("Materi Persamaan"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.adaptif=False
        st.session_state.materi = True
        st.session_state.kelompok['kondisi5']=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.rerun()
        
def soal_adaptif():
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px;background-color:grey;">
                    <img src='https://i.pinimg.com/originals/48/59/55/485955115c68020ce3ba16bf18a95d8a.gif' style='width:100px;'></img>
                    <div class="label">Level Pertama</div>
                    </div>""",unsafe_allow_html=True)
    st.markdown("""
                **Tentukan nilai $x$ dari persamaan:**
                """)
    st.latex("x+7=15")
    st.session_state.lvl1["jwb1"] = st.text_input("Jawaban 1")
    st.markdown("**Jika $x-4=10$, maka berapakah nilai $x$**")
    st.session_state.lvl1["jwb2"] = st.text_input("Jawaban 2")
    st.markdown("**Tentukan penyelesaian dari persamaan:**")
    st.latex("2x=18")
    st.session_state.lvl1["jwb3"] = st.text_input("jawaban 3")
    st.markdown("**Jika $5x=25$, maka $x=$ ...**")
    st.session_state.lvl1["jwb4"] = st.text_input("jawaban 4")
    st.markdown("**cailah nilai $x$ yang memenuhi:**")
    st.latex("x+12=30")
    st.session_state.lvl1["jwb5"] = st.text_input("jawaban 5")
    kunci = [8, 14, 9, 5, 18]
    skor = 0
    if st.button("Evaluasi 1"):
        indeks=-1
        skor=0
        for i in st.session_state.lvl1:
            indeks +=1
            if int(st.session_state.lvl1[i])==kunci[indeks]:
                skor +=20
    if skor==100:
        st.session_state.pengecekan1=True
    
if st.session_state.adaptif:
    soal_adaptif()
def level_kedua():
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px; background-color:grey">
                    <img src='https://i.pinimg.com/originals/48/59/55/485955115c68020ce3ba16bf18a95d8a.gif' style='width:100px;'></img>
                    <div class="label">Level Kedua</div>
                    </div>""",unsafe_allow_html=True)
    st.markdown("**Tentukan nilai $x$ dari persamaan:**")
    st.latex("3x+5=20")
    st.session_state.lvl2['jwb1']=st.text_input("Jawaban 6")
    st.markdown("**Jika $4x-7=21$, maka $x=...$**")
    st.session_state.lvl2['jwb2']=st.text_input("Jawaban 7")
    st.markdown("**Tentukan Penyelesaian:**")
    st.latex("7x+9=30")
    st.session_state.lvl2['jwb3']=st.text_input("Jawaban 8")
    st.markdown("**Carilah nilai $x$ dari persamaan:**")
    st.latex("12-3x=0")
    st.session_state.lvl2['jwb4']=st.text_input("Jawaban 9")
    st.markdown("**Jika $2x+15=3x-5$**")
    st.session_state.lvl2['jwb5']=st.text_input("Jawaban 10")
    kunci1=[5,7,3,4,20]
    skor1 = 0
    if st.button("Evaluasi 2"):
        indeks1=-1
        skor1=0
        for i in st.session_state.lvl2:
            indeks1 +=1
            if int(st.session_state.lvl2[i])==kunci1[indeks1]:
                skor1 +=20
    if skor1==100:
        st.session_state.pengecekan2=True

if st.session_state.pengecekan1:
    level_kedua()

def level_ketiga():
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px;background-color:grey">
                    <img src='https://i.pinimg.com/originals/48/59/55/485955115c68020ce3ba16bf18a95d8a.gif' style='width:100px;'></img>
                    <div class="label">Level Ketiga</div>
                    </div>""",unsafe_allow_html=True)
    st.markdown("**Umur Budi 3 tahun lebih tua dari umur Andi. Jika jumlah umur mereka adalah 29 tahun, berapakah umur Andi?**")
    st.text_input("Jawaban 11")
    st.markdown("**Tentukan nilai $x$ pada persamaan:**")
    st.latex("\\frac{x}{3}+5=11")
    st.text_input("Jawaban 12")
    st.markdown("**Seorang pedagang membeli 5 buku dan 3 pensil dengan total harga Rp27.000. Jika harga sebuah buku Rp5.000, tentukan harga sebuah pensil dengan menggunakan persamaan satu variabel.**")
    st.text_input("Jawaban 13")
    st.markdown("**Carilah nilai $x$ pada persamaan**")
    st.latex("2(x-4)+3=11")
    st.text_input("Jawaban 14")
    st.markdown("**Panjang suatu persegi panjang adalah $x+5$ cm dan lebarnya $x-3$ cm. Jika kelilingnya 34 cm, tentukan nilai $x$**")
    st.text_input("Jawaban 15")
if st.session_state.pengecekan2:
    level_ketiga()
    
if st.session_state.kelompok['kondisi5']:
    if st.sidebar.button("Soal Level"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.adaptif=True
        st.session_state.kelompok['kondisi6']=True
        st.rerun()
def soal_cerita1():
    st.markdown("""
                <div class="efek1">Gotong Royong</div>""",unsafe_allow_html=True)
    st.image("https://quizizz.com/media/resource/gs/quizizz-media/quizzes/4204f59e-cf7a-4ec0-b2a7-d99f33f5d1e7",use_container_width=True)
    st.markdown("##### Warga sebuah desa bergotong royong membangun pos ronda.")
    st.markdown("""
                - ##### Pak Andi menyumbang Rp50.000. 
                - ##### Pak Budi menyumbang dua kali lipat dari sumbangan Pak Andi.
                - ##### Jumlah sumbangan Pak Candra adalah Rp20.000 lebih banyak dari sumbangan Pak Budi.
                """)
    st.markdown("##### Total sumbangan mereka bertiga adalah Rp220.000.")
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tentukan berapa sumbangan Pak Candra dengan menggunakan persamaan satu variabel.
                - ##### Bagaimana kegiatan gotong royong ini mencerminkan nilai persatuan dalam Pancasila?
                """)
if st.session_state.cerita1:
    soal_cerita1()
if st.session_state.kelompok['kondisi6']:
    st.sidebar.write("**Persamaan 1 variabel**")
    if st.sidebar.button("Gotong Royong"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=True
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi7']=True
        st.rerun()

def soal_cerita2():
    st.markdown("""
                <div class="efek1">Jujur dalam Jual Beli (Sila ke-2: Kemanusiaan yang Adil dan Beradab)</div>""",unsafe_allow_html=True)
    st.image("https://st2.depositphotos.com/26922084/44234/v/450/depositphotos_442342356-stock-illustration-male-salesman-is-working-at.jpg",use_container_width=True)
    st.markdown("##### Dina membuka kios kecil di sekolah. Ia menjual roti seharga Rp4.000 dan teh botol seharga Rp6.000.")
    st.markdown("""
                - ##### Suatu hari, Dina mencatat jumlah roti yang terjual adalah $x$. 
                - ##### Jumlah teh botol yang terjual adalah 2 lebih banyak dari jumlah roti.
                - ##### Uang hasil penjualan seluruhnya adalah Rp62.000.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tentukan berapa sumbangan Pak Candra dengan menggunakan persamaan satu variabel.
                - ##### Mengapa kejujuran dalam mencatat hasil penjualan merupakan bagian dari nilai kemanusiaan yang adil dan beradab?
                """)
if st.session_state.cerita2:
    soal_cerita2()
if st.session_state.kelompok['kondisi7']:
    if st.sidebar.button('Jujur dalam Jual Beli'):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=False
        st.session_state.cerita2=True
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi8']=True
        st.rerun()

def soal_cerita3():
    st.markdown("""
                <div class="efek1">Membantu Sesama (Sila ke-5: Keadilan Sosial bagi Seluruh Rakyat Indonesia)</div>""",unsafe_allow_html=True)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKwEHXofbmzkBvgR5IsxLAkYnTZU04_7-qoA&s",use_container_width=True)
    st.markdown("##### Sebuah kelas menggalang dana untuk membantu teman mereka yang sedang sakit.")
    st.markdown("""
                - ##### Setiap siswa menyumbang jumlah yang sama. 
                - ##### ika jumlah siswa adalah $x$, maka uang terkumpul Rp1.500.000.
                - ##### Setelah dihitung ulang, ternyata ada 5 siswa yang tidak ikut menyumbang, sehingga total yang terkumpul hanya Rp1.350.000.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tentukan berapa jumlah siswa dalam kelas tersebut.
                - ##### Bagaimana sikap membantu teman ini mencerminkan nilai keadilan sosial dalam Pancasila?
                """)
if st.session_state.cerita3:
    soal_cerita3()
if st.session_state.kelompok['kondisi8']:
    if st.sidebar.button("Membantu Sesama"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=True
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi9']=True
        st.rerun()
        
def soal_cerita4():
    st.markdown("""
                <div class="efek1">Soal 4 – Musyawarah Kelas (Sila ke-4: Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan)</div>""",unsafe_allow_html=True)
    st.image("https://i.pinimg.com/736x/81/2b/1a/812b1acc0b6856b3eefde041db3bb318.jpg",use_container_width=True)
    st.markdown("##### Sebuah kelas melakukan musyawarah untuk menentukan biaya per siswa dalam acara perpisahan.")
    st.markdown("""
                - ##### Total biaya yang dibutuhkan adalah Rp2.400.000. 
                - ##### Jika jumlah siswa adalah $x$, maka uang terkumpul Rp1.500.000.
                - ##### Jika setiap siswa membayar Rp50.000, maka masih kurang Rp300.000.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tentukan jumlah siswa dalam kelas tersebut dengan menggunakan persamaan satu variabel.
                - ##### Bagaimana kegiatan musyawarah dalam menentukan biaya ini sesuai dengan nilai kerakyatan dalam Pancasila?
                """)
if st.session_state.cerita4:
    soal_cerita4()
if st.session_state.kelompok['kondisi9']:
    if st.sidebar.button("Musyawarah Kelas"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=True
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi10']=True
        st.rerun()

def soal_cerita5():
    st.markdown("""
                <div class="efek1">Menjaga Kerukunan Antar Umat Beragama (Sila ke-1: Ketuhanan Yang Maha Esa)</div>""",unsafe_allow_html=True)
    st.image("https://jateng.disway.id/upload/5bd9bad000e64e68ab0ded63f7be899f.JPG",use_container_width=True)
    st.markdown("##### Di sebuah kampung, ada kegiatan bakti sosial bersama antar umat beragama.")
    st.markdown("""
                - ##### Warga muslim menyumbang $x$ karung beras. 
                - ##### Warga kristiani menyumbang 3 karung lebih sedikit dari warga muslim.
                - ##### Warga hindu menyumbang 2 kali lipat dari warga kristiani.
                """)
    st.markdown("##### Jumlah seluruh karung beras yang terkumpul adalah 47 karung.")
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tentukan berapa banyak karung beras yang disumbangkan masing-masing kelompok dengan menggunakan persamaan satu variabel.
                - ##### Mengapa kegiatan ini mencerminkan nilai toleransi dan Ketuhanan Yang Maha Esa dalam Pancasila?
                """)
if st.session_state.cerita5:
    soal_cerita5()
if st.session_state.kelompok['kondisi10']:
    if st.sidebar.button("Kerukunan Agama"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=True
        st.session_state.cerita6=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi11']=True
        st.rerun()

def soal_cerita6():
    st.markdown("""
                <div class="efek1">Batas Maksimal Sumbangan Kegiatan Desa(Sila ke-3: Persatuan Indonesia)</div>""",unsafe_allow_html=True)
    st.image("https://pamongdidik.wordpress.com/wp-content/uploads/2014/07/3d324-berdagang-di-pasar-pamong-didik.gif",use_container_width=True)
    st.markdown("##### Dalam rangka memperingati Hari Kemerdekaan, sebuah desa mengadakan lomba 17 Agustus. Panitia memutuskan bahwa:.")
    st.markdown("""
                - ##### Setiap kepala keluarga menyumbang uang dalam jumlah yang sama, yaitu Rp $x$ 
                - ##### Agar tidak memberatkan warga, besar sumbangan tiap keluarga tidak boleh lebih dari Rp50.000.
                - ##### Jumlah keluarga di desa tersebut adalah 120.
                """)
    st.markdown("##### Jumlah seluruh karung beras yang terkumpul adalah 47 karung.")
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Nyatakan situasi ini dalam bentuk pertidaksamaan satu variabel.
                - ##### Berapakah rentang nilai sumbangan yang mungkin diminta panitia?
                - ##### Bagaimana kegiatan gotong royong ini mencerminkan nilai persatuan dan kebersamaan dalam Pancasila?
                """)
if st.session_state.cerita6:
    soal_cerita6()
if st.session_state.kelompok['kondisi11']:
    st.sidebar.write("**Pertidaksamaan 1 variabel**")
    if st.sidebar.button("Sumbangan Kegiatan"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi = False
        st.session_state.adaptif=False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.kelompok['kondisi12']=True
        st.rerun()
    





