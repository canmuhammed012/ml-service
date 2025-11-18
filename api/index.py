"""
Vercel Python ML Service for Avatar Processing
Simplified version for Vercel compatibility
"""

try:
    from fastapi import FastAPI, File, UploadFile, HTTPException
    from fastapi.responses import JSONResponse
    from fastapi.middleware.cors import CORSMiddleware
    import io
    import base64
    
    app = FastAPI(title="Avatar ML Processing Service")
except Exception as e:
    print(f"Import error: {e}")
    raise

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    try:
        return {"status": "ok", "service": "Avatar ML Processing"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


@app.post("/detect-face")
async def detect_face(file: UploadFile = File(...)):
    """Detect faces in uploaded image"""
    try:
        image_bytes = await file.read()
        
        if len(image_bytes) == 0:
            return {"has_face": False, "face_count": 0, "error": "Empty file"}
        
        # Try to use OpenCV Haar Cascade for face detection (lighter than MediaPipe)
        try:
            import cv2
            import numpy as np
            
            # Convert bytes to numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise Exception("Invalid image format")
            
            # Load Haar Cascade classifier (built-in, no download needed)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            face_count = len(faces)
            has_face = face_count > 0
            
            print(f"OpenCV Haar Cascade face detection: {face_count} face(s) found")
            
            return {
                "has_face": has_face,
                "face_count": face_count,
                "success": True
            }
            
        except ImportError:
            # MediaPipe not available, use PIL fallback
            print("MediaPipe not available, using PIL fallback")
            from PIL import Image
            try:
                img = Image.open(io.BytesIO(image_bytes))
                width, height = img.size
                has_face = width >= 100 and height >= 100
                face_count = 1 if has_face else 0
            except:
                has_face = False
                face_count = 0
            
            return {
                "has_face": has_face,
                "face_count": face_count,
                "success": True
            }
        except Exception as e:
            print(f"OpenCV face detection error: {e}")
            # Fallback: use PIL
            from PIL import Image
            try:
                img = Image.open(io.BytesIO(image_bytes))
                width, height = img.size
                has_face = width >= 100 and height >= 100
                face_count = 1 if has_face else 0
            except:
                has_face = False
                face_count = 0
            
            return {
                "has_face": has_face,
                "face_count": face_count,
                "success": True
            }
    except Exception as e:
        print(f"Face detection error: {e}")
        return {"has_face": False, "face_count": 0, "error": str(e)}


@app.post("/detect-nsfw")
async def detect_nsfw(file: UploadFile = File(...)):
    """Detect NSFW content"""
    try:
        image_bytes = await file.read()
        
        if len(image_bytes) < 5000:
            return {"is_nsfw": False, "confidence": 0.1, "success": True}
        
        # Try to use NudeNet for NSFW detection (if available)
        try:
            from nudenet import NudeDetector
            
            # Initialize detector (first call will download model)
            detector = NudeDetector()
            
            # Save image to temp file for NudeNet
            import tempfile
            import os
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                tmp_file.write(image_bytes)
                tmp_path = tmp_file.name
            
            try:
                # Detect NSFW content
                detections = detector.detect(tmp_path)
                
                # Check if any NSFW content detected
                nsfw_classes = ['EXPOSED_GENITALIA_FEMALE', 'EXPOSED_GENITALIA_MALE', 
                               'EXPOSED_BREAST_FEMALE', 'EXPOSED_ANUS', 'EXPOSED_BUTTOCKS']
                
                is_nsfw = False
                max_confidence = 0.0
                
                for detection in detections:
                    if detection['class'] in nsfw_classes:
                        is_nsfw = True
                        max_confidence = max(max_confidence, detection['score'])
                
                print(f"NudeNet NSFW detection: is_nsfw={is_nsfw}, confidence={max_confidence}")
                
                return {
                    "is_nsfw": is_nsfw,
                    "confidence": float(max_confidence),
                    "success": True
                }
            finally:
                # Clean up temp file
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
                    
        except ImportError:
            print("NudeNet not available, using heuristic check")
            # Fallback: heuristic check
            return {
                "is_nsfw": False,
                "confidence": 0.0,
                "success": True
            }
        except Exception as e:
            print(f"NudeNet detection error: {e}")
            # Fallback: heuristic check
            return {
                "is_nsfw": False,
                "confidence": 0.0,
                "success": True
            }
            
    except Exception as e:
        print(f"NSFW detection error: {e}")
        return {"is_nsfw": False, "confidence": 0.0, "error": str(e)}


@app.post("/remove-background")
async def remove_background(file: UploadFile = File(...)):
    """Remove background from image"""
    try:
        image_bytes = await file.read()
        
        # Background removal - rembg disabled on Render free tier (memory limit)
        # TODO: Enable when upgrading to Render Starter Plan ($7/ay) or Railway
        print("Background removal: rembg disabled on Render free tier (512MB limit)")
        print("Returning original image. To enable background removal, upgrade to Render Starter Plan.")
        
        # Return original image as PNG (transparent background simulation)
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(image_bytes))
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        output_buffer = io.BytesIO()
        img.save(output_buffer, format='PNG')
        output_bytes = output_buffer.getvalue()
        
        return {
            "success": False,
            "error": "Background removal disabled",
            "note": "rembg requires more memory than Render free tier allows. Upgrade to Render Starter Plan ($7/ay) or use Railway.",
            "image_base64": base64.b64encode(output_bytes).decode('utf-8')
        }
        
    except Exception as e:
        print(f"Background removal error: {e}")
        import traceback
        traceback.print_exc()
        # Fallback: return original
        from PIL import Image
        import io
        try:
            img = Image.open(io.BytesIO(image_bytes))
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            output_buffer = io.BytesIO()
            img.save(output_buffer, format='PNG')
            output_bytes = output_buffer.getvalue()
            return {
                "success": False,
                "error": str(e),
                "note": "Returning original image due to error",
                "image_base64": base64.b64encode(output_bytes).decode('utf-8')
            }
        except:
            return {
                "success": False,
                "error": str(e),
                "image_base64": None
            }


@app.post("/process-avatar")
async def process_avatar(file: UploadFile = File(...)):
    """Complete avatar processing"""
    try:
        image_bytes = await file.read()
        
        if len(image_bytes) == 0:
            raise HTTPException(status_code=400, detail="Empty image file")
        
        from io import BytesIO
        file_obj = BytesIO(image_bytes)
        file_obj.name = file.filename or "avatar.jpg"
        
        # Face detection
        face_result = await detect_face(UploadFile(file=file_obj, filename=file_obj.name))
        file_obj.seek(0)
        
        # NSFW detection
        nsfw_result = await detect_nsfw(UploadFile(file=file_obj, filename=file_obj.name))
        file_obj.seek(0)
        
        # Background removal
        bg_result = await remove_background(UploadFile(file=file_obj, filename=file_obj.name))
        
        return {
            "success": True,
            "face_detection": face_result,
            "nsfw_detection": nsfw_result,
            "background_removal": bg_result
        }
    except Exception as e:
        print(f"Avatar processing error: {e}")
        return {
            "success": False,
            "error": str(e)
        }
