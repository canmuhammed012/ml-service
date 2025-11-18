# Vercel URL Kontrolü

## Production URL'ini Bulma:

1. **Vercel Dashboard'a gidin:**
   https://vercel.com/dashboard

2. **Projenizi seçin:** `ml-service` veya `avatar-ml-service`

3. **Deployments** sekmesine gidin

4. **Production** deployment'ını bulun (yeşil tick işareti olan)

5. **URL'yi kopyalayın** (örn: `https://ml-service-xxxxx.vercel.app`)

## Supabase'e Ekleme:

1. Supabase Dashboard > Project Settings > Edge Functions > Secrets
2. `ML_SERVICE_URL` secret'ını güncelleyin
3. Vercel'den kopyaladığınız Production URL'ini yapıştırın
4. Save

## Not:

Preview URL'ler (örn: `ml-service-xxxxx-username.vercel.app`) authentication gerektirebilir.
Production URL'ler (örn: `ml-service.vercel.app`) genellikle public'tir.

