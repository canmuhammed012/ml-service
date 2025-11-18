# Vercel ML Servisi Test

## Servis URL'si:
```
https://ml-service-fx753yxxp-muhammedkavartkurts-projects.vercel.app
```

## Test Endpoint'leri:

### Health Check:
```bash
curl https://ml-service-fx753yxxp-muhammedkavartkurts-projects.vercel.app/
```

### Face Detection Test:
```bash
curl -X POST https://ml-service-fx753yxxp-muhammedkavartkurts-projects.vercel.app/detect-face \
  -F "file=@test-image.jpg"
```

## Sorun Giderme:

Eğer 401 hatası alıyorsanız:
1. Vercel Dashboard'da servisin public olduğundan emin olun
2. CORS ayarlarını kontrol edin
3. URL'nin doğru olduğundan emin olun

