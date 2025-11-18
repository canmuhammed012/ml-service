"""
Preload rembg models during build to avoid first-request delay
"""
import os

def preload_rembg_models():
    """Preload rembg models"""
    try:
        from rembg import remove
        from rembg.bg import remove as remove_bg
        
        # Create a dummy image to trigger model download
        from PIL import Image
        import io
        
        # Create a small test image
        test_img = Image.new('RGB', (100, 100), color='red')
        img_buffer = io.BytesIO()
        test_img.save(img_buffer, format='JPEG')
        test_bytes = img_buffer.getvalue()
        
        # This will download the model if not already cached
        print("Preloading rembg models...")
        try:
            remove(test_bytes)
            print("rembg models preloaded successfully")
        except Exception as e:
            print(f"Error preloading rembg models: {e}")
            
    except ImportError as e:
        print(f"rembg not available: {e}")
    except Exception as e:
        print(f"Error in preload: {e}")

if __name__ == "__main__":
    preload_rembg_models()

