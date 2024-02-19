arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nnditer ile iterasyon(tüm elemanları dolaşma)")
for x in np.nditer(arr4): print(x)