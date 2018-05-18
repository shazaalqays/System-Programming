from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .models import User,ogrenci, hoca, yonetim, kullanici_account,ogrenci_ders, dersdetaylari, ders, sorular, sonuclar, fakulte_bolum


def home(request):
    args = {'ad': request.user.ad,
            'soyad': request.user.soyad}

    if request.user.staff:
        return redirect('../admin/')
    elif request.user.ogr:
        return render(request, 'accounts/ogrenciHOME.html', args)
    elif request.user.hoc:
        return render(request, 'accounts/hocaHOME.html', args)
    elif request.user.yon:
        return render(request, 'accounts/yonetimHOME.html', args)


def anket(request):
    if request.user.ogr:
        profil          = ogrenci.objects.filter(ogrenci_no=request.user.username)
        ogrno           = [a.ogrenci_no for a in profil]
        dersler         = ogrenci_ders.objects.filter(ogrenci_no__in=ogrno)
        derskodlari     = [a.ders_kodu for a in dersler]
        dersgruplari    = [a.grup_no for a in dersler]
        anketyapilan    = sonuclar.objects.filter(ogrenci_no__in=ogrno)
        anketyapilanders= [a.ders_kodu for a in anketyapilan]
        dersler         = ders.objects.none()
        for index, kod in enumerate(derskodlari):
            derstmp         = ders.objects.filter(ders_kodu=kod, grup_no=dersgruplari[index])
            ekle = True
            derstmpDK   =  [a.ders_kodu.ders_kodu for a in derstmp]
            for DDK in derstmpDK:
                for ayd in anketyapilanders:
                    if DDK == ayd:
                        ekle = False
            if ekle:
                dersler         = dersler | derstmp
        tumsorular         = sorular.objects.all()
        args = {'dersler': dersler, 'sorular': tumsorular}
    return render(request, 'accounts/anket.html',args)


def sonucgor(request):
    if request.user.hoc:
        profil      = hoca.objects.filter(hoca_kodu=request.user.username)
        hocakodu    = [a.hoca_kodu for a in profil]
        dersler     = ders.objects.filter(hoca_kodu__in=hocakodu)
        derskodlari = [a.ders_kodu.ders_kodu for a in dersler]
        dersgruplari= [a.grup_no for a in dersler]
        dersson     = sonuclar.objects.none()
        for index, kod in enumerate(derskodlari):
            derstmp         = sonuclar.objects.filter(ders_kodu=kod, grup_no=dersgruplari[index])
            dersson         = dersson | derstmp
        counter = 0
        soru01 = 0
        soru02 = 0
        soru03 = 0
        soru04 = 0
        soru05 = 0
        soru06 = 0
        soru07 = 0
        soru08 = 0
        soru09 = 0
        sonuclarsoru01 = [a.sonuc01 for a in dersson]
        sonuclarsoru02 = [a.sonuc02 for a in dersson]
        sonuclarsoru03 = [a.sonuc03 for a in dersson]
        sonuclarsoru04 = [a.sonuc04 for a in dersson]
        sonuclarsoru05 = [a.sonuc05 for a in dersson]
        sonuclarsoru06 = [a.sonuc06 for a in dersson]
        sonuclarsoru07 = [a.sonuc07 for a in dersson]
        sonuclarsoru08 = [a.sonuc08 for a in dersson]
        sonuclarsoru09 = [a.sonuc09 for a in dersson]
        for s in sonuclarsoru01:
            soru01 += s
            counter += 1
        for s in sonuclarsoru02:
            soru02 += s
        for s in sonuclarsoru03:
            soru03 += s
        for s in sonuclarsoru04:
            soru04 += s
        for s in sonuclarsoru05:
            soru05 += s
        for s in sonuclarsoru06:
            soru06 += s
        for s in sonuclarsoru07:
            soru07 += s
        for s in sonuclarsoru08:
            soru08 += s
        for s in sonuclarsoru09:
            soru09 += s
        if counter > 0:
            soru01 /= counter
            soru02 /= counter
            soru03 /= counter
            soru04 /= counter
            soru05 /= counter
            soru06 /= counter
            soru07 /= counter
            soru08 /= counter
            soru09 /= counter
        tumsorular         = sorular.objects.all()
        args = {'sorular':tumsorular,'soru01':soru01,'soru02':soru02,'soru03':soru03,
        'soru04':soru04,'soru05':soru05,'soru06':soru06,'soru07':soru07,'soru08':soru08,
        'soru09':soru09}
    else:
        profil              = yonetim.objects.filter(YonetimID=request.user.username)
        makam               = [a.makam for a in profil]
        if makam == ['BY']:
            rapor               = []
            bolum               = [a.bolum_kodu for a in profil]
            hocalar             = hoca.objects.filter(bolum_kodu__in=bolum)
            for h in hocalar:
                dersler     = ders.objects.filter(hoca_kodu=h)
                derskodlari = [a.ders_kodu.ders_kodu for a in dersler]
                dersgruplari= [a.grup_no for a in dersler]
                dersson     = sonuclar.objects.none()
                fakultesi   = fakulte_bolum.objects.filter(bolum_kodu=h.bolum_kodu)
                for f in fakultesi:
                    fakultee    = f.fakulte_kodu.fakulte_adi
                for index, kod in enumerate(derskodlari):
                    derstmp         = sonuclar.objects.filter(ders_kodu=kod, grup_no=dersgruplari[index])
                    dersson         = dersson | derstmp
                counter = 0
                soru01 = 0
                soru02 = 0
                soru03 = 0
                soru04 = 0
                soru05 = 0
                soru06 = 0
                soru07 = 0
                soru08 = 0
                soru09 = 0
                sonuclarsoru01 = [a.sonuc01 for a in dersson]
                sonuclarsoru02 = [a.sonuc02 for a in dersson]
                sonuclarsoru03 = [a.sonuc03 for a in dersson]
                sonuclarsoru04 = [a.sonuc04 for a in dersson]
                sonuclarsoru05 = [a.sonuc05 for a in dersson]
                sonuclarsoru06 = [a.sonuc06 for a in dersson]
                sonuclarsoru07 = [a.sonuc07 for a in dersson]
                sonuclarsoru08 = [a.sonuc08 for a in dersson]
                sonuclarsoru09 = [a.sonuc09 for a in dersson]
                for s in sonuclarsoru01:
                    soru01 += s
                    counter += 1
                for s in sonuclarsoru02:
                    soru02 += s
                for s in sonuclarsoru03:
                    soru03 += s
                for s in sonuclarsoru04:
                    soru04 += s
                for s in sonuclarsoru05:
                    soru05 += s
                for s in sonuclarsoru06:
                    soru06 += s
                for s in sonuclarsoru07:
                    soru07 += s
                for s in sonuclarsoru08:
                    soru08 += s
                for s in sonuclarsoru09:
                    soru09 += s
                if counter > 0:
                    soru01 /= counter
                    soru02 /= counter
                    soru03 /= counter
                    soru04 /= counter
                    soru05 /= counter
                    soru06 /= counter
                    soru07 /= counter
                    soru08 /= counter
                    soru09 /= counter
                    rapor.append([int(h.hoca_kodu),h.ad,h.soyad,h.bolum,
                                fakultee,soru01,soru02,soru03,
                                soru04,soru05,soru06,soru07,soru08,soru09])
        elif makam == ['FY']:
            rapor               = []
            yonetimfakultesi    = [a.fakulte_kodu for a in profil]
            bolumler            = fakulte_bolum.objects.filter(fakulte_kodu__in=yonetimfakultesi)
            bolum               = [a.bolum_kodu for a in bolumler]
            hocalar             = hoca.objects.filter(bolum_kodu__in=bolum)
            for h in hocalar:
                dersler     = ders.objects.filter(hoca_kodu=h)
                derskodlari = [a.ders_kodu.ders_kodu for a in dersler]
                dersgruplari= [a.grup_no for a in dersler]
                dersson     = sonuclar.objects.none()
                fakultesi   = fakulte_bolum.objects.filter(bolum_kodu=h.bolum_kodu)
                for f in fakultesi:
                    fakultee    = f.fakulte_kodu.fakulte_adi
                for index, kod in enumerate(derskodlari):
                    derstmp         = sonuclar.objects.filter(ders_kodu=kod, grup_no=dersgruplari[index])
                    dersson         = dersson | derstmp
                counter = 0
                soru01 = 0
                soru02 = 0
                soru03 = 0
                soru04 = 0
                soru05 = 0
                soru06 = 0
                soru07 = 0
                soru08 = 0
                soru09 = 0
                sonuclarsoru01 = [a.sonuc01 for a in dersson]
                sonuclarsoru02 = [a.sonuc02 for a in dersson]
                sonuclarsoru03 = [a.sonuc03 for a in dersson]
                sonuclarsoru04 = [a.sonuc04 for a in dersson]
                sonuclarsoru05 = [a.sonuc05 for a in dersson]
                sonuclarsoru06 = [a.sonuc06 for a in dersson]
                sonuclarsoru07 = [a.sonuc07 for a in dersson]
                sonuclarsoru08 = [a.sonuc08 for a in dersson]
                sonuclarsoru09 = [a.sonuc09 for a in dersson]
                for s in sonuclarsoru01:
                    soru01 += s
                    counter += 1
                for s in sonuclarsoru02:
                    soru02 += s
                for s in sonuclarsoru03:
                    soru03 += s
                for s in sonuclarsoru04:
                    soru04 += s
                for s in sonuclarsoru05:
                    soru05 += s
                for s in sonuclarsoru06:
                    soru06 += s
                for s in sonuclarsoru07:
                    soru07 += s
                for s in sonuclarsoru08:
                    soru08 += s
                for s in sonuclarsoru09:
                    soru09 += s
                if counter > 0:
                    soru01 /= counter
                    soru02 /= counter
                    soru03 /= counter
                    soru04 /= counter
                    soru05 /= counter
                    soru06 /= counter
                    soru07 /= counter
                    soru08 /= counter
                    soru09 /= counter
                    rapor.append([int(h.hoca_kodu),h.ad,h.soyad,h.bolum,
                                fakultee,soru01,soru02,soru03,
                                soru04,soru05,soru06,soru07,soru08,soru09])
        else:
            rapor               = []
            hocalar             = hoca.objects.all()
            for h in hocalar:
                dersler     = ders.objects.filter(hoca_kodu=h)
                derskodlari = [a.ders_kodu.ders_kodu for a in dersler]
                dersgruplari= [a.grup_no for a in dersler]
                dersson     = sonuclar.objects.none()
                fakultesi   = fakulte_bolum.objects.filter(bolum_kodu=h.bolum_kodu)
                for f in fakultesi:
                    fakultee    = f.fakulte_kodu.fakulte_adi
                for index, kod in enumerate(derskodlari):
                    derstmp         = sonuclar.objects.filter(ders_kodu=kod, grup_no=dersgruplari[index])
                    dersson         = dersson | derstmp
                counter = 0
                soru01 = 0
                soru02 = 0
                soru03 = 0
                soru04 = 0
                soru05 = 0
                soru06 = 0
                soru07 = 0
                soru08 = 0
                soru09 = 0
                sonuclarsoru01 = [a.sonuc01 for a in dersson]
                sonuclarsoru02 = [a.sonuc02 for a in dersson]
                sonuclarsoru03 = [a.sonuc03 for a in dersson]
                sonuclarsoru04 = [a.sonuc04 for a in dersson]
                sonuclarsoru05 = [a.sonuc05 for a in dersson]
                sonuclarsoru06 = [a.sonuc06 for a in dersson]
                sonuclarsoru07 = [a.sonuc07 for a in dersson]
                sonuclarsoru08 = [a.sonuc08 for a in dersson]
                sonuclarsoru09 = [a.sonuc09 for a in dersson]
                for s in sonuclarsoru01:
                    soru01 += s
                    counter += 1
                for s in sonuclarsoru02:
                    soru02 += s
                for s in sonuclarsoru03:
                    soru03 += s
                for s in sonuclarsoru04:
                    soru04 += s
                for s in sonuclarsoru05:
                    soru05 += s
                for s in sonuclarsoru06:
                    soru06 += s
                for s in sonuclarsoru07:
                    soru07 += s
                for s in sonuclarsoru08:
                    soru08 += s
                for s in sonuclarsoru09:
                    soru09 += s
                if counter > 0:
                    soru01 /= counter
                    soru02 /= counter
                    soru03 /= counter
                    soru04 /= counter
                    soru05 /= counter
                    soru06 /= counter
                    soru07 /= counter
                    soru08 /= counter
                    soru09 /= counter
                    rapor.append([int(h.hoca_kodu),h.ad,h.soyad,h.bolum,
                                fakultee,soru01,soru02,soru03,
                                soru04,soru05,soru06,soru07,soru08,soru09])
        tumsorular          = sorular.objects.all()

        args = {'makam':makam, 'sorular':tumsorular, 'rapor':rapor}
    return render(request, 'accounts/sonuclar.html',args)


def profil(request):
    if request.user.ogr:
        profil          = ogrenci.objects.filter(ogrenci_no=request.user.username)
        ogrno           = [a.ogrenci_no for a in profil]
        dersler         = ogrenci_ders.objects.filter(ogrenci_no__in=ogrno)
        derskodlari     = [a.ders_kodu for a in dersler]
        dersDetaylari   = dersdetaylari.objects.filter(ders_kodu__in=derskodlari)
        args = {'profil': profil, 'dersdetaylari': dersDetaylari}
    elif request.user.hoc:
        profil      = hoca.objects.filter(hoca_kodu=request.user.username)
        hocakodu    = [a.hoca_kodu for a in profil]
        dersler     = ders.objects.filter(hoca_kodu__in=hocakodu)
        args = {'profil': profil, 'dersler': dersler}
    elif request.user.yon:
        profil      = yonetim.objects.filter(YonetimID=request.user.username)
        YonetimID   = [a.YonetimID for a in profil]
        makam       = [a.makam for a in profil]
        args = {'profil': profil}

    return render(request, 'accounts/profil.html', args)


def sonucOlustur(request):
    if request.method == 'POST':
        sonuc =  sonuclar.objects.create(ders_kodu=request.POST.get('derskodu'),
        ogrenci_no=request.user.username,grup_no=request.POST.get('dersgrubu'),
        sonuc01=request.POST.get('1'),sonuc02=request.POST.get('2'),
        sonuc03=request.POST.get('3'),sonuc04=request.POST.get('4'),
        sonuc05=request.POST.get('5'),sonuc06=request.POST.get('6'),
        sonuc07=request.POST.get('7'),sonuc08=request.POST.get('8'),
        sonuc09=request.POST.get('9'))

    return redirect('../anket/')
