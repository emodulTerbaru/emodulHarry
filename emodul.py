import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

if "peta" not in st.session_state:
    st.session_state.peta = False

if "prasyarat" not in st.session_state:
    st.session_state.prasyarat = False

if "pretest" not in st.session_state:
    st.session_state.pretest = False
if "pretest1" not in st.session_state:
    st.session_state.pretest1 = False
if "pretest2" not in st.session_state:
    st.session_state.pretest2 = False
if "video1" not in st.session_state:
    st.session_state.video1=False

if "video2" not in st.session_state:
    st.session_state.video2=False
    
if "materi_prasyarat" not in st.session_state:
    st.session_state.materi_prasyarat=False

if "nilai_prasyarat" not in st.session_state:
    st.session_state.nilai_prasyarat = 0

if "materi" not in st.session_state:
    st.session_state.materi=False
if "materi1" not in st.session_state:
    st.session_state.materi1=False
if "adaptif" not in st.session_state:
    st.session_state.adaptif=False
if "game" not in st.session_state:
    st.session_state.game=False

if "kelompok" not in st.session_state:
    st.session_state.kelompok = {'kondisi1':True,'kondisi2':True,'kondisi3':False,'kondisi4':False,'kondisi5':False,
                                 'kondisi6':False,'kondisi7':False,'kondisi8':False,'kondisi9':False, 'kondisi10':False,
                                 'kondisi11':False,'kondisi12':False,'kondisi13':False,'kondisi14':False, 'kondisi15':False,
                                 'kondisi16':False,'kondisi17':False,'kondisi18':False,'kondisi19':False,'kondisi20':False,
                                 'kondisi21':False,'kondisi22':False,'kondisi23':False, 'kondisi24':False, 'kondisi25':False, 'kondisi26':False,
                                 'kondisi27':False,'kondisi28':False,'kondisi29':False}

if "jawaban" not in st.session_state:
    st.session_state.jawaban = {"jawab1":0,"jawab2":0,"jawab3":0,"jawab4":0,"jawab5":0,
                                "jawab6":0,"jawab7":0,"jawab8":0,"jawab9":0,"jawab10":0}
if "lvl1" not in st.session_state:
    st.session_state.lvl1={"jwb1":'0',"jwb2":'0',"jwb3":'0',"jwb4":'0',"jwb5":'0'}

if "lvl2" not in st.session_state:
    st.session_state.lvl2={"jwb1":'0',"jwb2":'0',"jwb3":'0',"jwb4":'0',"jwb5":'0'}

if "lvl3" not in st.session_state:
    st.session_state.lvl3={"jwb1":'0',"jwb2":'0',"jwb3":'0',"jwb4":'0',"jwb5":'0'}

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
if "cerita7" not in st.session_state:
    st.session_state.cerita7 = False
if "cerita8" not in st.session_state:
    st.session_state.cerita8 = False
if "cerita9" not in st.session_state:
    st.session_state.cerita9 = False
if "cerita10" not in st.session_state:
    st.session_state.cerita10 = False
if "soal_kuisioner" not in st.session_state:
    st.session_state.soal_kuisioner=False
if "soal_kevalidan" not in st.session_state:
    st.session_state.soal_kevalidan=False
if "jawaban1" not in st.session_state:
    st.session_state.jawaban1 = {"jawab1":"","jawab2":"","jawab3":"","jawab4":"","jawab5":"",
                                "jawab6":"","jawab7":"","jawab8":"","jawab9":"","jawab10":""}
if "jawaban2" not in st.session_state:
    st.session_state.jawaban2 = {"jawab1":"","jawab2":"","jawab3":"","jawab4":""}
if "jawaban3" not in st.session_state:
    st.session_state.jawaban3 = {"jawab1":0,"jawab2":0,"jawab3":0,"jawab4":0,"jawab5":0,
                                "jawab6":0,"jawab7":0,"jawab8":0,"jawab9":0,"jawab10":0,
                                 "jawab11":0,"jawab12":0,"jawab13":0,"jawab14":0,"jawab15":0,
                                "jawab16":0,"jawab17":0,"jawab18":0,"jawab19":0,"jawab20":0,
                                 }
if "jawaban4" not in st.session_state:
    st.session_state.jawaban4 = {"jawab1":0,"jawab2":0,"jawab3":0,"jawab4":0,"jawab5":0,
                                "jawab6":0,"jawab7":0,"jawab8":0,"jawab9":0,"jawab10":0,
                                 "jawab11":0,"jawab12":0,"jawab13":0,"jawab14":0,"jawab15":0,
                                "jawab16":0,"jawab17":0,"jawab18":0,"jawab19":0,"jawab20":0,
                                 "jawab21":0,"jawab22":0,"jawab23":0, "jawab24":'',"jawab25":''
                                 }
if "akhir" not in st.session_state:
    st.session_state.akhir=False
if "jawaban5" not in st.session_state:
    st.session_state.jawaban5 = {"jawab1":"","jawab2":"","jawab3":"","jawab4":""}
if "posttest" not in st.session_state:
    st.session_state.posttest=False
if "jawaban6" not in st.session_state:
    st.session_state.jawaban6 = {"jawab1":0,"jawab2":0,"jawab3":0,"jawab4":0,"jawab5":0,
                                "jawab6":0,"jawab7":0,"jawab8":0,"jawab9":0,"jawab10":0,
                                 "jawab11":0,"jawab12":0,"jawab13":0,"jawab14":0,"jawab15":0,
                                "jawab16":0,"jawab17":0,"jawab18":0,"jawab19":0,"jawab20":0,
                                 "jawab21":0,"jawab22":0,"jawab23":0, "jawab24":0,"jawab25":0,
                                 "jawab26":'',"jawab27":''
                                 }
if "kevalidan_media" not in st.session_state:
    st.session_state.kevalidan_media = False
st.sidebar.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1753921874/logo_rw63xi.jpg", width=100)
if not st.session_state.kelompok['kondisi1']:
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
                #format{
                    text-decoration:none;
                    font-family:"Cooper Black";
                    font-size:30px;
                    color:blue;
                    text-shadow:0px 0px 3px white;
                    text-align:center;
                }
                .video{
                    font-family:stencil;
                    color:red;
                    text-shadow:0px 0px 3px yellow;
                    font-size:40px;
                }
                .cek{
                    font-family:broadway;
                    font-size:30px;
                    color:green;
                    text-shadow:0px 0px 3px cyan
                }
                #lanjutkan, #ket{
                    font-family:"broadway";
                    font-size:30px;
                    color:green;
                    text-shadow:0px 0px 3px red;
                }
                #ket{
                    color:yellow;
                    text-shadow:0px 0px 3px green;
                }
                #bantuan{
                    display:flex;
                }
                #bantuan a{
                    border:2px solid cyan;
                    text-decoration:none;
                    padding:5px;
                    margin:5px;
                    border-radius:10px;
                    background-color:red;
                    color:yellow;
                    
                }
                .st-key-tombol1 .e1obcldf2:active{
                    background-color:blue;
                    color:white;
                }
            </style>
            ''',unsafe_allow_html=True)


if st.session_state.kelompok['kondisi27']:
    st.markdown('''<div id="bantuan">
            <a href="https://emodulterbaru.github.io/penjumlahan/Operasi Penjumlahan.html">Penjumlahan</a>
            <a href="https://emodulterbaru.github.io/penjumlahan/perkalian1.html">Perkalian</a></div>
        ''',unsafe_allow_html=True)


def tampilkan_kevalidan():
    st.markdown('<style>.st-key-tombol32 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    st.markdown(f'''
        <div style="border:2px solid black; background-color:yellow;color:black; padding:10px; border-radius:10px; margin-bottom:10px; box-shadow:-2px -2px 3px 3px red,2px 2px 3px 3px green">
        <div style="font-weight:bold; font-size:20px">LEMBAR VALIDASI LMS OLEH AHLI MATERI</div>
        <div style="font-size:15px;text-align:justify;">Pengembangan LMS Adaftif
        Berbasis Deep Learning Terhadap Literasi dan Numerasi serta Profil Pelajar
        Pancasila Pada Siswa SMP</div>
        <div>
            <table>
                <tr>
                    <td>Materi Pokok</td>
                    <td>:</td>
                    <td>Persamaan dan Pertidaksamaan Satu Variabel</td>
                </tr>
                <tr>
                    <td>Sasaran</td>
                    <td>:</td>
                    <td>Siswa Kelas VIII Semester 1</td>
                </tr>
                <tr>
                    <td>Peneliti</td>
                    <td>:</td>
                    <td><ol>
                            <li>Dr. Harry Dwi Putra, M.Pd</li>
                            <li>Dr. H. Asep Ikin Sugandi, M.Pd</li>
                            <li>Martin Bernard, M.Pd</li>
                        </ol>
                    </td>
                </tr>
                <tr>
                    <td>Validator</td>
                    <td>:</td>
                    <td>{nama}</td>
                </tr>
                <tr>
                    <td>Tanggal</td>
                    <td>:</td>
                    <td></td>
                </tr>
            </table>
            <div style="text-align:justify">
                Lembar penilaian LMS ini bertujuan untuk memperoleh validitas muka sehingga memperoleh masukan-masukan terkait kesesuaian tingkat kelas dengan bahan ajar yang digunakan. Serta mengetahui pendapat Bapak/Ibu Guru tentang kevalidan produk yang dihasilkan untuk mengetahui
                layak atau tidaknya LKS tersebut digunakan dalam pembelajaran di sekolah. Atas kesediaan Bapak/Ibu Guru untuk mengisi angket
                ini saya ucapkan terima kasih.
            </div>
            <div>Petunjuk Pengisian</div>
        </div>
        <div>
            <ol>
                <li>Isilah pilihan pada kolom yang Bapak/Ibu anggap sesuai dengan aspek penilaian yang ada.
                Jika ada masukan, tulislah di kolom masukan.</li>
                <li>Rentang skala penilaian adalah sebagai berikut :
                    SS(4) = sangat setuju, S(3) = setuju,  TS(2) = tidak setuju, STS(1) = sangat tidak setuju
                </li>
            </ol>
        </div>
        </div>
        ''',unsafe_allow_html=True)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kesesuaian Kurikulum dan Kompetensi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab1']=st.radio("1 Materi dalam LMS sesuai dengan standar kurikulum yang berlaku.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab2']=st.radio("2 Materi mendukung pencapaian kompetensi inti dan kompetensi dasar (KI/KD)",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab3']=st.radio("3 Materi selaras dengan capaian pembelajaran/learning outcomes yang ditargetkan.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab4']=st.radio("4 Kedalaman materi sesuai dengan karakteristik peserta didik.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab5']=st.radio("5 Cakupan materi lengkap dan tidak ada bagian penting yang tertinggal.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Keakuratan dan Kejelasan Materi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab6']=st.radio("6 Konsep, teori, dan data yang disajikan sudah akurat dan bebas dari kesalahan.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab7']=st.radio("7 Istilah, simbol, atau notasi yang digunakan konsisten dalam seluruh materi.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab8']=st.radio("8 Bahasa penyajian materi jelas, lugas, dan mudah dipahami siswa.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab9']=st.radio("9 Materi disajikan secara runtut sesuai alur berpikir yang logis.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab10']=st.radio("10 Setiap bagian materi dilengkapi penjelasan memadai untuk mendukung pemahaman siswa.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Relevansi Kontekstual</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab11']=st.radio("11 Materi dikaitkan dengan situasi nyata atau permasalahan kontekstual..",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab12']=st.radio("12 Materi memiliki keterkaitan dengan kebutuhan dan perkembangan zaman.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab13']=st.radio("13 Contoh-contoh yang diberikan relevan dengan kehidupan sehari-hari siswa.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab14']=st.radio("14 Materi mendorong pengembangan keterampilan berpikir kritis, kreatif, kolaboratif, dan komunikatif.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab15']=st.radio("15 Latihan/soal yang tersedia bervariasi dan sesuai dengan konteks kehidupan siswa.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Integrasi Deep Learning dalam Materi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab16']=st.radio("16 LMS menyesuaikan materi dengan kebutuhan siswa (adaptive learning).",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab17']=st.radio("17 LMS memberikan rekomendasi materi tambahan sesuai kesulitan siswa",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab18']=st.radio("18 Integrasi deep learning membantu analisis hasil belajar siswa secara mendalam.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab19']=st.radio("19 Integrasi LMS membuat pembelajaran lebih efektif dibandingkan metode tradisional.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab20']=st.radio("20 Penerapan deep learning menambah nilai inovatif dalam penyajian materi.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Evaluasi Materi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab21']=st.radio("21 Instrumen evaluasi pada LMS sesuai dengan indikator pencapaian kompetensi.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab22']=st.radio("22 Soal dan kuis mengukur keterampilan berpikir tingkat tinggi, tidak hanya hafalan.",[1,2,3,4],index=None)
    st.session_state.jawaban4['jawab23']=st.radio("23 Feedback otomatis dari LMS sesuai dengan jawaban siswa dan membantu perbaikan belajar.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Komentar/ Saran untuk Perbaikan LMS</div>
    <div></div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab24']=st.text_area("Mohon isi di sini")
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kesimpulan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban4['jawab25']=st.radio("Bahan ajar berbentuk LKS dengan pendekatan LMS Adaptif Berbasis Deep Learning Terhadap Literasi Numerasi dan Profil Pelajar Pancasila dinyatakan *)",["1 Layak digunakan di lapangan tanpa revisi","2 Layak digunakan di lapangan dengan revisi","3 Tidak layak digunakan di lapangan"],index=None)
    st.markdown('''
    <div>*) Pilih salah satu</div>
    ''',unsafe_allow_html=True)
    if st.button("Masukan jawaban kevalidan"):
        poin = 0
        for i in st.session_state.jawaban4:
            if st.session_state.jawaban4[i]==None or st.session_state.jawaban4[i]=="":
                st.error(i+" Belum terisi")
                break
            else:
                poin +=1
        st.write(poin)
        if poin==25:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSc5AFFyrt8Ls8PoHVJ00T4YCDETux7tSD2iFE-0W9np8vSYtA/formResponse"
            data = {
            "entry.884183788": nama,   # Ganti dengan entry ID dari form
            "entry.609705951": kelas,   # Ganti dengan entry ID dari form
            "entry.1970482153": sekolah,   # Ganti dengan entry ID dari form
            "entry.2022976301": st.session_state.jawaban4['jawab1'],   # Ganti dengan entry ID dari form
            "entry.1143421917": st.session_state.jawaban4['jawab2'],   # Ganti dengan entry ID dari form
            "entry.692230187": st.session_state.jawaban4['jawab3'],   # Ganti dengan entry ID dari form
            "entry.1118222492": st.session_state.jawaban4['jawab4'],   # Ganti dengan entry ID dari form
            "entry.90781233": st.session_state.jawaban4['jawab5'],   # Ganti dengan entry ID dari form
            "entry.2412908": st.session_state.jawaban4['jawab6'],   # Ganti dengan entry ID dari form
            "entry.45074186": st.session_state.jawaban4['jawab7'],   # Ganti dengan entry ID dari form
            "entry.588722623": st.session_state.jawaban4['jawab8'],   # Ganti dengan entry ID dari form
            "entry.1126474833": st.session_state.jawaban4['jawab9'],   # Ganti dengan entry ID dari form
            "entry.1776452208": st.session_state.jawaban4['jawab10'],   # Ganti dengan entry ID dari form
            "entry.1894233351": st.session_state.jawaban4['jawab11'],   # Ganti dengan entry ID dari form
            "entry.807119423": st.session_state.jawaban4['jawab12'],   # Ganti dengan entry ID dari form
            "entry.962584938": st.session_state.jawaban4['jawab13'],   # Ganti dengan entry ID dari form
            "entry.1587149867": st.session_state.jawaban4['jawab14'],   # Ganti dengan entry ID dari form
            "entry.2081490996": st.session_state.jawaban4['jawab15'],   # Ganti dengan entry ID dari form
            "entry.1240199975": st.session_state.jawaban4['jawab16'],   # Ganti dengan entry ID dari form
            "entry.1517972685": st.session_state.jawaban4['jawab17'],   # Ganti dengan entry ID dari form
            "entry.1174466107": st.session_state.jawaban4['jawab18'],   # Ganti dengan entry ID dari form
            "entry.972246048": st.session_state.jawaban4['jawab19'],   # Ganti dengan entry ID dari form
            "entry.1280090027": st.session_state.jawaban4['jawab20'],   # Ganti dengan entry ID dari form
            "entry.1097175283": st.session_state.jawaban4['jawab21'],   # Ganti dengan entry ID dari form
            "entry.1660829012": st.session_state.jawaban4['jawab22'],   # Ganti dengan entry ID dari form
            "entry.355914659": st.session_state.jawaban4['jawab23'],   # Ganti dengan entry ID dari form
            "entry.1827587111": st.session_state.jawaban4['jawab24'],   # Ganti dengan entry ID dari form
            "entry.1648938937": st.session_state.jawaban4['jawab25'],   # Ganti dengan entry ID dari form
                }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
if st.session_state.soal_kevalidan:
    tampilkan_kevalidan()
#============ahli media
def tampilkan_kevalidan1():
    st.markdown('<style>.st-key-tombol32 .e1haskxa2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    st.markdown(f'''
        <div style="border:2px solid black; background-color:orange;color:black; padding:10px; border-radius:10px; margin-bottom:10px; box-shadow:-2px -2px 3px 3px red,2px 2px 3px 3px green">
        <div style="font-weight:bold; font-size:20px">LEMBAR VALIDASI LMS OLEH AHLI MEDIA</div>
        <div style="font-size:15px;text-align:justify;">Pengembangan LMS Adaftif
        Berbasis Deep Learning Terhadap Literasi dan Numerasi serta Profil Pelajar
        Pancasila Pada Siswa SMP</div>
        <div>
            <table>
                <tr>
                    <td>Materi Pokok</td>
                    <td>:</td>
                    <td>Persamaan dan Pertidaksamaan Satu Variabel</td>
                </tr>
                <tr>
                    <td>Sasaran</td>
                    <td>:</td>
                    <td>Siswa Kelas VIII Semester 1</td>
                </tr>
                <tr>
                    <td>Peneliti</td>
                    <td>:</td>
                    <td><ol>
                            <li>Dr. Harry Dwi Putra, M.Pd</li>
                            <li>Dr. H. Asep Ikin Sugandi, M.Pd</li>
                            <li>Martin Bernard, M.Pd</li>
                        </ol>
                    </td>
                </tr>
                <tr>
                    <td>Validator</td>
                    <td>:</td>
                    <td>{nama}</td>
                </tr>
                <tr>
                    <td>Tanggal</td>
                    <td>:</td>
                    <td></td>
                </tr>
            </table>
            <div style="text-align:justify">
                Lembar penilaian LMS ini bertujuan untuk memperoleh validitas muka sehingga memperoleh masukan-masukan terkait kesesuaian tingkat kelas dengan bahan ajar yang digunakan. Serta mengetahui pendapat Bapak/Ibu Guru tentang kevalidan produk yang dihasilkan untuk mengetahui
                layak atau tidaknya LKS tersebut digunakan dalam pembelajaran di sekolah. Atas kesediaan Bapak/Ibu Guru untuk mengisi angket
                ini saya ucapkan terima kasih.
            </div>
            <div>Petunjuk Pengisian</div>
        </div>
        <div>
            <ol>
                <li>Isilah pilihan pada kolom yang Bapak/Ibu anggap sesuai dengan aspek penilaian yang ada.
                Jika ada masukan, tulislah di kolom masukan.</li>
                <li>Rentang skala penilaian adalah sebagai berikut :
                    SS(4) = sangat setuju, S(3) = setuju,  TS(2) = tidak setuju, STS(1) = sangat tidak setuju
                </li>
            </ol>
        </div>
        </div>
        ''',unsafe_allow_html=True)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Tampilan </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab1']=st.radio("1 Desain visual (warna, ikon, layout) konsisten di seluruh laman.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab2']=st.radio("2 Tata letak/struktur informasi memudahkan pengguna menemukan fitur.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab3']=st.radio("3 Ukuran, jenis huruf, dan jarak antar teks mendukung keterbacaan.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab4']=st.radio("4 Kontras warna cukup untuk aksesibilitas (kemampuan baca semua pengguna).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab5']=st.radio("5 Visual (grafik, ikon, animasi) mendukung tujuan pembelajaran dan tidak mengganggu.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Fungsionalitas & Teknis</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab6']=st.radio("6 Sistem dapat dijalankan dengan cepat dan stabil (load time, respon).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab7']=st.radio("7 Proses login, pendaftaran, dan manajemen akun bekerja mudah dan aman.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab8']=st.radio("8 Fitur inti (kuis, upload tugas, forum, tracking) berfungsi sesuai spesifikasi.dan Berpikir Kritis).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab9']=st.radio("9 Aplikasi responsif di berbagai perangkat (desktop, tablet, smartphone)..",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab10']=st.radio("10 Mekanisme backup dan recovery/data protection tersedia dan memadai.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Interaktivitas Media</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab11']=st.radio("11 Tersedia mekanisme interaksi real-time (chat/forum) yang mudah digunakan.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab12']=st.radio("12 Media interaktif (kuis adaptif, simulasi, drag & drop, dsb.) berfungsi dengan baik.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab13']=st.radio("13 Umpan balik otomatis yang diberikan jelas, relevan, dan membantu belajar.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab14']=st.radio("14 Material multimedia (video/audio/gambar) terintegrasi dengan tata letak pembelajaran.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab15']=st.radio("15 Fitur kolaboratif (ruang kerja kelompok, penilaian peer) mendukung interaksi bermakna.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Keamanan & Privasi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab16']=st.radio("16 Sistem menggunakan model deep learning untuk memberikan rekomendasi materi yang relevan).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab17']=st.radio("17 Personalisasi (adaptive path) jelas terlihat berdasarkan performa dan profil pengguna.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab18']=st.radio("18 Learning analytics memvisualisasi capaian, tren, dan area yang perlu perhatian.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab19']=st.radio("19 Prediksi/alert (mis. risiko drop-out, butuh intervensi) akurat dan berguna.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab20']=st.radio("20 Sistem menjelaskan (explainability) dasar rekomendasi/keputusan AI agar dapat dipahami pengguna.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Aspek Keamanan & Privasi</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab21']=st.radio("21 Pengelolaan data pengguna sesuai prinsip privasi (minimasi data, enkripsi, dsb).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab22']=st.radio("22 Hak akses dan otorisasi pengguna terimplementasi dengan baik.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab23']=st.radio("23 Kebijakan privasi dan persetujuan penggunaan data tersedia dan jelas.",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab24']=st.radio("24 Sistem aman terhadap ancaman umum (autentikasi kuat, proteksi serangan umum).",[1,2,3,4],index=None)
    st.session_state.jawaban6['jawab25']=st.radio("25 Mekanisme penghapusan/permintaan data pengguna mudah diakses.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Komentar/ Saran untuk Perbaikan LMS</div>
    <div></div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab26']=st.text_area("Mohon isi di sini")
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kesimpulan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban6['jawab27']=st.radio("Bahan ajar berbentuk LKS dengan pendekatan LMS Adaptif Berbasis Deep Learning Terhadap Literasi Numerasi dan Pofil Pelajar Pancasila dinyatakan *)",["1 Layak digunakan di lapangan tanpa revisi","2 Layak digunakan di lapangan dengan revisi","3 Tidak layak digunakan di lapangan"],index=None)
    st.markdown('''
    <div>*) Pilih salah satu</div>
    ''',unsafe_allow_html=True)
    if st.button("Masukan jawaban Ahli Media"):
        poin = 0
        for i in st.session_state.jawaban6:
            if st.session_state.jawaban6[i]==None or st.session_state.jawaban6[i]=="":
                st.error(i+" Belum terisi")
                break
            else:
                poin +=1
        st.write(poin)
        if poin==27:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdbJKEX31Pmy6A6k1-dApWnNVAhOl7cmr9U2hy4_naNnOlqSw/formResponse"
            data = {
            "entry.1474505802": nama,   # Ganti dengan entry ID dari form
            "entry.22517126": sekolah,   # Ganti dengan entry ID dari form
            "entry.894743694": st.session_state.jawaban6['jawab1'],   # Ganti dengan entry ID dari form
            "entry.1181979855": st.session_state.jawaban6['jawab2'],   # Ganti dengan entry ID dari form
            "entry.49256181": st.session_state.jawaban6['jawab3'],   # Ganti dengan entry ID dari form
            "entry.633576234": st.session_state.jawaban6['jawab4'],   # Ganti dengan entry ID dari form
            "entry.778685164": st.session_state.jawaban6['jawab5'],   # Ganti dengan entry ID dari form
            "entry.853840279": st.session_state.jawaban6['jawab6'],   # Ganti dengan entry ID dari form
            "entry.1563002000": st.session_state.jawaban6['jawab7'],   # Ganti dengan entry ID dari form
            "entry.1597568141": st.session_state.jawaban6['jawab8'],   # Ganti dengan entry ID dari form
            "entry.879327998": st.session_state.jawaban6['jawab9'],   # Ganti dengan entry ID dari form
            "entry.2119178410": st.session_state.jawaban6['jawab10'],   # Ganti dengan entry ID dari form
            "entry.1710320937": st.session_state.jawaban6['jawab11'],   # Ganti dengan entry ID dari form
            "entry.91420189": st.session_state.jawaban6['jawab12'],   # Ganti dengan entry ID dari form
            "entry.521044252": st.session_state.jawaban6['jawab13'],   # Ganti dengan entry ID dari form
            "entry.1351075123": st.session_state.jawaban6['jawab14'],   # Ganti dengan entry ID dari form
            "entry.1739617730": st.session_state.jawaban6['jawab15'],   # Ganti dengan entry ID dari form
            "entry.661911191": st.session_state.jawaban6['jawab16'],   # Ganti dengan entry ID dari form
            "entry.1424280546": st.session_state.jawaban6['jawab17'],   # Ganti dengan entry ID dari form
            "entry.748854670": st.session_state.jawaban6['jawab18'],   # Ganti dengan entry ID dari form
            "entry.1984682441": st.session_state.jawaban6['jawab19'],   # Ganti dengan entry ID dari form
            "entry.663328225": st.session_state.jawaban6['jawab20'],   # Ganti dengan entry ID dari form
            "entry.769803424": st.session_state.jawaban6['jawab21'],   # Ganti dengan entry ID dari form
            "entry.9428513": st.session_state.jawaban6['jawab22'],   # Ganti dengan entry ID dari form
            "entry.303343529": st.session_state.jawaban6['jawab23'],   # Ganti dengan entry ID dari form
            "entry.1164439999": st.session_state.jawaban6['jawab24'],   # Ganti dengan entry ID dari form
            "entry.2130741694": st.session_state.jawaban6['jawab25'],   # Ganti dengan entry ID dari form
            "entry.19657503": st.session_state.jawaban6['jawab26'],   # Ganti dengan entry ID dari form
            "entry.1903400958": st.session_state.jawaban6['jawab27'],   # Ganti dengan entry ID dari form
                }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
#===============Batas Ahli Media
def tampil_kuisioner():
    st.markdown('<style>.st-key-tombol31 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    with st.container():
        st.markdown('''
        <div style="border:2px solid black; background-color:cyan;color:black; padding:10px; border-radius:10px; margin-bottom:10px; box-shadow:-2px -2px 3px 3px red,2px 2px 3px 3px green">
        <div style="font-weight:bold; font-size:20px">Pedoman Penilaian Menggunakan Angket dan Wawancara untuk Kepratisan Siswa</div>
        <div style="font-size:15px;text-align:justify;">Dalam rangka pengembangan bahan ajar berbasis ICT, saya mohon tanggapan peserta didik terhadap proses pembelajaran
        menggunakan bahan ajar berbantuan aplikasi Canva berdasarkan materi yang telah dilaksanakan. Jawablah dengan sejujurnya karena
        hal ini tidak akan berpengaruh terhadap nilai peserta didik.</div>
        <div>
            <ol>
                <li>Lembar validasi ini diisi oleh siswa.</li>
                <li>Lembar validasi digunakan dengan tujuan untuk mendapatkan hasil
                validasi tentang kualitas dilihat dari aspek Rekayasa Perangkat Lunak,
                Komunikasi Visual dan Pembelajaran dari program media pembelajaran pada pokok bahasan
                Persamaan dan Pertidaksamaan sau Variabel tingkat SMP.</li>
                <li>Rentang skala penilaian adalah sebagai berikut :
                    SS(4) = sangat setuju, S(3) = setuju,  TS(2) = tidak setuju, STS(1) = sangat tidak setuju
                </li>
            </ol>
        </div>
        </div>
        ''',unsafe_allow_html=True)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kebermanfaatan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban3['jawab1']=st.radio("1 LMS membantu saya memahami materi dengan lebih baik.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab2']=st.radio("2 LMS membuat pembelajaran lebih efisien dan terstruktur.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab3']=st.radio("3 Materi dapat saya akses kapan saja dan di mana saja melalui LMS.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab4']=st.radio("4 LMS memudahkan saya dalam mengerjakan evaluasi/tes secara online.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab5']=st.radio("5 LMS membuat saya lebih aktif  dalam pembelajaran.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kemenarikan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban3['jawab6']=st.radio("6 Tampilan desain LMS menarik dan nyaman digunakan.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab7']=st.radio("7 Fitur interaktif dalam LMS membuat pembelajaran lebih menyenangkan.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab8']=st.radio("8 LMS menyajikan materi dengan gambar, video, atau simulasi yang bervariasi.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab9']=st.radio("9 LMS mengurangi rasa bosan saat belajar.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab10']=st.radio("10 LMS menumbuhkan semangat belajar saya.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Kebaruan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban3['jawab11']=st.radio("11 LMS ini memberikan pengalaman belajar  yang berbeda dibanding LMS biasa.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab12']=st.radio("12 LMS menyajikan materi sesuai dengan kebutuhan belajar saya.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab13']=st.radio("13 LMS memberikan rekomendasi materi sesuai dengan kesulitan saya.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab14']=st.radio("14 Integrasi deep learning membuat pembelajaran lebih modern.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab15']=st.radio("15 LMS ini menghadirkan cara belajar yang lebih inovatif.",[1,2,3,4],index=None)
    st.markdown('''
    <div style="background-color:black;color:yellow;padding:5px; margin:5px; font-size:18px;border-radius:8px;border:2px solid cyan;
    font-family:'comic sans ms';text-align:center;font-weight:bold">Keterbantuan</div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban3['jawab16']=st.radio("16 LMS membantu guru memantau perkembangan belajar siswa secara real time.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab17']=st.radio("17 LMS membantu saya mengetahui kelemahan dalam belajar.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab18']=st.radio("18 LMS membantu saya mengenali kemampuan yang saya kuasai dengan baik.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab19']=st.radio("19 Feedback dari LMS membantu saya memperbaiki kesalahan belajar.",[1,2,3,4],index=None)
    st.session_state.jawaban3['jawab20']=st.radio("20 LMS memberikan arahan materi tambahan sesuai kebutuhan saya.",[1,2,3,4],index=None)
    if st.button("Masukan jawaban kuisioner"):
        poin = 0
        for i in st.session_state.jawaban3:
            if st.session_state.jawaban3[i]==None:
                st.error(i+" Belum terisi")
                break
            else:
                poin +=1
        if poin==20:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSd1UClu8LmeRVvqMdHQ0k2PZiy71SJH166BcKWz-jwleTG4ag/formResponse"
            data = {
            "entry.1163631663": nama,   # Ganti dengan entry ID dari form
            "entry.1676877244": kelas,   # Ganti dengan entry ID dari form
            "entry.553482788": sekolah,   # Ganti dengan entry ID dari form
            "entry.225145940": st.session_state.jawaban3['jawab1'],   # Ganti dengan entry ID dari form
            "entry.595868327": st.session_state.jawaban3['jawab2'],   # Ganti dengan entry ID dari form
            "entry.1559181336": st.session_state.jawaban3['jawab3'],   # Ganti dengan entry ID dari form
            "entry.1931664633": st.session_state.jawaban3['jawab4'],   # Ganti dengan entry ID dari form
            "entry.2006223433": st.session_state.jawaban3['jawab5'],   # Ganti dengan entry ID dari form
            "entry.1067599676": st.session_state.jawaban3['jawab6'],   # Ganti dengan entry ID dari form
            "entry.288123951": st.session_state.jawaban3['jawab7'],   # Ganti dengan entry ID dari form
            "entry.149839638": st.session_state.jawaban3['jawab8'],   # Ganti dengan entry ID dari form
            "entry.1263723978": st.session_state.jawaban3['jawab9'],   # Ganti dengan entry ID dari form
            "entry.1478937274": st.session_state.jawaban3['jawab10'],   # Ganti dengan entry ID dari form
            "entry.799404934": st.session_state.jawaban3['jawab11'],   # Ganti dengan entry ID dari form
            "entry.215889813": st.session_state.jawaban3['jawab12'],   # Ganti dengan entry ID dari form
            "entry.896056923": st.session_state.jawaban3['jawab13'],   # Ganti dengan entry ID dari form
            "entry.1112098553": st.session_state.jawaban3['jawab14'],   # Ganti dengan entry ID dari form
            "entry.847626171": st.session_state.jawaban3['jawab15'],   # Ganti dengan entry ID dari form
            "entry.1481221084": st.session_state.jawaban3['jawab16'],   # Ganti dengan entry ID dari form
            "entry.1642568100": st.session_state.jawaban3['jawab17'],   # Ganti dengan entry ID dari form
            "entry.1578518535": st.session_state.jawaban3['jawab18'],   # Ganti dengan entry ID dari form
            "entry.1986977592": st.session_state.jawaban3['jawab19'],   # Ganti dengan entry ID dari form
            "entry.1027523630": st.session_state.jawaban3['jawab20'],   # Ganti dengan entry ID dari form
                }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
    masukan = st.text_area("Masukan sarannya")
    if st.button("Masukan Saran terhadap LMS"):
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfHEeIY7Wb6YGTxekUhTUOPPtR7mxzLBYvSbhOQacaYlFeUZw/formResponse"
        data = {
            "entry.761075130": nama,   # Ganti dengan entry ID dari form
            "entry.1599802501": kelas,   # Ganti dengan entry ID dari form
            "entry.1874102655": sekolah,   # Ganti dengan entry ID dari form
            "entry.1379800760": masukan,   # Ganti dengan entry ID dari form
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            st.success("Berhasil dikirim!")
        else:
            st.error(f"Gagal mengirim. Status code: {response.status_code}")

            
if st.session_state.soal_kuisioner:
    tampil_kuisioner()

def pemetaan():
    st.markdown('<div id="konsep">Peta Konsep</div>',unsafe_allow_html=True)
    st.markdown('<div id="gambar1"></div>',unsafe_allow_html=True)
    st.markdown('##### Permainan tentang persamaan dan pertidaksamaan satu variabel')
    
    st.markdown("""
    <iframe src='https://emodulterbaru.github.io/persamaan1variabel/PSLV.html' style='width:100%; height:2400px'></iframe>
    """,unsafe_allow_html=True)

def kover():
    st.markdown('''
    <iframe src="https://scratch.mit.edu/projects/1216822076/embed" allowtransparency="true"
    width="600" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>
    ''',unsafe_allow_html=True)
    

def kover1():
    st.markdown('''
    <img src="https://res.cloudinary.com/dfkw4ux0e/image/upload/v1758599434/cover_fotuwr.jpg" allowtransparency="true"
    width="100%" height="1200px" frameborder="0" scrolling="no" allowfullscreen></img>
    ''',unsafe_allow_html=True)

if st.session_state.peta:
    st.markdown('<style>.st-key-tombol3 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    pemetaan()
    
if st.session_state.kelompok['kondisi1']:
    kover1()
if st.session_state.kelompok['kondisi2']:
    if st.sidebar.button("Prasyarat",key="tombol1"):
        st.session_state.peta=False
        st.session_state.prasyarat = True
        st.session_state.kelompok['kondisi1']=False
        st.session_state.kelompok['kondisi17']=True
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=True
        st.session_state.kevalidan_media = False
        st.rerun()
        
def soal_pretest():
    st.markdown('<style>.st-key-tombol2 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    st.markdown("<a id='format'> Soal Test Awal</a>",unsafe_allow_html=True)
    st.markdown("<iframe src='https://emodulterbaru.github.io/pretestHarry1/pretest1' style='width:100%; height:3500px'></iframe>",unsafe_allow_html=True)
if st.session_state.pretest:
    soal_pretest()
if st.session_state.kelompok['kondisi17']:
    if st.sidebar.button("Test Awal", key="tombol2"):
        st.session_state.peta=False
        st.session_state.prasyarat = False
        st.session_state.pretest = True
        st.session_state.kelompok['kondisi22']=True
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.materi_prasyarat = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
#===============================================================
def soal_pretest2():
    st.markdown('<style>.st-key-tombol30 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    st.write("## Soal1")
    st.markdown('''
    <style>
        .text-bar {
            min-height: 10vh; /* Tinggi penuh layar */
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            position: relative;
            overflow: hidden;
            text-align:justify;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .text-bar h1 {
            color: white;
            font-size: 1rem; /* Ukuran teks besar */
            text-shadow: 
                0 0 10px rgba(255, 255, 255, 0.5),
                0 0 20px rgba(255, 255, 255, 0.3),
                0 0 30px rgba(255, 255, 255, 0.2);
            letter-spacing: 3px;
            z-index: 2;
            position: relative;
            animation: textGlow 3s ease-in-out infinite alternate;
            color:black;
        }

        @keyframes textGlow {
            from {
                text-shadow: 
                    0 0 10px rgba(255, 255, 255, 0.5),
                    0 0 20px rgba(255, 255, 255, 0.3),
                    0 0 30px rgba(255, 255, 255, 0.2);
            }
            to {
                text-shadow: 
                    0 0 20px rgba(255, 255, 255, 0.8),
                    0 0 30px rgba(255, 255, 255, 0.6),
                    0 0 40px rgba(255, 255, 255, 0.4);
            }
        }

        /* Partikel animasi latar belakang */
        .particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 6s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) translateX(0);
                opacity: 0.5;
            }
            25% {
                transform: translateY(-20px) translateX(10px);
                opacity: 0.8;
            }
            50% {
                transform: translateY(-10px) translateX(-15px);
                opacity: 0.3;
            }
            75% {
                transform: translateY(-30px) translateX(5px);
                opacity: 0.9;
            }
        }

        /* Responsif untuk mobile */
        @media (max-width: 768px) {
            .text-bar h1 {
                font-size: 3rem;
            }
        }
    </style>
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Seorang pedagang buah menjual apel dengan harga Rp6.000 per buah. Ia juga menjual jeruk dengan harga
        Rp5.000 per buah. Pada suatu hari, seorang pembeli membeli beberapa apel dan beberapa jeruk. Jumlah apel
        yang dibeli tiga kali lebih banyak daripada jumlah jeruk. Jika total harga yang harus dibayar pembeli tersebut
        adalah Rp184.000, tentukan berapa banyak apel dan berapa banyak jeruk yang dibeli oleh pembeli tersebut.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban2['jawab1'] = st.text_area("Masuk Jawaban 1")
    st.write("## Soal2")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Rani menabung di celengan setiap hari dengan jumlah yang berbeda-beda. Pada minggu pertama, ia menabung Rp3.000
        setiap hari. Setelah satu minggu hari berikutnya, ia menaikkan jumlah tabungan hariannya Rp1.000 setiap hari. Rani berencana mengumpulkan
        uang lebih dari Rp121.000. Tentukan berapa hari minimal Rani harus menabung pada lebih dari Rp121.000.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban2['jawab2'] = st.text_area("Masuk Jawaban 2")
    st.write("## Soal3")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Sebuah taman kota berbentuk persegi panjang dengan panjang 4 kali lebarnya. Pemerintah kota berencana menambah panjang
        taman itu sebanyak 12 meter dan lebarnya sebanyak 6 meter. Setelah diperluas, keliling taman menjadi 180 meter. Tentukan ukuran
        panjang dan lebar taman sebelum diperluas.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban2['jawab3'] = st.text_area("Masuk Jawaban 3")
    st.write("## Soal4")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Andi ingin membeli buku tulis dan pulpen di sebuah toko alat tulis. Harga satu buku tulis adalah Rp8.000, sedangkan harga
        satu pulpen adalah Rp5.000. Uang yang dimiliki Andi hanya Rp94.000. Jika Andi membeli 8 buku tulis, berapa pulpen paling banyak
        yang masih bisa dibeli Andi? Tulis jawabanmu dalam bentuk pertidaksamaan dan tentukan nilai maksimum jumlah pulpen.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban2['jawab4'] = st.text_area("Masuk Jawaban 4")
    if st.button("Masukan Hasil"):
        if st.session_state.jawaban2['jawab1'] and st.session_state.jawaban2['jawab2'] and st.session_state.jawaban2['jawab3'] and st.session_state.jawaban2['jawab4']:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScHUxVhpKY7AFpxOX-JTHV0A1U9HQj3QrvnkX6hIsd9ybsqiA/formResponse"
            data = {
            "entry.664563842": nama,   # Ganti dengan entry ID dari form
            "entry.136617365": kelas,   # Ganti dengan entry ID dari form
            "entry.1370752344": sekolah,   # Ganti dengan entry ID dari form
            "entry.1509446676": st.session_state.jawaban2['jawab1'],   # Ganti dengan entry ID dari form
            "entry.2059852517": st.session_state.jawaban2['jawab2'],   # Ganti dengan entry ID dari form
            "entry.1017002842": st.session_state.jawaban2['jawab3'],   # Ganti dengan entry ID dari form
            "entry.1014904881": st.session_state.jawaban2['jawab4'],   # Ganti dengan entry ID dari form
                }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
        else:
            st.error("Ada Jawaban Soal yang masih kosong, Periksa lagi")

#=====Postest
def soal_pretest3():
    st.markdown('<style>.st-key-tombol30 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    st.write("## Soal1")
    st.markdown('''
    <style>
        .text-bar {
            min-height: 10vh; /* Tinggi penuh layar */
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            position: relative;
            overflow: hidden;
            text-align:justify;
            padding:10px;
            border-radius:10px;
            margin-bottom:10px;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .text-bar h1 {
            color: white;
            font-size: 1rem; /* Ukuran teks besar */
            text-shadow: 
                0 0 10px rgba(255, 255, 255, 0.5),
                0 0 20px rgba(255, 255, 255, 0.3),
                0 0 30px rgba(255, 255, 255, 0.2);
            letter-spacing: 3px;
            z-index: 2;
            position: relative;
            animation: textGlow 3s ease-in-out infinite alternate;
            color:black;
        }

        @keyframes textGlow {
            from {
                text-shadow: 
                    0 0 10px rgba(255, 255, 255, 0.5),
                    0 0 20px rgba(255, 255, 255, 0.3),
                    0 0 30px rgba(255, 255, 255, 0.2);
            }
            to {
                text-shadow: 
                    0 0 20px rgba(255, 255, 255, 0.8),
                    0 0 30px rgba(255, 255, 255, 0.6),
                    0 0 40px rgba(255, 255, 255, 0.4);
            }
        }

        /* Partikel animasi latar belakang */
        .particles {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: float 6s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) translateX(0);
                opacity: 0.5;
            }
            25% {
                transform: translateY(-20px) translateX(10px);
                opacity: 0.8;
            }
            50% {
                transform: translateY(-10px) translateX(-15px);
                opacity: 0.3;
            }
            75% {
                transform: translateY(-30px) translateX(5px);
                opacity: 0.9;
            }
        }

        /* Responsif untuk mobile */
        @media (max-width: 768px) {
            .text-bar h1 {
                font-size: 3rem;
            }
        }
    </style>
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Seorang pedagang buah menjual apel dengan harga Rp7.000 per buah. Ia juga menjual jeruk dengan harga
        Rp6.000 per buah. Pada suatu hari, seorang pembeli membeli beberapa apel dan beberapa jeruk. Jumlah apel
        yang dibeli dua kali lebih banyak daripada jumlah jeruk. Jika total harga yang harus dibayar pembeli tersebut
        adalah Rp200.000, tentukan berapa banyak apel dan berapa banyak jeruk yang dibeli oleh pembeli tersebut.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban5['jawab1'] = st.text_area("Masukan Jawaban 1")
    st.write("## Soal2")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Rani menabung di celengan setiap hari dengan jumlah yang berbeda-beda. Pada minggu pertama, ia menabung Rp4.000
        setiap hari. Setelah satu minggu hari berikutnya, ia menaikkan jumlah tabungan hariannya Rp2.000 setiap hari. Rani berencana mengumpulkan
        uang lebih dari Rp268.000. Tentukan berapa hari minimal Rani harus menabung pada lebih dari Rp268.000.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban5['jawab2'] = st.text_area("Masukan Jawaban 2")
    st.write("## Soal3")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Sebuah taman kota berbentuk persegi panjang dengan panjang 5 kali lebarnya. Pemerintah kota berencana menambah panjang
        taman itu sebanyak 15 meter dan lebarnya sebanyak 9 meter. Setelah diperluas, keliling taman menjadi 360 meter. Tentukan ukuran
        panjang dan lebar taman sebelum diperluas.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban5['jawab3'] = st.text_area("Masukan Jawaban 3")
    st.write("## Soal4")
    st.markdown('''
    <div class="text-bar">
        <div class="particles"></div>
        <h1>Andi ingin membeli buku tulis dan pulpen di sebuah toko alat tulis. Harga satu buku tulis adalah Rp7.000, sedangkan harga
        satu pulpen adalah Rp4.000. Uang yang dimiliki Andi hanya Rp162.000. Jika Andi membeli 6 buku tulis, berapa pulpen paling banyak
        yang masih bisa dibeli Andi? Tulis jawabanmu dalam bentuk pertidaksamaan dan tentukan nilai maksimum jumlah pulpen.</h1>
    </div>
    ''',unsafe_allow_html=True)
    st.session_state.jawaban5['jawab4'] = st.text_area("Masukan Jawaban 4")
    if st.button("Masukan Hasilnya"):
        if st.session_state.jawaban5['jawab1'] and st.session_state.jawaban5['jawab2'] and st.session_state.jawaban5['jawab3'] and st.session_state.jawaban5['jawab4']:
            url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdhYuNsgeSeGYP4PaX_K61jizyYpISAmjFs3rACGiuarpETKw/formResponse"
            data = {
            "entry.1901995254": nama,   # Ganti dengan entry ID dari form
            "entry.91265595": kelas,   # Ganti dengan entry ID dari form
            "entry.2066116752": sekolah,   # Ganti dengan entry ID dari form
            "entry.932030520": st.session_state.jawaban5['jawab1'],   # Ganti dengan entry ID dari form
            "entry.655296782": st.session_state.jawaban5['jawab2'],   # Ganti dengan entry ID dari form
            "entry.682901784": st.session_state.jawaban5['jawab3'],   # Ganti dengan entry ID dari form
            "entry.1986471437": st.session_state.jawaban5['jawab4'],   # Ganti dengan entry ID dari form
                }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                st.success("Berhasil dikirim!")
            else:
                st.error(f"Gagal mengirim. Status code: {response.status_code}")
        else:
            st.error("Ada Jawaban Soal yang masih kosong, Periksa lagi")
#========================================
if st.session_state.pretest2:
    soal_pretest2()
if st.session_state.kelompok['kondisi22']:
    if st.sidebar.button("Pretest", key="tombol30"):
        st.session_state.peta=False
        st.session_state.prasyarat = False
        st.session_state.pretest = False
        st.session_state.pretest2 = True
        st.session_state.kelompok['kondisi3']=True
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.materi_prasyarat = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
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
    st.markdown("<div class='submenu'>C. Sifat Kesetearaan</div>",unsafe_allow_html=True)
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
            st.session_state.cerita7=False
            st.session_state.cerita8=False
            st.session_state.cerita9=False
            st.session_state.cerita10=False
            st.session_state.pretest = False
            st.session_state.video1 = False
            st.session_state.video2 = False
            st.session_state.materi1 = False
            st.session_state.pretest1=False
            st.session_state.soal_kuisioner=False
            st.session_state.soal_kevalidan=False
            st.session_state.akhir=False
            st.session_state.kelompok['kondisi1']=False
            st.session_state.pretest2=False
            st.session_state.kelompok['kondisi1']=False
            st.session_state.posttest=False
            st.session_state.game=False
            st.session_state.kelompok['kondisi27']=False
            st.rerun()
    
if st.session_state.prasyarat:
    st.markdown('<style>.st-key-tombol1 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_prasyarat()

if st.session_state.kelompok['kondisi3']:
    if st.sidebar.button("Peta Konsep",key="tombol3"):
        st.session_state.kelompok['kondisi18']=True
        st.session_state.peta = True
        st.session_state.adaptif=False
        st.session_state.prasyarat = False
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.materi_prasyarat = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def tampilkan_video1():
    st.markdown("<div class='video'>Video Persamaan Satu variabel</div>",unsafe_allow_html=True)
    st.markdown('''
        <iframe src="https://drive.google.com/file/d/1U-60Jyervr5zTtUZJwCSUN5FmrxxrTcY/preview" width="640" height="480" allow="autoplay"></iframe>
    ''',unsafe_allow_html=True)
    st.markdown('**Courtesy by Youtube: https://www.youtube.com/embed/7veosRwnWVg?si=rt4Dahc9Ax30PAyw**')
if st.session_state.video1:
    st.markdown('<style>.st-key-tombol4 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    tampilkan_video1()
if st.session_state.kelompok['kondisi18']:
    if st.sidebar.button("Video Persamaan 1 Variabel", key="tombol4"):
        st.session_state.kelompok['kondisi4']=True
        st.session_state.peta = False
        st.session_state.video1 = True
        st.session_state.adaptif=False
        st.session_state.prasyarat = False
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.materi_prasyarat = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
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
    jawab1 = st.text_input("Jawaban no. 1")
    if jawab1:
        if int(jawab1)==4:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**2. Selesaikan Persamaan Berikut:**")
    st.latex("9x-4=23")
    jawab2 = st.text_input("Jawaban no. 2")
    if jawab2:
        if int(jawab2)==3:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**3. Tentukan nilai x:**")
    st.latex("12=3x+6")
    jawab3 = st.text_input("Jawaban no. 3")
    if jawab3:
        if int(jawab3)==2:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**4. Jika $4x-5=11$, tentukan nilai x**")
    jawab4 = st.text_input("Jawaban no. 4")
    if jawab4:
        if int(jawab4)==4:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**5. Selesaikan persamaan:**")
    st.latex("7x+8=3x+20")
    jawab5 = st.text_input("Jawaban no. 5")
    if jawab5:
        if int(jawab5)==3:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("""<div class='sublat1'>Soal Cerita</div>""",unsafe_allow_html=True)
    st.markdown("**6. Umur Dina 3 tahun lebih tua dari umur Rina. Jika jumlah umur mereka 27 tahun, tentukan umur Rina.**")
    jawab6 = st.text_input("Jawaban no. 6")
    if jawab6:
        if int(jawab6)==12:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**7. Sebuah bilangan jika dikalikan 4 hasilnya 28. Tentukan bilangan tersebut.**")
    jawab7 = st.text_input("Jawaban no. 7")
    if jawab7:
        if int(jawab7)==7:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**8. Jumlah dari 2 kali suatu bilangan dengan 5 sama dengan 19. Tentukan bilangan tersebut.**")
    jawab8 = st.text_input("Jawaban no. 8")
    if jawab8:
        if int(jawab8)==7:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**9. Harga sebuah buku tulis Rp2.500. Jika Andi membeli 4 buku tulis dan membayar Rp15.000, berapa uang kembalian Andi?**")
    jawab9 = st.text_input("Jawaban no. 9")
    if jawab9:
        if int(jawab9)==5000:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
    st.markdown("**10. Selisih dua kali suatu bilangan dengan 7 adalah 15. Tentukan bilangan tersebut.**")
    jawab10 = st.text_input("Jawaban no. 10")
    if jawab10:
        if int(jawab10)==11:
            st.markdown("<div class='cek'>Benar</div>",unsafe_allow_html=True)
        else:
            st.markdown("<div class='cek'>Salah</div>",unsafe_allow_html=True)
if st.session_state.materi:
    st.markdown('<style>.st-key-tombol5 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    materi_tampilkan()
if st.session_state.kelompok['kondisi4']:
    if st.sidebar.button("Materi Persamaan 1 Variabel",key="tombol5"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.adaptif=False
        st.session_state.materi = True
        st.session_state.kelompok['kondisi25']=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.materi_prasyarat = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.game=False
        st.session_state.kevalidan_media = False
        st.rerun()
#====permainan 1 variabel
def permainan_math():
    st.markdown('<style>.st-key-tombol40 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    kover()
if st.session_state['game']:
    permainan_math()
if st.session_state.kelompok["kondisi25"]:
    if st.sidebar.button("Permainan",key="tombol40"):
        st.session_state.peta=False
        st.session_state.prasyarat = False
        st.session_state.kelompok['kondisi19']=True
        st.session_state.game=True
        st.session_state.pretest1=False
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi_prasyarat = False
        st.session_state.materi1 = False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.posttest=False
        st.session_state.kevalidan_media = False
        st.rerun()

def video_pertidaksamaan():
    st.markdown("<div class='video'>Video Pertidaksamaan Satu variabel</div>",unsafe_allow_html=True)
    st.markdown('''
        <iframe src="https://drive.google.com/file/d/1mSF-vImZ8hxLOlcw8Gs8ME__Mcmy5Afn/preview" width="640" height="480" allow="autoplay"></iframe>
    ''',unsafe_allow_html=True)
    st.markdown('**Courtesy by Youtube: https://www.youtube.com/embed/SM7qejnJv28?si=8r2mqnQDD0-Eo1T5**')
if st.session_state.video2:
    st.markdown('<style>.st-key-tombol6 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    video_pertidaksamaan()
if st.session_state.kelompok['kondisi19']:
    if st.sidebar.button("Video Pertidaksamaan 1 Variabel", key="tombol6"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.adaptif=False
        st.session_state.materi = False
        st.session_state.kelompok['kondisi20']=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = True
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
def materi_pertidaksamaan():
    koding_html='''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pertidaksamaan 1 Variabel</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .nav-tabs {
            display: flex;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }

        .nav-tab {
            flex: 1;
            padding: 15px 20px;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            color: #6c757d;
            transition: all 0.3s ease;
        }

        .nav-tab:hover {
            background: #e9ecef;
        }

        .nav-tab.active {
            background: white;
            color: #4facfe;
            border-bottom: 3px solid #4facfe;
        }

        .content {
            padding: 30px;
            min-height: 600px;
        }

        .tab-content {
            display: none;
            animation: fadeIn 0.5s ease;
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .section {
            margin-bottom: 30px;
            padding: 25px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 5px solid #4facfe;
        }

        .section h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.4em;
        }

        .section p, .section li {
            color: #555;
            line-height: 1.6;
            margin-bottom: 10px;
        }

        .formula {
            background: #fff;
            padding: 15px;
            border-radius: 8px;
            border: 2px solid #e9ecef;
            font-family: 'Courier New', monospace;
            font-size: 1.1em;
            color: #333;
            margin: 15px 0;
        }

        .example {
            background: #e8f4f8;
            padding: 20px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #17a2b8;
        }

        .exercise {
            background: #fff;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border: 1px solid #e9ecef;
        }

        .exercise h4 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.2em;
        }

        .answer-input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            font-size: 16px;
            margin: 10px 0;
            transition: border-color 0.3s ease;
        }

        .answer-input:focus {
            outline: none;
            border-color: #4facfe;
            box-shadow: 0 0 0 3px rgba(79, 172, 254, 0.1);
        }

        .check-btn {
            background: linear-gradient(45deg, #28a745, #20c997);
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: transform 0.2s ease;
            margin-top: 10px;
        }

        .check-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(40, 167, 69, 0.3);
        }

        .result {
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-weight: 600;
            display: none;
        }

        .result.correct {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .result.incorrect {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .result.show {
            display: block;
            animation: slideDown 0.3s ease;
        }

        @keyframes slideDown {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .score-board {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }

        .score-board h3 {
            margin-bottom: 10px;
        }

        .score {
            font-size: 2em;
            font-weight: bold;
        }

        ul {
            padding-left: 20px;
        }

        @media (max-width: 768px) {
            .container {
                margin: 10px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .nav-tabs {
                flex-direction: column;
            }
            
            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔢 Pertidaksamaan 1 Variabel</h1>
            <p>Pelajari konsep dan latihan soal pertidaksamaan linear</p>
        </div>

        <div class="nav-tabs">
            <button class="nav-tab active" onclick="showTab('materi')">📚 Materi</button>
            <button class="nav-tab" onclick="showTab('latihan')">✏️ Latihan</button>
            <button class="nav-tab" onclick="showTab('hasil')">📊 Hasil</button>
        </div>

        <div class="content">
            <!-- Tab Materi -->
            <div id="materi" class="tab-content active">
                <div class="section">
                    <h3>🎯 Pengertian Pertidaksamaan 1 Variabel</h3>
                    <p>Pertidaksamaan linear satu variabel adalah kalimat matematika yang memuat variabel berpangkat satu dan dihubungkan dengan tanda pertidaksamaan.</p>
                    
                    <div class="formula">
                        Tanda-tanda pertidaksamaan:<br>
                        • &lt; (kurang dari)<br>
                        • &gt; (lebih dari)<br>
                        • ≤ (kurang dari atau sama dengan)<br>
                        • ≥ (lebih dari atau sama dengan)
                    </div>

                    <div class="example">
                        <strong>Contoh:</strong><br>
                        • 2x + 3 &lt; 7<br>
                        • -3x + 5 ≥ 11<br>
                        • 4x - 1 &gt; 2x + 5
                    </div>
                </div>

                <div class="section">
                    <h3>🔧 Cara Menyelesaikan Pertidaksamaan</h3>
                    <p>Langkah-langkah menyelesaikan pertidaksamaan linear:</p>
                    <ul>
                        <li>Kumpulkan suku-suku sejenis</li>
                        <li>Pindahkan variabel ke satu ruas dan konstanta ke ruas lain</li>
                        <li>Bagi atau kalikan dengan koefisien variabel</li>
                        <li><strong>PENTING:</strong> Jika membagi/mengalikan dengan bilangan negatif, balik tanda pertidaksamaan!</li>
                    </ul>

                    <div class="example">
                        <strong>Contoh Penyelesaian:</strong><br>
                        Selesaikan: 3x - 7 &lt; 2x + 5<br><br>
                        <strong>Langkah 1:</strong> 3x - 2x &lt; 5 + 7<br>
                        <strong>Langkah 2:</strong> x &lt; 12<br><br>
                        <strong>Jadi, penyelesaiannya adalah x &lt; 12</strong>
                    </div>
                </div>

                <div class="section">
                    <h3>⚠️ Aturan Khusus</h3>
                    <div class="example">
                        <strong>Ingat!</strong> Ketika membagi atau mengalikan dengan bilangan negatif, tanda pertidaksamaan dibalik.<br><br>
                        <strong>Contoh:</strong><br>
                        -2x &gt; 6<br>
                        x &lt; -3 (tanda &gt; berubah menjadi &lt; karena dibagi -2)
                    </div>
                </div>
            </div>

            <!-- Tab Latihan -->
            <div id="latihan" class="tab-content">
                <div class="score-board">
                    <h3>📊 Skor Anda</h3>
                    <div class="score" id="score">0 / 0</div>
                </div>

                <div class="exercise" id="exercise1">
                    <h4>Soal 1</h4>
                    <p>Selesaikan pertidaksamaan: <strong>2x + 5 &lt; 13</strong></p>
                    <input type="text" class="answer-input" id="answer1" placeholder="Contoh: x < 4 atau x > -2">
                    <button class="check-btn" onclick="checkAnswer(1, 'x < 4')">Periksa Jawaban</button>
                    <div class="result" id="result1"></div>
                </div>

                <div class="exercise" id="exercise2">
                    <h4>Soal 2</h4>
                    <p>Selesaikan pertidaksamaan: <strong>-3x + 7 ≥ 16</strong></p>
                    <input type="text" class="answer-input" id="answer2" placeholder="Masukkan jawaban Anda">
                    <button class="check-btn" onclick="checkAnswer(2, 'x ≤ -3')">Periksa Jawaban</button>
                    <div class="result" id="result2"></div>
                </div>

                <div class="exercise" id="exercise3">
                    <h4>Soal 3</h4>
                    <p>Selesaikan pertidaksamaan: <strong>4x - 3 &gt; 2x + 9</strong></p>
                    <input type="text" class="answer-input" id="answer3" placeholder="Masukkan jawaban Anda">
                    <button class="check-btn" onclick="checkAnswer(3, 'x > 6')">Periksa Jawaban</button>
                    <div class="result" id="result3"></div>
                </div>

                <div class="exercise" id="exercise4">
                    <h4>Soal 4</h4>
                    <p>Selesaikan pertidaksamaan: <strong>-5x + 2 &lt; 3x - 14</strong></p>
                    <input type="text" class="answer-input" id="answer4" placeholder="Masukkan jawaban Anda">
                    <button class="check-btn" onclick="checkAnswer(4, 'x > 2')">Periksa Jawaban</button>
                    <div class="result" id="result4"></div>
                </div>

                <div class="exercise" id="exercise5">
                    <h4>Soal 5</h4>
                    <p>Selesaikan pertidaksamaan: <strong>6x + 8 ≤ 2x - 4</strong></p>
                    <input type="text" class="answer-input" id="answer5" placeholder="Masukkan jawaban Anda">
                    <button class="check-btn" onclick="checkAnswer(5, 'x ≤ -3')">Periksa Jawaban</button>
                    <div class="result" id="result5"></div>
                </div>
            </div>

            <!-- Tab Hasil -->
            <div id="hasil" class="tab-content">
                <div class="score-board">
                    <h3>🎉 Hasil Akhir</h3>
                    <div class="score" id="finalScore">0 / 0</div>
                    <p id="performance"></p>
                </div>

                <div class="section">
                    <h3>📝 Detail Jawaban</h3>
                    <div id="answerDetails"></div>
                </div>

                <div class="section">
                    <h3>💡 Rekomendasi</h3>
                    <div id="recommendations"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let score = 0;
        let totalQuestions = 5;
        let answers = {};
        let correctAnswers = {
            1: 'x < 4',
            2: 'x ≤ -3', 
            3: 'x > 6',
            4: 'x > 2',
            5: 'x ≤ -3'
        };

        function showTab(tabName) {
            // Hide all tabs
            const tabs = document.querySelectorAll('.tab-content');
            tabs.forEach(tab => tab.classList.remove('active'));

            // Hide all nav tabs
            const navTabs = document.querySelectorAll('.nav-tab');
            navTabs.forEach(tab => tab.classList.remove('active'));

            // Show selected tab
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');

            // Update hasil tab when opened
            if (tabName === 'hasil') {
                updateResults();
            }
        }

        function normalizeAnswer(answer) {
            return answer.toLowerCase()
                         .replace(/\s+/g, '')
                         .replace(/≤/g, '<=')
                         .replace(/≥/g, '>=')
                         .replace(/</g, '<')
                         .replace(/>/g, '>');
        }

        function checkAnswer(questionNum, correctAnswer) {
            const userAnswer = document.getElementById(`answer${questionNum}`).value.trim();
            const resultDiv = document.getElementById(`result${questionNum}`);
            
            if (!userAnswer) {
                resultDiv.innerHTML = '⚠️ Silakan masukkan jawaban terlebih dahulu!';
                resultDiv.className = 'result incorrect show';
                return;
            }

            const normalizedUser = normalizeAnswer(userAnswer);
            const normalizedCorrect = normalizeAnswer(correctAnswer);

            // Store answer
            answers[questionNum] = {
                userAnswer: userAnswer,
                correctAnswer: correctAnswer,
                isCorrect: normalizedUser === normalizedCorrect
            };

            if (normalizedUser === normalizedCorrect) {
                resultDiv.innerHTML = '✅ Benar! Jawaban Anda tepat.';
                resultDiv.className = 'result correct show';
                if (!answers[questionNum].wasCorrect) {
                    score++;
                    answers[questionNum].wasCorrect = true;
                }
            } else {
                resultDiv.innerHTML = `❌ Kurang tepat. Jawaban yang benar: <strong>${correctAnswer}</strong><br>
                                     <small>Coba periksa kembali langkah penyelesaian Anda.</small>`;
                resultDiv.className = 'result incorrect show';
            }

            updateScore();
        }

        function updateScore() {
            document.getElementById('score').textContent = `${score} / ${totalQuestions}`;
        }

        function updateResults() {
            const finalScore = document.getElementById('finalScore');
            const performance = document.getElementById('performance');
            const answerDetails = document.getElementById('answerDetails');
            const recommendations = document.getElementById('recommendations');

            finalScore.textContent = `${score} / ${totalQuestions}`;

            // Performance message
            const percentage = (score / totalQuestions) * 100;
            if (percentage >= 80) {
                performance.innerHTML = '🌟 Excellent! Anda menguasai materi dengan baik.';
                performance.style.color = '#28a745';
            } else if (percentage >= 60) {
                performance.innerHTML = '👍 Good! Anda cukup memahami materi.';
                performance.style.color = '#ffc107';
            } else {
                performance.innerHTML = '📚 Perlu lebih banyak latihan untuk menguasai materi.';
                performance.style.color = '#dc3545';
            }

            // Answer details
            let detailsHTML = '';
            for (let i = 1; i <= totalQuestions; i++) {
                if (answers[i]) {
                    const icon = answers[i].isCorrect ? '✅' : '❌';
                    const status = answers[i].isCorrect ? 'Benar' : 'Salah';
                    detailsHTML += `
                        <div class="example">
                            <strong>Soal ${i}:</strong> ${icon} ${status}<br>
                            <strong>Jawaban Anda:</strong> ${answers[i].userAnswer || 'Tidak dijawab'}<br>
                            <strong>Jawaban Benar:</strong> ${answers[i].correctAnswer}
                        </div>
                    `;
                } else {
                    detailsHTML += `
                        <div class="example">
                            <strong>Soal ${i}:</strong> ⭕ Belum dijawab<br>
                            <strong>Jawaban Benar:</strong> ${correctAnswers[i]}
                        </div>
                    `;
                }
            }
            answerDetails.innerHTML = detailsHTML;

            // Recommendations
            let recHTML = '';
            if (percentage < 60) {
                recHTML = `
                    <p>💡 Disarankan untuk:</p>
                    <ul>
                        <li>Membaca kembali materi tentang aturan membalik tanda pertidaksamaan</li>
                        <li>Berlatih lebih banyak soal pertidaksamaan</li>
                        <li>Memperhatikan langkah-langkah penyelesaian dengan teliti</li>
                    </ul>
                `;
            } else if (percentage < 80) {
                recHTML = `
                    <p>💡 Untuk meningkatkan pemahaman:</p>
                    <ul>
                        <li>Latihan soal yang lebih variatif</li>
                        <li>Fokus pada soal dengan koefisien negatif</li>
                    </ul>
                `;
            } else {
                recHTML = `
                    <p>🎉 Selamat! Anda sudah menguasai materi dengan baik. Lanjutkan dengan materi pertidaksamaan yang lebih kompleks.</p>
                `;
            }
            recommendations.innerHTML = recHTML;
        }

        // Initialize score
        updateScore();
    </script>
</body>
</html>
'''
    components.html(koding_html, height=2600, width=None)
if st.session_state.materi1:
    st.markdown('<style>.st-key-tombol7 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    materi_pertidaksamaan()
if st.session_state.kelompok['kondisi20']:
    if st.sidebar.button("Materi Pertidaksamaan 1 Variabel",key="tombol7"):
        st.session_state.peta = False
        st.session_state.prasyarat = False
        st.session_state.materi_prasyarat = False
        st.session_state.adaptif=False
        st.session_state.materi = False
        st.session_state.kelompok['kondisi5']=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.cerita1=False
        st.session_state.cerita2=False
        st.session_state.cerita3=False
        st.session_state.cerita4=False
        st.session_state.cerita5=False
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pretest = False
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = True
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
def soal_adaptif():
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px; background-color:grey">
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
    st.markdown('<style>.st-key-tombol8 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_adaptif()
def level_kedua():
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px;">
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
    st.markdown(""" <div style="display:flex; justify-content:space-evenly;align-items:center; border:2px solid white; margin-bottom:10px; padding:2px;">
                    <img src='https://i.pinimg.com/originals/48/59/55/485955115c68020ce3ba16bf18a95d8a.gif' style='width:100px;'></img>
                    <div class="label">Level Ketiga</div>
                    </div>""",unsafe_allow_html=True)
    st.markdown("**Umur Budi 3 tahun lebih tua dari umur Andi. Jika jumlah umur mereka adalah 29 tahun, berapakah umur Andi?**")
    st.session_state.lvl3["jwb1"]=st.text_input("Jawaban 11")
    st.markdown("**Tentukan nilai $x$ pada persamaan:**")
    st.latex("\\frac{x}{3}+5=11")
    st.session_state.lvl3["jwb2"]=st.text_input("Jawaban 12")
    st.markdown("**Seorang pedagang membeli 5 buku dan 3 pensil dengan total harga Rp28.000. Jika harga sebuah buku Rp5.000, tentukan harga sebuah pensil dengan menggunakan persamaan satu variabel.**")
    st.session_state.lvl3["jwb3"]=st.text_input("Jawaban 13")
    st.markdown("**Carilah nilai $x$ pada persamaan**")
    st.latex("2(x-4)+3=11")
    st.session_state.lvl3["jwb4"]=st.text_input("Jawaban 14")
    st.markdown("**Panjang suatu persegi panjang adalah $x+5$ cm dan lebarnya $x-3$ cm. Jika kelilingnya 34 cm, tentukan nilai $x$**")
    st.session_state.lvl3["jwb5"]=st.text_input("Jawaban 15")
    kunci2 = [13,18,1000,8,7.5]
    skor2 = 0
    if st.button("Evaluasi 3"):
        indeks2=-1
        skor2=0
        for i in st.session_state.lvl3:
            indeks2 +=1
            if float(st.session_state.lvl3[i])==float(kunci2[indeks2]):
                skor2 +=20
    if skor2==100:
        st.markdown("<div id='lanjutkan'> Anda Sudah Berhasil...</div><div id=''ket>Silahkan Lanjut ke Soal Cerita berikutnya</div>",unsafe_allow_html=True)
        
if st.session_state.pengecekan2:
    level_ketiga()
    
if st.session_state.kelompok['kondisi5']:
    if st.sidebar.button("Soal Level",key="tombol8"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.adaptif=True
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi6']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.pretest2 = False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
def soal_cerita1():
    st.markdown("""
                <div class="efek1">Gotong Royong</div>""",unsafe_allow_html=True)
    st.image("https://quizizz.com/media/resource/gs/quizizz-media/quizzes/4204f59e-cf7a-4ec0-b2a7-d99f33f5d1e7",use_container_width=True)
    st.markdown("##### Warga sebuah desa bergotong royong membangun pos ronda.")
    st.markdown("""
                - ##### Pak Andi menyumbang Rp x. 
                - ##### Pak Budi menyumbang dua kali lipat dari sumbangan Pak Andi.
                - ##### Jumlah sumbangan Pak Candra adalah Rp20.000 lebih banyak dari sumbangan Pak Budi.
                """)
    st.markdown("##### Total sumbangan mereka bertiga adalah Rp270.000.")
    st.markdown("##### Pertanyaan")
    st.markdown("""
                <ol type="A">
                  <li style="font-size:20px">Tentukan berapa sumbangan Pak Candra dengan menggunakan persamaan satu variabel.</li>
                  <li style="font-size:20px">Bagaimana kegiatan gotong royong ini mencerminkan nilai persatuan dalam Pancasila?</li>
                </ol>
                """,unsafe_allow_html=True)
    st.session_state.jawaban1['jawab1']=st.text_area("Keterangan Jawaban1",value=st.session_state.jawaban1['jawab1'])
if st.session_state.cerita1:
    st.markdown('<style>.st-key-tombol10 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita1()
if st.session_state.kelompok['kondisi6']:
    st.sidebar.write("**Persamaan 1 variabel**")
    if st.sidebar.button("Gotong Royong",key="tombol10"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi7']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita2():
    st.markdown("""
                <div class="efek1">Jujur dalam Jual Beli (Sila ke-2: Kemanusiaan yang Adil dan Beradab)</div>""",unsafe_allow_html=True)
    st.image("https://st2.depositphotos.com/26922084/44234/v/450/depositphotos_442342356-stock-illustration-male-salesman-is-working-at.jpg",use_container_width=True)
    st.markdown("##### Dina membuka kios kecil di sekolah. Ia menjual roti seharga Rp4.000 dan teh botol seharga Rp6.000.")
    st.markdown("""
                 - ##### Suatu hari, Dina mencatat jumlah roti yang terjual adalah x. 
                 - ##### Jumlah teh botol yang terjual adalah 2 lebih banyak dari jumlah roti.
                 - ##### Uang hasil penjualan seluruhnya adalah Rp62.000.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""<ol type="A">
                <li style="font-size:20px"> Tentukan berapa jumlah roti yang Dina jual dengan menggunakan persamaan satu variabel.</li>
                <li style="font-size:20px"># Mengapa kejujuran dalam mencatat hasil penjualan merupakan bagian dari nilai kemanusiaan yang adil dan beradab?</li>
                """, unsafe_allow_html=True)
    st.session_state.jawaban1['jawab2']=st.text_area("Keterangan Jawaban2",value=st.session_state.jawaban1['jawab2'])
if st.session_state.cerita2:
    st.markdown('<style>.st-key-tombol11 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita2()
if st.session_state.kelompok['kondisi7']:
    if st.sidebar.button('Jujur dalam Jual Beli',key="tombol11"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi8']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita3():
    st.markdown("""
                <div class="efek1">Membantu Sesama (Sila ke-5: Keadilan Sosial bagi Seluruh Rakyat Indonesia)</div>""",unsafe_allow_html=True)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKwEHXofbmzkBvgR5IsxLAkYnTZU04_7-qoA&s",use_container_width=True)
    st.markdown("##### Sebuah kelas menggalang dana untuk membantu teman mereka yang sedang sakit.")
    st.markdown("""
                - ##### Setiap siswa menyumbang jumlah yang sama. 
                - ##### Jika jumlah siswa adalah $x$, maka uang terkumpul Rp1.500.000.
                - ##### Setelah dihitung ulang, ternyata ada 5 siswa yang tidak ikut menyumbang, sehingga total yang terkumpul hanya Rp1.350.000.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""<ol type='A'>
                <li style='font-size:20px'> Tentukan berapa jumlah siswa dalam kelas tersebut.</li>
                <li style='font-size:20px'>Bagaimana sikap membantu teman ini mencerminkan nilai keadilan sosial dalam Pancasila?</li>
                """,unsafe_allow_html=True)
    st.session_state.jawaban1['jawab3']=st.text_area("Keterangan Jawaban3",value=st.session_state.jawaban1['jawab3'])
if st.session_state.cerita3:
    st.markdown('<style>.st-key-tombol12 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita3()
if st.session_state.kelompok['kondisi8']:
    if st.sidebar.button("Membantu Sesama",key="tombol12"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi9']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
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
    st.markdown("""<ol type='A'>
                <li style='sont-size:20px'>Tentukan jumlah siswa dalam kelas tersebut dengan menggunakan persamaan satu variabel.</li>
                <li style='sont-size:20px'> Bagaimana kegiatan musyawarah dalam menentukan biaya ini sesuai dengan nilai kerakyatan dalam Pancasila?</li>
                """,unsafe_allow_html=True)
    st.session_state.jawaban1['jawab4']=st.text_area("Keterangan Jawaban4", value=st.session_state.jawaban1['jawab4'])
if st.session_state.cerita4:
    st.markdown('<style>.st-key-tombol13 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita4()
if st.session_state.kelompok['kondisi9']:
    if st.sidebar.button("Musyawarah Kelas",key="tombol13"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi10']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
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
    st.markdown("""<ol type='A'>
                <li style='font-size:20px'> Tentukan berapa banyak karung beras yang disumbangkan masing-masing kelompok dengan menggunakan persamaan satu variabel.</li>
                <li style='font-size:20px'> Mengapa kegiatan ini mencerminkan nilai toleransi dan Ketuhanan Yang Maha Esa dalam Pancasila?</li>
                """,unsafe_allow_html=True)
    st.session_state.jawaban1['jawab5']=st.text_area("Keterangan Jawaban5",value=st.session_state.jawaban1['jawab5'])
if st.session_state.cerita5:
    st.markdown('<style>.st-key-tombol15 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita5()
if st.session_state.kelompok['kondisi10']:
    if st.sidebar.button("Kerukunan Agama", key="tombol15"):
        st.session_state.kelompok['kondisi16']=False
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi11']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita6():
    st.markdown("""
                <div class="efek1">Batas Maksimal Sumbangan Kegiatan Desa(Sila ke-3: Persatuan Indonesia)</div>""",unsafe_allow_html=True)
    st.image("https://pamongdidik.wordpress.com/wp-content/uploads/2014/07/3d324-berdagang-di-pasar-pamong-didik.gif",use_container_width=True)
    st.markdown("##### Dalam rangka memperingati Hari Kemerdekaan, sebuah desa mengadakan lomba 17 Agustus. Panitia memutuskan bahwa:.")
    st.markdown("""
                - ##### Setiap kepala keluarga menyumbang uang dalam jumlah yang sama, yaitu Rp $x$ 
                - ##### Agar tidak memberatkan warga, besar sumbangan tiap keluarga tidak boleh lebih dari Rp50.000 dan tidak boleh kurang dari Rp. 5.000.
                - ##### Jumlah keluarga di desa tersebut adalah 120.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Nyatakan situasi ini dalam bentuk pertidaksamaan satu variabel.
                - ##### Berapakah rentang nilai sumbangan yang mungkin diminta panitia?
                - ##### Bagaimana kegiatan gotong royong ini mencerminkan nilai persatuan dan kebersamaan dalam Pancasila?
                """)
    st.session_state.jawaban1['jawab6']=st.text_area("Keterangan Jawaban6",value=st.session_state.jawaban1['jawab6'])
if st.session_state.cerita6:
    st.markdown('<style>.st-key-tombol16 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita6()
if st.session_state.kelompok['kondisi11']:
    st.sidebar.write("**Pertidaksamaan 1 variabel**")
    if st.sidebar.button("Sumbangan Kegiatan", key="tombol16"):
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
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi12']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita7():
    st.markdown("""
                <div class="efek1">Kejujuran dalam Jualan Kantin(Sila ke-2: Kemanusiaan yang Adil dan Beradab)</div>""",unsafe_allow_html=True)
    st.image("https://bimamedia-gurusiana.ap-south-1.linodeobjects.com/dd6298e7c9a2c63b6ab43846ddd7ddbe/2023/09/19/l-img20230919132907jpg20230919132935.jpeg",use_container_width=True)
    st.markdown("##### Ani berjualan roti di kantin sekolah.")
    st.markdown("""
                - ##### Harga satu roti adalah Rp3.500. 
                - ##### Dalam sehari, Ani membawa paling sedikit 40 roti, tetapi tidak lebih dari 80 roti.
                - ##### Jika jumlah roti yang tidak terjual dikurangi, Ani akan rugi. Oleh karena itu, ia ingin memastikan jumlah roti yang dibawa masih cukup wajar agar bisa laku habis.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Tuliskan pertidaksamaan yang menyatakan jumlah roti yang dibawa Ani.
                - ##### Jika setiap roti yang terjual memberi keuntungan Rp1.000, tentukan batas minimum dan maksimum keuntungan Ani dalam sehari.
                - ##### Mengapa sikap jujur Ani dalam mencatat hasil penjualan sesuai dengan nilai kemanusiaan yang adil dan beradab?
                """)
    st.session_state.jawaban1['jawab7']=st.text_area("Keterangan Jawaban7",st.session_state.jawaban1['jawab7'])
if st.session_state.cerita7:
    st.markdown('<style>.st-key-tombol17 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita7()
if st.session_state.kelompok['kondisi12']:
    if st.sidebar.button("Kejujuran", key="tombol17"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=True
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi13']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita8():
    st.markdown("""
                <div class="efek1">Membantu Teman yang Sakit(Sila ke-5: Keadilan Sosial bagi Seluruh Rakyat Indonesia)</div>""",unsafe_allow_html=True)
    st.image("https://i0.wp.com/legutykids.com/wp-content/uploads/2021/05/Terima-kasih-sudah-memberikan-apresiasi-terhadap-buku-Aku-Cinta-Al-Quran.jpg?fit=2000%2C1332&quality=99&ssl=1",use_container_width=True)
    st.markdown("##### Siswa kelas 8 SMP mengadakan penggalangan dana untuk membantu teman yang sedang dirawat di rumah sakit.")
    st.markdown("""
                - ##### Setiap siswa menyumbang minimal Rp10.000, tetapi maksimal Rp30.000. 
                - ##### Jumlah siswa di kelas ada 36 orang.
                - ##### Total dana yang akan terkumpul bergantung pada berapa besar sumbangan tiap siswa.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Nyatakan jumlah sumbangan tiap siswa sebagai $x$, lalu buat pertidaksamaan yang menggambarkan kondisi tersebut.
                - ##### Tentukan rentang total dana yang mungkin terkumpul.
                - ##### Bagaimana kegiatan ini mencerminkan nilai keadilan sosial dalam Pancasila?
                """)
    st.session_state.jawaban1['jawab8']=st.text_area("Keterangan Jawaban8",value=st.session_state.jawaban1['jawab8'])
if st.session_state.cerita8:
    st.markdown('<style>.st-key-tombol18 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita8()
if st.session_state.kelompok['kondisi13']:
    if st.sidebar.button("Membantu Teman", key="tombol18"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=True
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi14']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita9():
    st.markdown("""
                <div class="efek1">Musyawarah Menentukan Uang Kas(Sila ke-4: Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan)</div>""",unsafe_allow_html=True)
    st.image("https://i.pinimg.com/736x/81/2b/1a/812b1acc0b6856b3eefde041db3bb318.jpg",use_container_width=True)
    st.markdown("##### Sebuah kelas berencana mengumpulkan uang kas untuk kegiatan akhir tahun.")
    st.markdown("""
                - ##### Mereka bermusyawarah dan memutuskan bahwa uang kas per siswa adalah Rp $x$   
                - ##### Agar tidak memberatkan siswa, uang kas minimal Rp20.000 dan maksimal Rp40.000 per bulan.
                - ##### Jumlah siswa dalam kelas adalah 30 orang.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Nyatakan kondisi di atas dalam bentuk pertidaksamaan.
                - ##### Tentukan batas minimum dan maksimum uang kas kelas dalam sebulan.
                - ##### Bagaimana kegiatan musyawarah ini mencerminkan nilai demokrasi dalam Pancasila?
                """)
    st.session_state.jawaban1['jawab9']=st.text_area("Keterangan Jawaban9",value=st.session_state.jawaban1['jawab9'])
if st.session_state.cerita9:
    st.markdown('<style>.st-key-tombol19 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita9()
if st.session_state.kelompok['kondisi14']:
    if st.sidebar.button("Musyawarah", key="tombol19"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=True
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi15']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def soal_cerita10():
    st.markdown("""
                <div class="efek1">Toleransi dalam Bakti Sosial Antar Umat Beragama(Sila ke-1: Ketuhanan Yang Maha Esa)</div>""",unsafe_allow_html=True)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT73VR8497iR5RWViDdDXNK_Vwz1fole01r7g&s",use_container_width=True)
    st.markdown("##### Sebuah kampung mengadakan bakti sosial lintas agama.")
    st.markdown("""
                - ##### Setiap warga berkomitmen menyumbangkan beras minimal 2 kg, tetapi tidak lebih dari 8 kg.   
                - ##### Jika jumlah warga yang ikut serta adalah 60 orang, maka jumlah total beras yang terkumpul akan berada dalam batas tertentu.
                """)
    st.markdown("##### Pertanyaan")
    st.markdown("""
                - ##### Buat pertidaksamaan untuk menggambarkan jumlah sumbangan beras tiap warga.
                - ##### Tentukan rentang jumlah total beras yang mungkin terkumpul.
                - ##### Bagaimana kegiatan ini mencerminkan nilai toleransi antar umat beragama dan Ketuhanan Yang Maha Esa?
                """)
    st.session_state.jawaban1['jawab10']=st.text_area("Keterangan Jawaban10",st.session_state.jawaban1['jawab10'])
if st.session_state.cerita10:
    st.markdown('<style>.st-key-tombol20 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_cerita10()
if st.session_state.kelompok['kondisi15']:
    if st.sidebar.button("Toleransi", key="tombol20"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=True
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi16']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()

def hasil_akhir():
    st.write(st.session_state.jawaban1)
    if nama and kelas and sekolah:
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSewIefkRWG20MZKNTE9uj2GsAGcJh7692-F9sA3MZBmwwmLIg/formResponse"
        data = {
            "entry.998794637": nama,   # Ganti dengan entry ID dari form
            "entry.1343498210": kelas,   # Ganti dengan entry ID dari form
            "entry.1376928479": sekolah,   # Ganti dengan entry ID dari form
            "entry.830868808": st.session_state.jawaban1['jawab1'],   # Ganti dengan entry ID dari form
            "entry.737462487": st.session_state.jawaban1['jawab2'],   # Ganti dengan entry ID dari form
            "entry.489962711": st.session_state.jawaban1['jawab3'],   # Ganti dengan entry ID dari form
            "entry.1164660499": st.session_state.jawaban1['jawab4'],   # Ganti dengan entry ID dari form
            "entry.745281971": st.session_state.jawaban1['jawab5'],   # Ganti dengan entry ID dari form
            "entry.1568896331": st.session_state.jawaban1['jawab6'],   # Ganti dengan entry ID dari form
            "entry.433217618": st.session_state.jawaban1['jawab7'],   # Ganti dengan entry ID dari form
            "entry.1675641791": st.session_state.jawaban1['jawab8'],   # Ganti dengan entry ID dari form
            "entry.1207143181": st.session_state.jawaban1['jawab9'],   # Ganti dengan entry ID dari form
            "entry.125676604": st.session_state.jawaban1['jawab10'],   # Ganti dengan entry ID dari form
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            st.success("Berhasil dikirim!")
        else:
            st.error(f"Gagal mengirim. Status code: {response.status_code}")
if st.session_state.akhir:
    st.markdown('<style>.st-key-tombol21 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    hasil_akhir()
if st.session_state.kelompok['kondisi16']:
    if st.sidebar.button("Lihat Hasil Akhir",key="tombol21"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi26']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=True
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
#==========================================
if st.session_state.posttest:
    st.markdown('<style>.st-key-tombol50 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    soal_pretest3()
if st.session_state.kelompok['kondisi26']:
    if st.sidebar.button("Postest",key="tombol50"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi23']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=True
        st.session_state.akhir=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
#========================================
if st.session_state.kelompok['kondisi23']:
    if st.sidebar.button("Pendapat Siswa",key="tombol31"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi24']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=True
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
#===============================================
if st.session_state.kelompok['kondisi24']:
    if st.sidebar.button("Pendapat Guru",key="tombol32"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi29']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=True
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = False
        st.rerun()
#===============
if st.session_state.kevalidan_media:
    st.markdown('<style>.st-key-tombol60 .e8vg11g2{background-color:blue;color:yellow}</style>',unsafe_allow_html=True)
    tampilkan_kevalidan1()
if st.session_state.kelompok['kondisi29']:
    if st.sidebar.button("Pendapat Ahli Media",key="tombol60"):
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
        st.session_state.cerita6=False
        st.session_state.cerita7=False
        st.session_state.cerita8=False
        st.session_state.cerita9=False
        st.session_state.cerita10=False
        st.session_state.pengecekan1 = False
        st.session_state.pengecekan2 = False
        st.session_state.pretest = False
        st.session_state.kelompok['kondisi29']=True
        st.session_state.video1 = False
        st.session_state.video2 = False
        st.session_state.materi1 = False
        st.session_state.pretest1=False
        st.session_state.soal_kuisioner=False
        st.session_state.soal_kevalidan=False
        st.session_state.akhir=False
        st.session_state.kelompok['kondisi1']=False
        st.session_state.posttest=False
        st.session_state.game=False
        st.session_state.kelompok['kondisi27']=False
        st.session_state.kevalidan_media = True
        st.rerun()





























