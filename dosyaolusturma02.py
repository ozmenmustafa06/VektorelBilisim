for a in range(10):
    dosya_adi = f"rehber{a}.txt"
    with open(dosya_adi, 'w') as dosya:
        dosya.write(f"Bu {dosya_adi} dosyasıdır.")
