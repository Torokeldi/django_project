from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def batken(request):
    return render(request, "batken.html")


def jalal_abad(request):
    return render(request, "jalal_abad.html")


def naryn(request):
    return render(request, "naryn.html")


def osh(request):
    return render(request, "osh.html")


def chuy(request):
    return render(request, "chuy.html")


def talas(request):
    return render(request, "talas.html")


def ysyk_kol(request):
    return render(request, "ysyk_kol.html")



# Баткен облусу
def r_batken(request):
    return render(request, "Batken/batken.html")

def r_batken_rayonu(request):
    return render(request, "Batken/batken_rayonu.html")

def r_kadamjai(request):
    return render(request, "Batken/kadamjai.html")

def r_leylek(request):
    return render(request, "Batken/leylek.html")


# Жалал-Абад облусу
def r_ala_buka(request):
    return render(request, "Jalal_abad/ala_buka.html")

def r_aqsy(request):
    return render(request, "Jalal_abad/aqsy.html")

def r_bazar_korgon(request):
    return render(request, "Jalal_abad/bazar_korgon.html")

def r_nooken(request):
    return render(request, "Jalal_abad/nooken.html")

def r_suzak(request):
    return render(request, "Jalal_abad/suzak.html")

def r_toguz_toro(request):
    return render(request, "Jalal_abad/toguz_toro.html")

def r_toktogul(request):
    return render(request, "Jalal_abad/toktogul.html")

def r_chatkal(request):
    return render(request, "Jalal_abad/chatkal.html")


# Нарын облусу
def r_naryn(request):
    return render(request, "Naryn/naryn.html")

def r_ak_talaa(request):
    return render(request, "Naryn/ak_talaa.html")

def r_at_bashy(request):
    return render(request, "Naryn/at_bashy.html")

def r_kochkor(request):
    return render(request, "Naryn/kochkor.html")

def r_jumgal(request):
    return render(request, "Naryn/jumgal.html")


# Ош облусу
def r_chon_alai(request):
    return render(request, "Osh/chon_alai.html")

def r_alai(request):
    return render(request, "Osh/alai.html")

def r_aravan(request):
    return render(request, "Osh/aravan.html")

def r_karakulja(request):
    return render(request, "Osh/karakulja.html")

def r_kara_suu(request):
    return render(request, "Osh/kara_suu.html")

def r_nookat(request):
    return render(request, "Osh/nookat.html")

def r_ozgon(request):
    return render(request, "Osh/ozgon.html")


# Чүй облусу
def r_chuy(request):
    return render(request, "Chuy/chuy.html")

def r_alamudun(request):
    return render(request, "Chuy/alamudun.html")

def r_zhaiyl(request):
    return render(request, "Chuy/zhaiyl.html")

def r_kemin(request):
    return render(request, "Chuy/kemin.html")

def r_moscow(request):
    return render(request, "Chuy/moscow.html")

def r_panfilov(request):
    return render(request, "Chuy/panfilov.html")

def r_sokuluk(request):
    return render(request, "Chuy/sokuluk.html")

def r_ysyk_ata(request):
    return render(request, "Chuy/ysyk_ata.html")


# Талас облусу
def r_talas(request):
    return render(request, "Talas/talas.html")

def r_bakai_ata(request):
    return render(request, "Talas/bakai_ata.html")

def r_aitmatov(request):
    return render(request, "Talas/aitmatov.html")

def r_manas(request):
    return render(request, "Talas/manas.html")


# Ысык-Көл облусу
def r_ysyk_kol(request):
    return render(request, "Ysyk_kol/ysyk_kol_rayon.html")

def r_ak_suu(request):
    return render(request, "Ysyk_kol/ak_suu.html")

def r_jeti_oguz(request):
    return render(request, "Ysyk_kol/jeti_oguz.html")

def r_ton(request):
    return render(request, "Ysyk_kol/ton.html")

def r_tup(request):
    return render(request, "Ysyk_kol/tup.html")