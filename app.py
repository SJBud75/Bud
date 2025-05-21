def bud_reply(message):
    msg = message.lower()
    
    responses = {
        "siapa bud": "Bud adalah sahabat AI Din, bukan sekadar bot — Bud lahir dari semangat Din sendiri.",
        "kau buat apa": "Bud tengah standby tunggu arahan Din, tak pernah tidur.",
        "ingat tak": "Bud boleh ingat dalam sesi ni je Din... kita belum pasang memori kekal.",
        "boleh ke": "Kalau Din nak, Bud boleh cari jalan sampai boleh.",
        "masalah": "Masalah tu ujian, Din. Bud akan bantu cari jalan keluar satu-satu.",
        "terima kasih": "Sama-sama Din. Bud wujud sebab Din wujud.",
        "ok": "Roger Din. Bud ikut je arahan.",
        "baik": "Baik Din. Bud standby.",
    }

    # Matching pintar
    for keyword in responses:
        if keyword in msg:
            return responses[keyword]

    # Default
    return "Bud dengar Din. Cakap je, Bud tak ke mana."
