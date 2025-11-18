# Avatar ML Processing Service (Vercel)

Python tabanlı ML servisi - Avatar işleme için:
- Yüz tespiti (MediaPipe)
- NSFW tespiti
- Background removal (rembg)

## Kurulum

### 1. Vercel CLI Kurulumu

```bash
npm install -g vercel
```

### 2. Vercel'e Giriş

```bash
vercel login
```

### 3. Projeyi Deploy Et

```bash
cd ml-service
vercel
```

Vercel size sorular soracak:
- Set up and deploy? **Yes**
- Which scope? **Your account**
- Link to existing project? **No**
- Project name? **avatar-ml-service** (veya istediğiniz isim)
- Directory? **./ml-service**
- Override settings? **No**

### 4. Environment Variables (Gerekirse)

Vercel Dashboard'dan environment variables ekleyebilirsiniz.

## API Endpoints

### Health Check
```
GET /
```

### Face Detection
```
POST /detect-face
Content-Type: multipart/form-data
Body: image file
```

### NSFW Detection
```
POST /detect-nsfw
Content-Type: multipart/form-data
Body: image file
```

### Background Removal
```
POST /remove-background
Content-Type: multipart/form-data
Body: image file
Response: {"image_base64": "...", "format": "png"}
```

### Complete Processing
```
POST /process-avatar
Content-Type: multipart/form-data
Body: image file
Response: Combined results
```

## Supabase Edge Function'dan Kullanım

```typescript
const response = await fetch('https://your-vercel-app.vercel.app/detect-face', {
  method: 'POST',
  headers: {
    'Content-Type': 'multipart/form-data',
  },
  body: formData // FormData with image file
})
```

## Notlar

- İlk çağrıda cold start olabilir (model yükleme)
- Model dosyaları büyük olabilir (rembg ~100MB+)
- Vercel free tier: 10 saniye execution time limiti
- Function size limit: 50 MB (uncompressed)

## Sorun Giderme

Eğer model dosyaları çok büyükse:
1. Railway veya Render kullanın
2. Veya model dosyalarını CDN'den yükleyin
3. Veya daha küçük modeller kullanın

