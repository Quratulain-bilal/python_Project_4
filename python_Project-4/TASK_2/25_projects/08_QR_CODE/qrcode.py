import qrcode  # 📌 QR Code Library

# ✏️ User Input
data = input("Enter text or URL to generate QR Code: ")

# ✅ Generate QR Code
qr = qrcode.QRCode(
    version=1,  # QR Code Size (1-40)
    box_size=10,  # Size of Each Box
    border=5  # Border Thickness
)
qr.add_data(data)
qr.make(fit=True)

# 🎨 Create and Save QR Code
qr_img = qr.make_image(fill="black", back_color="white")
qr_img.save("my_qr_code.png")

print("✅ QR Code Generated & Saved as my_qr_code.png")
