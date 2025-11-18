# ML Service - Railway Deployment

Bu servis Railway'de deploy edilmek üzere hazırlanmıştır.

## Özellikler

✅ **Face Detection**: OpenCV Haar Cascade ile gerçek yüz algılama
✅ **NSFW Detection**: NudeNet ile NSFW içerik tespiti
✅ **Background Removal**: rembg ile arka plan kaldırma

## Railway'a Deploy

1. Railway.app'e git ve GitHub ile giriş yap
2. "New Project" > "Deploy from GitHub repo"
3. `ml-service` klasörünü seç
4. Railway otomatik olarak deploy edecek
5. Production URL'yi al ve Supabase'de `ML_SERVICE_URL` secret'ına ekle

## Lokal Test

```bash
cd ml-service
pip install -r requirements.txt
uvicorn api.index:app --reload
```

## Endpoints

- `GET /` - Health check
- `POST /detect-face` - Yüz algılama
- `POST /detect-nsfw` - NSFW tespiti
- `POST /remove-background` - Arka plan kaldırma
- `POST /process-avatar` - Tüm işlemleri birleştirir

## Notlar

- Railway ücretsiz tier'da aylık $5 kredi verir
- İlk deploy biraz uzun sürebilir (paketler indiriliyor)
- Production URL'yi Supabase'e eklemeyi unutma

