# Vercel Deployment - Adım Adım Talimatlar

## Vercel CLI ile Deploy

Terminal'de `ml-service` klasöründe şu komutu çalıştırın:

```bash
vercel
```

## Sorular ve Yanıtlar

Vercel size şu soruları soracak:

1. **Set up and deploy?** 
   → `Y` (Yes) yazın ve Enter'a basın

2. **Which scope should contain your project?**
   → Hesabınızı seçin (MuhammedKavartkurt's projects)

3. **Link to existing project?**
   → `N` (No) yazın ve Enter'a basın ⚠️ ÖNEMLİ: Yeni proje oluşturuyoruz

4. **What's the name of your existing project?**
   → Bu soru gelmeyecek çünkü "no" dediniz

5. **What's your project's name?**
   → `avatar-ml-service` yazın (veya istediğiniz isim)

6. **In which directory is your code located?**
   → `.` yazın (mevcut klasör) veya Enter'a basın

7. **Want to override the settings?**
   → `N` (No) yazın

## Deployment Sonrası

Deployment tamamlandıktan sonra şu çıktıyı göreceksiniz:

```
✅ Production: https://avatar-ml-service-xxxxx.vercel.app
```

Bu URL'yi kopyalayın!

## Supabase'e URL Ekleme

1. Supabase Dashboard'a gidin
2. **Project Settings** > **Edge Functions** > **Secrets**
3. **New Secret** butonuna tıklayın
4. **Name**: `ML_SERVICE_URL`
5. **Value**: Vercel URL'niz (örn: `https://avatar-ml-service-xxxxx.vercel.app`)
6. **Save**

## Test

1. Uygulamada bir avatar yükleyin
2. Supabase Edge Function loglarını kontrol edin
3. Vercel servisinin çağrıldığını görmelisiniz

