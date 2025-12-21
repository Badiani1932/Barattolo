#!/usr/bin/env python3
"""
BADIANI - Convertitore HTML Email-Ready
Questo script converte le immagini in base64 e crea un HTML standalone
"""

import base64
import os
import glob

def image_to_base64(filepath):
    """Converte un'immagine in base64 data URI"""
    try:
        with open(filepath, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            ext = filepath.split('.')[-1].lower()

            mime_types = {
                'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg',
                'png': 'image/png',
                'gif': 'image/gif',
                'webp': 'image/webp',
                'svg': 'image/svg+xml'
            }

            mime_type = mime_types.get(ext, f'image/{ext}')
            return f'data:{mime_type};base64,{encoded}'
    except Exception as e:
        print(f"❌ Errore con {filepath}: {e}")
        return None

def convert_all_images():
    """Converte tutte le immagini nella cartella corrente"""

    # Immagini necessarie
    required_images = [
        'logo-badiani.png',
        'group-barattoli.jpg',
        'mission.jpg',
        'vision.jpg',
        'pattern-dots.png',
        'worldwide.jpg',
        'pattern-geometric.png',
        'group-barattoli-2.jpg',
        'classico.jpg',
        'dolcevita.jpg',
        'pistacchio.jpg',
        'classico-open.jpg',
        'dolcevita-open.jpg',
        'pistacchio-open.jpg',
        'top-classico.jpg',
        'top-dolcevita.jpg',
        'top-pistacchio.jpg',
        'logo-b-blue.png'
    ]

    print("🔄 CONVERSIONE IMMAGINI IN BASE64")
    print("=" * 80)

    image_data = {}
    found = 0
    missing = []

    for img_file in required_images:
        if os.path.exists(img_file):
            base64_data = image_to_base64(img_file)
            if base64_data:
                image_data[img_file] = base64_data
                size_kb = len(base64_data) / 1024
                print(f"✅ {img_file:<30} ({size_kb:.1f} KB)")
                found += 1
        else:
            missing.append(img_file)
            print(f"❌ {img_file:<30} NON TROVATA")

    print("=" * 80)
    print(f"✅ Trovate: {found}/{len(required_images)}")
    print(f"❌ Mancanti: {len(missing)}/{len(required_images)}")

    if missing:
        print("\n⚠️  IMMAGINI MANCANTI:")
        for img in missing:
            print(f"   • {img}")
        print("\n💡 Metti tutte le immagini nella stessa cartella di questo script")

    return image_data

if __name__ == "__main__":
    print("\n🍦 BADIANI - Convertitore HTML Email-Ready\n")

    image_data = convert_all_images()

    if image_data:
        print(f"\n✅ {len(image_data)} immagini convertite con successo!")
        print("\n📧 Ora puoi usare 'badiani-email-ready.html'")
    else:
        print("\n❌ Nessuna immagine trovata!")
        print("💡 Assicurati che le immagini siano nella stessa cartella")
