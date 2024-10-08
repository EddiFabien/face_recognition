import cv2
from pyzbar.pyzbar import decode

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

while True:
    # Lire une image de la webcam
    ret, frame = cap.read()
    if not ret:
        print("Impossible d'accéder à la webcam.")
        break

    # Décoder les QR codes dans l'image
    decoded_objects = decode(frame)

    # Afficher chaque QR code détecté
    for obj in decoded_objects:
        # Dessiner un rectangle autour du QR code
        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Afficher le contenu du QR code
        qr_data = obj.data.decode('utf-8')
        cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print("QR Code détecté :", qr_data)

    # Afficher l'image
    cv2.imshow("Scanner QR Code", frame)

    # Quitter si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la webcam et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()

