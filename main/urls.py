from .views import *
from django.urls import path

urlpatterns = [

    # ОБЛУСТАР

    path("", home, name="home"),
    path("batken/", batken, name="batken"),
    path("jalal-abad/", jalal_abad, name="jalal_abad"),
    path("naryn/", naryn, name="naryn"),
    path("osh/", osh, name="osh"),
    path("chuy/", chuy, name="chuy"),
    path("talas/", talas, name="talas"),
    path("ysyk-kol/", ysyk_kol, name="ysyk_kol"),


    # БАТКЕН ОБЛУСУ 

    path("batken/batken_rayon/", r_batken, name="batken_rayon"),
    path("batken/kadamjai/", r_kadamjai, name="kadamjai"),
    path("batken/leylek/", r_leylek, name="leylek"),


    # ЖАЛАЛ-АБАД ОБЛУСУ 

    path("jalal-abad/aqsy/", r_aqsy, name="aqsy"),
    path("jalal-abad/ala-buka/", r_ala_buka, name="ala_buka"),
    path("jalal-abad/bazar-korgon/", r_bazar_korgon, name="bazar_korgon"),
    path("jalal-abad/nooken/", r_nooken, name="nooken"),
    path("jalal-abad/suzak/", r_suzak, name="suzak"),
    path("jalal-abad/toguz-toro/", r_toguz_toro, name="toguz_toro"),
    path("jalal-abad/toktogul/", r_toktogul, name="toktogul"),
    path("jalal-abad/chatkal/", r_chatkal, name="chatkal"),


    # НАРЫН ОБЛУСУ 

    path("naryn/ak-talaa/", r_ak_talaa, name="ak_talaa"),
    path("naryn/at-bashy/", r_at_bashy, name="at_bashy"),
    path("naryn/jumgal/", r_jumgal, name="jumgal"),
    path("naryn/kochkor/", r_kochkor, name="kochkor"),
    path("naryn/naryn_rayon/", r_naryn, name="naryn_rayon"),


    # ОШ ОБЛУСУ 

    path("osh/alai/", r_alai, name="alai"),
    path("osh/aravan/", r_aravan, name="aravan"),
    path("osh/karakulja/", r_karakulja, name="karakulja"),
    path("osh/kara-suu/", r_kara_suu, name="kara_suu"),
    path("osh/nookat/", r_nookat, name="nookat"),
    path("osh/ozgon/", r_ozgon, name="ozgon"),
    path("osh/chon-alai/", r_chon_alai, name="chon_alai"),


    # ТАЛАС ОБЛУСУ 

    path("talas/bakai-ata/", r_bakai_ata, name="bakai_ata"),
    path("talas/aitmatov/", r_aitmatov, name="aitmatov"),
    path("talas/manas/", r_manas, name="manas"),
    path("talas/talas_rayon/", r_talas, name="talas_rayon"),


    # ЧҮЙ ОБЛУСУ

    path("chuy/alamudun/", r_alamudun, name="alamudun"),
    path("chuy/zhaiyl/", r_zhaiyl, name="zhaiyl"),
    path("chuy/kemin/", r_kemin, name="kemin"),
    path("chuy/moscow/", r_moscow, name="moscow"),
    path("chuy/panfilov/", r_panfilov, name="panfilov"),
    path("chuy/sokuluk/", r_sokuluk, name="sokuluk"),
    path("chuy/ysyk-ata/", r_ysyk_ata, name="ysyk_ata"),
    path("chuy/chuy_rayon/", r_chuy, name="chuy_rayon"),


    # ЫСЫК-КӨЛ ОБЛУСУ 

    path("ysyk-kol/ak-suu/", r_ak_suu, name="ak_suu"),
    path("ysyk-kol/jeti-oguz/", r_jeti_oguz, name="jeti_oguz"),
    path("ysyk-kol/ysyk-kol_rayon/", r_ysyk_kol, name="ysyk_kol_rayon"),
    path("ysyk-kol/ton/", r_ton, name="ton"),
    path("ysyk-kol/tup/", r_tup, name="tup"),
]