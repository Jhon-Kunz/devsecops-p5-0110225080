def is_valid_number(value):
    """Memvalidasi apakah input bisa diubah menjadi tipe angka (float)."""
    try:
        float(value)
        return True
    except ValueError:
        return False